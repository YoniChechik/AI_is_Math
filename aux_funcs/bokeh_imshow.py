import numpy as np
import bokeh.models
import bokeh.io
import bokeh.plotting
import cv2

def bokeh_imshow(img_orig, scale=1, colorbar=False, show=True, **figure_kwargs):

    # check if ipython or regular run
    def is_run_from_ipython():
        try:
            __IPYTHON__
            return True
        except NameError:
            return False

    if is_run_from_ipython():
        bokeh.io.output_notebook()
    else:
        import tempfile
        bokeh.plotting.output_file(tempfile.mkstemp(".html")[1])

    # we will change the image
    img = img_orig.copy()

    # check img type
    if (img.ndim == 2) and (img.dtype == np.uint8):  # grayscale image
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGBA)
    elif img.ndim == 3:  # rgb input
        img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
    else:  # regular 2D array
        pass

    # needed for flipped axis bug
    img = np.flipud(img)

    p = bokeh.plotting.figure(
        x_range=(0, img.shape[1]),
        y_range=(img.shape[0], 0),
        frame_width=img.shape[1]*scale,
        frame_height=img.shape[0]*scale,
        **figure_kwargs)

    if img.ndim == 2:
        source = bokeh.plotting.ColumnDataSource(data=dict(
            img=[img], x=[0], y=[img.shape[0]],
            dw=[img.shape[1]], dh=[img.shape[0]],
            value=[img[::-1, :]]))
        p.add_tools(bokeh.models.HoverTool(
            tooltips=[
                ("(x, y)", "($x, $y)"),
                ("value", "@value")]))
        p.image(source=source, image='img', x='x', y='y',
                dw='dw', dh='dh', palette="Viridis256")

        # add colorbar
        if colorbar:
            from bokeh.models import LinearColorMapper, ColorBar
            color_mapper = LinearColorMapper(
                palette="Viridis256", low=img.min(), high=img.max())
            color_bar = ColorBar(color_mapper=color_mapper, location=(0, 0))
            p.add_layout(color_bar, 'right')
    else:  # img.ndim == 3
        source = bokeh.plotting.ColumnDataSource(data=dict(
            img=[img], x=[0], y=[img.shape[0]],
            dw=[img.shape[1]], dh=[img.shape[0]],
            R=[img[::-1, :, 0]], G=[img[::-1, :, 1]], B=[img[::-1, :, 2]]))
        p.add_tools(bokeh.models.HoverTool(
            tooltips=[
                ("(x, y)", "($x, $y)"),
                ("RGB", "(@R, @G, @B)")]))
        p.image_rgba(source=source, image='img',
                     x='x', y='y', dw='dw', dh='dh')
    if show:
        bokeh.plotting.show(p)
    return p