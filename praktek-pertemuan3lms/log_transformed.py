import skimage.io as io
import numpy as np
gambar=io.imread('soeharto1.jpg')
d = 255/(np.log(1+np.max(gambar)))
log_transformed = d * np.log(1 + gambar)
log_transformed = np.array(log_transformed, dtype = np.uint8)
io.imsave('log_transformed.jpg', log_transformed)
