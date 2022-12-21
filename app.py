import sys

def encrypt(input_file, output_file, key):
    # Read the input file
    with open(input_file, 'r') as f:
        text = f.read()

    # Perform the encryption
    encrypted_text = ''
    for char in text:
        encrypted_char = chr(ord(char) ^ ord(key))
        encrypted_text += encrypted_char

    # Write the encrypted text to the output file
    with open(output_file, 'w') as f:
        f.write(encrypted_text)

def decrypt(input_file, output_file, key):
    # Read the input file
    with open(input_file, 'r') as f:
        encrypted_text = f.read()

    # Perform the decryption
    text = ''
    for char in encrypted_text:
        decrypted_char = chr(ord(char) ^ ord(key))
        text += decrypted_char

    # Write the decrypted text to the output file
    with open(output_file, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    # Ensure that the correct number of arguments was provided
    if len(sys.argv) != 5:
        print('Usage: python app.py (encrypt|decrypt) input_file output_file key')
        sys.exit(1)

    # Get the command and the file paths
    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    key = sys.argv[4]

    # Ensure that the key is the correct length
    if len(key) != 1:
        print('Error: the key must be a single character')
        sys.exit(1)

    # Execute the appropriate command
    if command == 'encrypt':
        encrypt(input_file, output_file, key)
    elif command == 'decrypt':
        decrypt(input_file, output_file, key)
    else:
        print('Error: invalid command')
        sys.exit(1)
