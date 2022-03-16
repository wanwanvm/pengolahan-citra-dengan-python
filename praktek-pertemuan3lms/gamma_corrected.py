import skimage.io as io
import numpy as np
gambar=io.imread('soeharto1.jpg')
for gamma in [0.1, 0.5, 1.2, 2.2]: 
    gamma_corrected = np.array(255*(gambar / 255) ** gamma, dtype = 'uint8')
    io.imsave('Gambargama'+str(gamma)+'.jpg', gamma_corrected)
