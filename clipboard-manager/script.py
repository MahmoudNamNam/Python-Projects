import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error: Failed to save data to '{filepath}': {e}")

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON data from '{filepath}'.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

def get_valid_key(prompt="Enter a Key: "):
    while True:
        key = input(prompt).strip()
        if key:
            return key
        else:
            print("Invalid key. Please try again.")

if len(sys.argv) != 2 or sys.argv[1] not in ["save", "load", "list", "delete", "clear", "help"]:
    print("Invalid command. Please pass exactly one valid command.")
    print("Use 'python script.py help' for usage instructions.")
    sys.exit(1)


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = get_valid_key()
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved!")
    
    elif command == "load":
        key = get_valid_key()
        if key in data:
            clipboard.copy(data[key])
            print('Data Copied To Clipboard')
        else:
            print("Key does not exist")
    
    elif command == "list":
        print("Stored Keys and Values:")
        for key, value in data.items():
            print(f"Key: {key}, Value: {value}")

    elif command == "delete":
        key = input("Enter a Key to delete: ")
        if key in data:
            del data[key]
            save_data(SAVED_DATA, data)
            print(f"Key '{key}' deleted successfully.")
        else:
            print(f"Key '{key}' not found.")

    elif command == "clear":
        confirmation = input("Are you sure you want to clear all data? (yes/no): ").lower()
        if confirmation == "yes":
            data.clear()
            save_data(SAVED_DATA, data)
            print("All data cleared.")
        else:
            print("Operation cancelled.")
    elif command == "help":
        print("Usage: python script.py <command>")
        print("Available commands:")
        print("  save    - Save clipboard content with a key")
        print("  load    - Load clipboard content by key")
        print("  list    - List all stored keys and values")
        print("  delete  - Delete a specific key and its value")
        print("  clear   - Clear all stored clipboard data")
        print("  help    - Display usage instructions")
    else:
        print('Unknown command')
