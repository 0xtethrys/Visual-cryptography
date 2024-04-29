try:
    # Prompt user to enter the path of the image file and encryption key
    path = input(r'Enter path of Image: ')
    key = int(input('Enter Key for encryption/decryption of Image: '))
    
    # Print the input values for verification
    print('Image file path: ', path)
    print('Encryption/Decryption key: ', key)
    
    # Read the image file and store the data in a variable
    with open(path, 'rb') as fin:
        image = bytearray(fin.read())
    
    # Perform XOR operation on each value of the bytearray for encryption/decryption
    for index, value in enumerate(image):
        image[index] = value ^ key
    
    # Open file for writing purpose
    with open(path, 'wb') as fout:
        # Write encrypted/decrypted data to the image file
        fout.write(image)
    
    # Print message to confirm encryption/decryption completion
    if key != 0:
        print('Encryption Done...')
    else:
        print('Decryption Done...')

# Catch and handle any exceptions that may arise
except Exception as e:
    print('Error caught:', e)
