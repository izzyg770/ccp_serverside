"""CCP model (database) API."""
import flask
import ccp


def dict_factory(cursor, row):
    """Convert database row objects to a dictionary keyed on column name.

    This is useful for building dictionaries which are then used to render a
    template.  Note that this would be inefficient for large queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def get_all_users():
    """Get all users from DB."""
    connection = ccp.model.get_db()
    cur = connection.execute(
        "SELECT * FROM users"
    )
    return cur.fetchall()


def get_one_user(username):
    """Get one user from DB."""
    connection = ccp.model.get_db()
    cur = connection.execute(
        "SELECT * FROM users "
        "WHERE username=?",
        (username, )
    )
    return cur.fetchone()


def get_one_pet(petid): 
    """Get post from db."""
    connection = ccp.model.get_db()
    cur = connection.execute(
        "SELECT * FROM pets "
        "WHERE petid=?",
        (petid, )
    )
    if cur is None:
        context = {
            "message": "Not Found",
            "status_code": 404
        }
        return flask.jsonify(**context), 404
    return cur.fetchone()


def create_user(username, description):
    """Create user in DB."""
    connection = ccp.model.get_db()
    connection.execute(
        "INSERT INTO users(username, description) "
        "VALUES (?, ?)",
        (username, description)
    )
    connection.commit()
    new_user = {"username": username, "description": description}
    return new_user


def update_description(username, description):
    """Update description from DB."""
    connection = ccp.model.get_db()
    connection.execute(
        "UPDATE users "
        "SET description=? "
        "WHERE username=?",
        (description, username)
    )
    connection.commit()
    return ''


def delete_user(username):
    """Delete user from DB."""
    connection = ccp.model.get_db()
    connection.execute(
        "DELETE FROM users "
        "WHERE username=?",
        (username,)
    )
    connection.commit()
    return ''


def get_likeid(postid, username):
    """Get the ID of the like for a specific post and user."""
    connection = ccp.model.get_db()
    cur = connection.execute(
        "SELECT likeid FROM likes "
        "WHERE postid = ? AND owner = ?",
        (postid, username)
    )
    row = cur.fetchone()
    if row is not None:
        return row["likeid"]
    return None


def create_like(postid, username):
    """Create a new like for a specific post."""
    connection = ccp.model.get_db()
    connection.execute(
        "INSERT INTO likes (postid, owner) "
        "VALUES (?, ?)",
        (postid, username)
    )
    connection.commit()
    likeid = get_likeid(postid, username)
    return likeid


def get_commentid(postid, username, text):
    """Get the ID of the like for a specific post and user."""
    connection = ccp.model.get_db()
    cur = connection.execute(
        "SELECT commentid FROM comments "
        "WHERE postid = ? AND owner = ? AND text = ?",
        (postid, username, text)
    )
    row = cur.fetchone()
    if row is not None:
        return row["commentid"]
    return None


def create_comment(postid, username, text):
    """Create a new comment for a specific post."""
    connection = ccp.model.get_db()
    connection.execute(
        "INSERT INTO comments (postid, owner, text) "
        "VALUES (?, ?, ?)",
        (postid, username, text)
    )
    connection.commit()
    comment_id = get_commentid(postid, username, text)
    return comment_id
