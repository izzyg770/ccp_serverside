"""
CCP user view.

"""
import flask
from flask import send_from_directory
import ccp


@ccp.app.route('/users/<user_url_slug>/')  # ----complete----
def show_user_profile(user_url_slug):
    """Display /user/ route."""
    # if 'username' not in flask.session:
    #    return flask.redirect(flask.url_for('show_login'))

    connect = ccp.model.get_db()

    logname = flask.session['username']
    # Query database for the specific user and their posts
    cur_user = connect.execute(
        "SELECT "
        "u.username, "
        "u.fullname, "
        "u.filename, "
        "(SELECT COUNT(*) FROM following WHERE username2 = ?) "
        "AS num_followers, "
        "(SELECT COUNT(*) FROM following WHERE username1 = ?) "
        "AS num_following, "
        "(SELECT COUNT(*) FROM following WHERE username1 = ? "
        "AND username2 = ?) AS relationship "
        "FROM users u "
        "WHERE u.username = ?",
        (user_url_slug, user_url_slug, logname, user_url_slug, user_url_slug)
    )
    user = cur_user.fetchone()
    if user is None:
        flask.abort(404)
    else:
        username = user['username']
        fullname = user['fullname']
        filename = user['filename']
        num_followers = user['num_followers']
        num_following = user['num_following']
        relationship = user['relationship']
    # Query for the pets of the specified user
    cur_pets = connect.execute(
        "SELECT petid, petname, filename, alt, owner "
        "FROM pets "
        "WHERE owner = ? "
        "ORDER BY petid ASC",  
        (user_url_slug, )  # Only fetch posts of the specified user
    )
    pets = cur_pets.fetchall()

    # Query for the recipes of the specified user
    cur_recipes = connect.execute(
        "SELECT recipeid, recipename, filename, alt, owner "
        "FROM recipes "
        "WHERE owner = ? "
        "ORDER BY recipeid ASC",  
        (user_url_slug, )  # Only fetch posts of the specified user
    )
    recipes = cur_recipes.fetchall()

    # Query for the travel locations of the specified user
    cur_travels = connect.execute(
        "SELECT t.travelid, t.travelname, t.owner, "
        "m.still, m.alt "  
        "FROM travel t "  
        "LEFT JOIN travel_main m ON m.travelid = t.travelid " 
        "WHERE t.owner = ? " 
        "ORDER BY t.travelid ASC", 
        (user_url_slug, )  
    )
    travels = cur_travels.fetchall()

    # Add database info to context
    context = {
        "logname": logname,
        "username": username,
        'filename': filename,
        "fullname": fullname,
        "relationship": relationship,
        "total_posts": len(pets) + len(recipes) + len(travels),
        "num_followers": num_followers,
        "num_following": num_following,
        "pets": pets,
        "recipes": recipes,
        "travels": travels,
        "user_image": "user_image",
    }
    return flask.render_template("user.html", **context)


@ccp.app.route('/uploads/<path:filename>')
def download_file(filename):
    """Display /uploads/ route."""
    if 'username' not in flask.session:
        flask.abort(403)
    return send_from_directory(
        ccp.app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )


@ccp.app.route('/users/<user_url_slug>/followers/')  
def show_user_followers(user_url_slug):
    """Display /user/ route."""
    if 'username' not in flask.session:
        print('wrong')
        return flask.redirect(flask.url_for('show_login'))
    # Connect to database
    connection = ccp.model.get_db()
    logname = flask.session['username']  # fix after login

    followers = connection.execute(
        f"SELECT u.username AS user, \
            u.filename AS filename, f.username1 AS user1, \
            CASE \
                WHEN EXISTS (SELECT 1 FROM following \
                    WHERE username1 = '{logname}'\
                AND username2 = f.username1) THEN 'Following' \
                ELSE 'Not Following' \
            END AS follow_status \
        FROM users u JOIN following f ON u.username = f.username1 \
        WHERE f.username2 = '{user_url_slug}'"
    )
    # logname = 'awdeorio'
    follows = followers.fetchall()

    # Context dictionary with the required data
    context = {
        "follows": follows,
        "logname": logname,
    }

    return flask.render_template('followers.html', **context)


@ccp.app.route('/users/<user_url_slug>/following/')
def show_user_following(user_url_slug):
    """Display /user/ route."""
    if 'username' not in flask.session:
        print('wrong')
        return flask.redirect(flask.url_for('show_login'))
    # Connect to database
    connection = ccp.model.get_db()
    logname = flask.session['username']  # fix after login

    followings = connection.execute(
        f"SELECT u.username AS user, \
            u.filename AS filename, f.username1 AS user1, \
            CASE \
                WHEN EXISTS (SELECT 1 FROM following \
                    WHERE username1 = '{logname}') THEN 'Following' \
                ELSE 'Not Following' \
            END AS follow_status \
        FROM users u JOIN following f ON u.username = f.username2 \
        WHERE f.username1 = '{user_url_slug}'"
    )
    # logname = 'awdeorio'
    following = followings.fetchall()

    # Context dictionary with the required data
    context = {
        "following": following,
        "logname": logname,
    }

    # Render a template with the context
    return flask.render_template('following.html', **context)
