#sorting/moving files into their specific folder(extension wise)

import os
import shutil
import glob

# #To get the file names from folder
# def list_files(folderpath):
#     filenames = os.listdir(folderpath)
#     return filenames

folderpath = "E:/My Programs/Python/FileSorting/TrialFolder/*"

#folders
document_folder = "E:/My Programs/Python/FileSorting/TrialFolder/Documents"
image_folder = "E:/My Programs/Python/FileSorting/TrialFolder/Images"
video_folder = "E:/My Programs/Python/FileSorting/TrialFolder/Videos"
setup_folder = "E:/My Programs/Python/FileSorting/TrialFolder/Setups"
webfiles_folder = "E:/My Programs/Python/FileSorting/TrialFolder/WebFiles"
compressed_folder = "E:/My Programs/Python/FileSorting/TrialFolder/Compressed"

#files lists
documents = ['.doc', '.docx', '.pdf']
videos = ['.mp4', '.3gp']
images = ['.jpeg', '.jpg', '.gif', '.svg', '.jfif', '.png']
setups = ['.exe', '.apk']
webfiles = ['.html', '.css', '.js']
compresseds = ['.zip', '.rar', '.giz']

filenames = glob.glob(folderpath)
for filename in filenames:
    #checking documents
    if os.path.splitext(filename)[1] in documents:
        if os.path.exists(document_folder):
            if os.path.exists(document_folder + "/" + os.path.basename(filename)):
                count = 0
                tempfilename = os.path.splitext(os.path.basename(filename))[0]
                tempfileext = os.path.splitext(os.path.basename(filename))[1]
                tempfilepath = "E:/My Programs/Python/FileSorting/TrialFolder/" + tempfilename + tempfileext
                while True:
                    count += 1
                    newfilename = tempfilename + "(" + str(count) + ")" + tempfileext
                    print(document_folder + "/" + newfilename)
                    if os.path.exists(document_folder + "/" + newfilename):
                        os.rename(tempfilepath, newfilename)
                    else:
                        shutil.move(filename, document_folder)
        else:
            os.mkdir(document_folder)
            shutil.move(filename, document_folder)
    #checking images
    elif os.path.splitext(filename)[1] in images:
        if os.path.exists(image_folder):
            shutil.move(filename,image_folder)
        else:
            os.mkdir(image_folder)
            shutil.move(filename, image_folder)
    # checking videos
    elif os.path.splitext(filename)[1] in videos:
        if os.path.exists(video_folder):
            shutil.move(filename, video_folder)
        else:
            os.mkdir(video_folder)
            shutil.move(filename, video_folder)
    # checking setups
    elif os.path.splitext(filename)[1] in setups:
        if os.path.exists(setup_folder):
            shutil.move(filename, setup_folder)
        else:
            os.mkdir(setup_folder)
            shutil.move(filename, setup_folder)
    # checking webfiles
    elif os.path.splitext(filename)[1] in webfiles:
        if os.path.exists(webfiles_folder):
            shutil.move(filename, webfiles_folder)
        else:
            os.mkdir(webfiles_folder)
            shutil.move(filename, webfiles_folder)
    # checking compressed
    elif os.path.splitext(filename)[1] in compresseds:
        if os.path.exists(compressed_folder):
            shutil.move(filename, compressed_folder)
        else:
            os.mkdir(compressed_folder)
            shutil.move(filename, compressed_folder)
