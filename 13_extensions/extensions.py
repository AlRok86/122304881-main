"""
CS50. Problem Set 1. File Extensions.
In a file called extensions.py, implement a program that
prompts the user for the name of a file
and then outputs that file’s media type if the file’s name ends,
case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all,
output application/octet-stream instead, which is a common default.
"""


def main():
    """
    file extensions to media types
    """
    file_name = input("File Name:").lower().strip()
    extension = extract_extension(file_name)
    if is_application(extension):
        print("application/" + extension)
    elif is_image(extension):
        print("image/" + change_jpg(extension))
    elif is_text(extension):
        print("text/plain")
    else:
        print("application/octet-stream")


def extract_extension(file_name):
    """
    gets extension
    """
    file_name = file_name.lower().strip()
    extension = file_name.rpartition(".")[2]
    return extension


def is_application(extension):
    """
    condition for application
    """
    match extension:
        case "pdf" | "zip":
            return True
        case _:
            return False


def is_image(extension):
    """
    condition for image
    """
    match extension:
        case "png" | "jpg" | "jpeg" | "gif":
            return True
        case _:
            return False


def is_text(extension):
    """
    condition for text
    """
    match extension:
        case "txt":
            return True
        case _:
            return False


def change_jpg(extension):
    """
    helper for image
    """
    return extension.replace("jpg", "jpeg")


main()
