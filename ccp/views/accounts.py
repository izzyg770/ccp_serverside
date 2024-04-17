"""
CCP account management.

"""
import hashlib
import uuid
import pathlib
import os
import flask
from flask import abort
import ccp

ccp.app.secret_key = b'w\xb7\xc5\xd4\x98D\xe8v\xa7\xd0\x9b{\xd7Uq\
                          x14\x0c\xae\xca\xc8\xca\xd9r\x01'


@ccp.app.route('/accounts/', methods=['POST'])
def post():
    """Display posts."""
    target = flask.request.args.get('target')
    operation = flask.request.form.get('operation')

    if operation == 'login':
        handle_login()
        return flask.redirect(flask.url_for('show_index'))

    if operation == 'create':
        handle_create()
        return flask.redirect(flask.url_for('show_index'))

    if operation == 'edit_account':
        handle_edit_account()
        return flask.redirect(flask.url_for('edit'))

    if operation == 'delete':
        handle_delete(target)
        return flask.redirect(flask.url_for('login'))

    if operation == 'update_password':
        handle_update_password()
        return flask.redirect(flask.url_for('edit'))

    return abort(404)


def fetch_db_password(username):
    """Fetch password from DB."""
    connection = ccp.model.get_db()
    pw = connection.execute(
        "SELECT username, password "
        "FROM users WHERE username = ?",
        (username,)
    ).fetchone()
    return pw


def handle_login():
    """Handle the login operation."""
    username = flask.request.form['username']

    pw = fetch_db_password(username)
    if not pw:
        flask.abort(403)
    else:
        hashed_pw = pw['password']
        verify_password(hashed_pw, flask.request.form['password'])
        connection = ccp.model.get_db()
        cur = connection.execute(
            "SELECT username, password "
            "FROM users "
            "WHERE username=? and password=?",
            [username, hashed_pw]
        )
        if not cur:
            flask.abort(403)
        flask.session['username'] = username


def verify_password(hashed_pw, input_pw):
    """Handle password verification."""
    if "$" in hashed_pw:
        algorithm, stored_salt, stored_hashed_password = (
            hashed_pw.split('$')
        )
        m = hashlib.new(algorithm)
        password_to_hash = stored_salt + input_pw
        m.update(password_to_hash.encode('utf-8'))
        hashed_password_to_check = m.hexdigest()
    else:
        hashed_password_to_check = input_pw
        stored_hashed_password = hashed_pw
    if hashed_password_to_check != stored_hashed_password:
        flask.abort(403)


def generate_filename(fileobj):
    """Generate a unique filename for the uploaded file."""
    stem = uuid.uuid4().hex
    suffix = pathlib.Path(fileobj.filename).suffix.lower()
    return f"{stem}{suffix}"


def save_file(fileobj, filename):
    """Save the uploaded file to the configured UPLOAD_FOLDER."""
    path = ccp.app.config["UPLOAD_FOLDER"] / filename
    fileobj.save(path)
    return filename


def hash_password(password):
    """Hash the provided password."""
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    m = hashlib.new(algorithm)
    m.update((salt + password).encode('utf-8'))
    return "$".join([algorithm, salt, m.hexdigest()])


def insert_user(username, fullname, email, filename, password_db_string):
    """Insert a new user into the database."""
    connection = ccp.model.get_db()
    image_description = "Image of {}".format(fullname)
    connection.execute(
        "INSERT INTO users"
        "(username, fullname, email, filename, password, alt) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (username, fullname, email, filename, password_db_string, image_description)
    )
    connection.commit()


def handle_create():
    """Handle the create operation."""
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('edit'))
    fullname = flask.request.form['fullname']
    email = flask.request.form['email']
    password = flask.request.form['password']
    fileobj = flask.request.files["file"]
    username = flask.request.form['username']
    empty1 = not fullname or not email or not password
    empty2 = not fileobj or not username
    if (empty1 or empty2):
        flask.abort(400) 
    connection = ccp.model.get_db()
    cur = connection.execute(
        "SELECT username "
        "FROM users "
        "WHERE username=?",
        (username, )
    )
    if cur.fetchone():
        flask.abort(409)
    filename = generate_filename(fileobj)
    filename = save_file(fileobj, filename)
    password_db_string = hash_password(password)
    insert_user(username, fullname, email, filename, password_db_string)
    flask.session['username'] = username


def handle_edit_account():
    """Handle the edit_account operation."""
    connection = ccp.model.get_db()
    cur_user = connection.execute(
        "SELECT "
        "username, "
        "fullname, "
        "email, "
        "filename "
        "FROM users WHERE username = ?",
        (flask.session['username'],)
    ).fetchone()

    username = cur_user['username']
    fileobj = flask.request.files["file"]
    fullname = flask.request.form['fullname']
    email = flask.request.form['email']

    if not (fullname and email):
        flask.abort(400)

    if fileobj:
        stem = uuid.uuid4().hex
        suffix = pathlib.Path(fileobj.filename).suffix.lower()
        uuid_basename = f"{stem}{suffix}"
        file_path = ccp.app.config["UPLOAD_FOLDER"] / uuid_basename
        fileobj.save(file_path)

        old_file_path = (
            ccp.app.config["UPLOAD_FOLDER"] /
            cur_user['filename']
        )
        if os.path.exists(old_file_path):
            os.remove(old_file_path)
    else:
        uuid_basename = cur_user['filename']

    connection.execute(
        "UPDATE users "
        "SET fullname = ?, email = ?, filename = ? "
        "WHERE username = ?",
        (fullname, email, uuid_basename, username)
    )
    connection.commit()


def handle_delete(target):
    """Handle the delete operation."""
    connection = ccp.model.get_db()
    username = flask.session['username']

    results = connection.execute(
        "SELECT "
        "u.filename AS filename, "
        "p.filename AS filename "
        "FROM users u "
        "LEFT JOIN pets p ON u.username = p.owner "
        "LEFT JOIN comments c ON u.username = c.owner "
        "LEFT JOIN following f ON u.username = f.username1 "
        "LEFT JOIN likes l ON u.username = l.owner "
        "WHERE u.username = ? ",
        (username,)
    ).fetchall()

    if results:
        for result in results:
            filename = result['filename']
            upload_folder = ccp.app.config['UPLOAD_FOLDER']
            file_path = os.path.join(upload_folder, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
    connection.execute("DELETE FROM likes WHERE owner = ?", (username,))
    connection.execute("DELETE FROM comments WHERE owner = ?", (username,))
    connection.execute("DELETE FROM posts WHERE owner = ?", (username,))
    connection.execute("DELETE FROM following "
                       "WHERE username1 = ? OR username2 = ?",
                       (username, username))
    connection.execute("DELETE FROM users WHERE username = ?", (username,))
    connection.commit()
    flask.session.pop('username', None)
    return flask.redirect(target)


def handle_update_password():
    """Handle the update_password operation."""
    connection = ccp.model.get_db()
    pw = connection.execute(
        "SELECT password FROM users WHERE username = ?",
        (flask.session['username'],)
    ).fetchone()

    hashed_pw = pw['password']
    new_pw1 = flask.request.form['new_password1']
    new_pw2 = flask.request.form['new_password2']
    if not (new_pw1 or new_pw2 or hashed_pw):
        flask.abort(400)
    verify_password(hashed_pw, flask.request.form['password'])  # fixed to spec

    if new_pw1 != new_pw2:
        flask.abort(401)  # fixed to spec
    if "$" in hashed_pw:
        algorithm, stored_salt, stored_hashed_password = hashed_pw.split('$')
        m = hashlib.new(algorithm)
        password_to_hash = stored_salt + flask.request.form['password']
        m.update(password_to_hash.encode('utf-8'))
        hashed_password_to_check = m.hexdigest()
    else:
        hashed_password_to_check = flask.request.form['password']
        stored_hashed_password = hashed_pw

    if hashed_password_to_check != stored_hashed_password:
        flask.abort(400)
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    m = hashlib.new(algorithm)
    m.update((salt + new_pw1).encode('utf-8'))
    pw_db_string = "$".join([algorithm, salt, m.hexdigest()])
    username = flask.session['username']
    connection.execute(
        "UPDATE users SET password = ? WHERE username = ?",
        (pw_db_string, username)
    )
    connection.commit()


@ccp.app.route('/accounts/logout/', methods=['POST'])
def logout():
    """Logout routing."""
    print("DEBUG Logout:", flask.session['username'])
    flask.session.clear()
    return flask.redirect(flask.url_for('show_login'))


@ccp.app.route('/accounts/create/', methods=['GET'])
def create():
    """Create account."""
    # print("DEBUG: test")

    if 'username' in flask.session:
        return flask.redirect(flask.url_for('edit'))
    # If it's a GET request, render the create.html template
    return flask.render_template("/accounts/create.html")


@ccp.app.route('/accounts/login/', methods=['GET'])
def show_login():
    """Login page."""
    return flask.render_template("/accounts/login.html")


@ccp.app.route('/accounts/edit/', methods=['GET'])
def edit():
    """Edit account."""
    if 'username' not in flask.session:
        flask.abort(403)

    print("DEBUG edit function")
    # Get the current user's information
    connection = ccp.model.get_db()
    cur_user = connection.execute(
        "SELECT "
        "username, "
        "fullname, "
        "email, "
        "filename "
        "FROM users WHERE username = ?",
        (flask.session['username'],)
    ).fetchone()

    context = {
        "logname": cur_user['username'],
        "fullname": cur_user['fullname'],
        "email": cur_user['email'],
        "user_image": cur_user['filename'],
    }
    return flask.render_template("/accounts/edit.html", **context)


@ccp.app.route('/accounts/password/')
def show_password():
    """Show password change form."""
    context = {
        "logname": flask.session['username']
    }
    # print(flask.session['username'])
    return flask.render_template("/accounts/password.html", **context)


@ccp.app.route('/accounts/delete/')
def show_delete():
    """Show delete account confirmation."""
    return flask.render_template("/accounts/delete.html")


@ccp.app.route('/accounts/auth/')
def show_auth():
    """Authenticate."""
    if 'username' not in flask.session:
        abort(403)
    else:
        auth_message = "User is authenticated."
        response = flask.make_response(auth_message)
        response.status_code = 200
        return response
