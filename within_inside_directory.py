import shutil
import os

#desktop path
desktop_dir = os.path.join(os._environ['USERPROFILE'],'Desktop')

#destination file
destination_dir = r"E:\Day4"

#ensuring directory exists
os.makedirs(destination_dir,exist_ok=True)

#os.walk traverse dir and sub.dir
for root, dirs, files in os.walk(desktop_dir):
    for filename in files:
        if filename.endswith((".txt",".pdf",".docx",".rar",".doc")):
            
            #getting full path for source and destination
            source_file = os.path.join(root, filename)
            
            
            #maintaining folder in destination dir
            relative_path = os.path.relpath(root,desktop_dir)
            target_folder = os.path.join(destination_dir,relative_path)
            
            
            #ensuring target folder in destination exists
            os.makedirs(target_folder,exist_ok=True)
            
            #setting destination file path
            destination_file = os.path.join(target_folder,filename)
            
            #copying files
            shutil.copy(source_file,destination_file)
            print(f"Sucessfully copied {filename} to {target_folder}")
print("All the files have been transformed")