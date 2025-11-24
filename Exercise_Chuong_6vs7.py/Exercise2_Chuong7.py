import sys
def trung_binh_Confidence():
    cau_truc = "X-DSPAM-Confidence:"
    tong_confidence = 0.0
    dem_dong = 0
    ten_file = input("Enter a file name (e.g., mbox-short.txt): ")
    try:
        with open(ten_file, 'r') as file_xu_li:
            for line in file_xu_li:
                if line.startswith(cau_truc):
                    dem_dong += 1
                    parts = line.split(':')
                    confidence_str = parts[1].strip() 
                    try:
                        gia_tri_confidence = float(confidence_str)
                        tong_confidence += gia_tri_confidence                       
                    except ValueError:
                        print("Warning: Skipped line with non-numeric value: ",line.strip())
        if dem_dong > 0:
            trung_binh_confidence = tong_confidence / dem_dong
            print("Count of confidence lines: ",dem_dong)
            print(f"Total confidence value: {tong_confidence:.4f}")
            print("Average spam confidence: ",trung_binh_confidence)
        else:
            print("No lines found starting with ",cau_truc, "in the file.")           
    except FileNotFoundError:
        # Handle error if the file doesn't exist
        print("Error: File not found or could not be opened: ",ten_file)
        sys.exit(1)
if __name__ == "__main__":
    trung_binh_Confidence()