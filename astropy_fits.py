from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def hdul_show(filename):
    hdulist = fits.open(filename)
    hdulist.info()
    image_data = hdulist[0].data
    brightest = np.argmax(image_data)
    print(f'brightest: {np.unravel_index(brightest, image_data.shape)}')
    hdulist.close()


def display_fits(filename):
    with fits.open(filename) as hdul:
        image_data = hdul[0].data
        # Plot the 2D array
        plt.imshow(image_data, cmap=plt.cm.viridis)
        plt.xlabel('x-pixels (RA)')
        plt.ylabel('y-pixels (Dec)')
        plt.colorbar()
        plt.savefig('files/andromeda.png')
        plt.show()


def convert_fits(fits_location):
    with fits.open(fits_location) as hdulist:
        image_data = hdulist[0].data
        image_array = np.array(image_data)
        image = Image.fromarray(image_array)
        image.show()


if __name__ == '__main__':
    fits_location = 'files/f001a1hr.fits'
    hdul_show(fits_location)
    display_fits(fits_location)
    # convert_fits(fits_location)
