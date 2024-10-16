#Handles Image Processing

from PIL import Image
from PIL import ImageChops

im1 = Image.open("resources\\1.png")
im2 = Image.open("resources\\2.png")
im3 = Image.open("resources\\3.png")
im4 = Image.open("resources\\4.png")
im5 = Image.open("resources\\5.png")
im6 = Image.open("resources\\6.png")
closed_tile = Image.open("resources\\closed.png")
flag = Image.open("resources\\flag.png")
open_tile = Image.open("resources\\open.png")
mine = Image.open("resources\\mine.png")
trig_mine = Image.open("resources\\trigmine.png")

lookup_table = {'flag': flag, 'open_tile': open_tile, 'closed_tile': closed_tile, 'mine': mine, 'trig_mine': trig_mine, '1': im1, '2': im2, '3': im3, '4': im4, '5': im5, '5': im5}
conversion_table = {'flag': "F", 'open_tile': "O", 'closed_tile': "C", 'mine': 'M', 'trig_mine': 'T', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6'}

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
                row.append("U")
        state_array.append(row)
    return state_array

