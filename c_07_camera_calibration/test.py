import numpy as np
import cv2
import os
import sys
from glob import glob

def splitfn(fn):
    _dir = os.path.dirname(fn)
    name, ext = os.path.basename(fn).split('.')
    return _dir, name,ext



def main(square_size=1.0,debug_dir='./output/', img_mask='./images/left??.jpg'):
    '''
    camera calibration for distorted images with chess board samples
    reads distorted images, calculates the calibration and write undistorted images

    original code is from opencv tutorials:
    https://github.com/opencv/opencv/blob/master/samples/python/calibrate.py
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_pose/py_pose.html

    read more about the functions here:
    https://docs.opencv2.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html
    '''

    img_names = glob(img_mask)

    if debug_dir and not os.path.isdir(debug_dir):
        os.mkdir(debug_dir)

    pattern_size = (9, 6)
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = cv2.imread(img_names[0], cv2.IMREAD_GRAYSCALE).shape[:2]  # TODO: use imquery call to retrieve results

    def processImage(fn):
        print('processing %s... ' % fn)
        img = cv2.imread(fn, 0)
        if img is None:
            print("Failed to load", fn)
            return None

        assert w == img.shape[1] and h == img.shape[0], ("size: %d x %d ... " % (img.shape[1], img.shape[0]))
        found, corners = cv2.findChessboardCorners(img, pattern_size)
        if found:
            term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
            cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)

        if debug_dir:
            vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.drawChessboardCorners(vis, pattern_size, corners, found)
            _path, name, _ext = splitfn(fn)
            outfile = os.path.join(debug_dir, name + '_chess.png')
            cv2.imwrite(outfile, vis)

        if not found:
            print('chessboard not found')
            return None

        print('           %s... OK' % fn)
        return (corners.reshape(-1, 2), pattern_points)


    chessboards = [processImage(fn) for fn in img_names]
    chessboards = [x for x in chessboards if x is not None]
    for (corners, pattern_points) in chessboards:
        img_points.append(corners)
        obj_points.append(pattern_points)

    # calculate camera distortion
    rms, camera_matrix, dist_coefs, _rvecs, _tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h), None, None)

    print("\nRMS:", rms)
    print("camera matrix:\n", camera_matrix)
    print("distortion coefficients: ", dist_coefs.ravel())

    # undistort the image with the calibration
    print('')
    for fn in img_names if debug_dir else []:
        _path, name, _ext = splitfn(fn)
        img_found = os.path.join(debug_dir, name + '_chess.png')
        outfile = os.path.join(debug_dir, name + '_undistorted.png')

        img = cv2.imread(img_found)
        if img is None:
            continue

        dst = cv2.undistort(img, camera_matrix, dist_coefs)#, None, newcameramtx)

        print('Undistorted image written to: %s' % outfile)
        cv2.imwrite(outfile, dst)

    print('Done')


    objectPoints = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],[0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])
    
    imgpts = cv2.projectPoints(	objectPoints, _rvecs[0], _tvecs[0], camera_matrix, dist_coefs)[0]
    
    def draw(img, imgpts):
        imgpts = np.int32(imgpts).reshape(-1,2)

        # draw ground floor in green
        img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-1)

        # draw pillars in blue color
        for i,j in zip(range(4),range(4,8)):
            img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)

        # draw top layer in red color
        img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

        return img

    img = cv2.imread(os.path.join(debug_dir, 'left01' + '_undistorted.png'))
    drawn_image = draw(img, imgpts)
    cv2.imshow('img',drawn_image)
    cv2.waitKey(0)



if __name__ == '__main__':
    # main(square_size=2.88,debug_dir='./output2/', img_mask='./images2/*.jpeg')
    main()

    # cv2.destroyAllWindows()