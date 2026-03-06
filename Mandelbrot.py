import numpy as np
import matplotlib.pyplot as plt

class MandelbrotSet:
    def __init__(self, re_min, re_max, im_min, im_max, width, height, max_iter=255):
        """
        Args:
            re_min (float): Minimum real part of the image
            re_max (float): Maximum real part of the image
            im_min (float): Minimum imaginary part of the image
            im_max (float): Maximum imaginary part of the image
            width (int): Width of the image
            height (int): Height of the image
            max_iter (int): Maximum number of iterations. Default value set to 255
        """
        self.re_min, self.re_max = re_min, re_max
        self.im_min, self.im_max = im_min, im_max

        # Define the resolution (number of pixels) for the output image
        self.width = width
        self.height = height

        # Set the iteration limit
        self.max_iter = max_iter

    def compute_set(self):
        """Create a linear space of real and imaginary parts based on range and resolution"""
        # linspace divides the range in even intervales based on 3rd argument
        re = np.linspace(self.re_min, self.re_max, self.width)
        im = np.linspace(self.im_min, self.im_max, self.height)

        # Create a 2D grid (Complex Plane) where each point is a complex number C
        real_grid, imag_grid = np.meshgrid(re, im)
        C = real_grid + 1j * imag_grid  #put the values in complex number form

        #Initialize array Z as zeros with the same shape as the complex plane grid
        Z = np.zeros(C.shape, dtype=complex)

        # Initialize an array to store the iteration count N for each point to diverge
        escape_time = np.zeros(C.shape, dtype=int)

        #Array to track which points have not yet diverged (|z| <= 2). Initially true for all points
        track = np.full(C.shape, fill_value=True, dtype=bool)

        for i in range(self.max_iter):
            # Apply the z = z^2 + C only to points that haven't diverged
            Z[track] = Z[track] * Z[track] + C[track]  #Boolean Indexing, only updates the indices where track[i] i=True
            diverged = np.abs(Z) > 2 #Boolean which identifies points that have |z| > 2

            escaping_now = diverged & track # Boolean & operation between elements of diverged and track arrays
            escape_time[escaping_now] = i  #An array of same length as Z

            """
            The reason for comparing diverged & track is because if a number diverges on the first iteration,
            it will stay diverged forever.
            Unless we change its status in the track array, the function will continue to change its 
            escape time to 2,3,...,255. This is why the comparison is needed.
            """

            # Remove diverged points from the active mask to stop calculating them
            track[diverged] = False #Changes the boolean state of points which have diverged


        return escape_time

    def plot(self):
        # Call the computation method to get the grid of iteration values
        data = self.compute_set()

        plt.figure(figsize=(10, 7))
        plt.imshow(data, extent=(self.re_min, self.re_max, self.im_min, self.im_max), cmap='magma')
        plt.colorbar(label='Iterations to Divergence (N)')
        plt.xlabel('Re(C)')
        plt.ylabel('Im(C)')
        plt.title('Mandelbrot Set Visualization')
        plt.show()
