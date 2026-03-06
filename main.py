from Mandelbrot import MandelbrotSet

# Define the specific ranges provided in the task requirements
re_range = (-2.025, 0.6)
im_range = (-1.125, 1.125)

# MandelbrotSet with the required ranges and a 1000x1000 resolution
mandel = MandelbrotSet(re_range[0], re_range[1], im_range[0], im_range[1], 1000, 1000)

mandel.plot()