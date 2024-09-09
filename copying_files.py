import shutil
import os

source_dir = r"E:\\"  
# Directly access the Desktop folder using the environment variable
#desktop_dir = os.path.join(os.environ['USERPROFILE'], 'Desktop')

destination_dir = r"E:\Day3"  

os.makedirs(destination_dir, exist_ok=True)

for filename in os.listdir(source_dir): #desktop_dir
    if filename.endswith((".txt", ".pdf", ".docx", ".doc", ".rar")):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        
        shutil.copy(source_file, destination_file)
        print(f"Successfully copied {filename} to {destination_dir}")
    
print("All applicable files have been copied successfully.")
