"""
this script to resizes images in source path folder
to format 512x512px with 16px transparent margins on all sides and png extension
and saves them in target path folder

intended specifically for making Signal stickers

usage:
either execute the file from your IDE
OR
open a command line (cmd), navigate to folder where the script is held and run
'python signal_stickerize.py'
OR
open a command line (cmd), navigate to folder where the script is held and run
'python signal_stickerize.py [source_path] [target_path]' to make things faster

requirements:
1. python installed and the python.exe has to be in ur windows PATH variables (so u can execute
python commands from command line)
2. the python image library (pillow), you can get it by running 'pip install pillow' in cmd
"""

from PIL import Image  # run 'pip install pillow' if you don't have this library

import glob, sys, os

if len(sys.argv) > 1:
    source_path = str(sys.argv[1])
    target_path = str(sys.argv[2])
else:
    source_path = input('enter path of source folder:\n').replace('\\', '/')
    target_path = input('enter path of target folder:\n').replace('\\', '/')

# turn potential file references into a folder
if source_path[-1] != '/':
    source_path += '/'

if target_path[-1] != '/':
    target_path += '/'

# check if source path exists
if not os.path.exists(source_path):
    raise Exception('source path does not exists')

if source_path == target_path :
    cont = input('WARNING: source and target paths are the same\nif you continue '
                 'your images might be overwritten by new, possibly lower resolution '
                 'ones\ndo you wish to continue ? (y/n)\n')
    if cont != 'y':
        raise Exception('target and source paths were the same but user did not want to lose original files')

# check if target path exists
if not os.path.exists(target_path):
    # if it doesn't, create it
    os.makedirs(target_path)

# images list
images = []

# get all files in the source folder
for filename in glob.glob(source_path + '*'):
    try:
        # try to open the file as an image
        images.append(Image.open(filename))
    except:
        # complain if it's not an image
        print(filename + ' not an image')

sticker_size = (512, 512)   # signal advises 512x512 pics
max_side = 480              # the bigger side will be 480, accommodating for 2x16 margins

for image in images:
    width, height = image.size
    if width == height:
        new_image_size = (max_side, max_side)
        new_image_location = (16, 16)
    elif width > height:
        new_width = max_side
        new_height = int(new_width * (height/width))
        new_image_size = (new_width, new_height)
        new_image_location = (16, int(16 + ((480 - new_height)/2)))
    else:
        new_height = max_side
        new_width = int(new_height * (width/height))
        new_image_size = (new_width, new_height)
        new_image_location = (int(16 + ((480 - new_width)/2)), 16)
    # create transparent image with size 512x512
    new_image = Image.new('RGBA', sticker_size, (255, 0, 0, 0))
    # paste a resized source image at location 16x16 to accommodate for margins
    new_image.paste(image.resize(new_image_size), new_image_location)
    # save the processed picture in target location with same file name but make sure extension is png
    new_image.save(target_path + (image.filename.split('\\')[-1]).split('.', 1)[0] + '.png', 'PNG')