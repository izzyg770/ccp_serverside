"""Authenticate.py."""
import base64
from flask import abort
import flask
from .accounts import verify_password, fetch_db_password


def authenticate():
    """Authenticate the user using session cookies or HTTP Basic Auth."""
    # Check if the user is already logged in using session cookies
    if 'username' in flask.session:
        return

    # If session cookies are not present, check for HTTP Basic Auth headers
    auth_header = flask.request.headers.get('Authorization')
    if auth_header:
        auth_type, auth_value = auth_header.split()
        # only type in SPEC to account for
        if auth_type.lower() == 'basic':
            # decode base 64 encoding
            decoded_cred = base64.b64decode(auth_value).decode('utf-8')
            username, password = decoded_cred.split(':')

            user_data = fetch_db_password(username)
            verify_password(user_data['password'], password)
            flask.session['username'] = username
            return

    abort(403)
