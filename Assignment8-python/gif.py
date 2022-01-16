import os
import imageio

images = []
myfile = os.listdir('image')

for i in range(len(myfile)):
    image = imageio.imread("image/" + myfile[i])
    images.append(image)

imageio.mimsave('fun.gif' , images)