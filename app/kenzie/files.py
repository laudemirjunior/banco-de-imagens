import os
from dotenv import load_dotenv
from flask import send_from_directory
import shutil

load_dotenv()

ALLOWED_EXTENSIONS = os.getenv('ALLOWED_EXTENSIONS')
FILES_DIRECTORY = os.getenv('FILES_DIRECTORY')
DOWNLOAD = os.getenv('DOWNLOAD')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file, extension, filename):
    return file.save(os.path.join(f'{FILES_DIRECTORY}/{extension}', filename))      

def dowload_file(file_name, extension):
    return send_from_directory(
        directory=f'{FILES_DIRECTORY}/{extension}', 
        path=file_name, 
        as_attachment=True
        )

def zip_file(query_params, directory):
    return shutil.make_archive(f"{DOWNLOAD}/{query_params}", 'zip', directory) 

def get_files():
    files = []
    image = list(filenames for dirpath, dirnames, filenames in os.walk(FILES_DIRECTORY))
    for folders in image:
        for file in folders:
            files.append(file)
    return files