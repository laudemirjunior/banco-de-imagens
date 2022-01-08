import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from app.kenzie import allowed_file, save_file, dowload_file, zip_file, get_files

load_dotenv()

FILES_DIRECTORY = os.getenv('FILES_DIRECTORY')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FILES_DIRECTORY
app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify(mesage= "Request entity too large"), 413

@app.get('/')
def home():
    return jsonify(message= "Entrega 6 - Banco de Imagens"), 201

@app.post('/upload')
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    extension = filename[-3::]
    road = f'{FILES_DIRECTORY}/{extension}/{filename}'

    if os.path.exists(road):
        return jsonify(message= "File already exists"), 409

    if file and not allowed_file(filename):
        return jsonify(message= "File not supported"), 415

    else:   
        save_file(file, extension, filename)    
        return jsonify(message= "Success"), 201

@app.get('/download/<file_name>')
def dowload_file_name(file_name):
    extension = file_name[-3::]
    try:
        return dowload_file(file_name, extension), 200
    except:
        if not os.path.exists(f'{FILES_DIRECTORY}/{extension}/{file_name}') and allowed_file(file_name) == True:
            return jsonify(message= "File not exists"), 409
        else:
            return jsonify(message= "File not supported"), 404

@app.get('/download-zip')
def download_zip():
    query_params = request.args.get("file_extension")
    directory=f'{FILES_DIRECTORY}/{query_params}'
    try:
        if os.listdir(directory) == []:
            return jsonify(message = "There are no files in the requestor directory"), 409    
        else:
            zip_file(query_params, directory)
            return jsonify(message = "Success"), 200   
    except:
        return jsonify(message="File does not exist"), 404
  

@app.get('/files')
def files():
    return jsonify(get_files()), 200

@app.get('/files/<extension>')
def files_extension(extension):
    for _, _, arquivo in os.walk(f'{FILES_DIRECTORY}/{extension}'):
        return jsonify(arquivo), 200
    return jsonify(message= "File not supported"), 404
