"""
CCP index view.

URLs include:
/
"""
import flask
import ccp


@ccp.app.route('/')
def show_index():
    """Index page view showing summaries of pets, recipes, and travels."""

    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    
    connection = ccp.model.get_db()
    logname = flask.session['username']

    pets = connection.execute(
        "SELECT petid, petname FROM pets ORDER BY petid ASC LIMIT 5"
    ).fetchall()

    recipes = connection.execute(
        "SELECT recipeid, recipename FROM recipes ORDER BY recipeid ASC LIMIT 5"
    ).fetchall()

    travels = connection.execute(
        "SELECT travelid, travelname FROM travel ORDER BY travelid ASC LIMIT 5"
    ).fetchall()

    context = {
        "logname": logname,
        "pets": pets,
        "recipes": recipes,
        "travels": travels
    }
    return flask.render_template("index.html", **context)