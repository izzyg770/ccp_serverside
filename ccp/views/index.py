"""
CCP index view.

URLs include:
/
"""
import flask
import ccp


@ccp.app.route('/')
def show_index():
    """Index view."""
    # if 'username' not in flask.session:
    #    return flask.redirect(flask.url_for('show_login'))

    connection = ccp.model.get_db()

    logname = flask.session['username']
    # Query users that the logged-in user is not following
    cur_users = connection.execute(
        "SELECT "
        "u.username, "
        "u.fullname, "
        "u.filename, "
        "u.alt "
        "FROM users u "
        "WHERE username != ? AND username NOT IN "
        "(SELECT username2 FROM following WHERE username1 = ?)",
        (logname, logname)
    )
    # Fetch all the users
    users = cur_users.fetchall()

    user_data = []
    for user in users:
        username = user['username']
        fullname = user['fullname']
        user_image = user['filename']
        user_alt = user['alt']
        user_data.append({
            'username': username,
            'fullname': fullname,
            'user_image': user_image,
            'user_alt': user_alt,
        })
    context = {
        "logname": logname,
        "users": user_data,
    }
    # Render the explore template with the user data
    return flask.render_template("index.html", **context)
