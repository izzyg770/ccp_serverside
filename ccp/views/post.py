import flask
import ccp
import os


ccp.app.secret_key = (
    b'w\xb7\xc5\xd4\x98D\xe8v\xa7\xd0\x9b{\xd7Uq' +
    b'\x14\x0c\xae\xca\xc8\xca\xd9r\x01'
)

@ccp.app.route('/posts/', methods=['POST'])
def create_post():
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    logname = flask.session['username']

    if 'create_post' in flask.request.form:
        post_type = flask.request.form.get('post_type')
        file = flask.request.files['file']
        alt_text = flask.request.form.get('alt_text')

        file_path = os.path.join(ccp.app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        connection = ccp.model.get_db()
        if post_type == 'pet':
            cursor = connection.cursor()
            petname = flask.request.form.get('petname')
            petlikes = flask.request.form.get('petlikes')
            petblurb = flask.request.form.get('petblurb')
            cursor.execute("INSERT INTO pets (petname, filename, alt, owner) VALUES (?, ?, ?, ?)",
               (petname, file_path, alt_text, logname))
            petid = cursor.lastrowid
            cursor.execute("INSERT INTO petlikes (petid, text) VALUES (?, ?)",
               (petid, petlikes))
            cursor.execute("INSERT INTO petblurbs (petid, text) VALUES (?, ?)",
                        (petid, petblurb))
            cursor.close()

        elif post_type == 'travel':
            connection.execute("INSERT INTO travel (travelname, filename) VALUES (?, ?, ?, ? )", (file.filename, file_path, alt_text, logname))
        elif post_type == 'recipe':
            connection.execute("INSERT INTO recipes (recipename, filename) VALUES (?, ?, ?, ? )", (file.filename, file_path, alt_text, logname))

        connection.commit()

        return flask.redirect('/')
    else:
        return flask.abort(400)
