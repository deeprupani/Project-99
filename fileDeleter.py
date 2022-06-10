import shutil
import os
import time

def main():
    deleted_folders=0
    deleted_files=0
    path=input("Enter the File to be Deleted")
    #path="C:\Users\lalit\Documents\Deep Projects\School\Computers"
    days=30
    #Converting days into seconds
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folders,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(root_folders):
                remove_folder(root_folders)
                deleted_folders+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folders,folder)
                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders+=1
                for file in files:
                    file_path=os.path.join(root_folders,file)
                    if seconds>=get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files+=1
        else:
            if seconds>=get_file_or_folder_age(path):
                remove_file(path)
                deleted_files+=1
    else:
        print(f'"{path}"is not found')
        deleted_files+=1
    print(f"Total folders deleted: {deleted_folders}")
    print(f"Total files deleted: {deleted_files}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete the"+path)

def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete the"+path)

def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime

main()
