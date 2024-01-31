import os, shutil 

from_dir = 'C:/Users/Thomas/Downloads'
to_dir = 'D:\RandomDocuments'

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for i in list_of_files:
    name,extension = os.path.splitext(i)
    
    if extension == '':
        continue
    # if extension in ['.png', '.jpg', '.jpeg','.gif','.bmp']:
    #     path1 = from_dir + '/' + i 
    #     path2 = to_dir + '/' + 'ImageFiles'
    #     path3 = to_dir + '/' + 'ImageFiles' + '/' + i
        
    #     print(path1)
    #     print(path3)
        
    #     if os.path.exists(path2):
    #         print('The file is being moved.')
    #         shutil.move(path1,path3)      
    #     else: 
    #         os.makedirs(path2)
    #         print('The file is being moved.')
    #         shutil.move(path1,path3)
                
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + i 
        path2 = to_dir + '/' + 'DocumentFiles'
        path3 = to_dir + '/' + 'DocumentFiles' + '/' + i
        
        print(path1)
        print(path3)
        
        if os.path.exists(path2):
            print('The file is being moved.')
            shutil.move(path1,path3)      
        else: 
            os.makedirs(path2)
            print('The file is being moved.')
            shutil.move(path1,path3)    