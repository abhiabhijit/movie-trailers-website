import os

def rename_files() :
 file_list=os.listdir(r"C:\Users\user123\Desktop\mymsg")
 
 saved_path=os.getcwd()
 print("current working directiory :"+saved_path)
 os.chdir(r"C:\Users\user123\Desktop\mymsg")
 for file_name in file_list:
     old_string = file_name
     to_remove = "0123456789"
     table = str.maketrans("", "", to_remove)
      
     os.rename(file_name,old_string.translate(table))
       
 os.chdir(saved_path)   
rename_files()
