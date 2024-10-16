#Handles Image Processing

from PIL import Image
from PIL import ImageChops

im1 = Image.open("resources\\1.png")
im2 = Image.open("resources\\2.png")
im3 = Image.open("resources\\3.png")
im4 = Image.open("resources\\4.png")
closed_tile = Image.open("resources\\closed.png")
flag = Image.open("resources\\flag.png")
open_tile = Image.open("resources\\open.png")

lookup_table = {'flag': flag, 'open_tile': open_tile, 'closed_tile': closed_tile}
conversion_table = {'flag': "F", 'open_tile': "O", 'closed_tile': "C"}

def convert_to_array(state_image):
    state_array = []
    for i in range(16):
        row = []
        for j in range(16):
            reg = (16 * j, 16 * i, 16 * (j + 1) - 1, 16 * (i + 1) - 1)
            temp_image = state_image.crop(reg)
            for img_id in lookup_table:
                diff = ImageChops.difference(temp_image, lookup_table[img_id])
                if not diff.getbbox():
                    row.append(conversion_table[img_id])
                    break
            else:
                row.append("N")
        state_array.append(row)
    return state_array

