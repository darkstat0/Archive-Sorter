import os
import zipfile
import shutil

def extract_and_sort(archive_path, output_dir):
    # Check if the output directory exists, create it if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a temporary directory for extraction
    temp_dir = os.path.join(output_dir, 'temp_extraction')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Extract the archive
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        print(f"Archive successfully extracted to {temp_dir}")
    except Exception as e:
        print("Error extracting the archive:", e)
        return

    # Iterate through all files in the temporary directory
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            src_path = os.path.join(root, file)
            # Sorting logic: example based on file name prefix
            # If the file name starts with "invoice" -> category "invoices"
            # If the file name starts with "report"  -> category "reports"
            # Other files will be placed in the "others" category
            if file.lower().startswith("invoice"):
                category = "invoices"
            elif file.lower().startswith("report"):
                category = "reports"
            else:
                category = "others"
            
            dest_dir = os.path.join(output_dir, category)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            dest_path = os.path.join(dest_dir, file)
            try:
                shutil.move(src_path, dest_path)
                print(f"File {file} moved to {category}")
            except Exception as e:
                print(f"Error moving file {file}:", e)
    
    # Remove the temporary directory after processing
    try:
        shutil.rmtree(temp_dir)
        print("Temporary directory removed.")
    except Exception as e:
        print("Error removing temporary directory:", e)

    print("Data extraction and sorting completed.")

if __name__ == '__main__':
    archive_path = input("Enter the path to the archive: ")
    output_dir = input("Enter the path to save sorted files: ")
    extract_and_sort(archive_path, output_dir)
