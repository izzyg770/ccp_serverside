"""
CCP user view.

"""
import flask
import ccp


@ccp.app.route('/following/', methods=['POST'])
def following_handler():
    """Display following."""
    operation = flask.request.form.get('operation')
    logname = flask.session['username']
    target_username = flask.request.form.get('username')
    connection = ccp.model.get_db()
    if operation == 'follow':
        # Check if the user is already following the target user
        print(logname, "following", target_username)
        existing_follow = connection.execute(
            "SELECT * FROM following WHERE username1 = ? AND username2 = ? ",
            (logname, target_username)
        ).fetchone()

        if existing_follow:
            # User is already following the target user, abort with 409Conflict
            flask.abort(409)
        print(logname, target_username)

        result = connection.execute(
            "SELECT * FROM following WHERE username1 = ? AND username2 = ?",
            (logname, target_username)
        ).fetchone()

        if result:
            connection.execute(
                "UPDATE following "
                "WHERE username1 = ? AND username2 = ?",
                (logname, target_username)
            )
        else:
            connection.execute(
                "INSERT INTO following"
                "(username1, username2) "
                "VALUES (?, ?)",
                (logname, target_username)
            )

        connection.commit()
        return flask.redirect(flask.request.args.get('target', '/'))

    if operation == 'unfollow':
        # Check if the user is not following the target user
        non_existing_follow = connection.execute(
            "SELECT * FROM following WHERE username1 = ? AND username2 = ?",
            (logname, target_username)
        ).fetchone()

        if not non_existing_follow:
            # User is not following the target user, abort with 409 Conflict
            flask.abort(409)

        # Delete the follow relationship from the database
        print(logname, target_username)
        connection.execute(
            "DELETE FROM following WHERE username1 = ? AND username2 = ?",
            (logname, target_username)
        )
        connection.commit()

        return flask.redirect(flask.request.args.get('target', '/'))
    return flask.abort(404)
