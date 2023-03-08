"""
CS50. Problem Set 6. P-Shirt

In a file called shirt.py, implement a program that expects exactly
two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG
to read (i.e., open) as input

in sys.argv[2], the name (or path) of a JPEG or PNG
to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent
background) on the input after resizing and cropping the input to
be the same size, saving the result as its output.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png,
case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.

Open the input with Image.open,
resize and crop the input with ImageOps.fit, using default values for
method, bleed, and centering,
overlay the shirt with Image.paste,
and save the result with Image.save
"""
import sys
from PIL import Image, ImageOps

def main():
    """
    overlay images
    """
    check_commandline_argument(sys.argv)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    change_image(input_filename, output_filename)


def check_commandline_argument(arguments):
    """
    checks specified command line arguments
    """
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")
    extension1 = arguments[1].rsplit(".")[1]
    extension2 = arguments[2].rsplit(".")[1]
    if extension1 not in ["jpg", "jpeg", "png"]:
        sys.exit("File1 not an image")
    if extension2 not in ["jpg", "jpeg", "png"]:
        sys.exit("File2 not an image")
    if extension1 != extension2:
        sys.exit("Different extensions")
    try:
        with open(arguments[1], "r", encoding="utf-8"):
            pass
    except FileExistsError:
        sys.exit("File does not exist")


def change_image(input_filename, output_filename):
    """
    uses library PIL
    """
    with Image.open(input_filename) as input_image:
        with Image.open("shirt.png") as shirt:
            resized_image = ImageOps.fit(input_image, shirt.size)
            resized_image.paste(shirt, shirt)
            resized_image.save(output_filename)


if __name__ == "__main__":
    main()
