# Visual Cryptography Python Algorithm
import os
import traceback

try:
    # Take the path of the image as input
    path = input(r'Enter path of Image : ')
    
    # Validate the path
    if not os.path.isfile(path):
        print("Invalid path or file does not exist")
        exit()
    
    # Take the encryption key as input
    key = input('Enter Key for encryption of Image : ')
    
    # Validate the key
    if not key.isdigit():
        print("Invalid key, must be an integer")
        exit()
    
    key = int(key)
    
    # Print the path of the image file and the encryption key
    print('The path of file : ', path)
    print('Key for encryption : ', key)
    
    # Open the file for reading
    with open(path, 'rb') as fin:
        # Read the image data
        image = bytearray(fin.read())
    
    # Perform XOR operation on each value of the bytearray
    for index, value in enumerate(image):
        image[index] = value ^ key
    
    # Open the file for writing
    with open(path, 'wb') as fin:
        # Write the encrypted data back to the image file
        fin.write(image)
    
    print('Encryption Done...')
    
except Exception:
    print('Error caught : ', traceback.format_exc())
