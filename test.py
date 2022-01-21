# Import library
from PIL import Image

# ////////////////
# /// Phase 1 ///
# //////////////

# Open sample image as original image
orig_image = Image.open('materialism 0.png')

# Set cropped values for left, top, right, and bottom
crop_vals = {'left':187, 'top':10, 'right':1400, 'bottom':2100}

# Create values from dictionary
left = crop_vals['left']
top = crop_vals['top']
right = crop_vals['right']
bottom = crop_vals['bottom']

# Pass values to "crop" function
def crop(left,top,right,bottom):
    crop_vals['left'] = left
    crop_vals['top'] = top
    crop_vals['right'] = right
    crop_vals['bottom'] = bottom

# Call the crop function
edited_image = orig_image.crop((left,top,right,bottom))
# width, height = edited_image.size
edited_image.save('./tmp/crop.png') # Save cropped verison to tmp folder

# ////////////////
# /// Phase 2 ///
# //////////////

# Open resulted cropped image
cropped_image = Image.open('./tmp/crop.png')
# Gather cropped image's size
width, height = cropped_image.size
# Load all pixels from the image
orig_pixel_map = cropped_image.load()
# Gather mode
mode = cropped_image.mode
# Create a new image matching the original image's color mode, and size
new_image = Image.new(mode, (width, height))
# Load all the pixels from this new image as well
new_pixel_map = new_image.load()

# Set levels values for threshold and darkness
levels_vals = {'threshold':420, 'darkness':0}

# Create values from dictionary
threshold = levels_vals['threshold']
darkness = levels_vals['darkness']

# Pass values to "levels" function
def levels(threshold, darkness):
    new_image = Image.new(mode, (width,height))
    new_pixel_map = new_image.load()

    for x in range(width):
        for y in range(height):
            r,g,b = orig_pixel_map[x,y]
            if sum((r,g,b)) > threshold:
                new_pixel_map[x,y] = (255,255,255)
            else:
                new_pixel_map[x,y] = (r*darkness,g*darkness,b*darkness)
    # must run inside function
    new_image.save('./tmp/levels.png') # Save adjusted verison to tmp folder

# Execute levels function
levels(threshold, darkness)

# ////////////////
# // complete ///
# //////////////

# Batch phase

# Import libraries
import glob
import os

# ////////////////
# /// Phase 1 ///
# //////////////

# get cwd and set file pattern
cwd = os.getcwd()
file_pattern = '*.png'
file_name_list = []

# change directory to source of collection
os.chdir('collection')
# extend file name list to match collection
if '*' in file_pattern:
    file_name_list.extend(glob.glob(file_pattern))

# crop all files in the collection
for target in file_name_list:
    orig_image = Image.open(target)
    edited_image = orig_image.crop((left,top,right,bottom))
    edited_image.save(target)


# ////////////////
# /// Phase 2 ///
# //////////////

# apply levels adjustment to all files in the collection
def batch_levels(threshold, darkness):
    # Open resulted cropped image
    cropped_image = Image.open(target)
    # Gather cropped image's size
    width, height = cropped_image.size
    # Load all pixels from the image
    orig_pixel_map = cropped_image.load()
    # Gather mode
    mode = cropped_image.mode
    # Create a new image matching the original image's color mode, and size
    new_image = Image.new(mode, (width, height))
    # Load all the pixels from this new image as well
    new_pixel_map = new_image.load()

    new_image = Image.new(mode, (width,height))
    new_pixel_map = new_image.load()

    for x in range(width):
        for y in range(height):
            r,g,b = orig_pixel_map[x,y]
            if sum((r,g,b)) > threshold:
                new_pixel_map[x,y] = (255,255,255)
            else:
                new_pixel_map[x,y] = (r*darkness,g*darkness,b*darkness)
    # must run inside function
    new_image.save(target) # Save adjusted verison to tmp folder


# adjust levels for all files in collection
for target in file_name_list:
    batch_levels(threshold, darkness)

# ////////////////
# // complete ///
# //////////////
