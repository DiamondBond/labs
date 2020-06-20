from PIL import Image
from random import randint

img = Image.new('RGB', (500, 500), "white")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if randint(0,1) == 1:
            pixels[i,j] = (0, 0, 0)
img.save('pic.png')
