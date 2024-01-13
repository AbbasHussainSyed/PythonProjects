def decode(message_file):
    pyramid_lines = []

    # Read the pyramid lines from the file
    with open(message_file, 'r') as file:
        for line in file:
            line = line.strip().split()
            pyramid_lines.append(line)

    # Extract the message words based on the pyramid structure
    message_words = [line[-1] for line in pyramid_lines]

    # Return the decoded message as a string
    decoded_message = ' '.join(message_words)
    return decoded_message


# Example usage:
message_file_path = "/Users/abbassyed/Documents/Assignments/coding.txt"
decoded_message = decode(message_file_path)
print(decoded_message)