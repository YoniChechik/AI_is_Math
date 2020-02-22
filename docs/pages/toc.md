---
title: Course syllabus
bigimg: /img/FedTech-ComputerVision.jpg
share-img: https://raw.githubusercontent.com/YoniChechik/AI_is_Math/master/docs/img/FedTech-ComputerVision.jpg
---

## **Intro to CV and Python** [(slides)](/pages/c_01_intro_to_CV_and_Python/intro_to_Computer_Vision.pdf)

- [Python, Pycharm & packages installation guide](/pages/python_pycharm_installation/python_pycharm_installation/)]
- Course details
- What is computer vision (CV)?
- Course outline
- Intro to Python
  - [Basic python tutorial notebook- part 1](/pages/c_01_intro_to_CV_and_Python/basic_python_tutorial_nb/)
  - [Basic python tutorial notebook- part 2](/pages/c_01_intro_to_CV_and_Python/basic_python_tutorial_part_2_nb/)
  - [NumPy tutorial notebook](/pages/c_01_intro_to_CV_and_Python/NumPy_tutorial_nb/)
  - [Matplotlib tutorial notebook](/pages/c_01_intro_to_CV_and_Python/Matplotlib_tutorial_nb/)
  - [OpenCV tutorial notebook](/pages/c_01_intro_to_CV_and_Python/OpenCV_tutorial_nb/)
- [Ex1: basic python, numpy & matplotlib, opencv](/pages/c_01_intro_to_CV_and_Python/ex1/)


## **Basic image processing** [(slides)](/pages/c_02a_basic_image_processing/Basic_image_processing.pdf)

- Image representation
- Pixel-wise operations
- Histogram equalization [(notebook)](/pages/c_02a_basic_image_processing/histogram_equalization_nb/)
- Template matching
- Morphology operators
- Connected components
- Color space [(notebook)](/pages/c_02a_basic_image_processing/hsv_nb/)
- [Ex2: morphological operators and friends](/pages/c_02a_basic_image_processing/ex2/)


## **Filtering and resampling** [(slides)](/pages/c_02b_filtering_and_resampling/Filtering_and_resampling.pdf)

- Noise and filtering [(notebook)](/pages/c_02b_filtering_and_resampling/noise_and_filtering_nb/)
- Frequency representation
- Decimation
- Interpolation 



## **Edge Detection** [(slides)](/pages/c_03_edge_detection/edge_detection.pdf), [(edge detection notebook)](/pages/c_03_edge_detection/edge_detection_nb/)
- Intro to edges
- Basic edge image
- Edge thinning
  - LoG
  - NMS
- Edge mask
- Canny edge detector
- Other edge related topics
  - Frequency representation
  - Unsharp filter
- [Ex3: Bilateral filter](/pages/c_03_edge_detection/ex3/)

## **Curve fitting** [(slides)](/pages/c_04_curve_fitting/Curve_fitting.pdf)
- Linear least squares
- Total least squares
- Least squares [(Least squares & RANSAC notebook)](/pages/c_04_curve_fitting/least_squares_nb/)
- RANSAC
- Hough transform [(Hough transform notebook)](/pages/c_04_curve_fitting/hough_transform_nb/)
  - $(m,b)$ parameter space
  - $(\rho,\theta)$ parameter space
- [Ex4: Hough circles](/pages/c_04_curve_fitting/ex4/)



## **Image formation** [(slides)](/pages/c_05_image_formation/Image_formation.pdf)

- BRDF
- Pinhole camera
- Digital camera
- The human eye
- [Ex5: vignetting](/pages/c_05_image_formation/ex5/)

## **Geometric transformation** [(slides)](/pages/c_06_geometric_transformation/geometric_transformation.pdf)

- 2D->2D transformations [(notebook)](/pages/c_06_geometric_transformation/image_transformation_2d_nb/)
- 3D->3D transformations
- 3D->2D transformations (3D projections)
  - Perspective projection
  - Orthographic projection


## **Camera calibration** [(slides)](/pages/c_07_camera_calibration/camera_calibration.pdf)

- What is camera calibration?
- Camera extrinsics
- Camera intrinsics
- Full camera matrix
- Calibration methods and distortions [(notebook)](/pages/c_07_camera_calibration/multi_plane_calib_nb/)



## **Features** [(slides)](/pages/c_08_features/features.pdf)

- What and why we need features detection?
- Feature detection
  - Blob detection
  - Harris corner detection [(Harris notebook)](/pages/c_08_features/harris_nb/)
  - SIFT detector 
- Feature description
  - Template matching
  - HOG
  - SIFT descriptor
- SIFT feature matching [(SIFT notebook)](/pages/c_08_features/sift_nb/)
- Panoramas



## **Stereo** [(slides)](/pages/c_09_stereo/stereo.pdf)

- Structure from motion
- Epipolar geometry
     - Essential matrix
     - Fundamental matrix
     - Estimating the fundamental matrix
- Camera rectification
- Triangulation
- Stereo matching
- Other 3D sensors





## **Neural networks basics** [(slides)](/pages/c_10_neural_networks_basics/neural_networks_basics.pdf)

- Perceptrons
- Dense NN



## **Neural networks 2** [(slides)](/pages/c_11_neural_networks_2/neural_networks_2.pdf)

- [Fully connected net](/pages/c_11_neural_networks_2/fully_connected_nb/)
- [Conv net](/pages/c_11_neural_networks_2/conv_nn_nb/)



