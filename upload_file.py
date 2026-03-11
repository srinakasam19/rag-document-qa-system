import shutil
import os

def upload_file_to_rag_folder(source_file_path):

    destination_folder = r"C:\Users\KasamLaxmiSrina\Documents\rag aiml hitachi\documents"

    if not os.path.exists(source_file_path):
        return "Source file not found ❌"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    destination_path = os.path.join(
        destination_folder,
        os.path.basename(source_file_path)
    )

    shutil.copy(source_file_path, destination_path)

    return f"✅ File uploaded to {destination_path}"
print(os.path.exists(r"C:\Users\KasamLaxmiSrina\Downloads\Company Work Policy.pdf"))
if __name__ == "__main__":
    result = upload_file_to_rag_folder(
        r"C:\Users\KasamLaxmiSrina\Downloads\Linux-Tutorial.pdf"
    )
    print(result)