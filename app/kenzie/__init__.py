import os
from dotenv import load_dotenv

from .files import allowed_file
from .files import save_file
from .files import dowload_file
from .files import zip_file
from .files import get_files

load_dotenv()
FILES_DIRECTORY = os.getenv('FILES_DIRECTORY')
if not os.path.exists(FILES_DIRECTORY):
    os.mkdir(FILES_DIRECTORY)

if not os.path.exists(f'{FILES_DIRECTORY}/gif'):
    os.mkdir(f'{FILES_DIRECTORY}/gif')

if not os.path.exists(f'{FILES_DIRECTORY}/png'):
    os.mkdir(f'{FILES_DIRECTORY}/png')

if not os.path.exists(f'{FILES_DIRECTORY}/jpg'):
    os.mkdir(f'{FILES_DIRECTORY}/jpg')