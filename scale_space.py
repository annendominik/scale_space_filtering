import numpy as np
import scipy.fft
import scipy.signal
import scipy.ndimage
import matplotlib.pyplot as plt
import skimage.data as data


def scale_kernel(gamma, c=1):
    five_kernel = np.zeros((3, 3))
    cross_kernel = np.zeros((3, 3))
    kernel = c * ((1 - gamma) * five_kernel + gamma * cross_kernel)
    return kernel


def create_scale_space(image, kernel):
    scipy.signal.convolve(image, kernel, method='direct')
    return scale_image


def create_scale_space_fft(image, kernel, sigma):
    scipy.signal.convolve(image, kernel, method='fft')
    return scale_image