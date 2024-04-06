"""CCP development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xa8Tl \xd3M7\xee\x83Z\xcf\x04\xd1\n\
             x08\xd4\xdc\x124g\xe4\x89p\x04'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
CCP_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = CCP_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'mov'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = CCP_ROOT/'var'/'ccp.sqlite3'
