#Handles Image Processing

from PIL import Image

im1 = Image.open("resources\\1.png")
im2 = Image.open("resources\\2.png")
im3 = Image.open("resources\\3.png")
im4 = Image.open("resources\\4.png")
closed_tile = Image.open("resources\\closed.png")

def convert_to_array(state_image):
    state_array = []
    for i in range(16):
        row = []
        for j in range(16):
            reg = (16 * j, 16 * i, 16, 16)
            temp_image = state_image.crop()

