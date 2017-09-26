import colorlabel
import PIL.Image
img = PIL.Image.open('label.png')
import numpy as np
from skimage import io,data,color
label = np.array(img)
dst = colorlabel.label2rgb(label,bg_label = 0,bg_color =(0,0,0))
#final = PIL.Image.fromarray(np.uint8(dst * 255))
#final.show()
#final.save('000001.png')
io.imsave('000001.png',dst)

