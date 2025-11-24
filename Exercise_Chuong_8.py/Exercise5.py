# This program reads a file line by line, finds lines starting with "From ",
# extracts the sender's email (the second word), prints it, and counts the lines.

# 1. Get the file name from the user
fname = input("Enter file name: ")

# Initialize counter for 'From ' lines
from_line_count = 0

try:
    # Open the file for reading
    file_handle = open(fname)
except FileNotFoundError:
    # Handle the case where the file does not exist
    print(f"File not found: {fname}")
    # Exit the program gracefully
    exit()

print("\n--- Senders Found ---")

# 2. Iterate through each line in the file
for line in file_handle:
    # Remove leading/trailing whitespace, including the newline character
    line = line.strip()

    # 3. Check if the line starts with "From " (with a space)
    # This ensures we don't count "From:".
    if line.startswith("From "):
        # 4. Split the line into a list of words
        words = line.split()

        # 5. The sender's email is the second word (at index 1)
        # We assume the line always has at least two words if it starts with "From "
        try:
            sender_email = words[1]
            
            # 6. Print the sender's email
            print(sender_email)
            
            # 7. Increment the counter
            from_line_count += 1
            
        except IndexError:
            # Simple error handling for malformed 'From' lines (shouldn't happen in typical mailbox data)
            print(f"Skipping malformed 'From' line: {line[:50]}...")
            continue # Go to the next line

# Close the file when done
file_handle.close()

# 8. Print the final count
print("---------------------")
print(f"There were {from_line_count} lines in the file with From as the first word.")
