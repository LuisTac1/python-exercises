"""
Pillow: resize images automatically
"""
import os
from PIL import Image

def main(main_images_folder):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} does not exist.')

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            converted_tag = '_COVERTED'

            new_file = file.name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            if converted_tag in new_file_full_path:
                continue

            img_pillow = Image.open(file_full_path)
            widht, height = img_pillow.size
            print(widht, height)
            img_pillow.close()


if __name__ == '__main__':
    main_images_folder = 'Your/file/path/here'
    main(main_images_folder)
