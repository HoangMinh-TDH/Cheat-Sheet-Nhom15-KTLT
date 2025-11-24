import sys
def doc_va_in_hoa():
    ten_file = input("Enter a file name: ")
    try:
        with open(ten_file, 'r') as file_xu_li:
            for line in file_xu_li:
                print(line.upper(), end="")
    except FileNotFoundError:
        print("Error: File not found or could not be opened: ",ten_file)
        sys.exit(1)
if __name__ == "__main__":
    doc_va_in_hoa()
