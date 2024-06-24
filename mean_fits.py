from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


def mean_fits(files):
    filecount = len(files)

    if filecount > 0:
        hdulist = fits.open(files[0])
        data = hdulist[0].data
        # plot_result(data)
        for x in range(1, filecount):
            hdulist = fits.open(files[x])
            data += hdulist[0].data

        return data / filecount


def plot_result(data):
    print(data[100, 100])
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    data = mean_fits(
        ['fits/image0.fits', 'fits/image1.fits', 'fits/image2.fits', 'fits/image3.fits', 'fits/image4.fits'])
    plot_result(data)
