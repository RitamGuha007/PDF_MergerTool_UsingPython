from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()

if __name__ == "__main__":
    print("=== PDF Merger Tool ===")
    files = []
    while True:
        path = input("Enter PDF file path (or press Enter to finish): ")
        if path == "":
            break
        files.append(path)
    if files:
        output_file = input("Enter output file name (e.g., merged.pdf): ")
        merge_pdfs(files, output_file)
        print(f"Merged PDF saved as {output_file}")
    else:
        print("No files provided. Exiting.")
