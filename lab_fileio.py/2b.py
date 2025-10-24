import os

filename = "my_custom_spreadsheet.csv"

# Check if the file exists and is readable
if os.path.exists(filename) and os.access(filename, os.R_OK):
    # Get file info using os.stat()
    file_info = os.stat(filename)
    
    print(f"File Name: {filename}")
    print(f"File Size: {file_info.st_size} bytes")
    print(f"Readable: {os.access(filename, os.R_OK)}")
    print(f"Writable: {os.access(filename, os.W_OK)}")
    print(f"Executable: {os.access(filename, os.X_OK)}")
    
    # Optional: open and read file
    with open(filename, "r") as file:
        print("\nFile opened successfully.")
else:
    print("Error: File does not exist or is not readable.")
