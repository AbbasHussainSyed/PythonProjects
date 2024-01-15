# Pyramid Message Decoder

## Overview

This Python script is designed to decode a message encoded in a pyramid structure. The encoded message is stored in a text file, and the script extracts the message by following the pyramid structure.

## Usage

### Function Signature

```python
def decode(message_file):
    """
    Decode the pyramid-encoded message.

    Parameters:
    - message_file (str): Path to the text file containing the pyramid-encoded message.

    Returns:
    - str: Decoded message.
    """
    # Implementation details...
```

### Example Usage

```python
# Example usage:
message_file_path = "/path/to/your/message/file.txt"
decoded_message = decode(message_file_path)
print(decoded_message)
```

Replace `"/path/to/your/message/file.txt"` with the actual path to your text file containing the pyramid-encoded message.

## How It Works

1. The script reads the lines from the specified text file, assuming each line represents a level of the pyramid.
2. It extracts the last word from each line to reconstruct the encoded message.
3. The decoded message is returned as a string.

## File Structure

- **decode.py**: The main script file.
- **/examples**: Contains example text files with pyramid-encoded messages.
- **README.md**: This documentation file.

## Example

For a text file like:

```
Hello
World Bye
Python is Awesome
Decode Me
```

The decoded message would be: "Hello Bye Awesome Me"

## Getting Started

1. Clone this repository to your local machine.
2. Modify the `message_file_path` variable in the example usage to point to your specific text file.
3. Run the script to decode the message.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
