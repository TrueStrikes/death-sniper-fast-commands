import os
import re
import pyperclip
from colorama import init, Fore, Style

# Initialize colorama
init()

def extract_id_from_url(url):
    # Define the regular expression pattern to match the ID in the URL
    pattern = r'(?:https?://)?(?:www\.)?roblox\.com/catalog/(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def read_prefix_from_file(file_path):
    if not os.path.isfile(file_path):
        return ""

    with open(file_path, 'r') as file:
        return file.read().strip()

def print_message(message, color):
    print(f"{color}{message}{Style.RESET_ALL}")

def main():
    print_message("Clipboard monitor started..", Fore.RED)
    prefix = read_prefix_from_file("prefix.txt")

    # Initialize the previous clipboard text
    prev_clipboard_text = ""

    while True:
        # Get the URL from the clipboard
        clipboard_text = pyperclip.paste()

        # Check if clipboard text has changed
        if clipboard_text != prev_clipboard_text:
            # Update the previous clipboard text
            prev_clipboard_text = clipboard_text

            # Extract the ID from the URL
            item_id = extract_id_from_url(clipboard_text)

            if item_id:
                # Set the clipboard with the formatted text
                clipboard_formatted = f"{prefix}aid {item_id}" if prefix else f"aid {item_id}"
                pyperclip.copy(clipboard_formatted)
                print_message(f"Extracted ID: {item_id} | Copied to clipboard: {clipboard_formatted}", Fore.GREEN)

if __name__ == "__main__":
    # Clear the console before starting the loop
    os.system("cls" if os.name == "nt" else "clear")
    main()
