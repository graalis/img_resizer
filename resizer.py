import PIL, os
from PIL import Image

# put images to resize in this subdirectory
subdir_in = "to_resize"
# output subdirectory
subdir_out = "resized"

files = os.listdir(subdir)
for elem in files:
    print(elem)

def resize(img_addr, basewidth):
    """
    Resizes an image. Output: width 300px, autoheight 
    """
    # img_addr = raw_input("Name of image file in the current dir: ")
    # basewidth = int(raw_input("Width of resulting image: "))
    img = Image.open(subdir_in + "/" + img_addr)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(subdir_out + "/F_"+img_addr) # F means Formatted

for elem in files:
    resize(elem, 300)
