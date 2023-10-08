'''
python3 utils/rename.py dataset/test
'''
import os
import sys
import random
import string

N = 5 # lenght of random string

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' has been renamed to '{new_name}'")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
old_file_name = "old_file.txt"
new_file_name = "new_file.txt"


def generate_random_string(length):
    # Define the characters from which the random string will be generated
    characters = string.ascii_letters + string.digits  # You can customize this as needed

    # Generate the random string by selecting characters randomly
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

src = sys.argv[1]

if __name__ == "__main__":

    print('Starting rename files at',src)

    images = os.listdir(src)

    for image in images:
        
        image_path = os.path.join(src,image)
        
        new_file_name = generate_random_string(N) + ".jpg"

        dst_image_path = os.path.join(src,new_file_name)

        # rename
        rename_file(image_path, dst_image_path)
