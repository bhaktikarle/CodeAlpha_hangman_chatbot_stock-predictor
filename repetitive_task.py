import shutil
import os

source_folder = r"C:\Users\bhakt\OneDrive\Desktop\source"
destination_folder = r"C:\Users\bhakt\OneDrive\Desktop\destination"

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith(".jpg"):
        src = os.path.join(source_folder,filename)
        dst = os.path.join(destination_folder,filename)
        shutil.move(src,dst)
        print(f"file moved: {filename}")