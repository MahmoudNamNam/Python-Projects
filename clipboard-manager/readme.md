## Clipboard Manager Script

This Python script provides a command-line interface to manage a clipboard-like functionality, allowing users to save, load, list, delete, or clear stored data associated with keys.

### Features

- **Save**: Save the current clipboard content with a specified key.
- **Load**: Load previously saved clipboard content using a specified key.
- **List**: Display all stored keys and their associated values.
- **Delete**: Delete a specific key and its associated value from storage.
- **Clear**: Clear all stored clipboard data.
- **Help**: Display usage instructions for the script.

### Prerequisites

- Python 3.x installed
- Required Python libraries:
  - `clipboard` (Install using `pip install clipboard` if not already installed)

### Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MahmoudNamNam/Python-Projects.git
   cd clipboard-manager
   ```

2. **Run the Script**

   Use the following commands to interact with the clipboard manager:

   ```bash
   python script.py save    # Save clipboard content with a key
   python script.py load    # Load clipboard content by key
   python script.py list    # List all stored keys and values
   python script.py delete  # Delete a specific key and its value
   python script.py clear   # Clear all stored clipboard data
   python script.py help    # Display usage instructions
   ```

3. **Commands**

   - **Save**
     - Prompts the user to enter a key and saves the current clipboard content under that key.

   - **Load**
     - Prompts the user to enter a key and copies the stored content associated with that key to the clipboard.

   - **List**
     - Displays all stored keys and their associated values.

   - **Delete**
     - Prompts the user to enter a key and deletes the associated key-value pair if it exists.

   - **Clear**
     - Asks for confirmation before clearing all stored data.

   - **Help**
     - Displays usage instructions for the script.

### File Structure

- `script.py`: Main Python script containing the clipboard management functions.
- `clipboard.json`: JSON file used for storing the clipboard data.

### Additional Notes

- Make sure to have the `clipboard` library installed (`pip install clipboard`) for clipboard-related operations.
- The script handles various exceptions such as file not found, JSON decoding errors, and unexpected errors during data manipulation.


### Author

- Mahmoud Namnam
- GitHub: [GitHub Profile](https://github.com/MahmoudNamNam)

