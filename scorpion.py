import sys
from exif import Image

with open('./palm-tree-2.jpeg', 'rb') as image_file:
    my_image = Image(image_file)
print(my_image.has_exif)
print(my_image.list_all())