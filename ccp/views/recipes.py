"""
CCP recipes view.

URLs include:
/recipes/
"""
import flask
from flask import send_from_directory
import ccp

ccp.app.secret_key = (
    b'w\xb7\xc5\xd4\x98D\xe8v\xa7\xd0\x9b{\xd7Uq' +
    b'\x14\x0c\xae\xca\xc8\xca\xd9r\x01'
)


@ccp.app.route("/recipes/")
def show_recipes():
    """Recipes page default view."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    
    connection = ccp.model.get_db()
    logname = flask.session['username']
    cur_user = connection.execute(
        "SELECT username, fullname, filename, alt "
        "FROM users "
        "WHERE username != ?",
        (logname, )
    )
    users = cur_user.fetchall()

    cur_recipes = connection.execute(
        "SELECT "
        "r.recipeid, "
        "r.recipename, "
        "r.origin, "
        "r.source, "
        "r.category, "
        "r.filename AS recipe_filename, "
        "r.alt AS recipe_alt, "
        "r.owner AS recipe_owner, "
        "u.filename AS user_filename, "
        "u.alt AS user_alt, "
        "u.username, "
        "u.fullname, "
        "rb.recipeblurbid  AS recipeblurbid, "
        "rb.text AS rb_blurb, "
        "i.ingredientid AS ingredientid, "
        "i.text AS ingredient, "
        "s.stepid  AS stepid, "
        "s.text AS step, "
        "rm.recipemediaid AS recipemediaid, "
        "rm.filename AS recipe_media, "
        "rm.alt AS recipe_media_alt "
        "FROM recipes r "
        "LEFT JOIN recipe_blurbs rb ON r.recipeid = rb.recipeid "
        "LEFT JOIN ingredients i ON r.recipeid = i.recipeid "
        "LEFT JOIN steps s ON r.recipeid = s.recipeid "
        "LEFT JOIN recipe_media rm on r.recipeid = rm.recipeid "
        "JOIN users u ON r.owner = u.username "
        "ORDER BY r.recipeid ASC, rb.recipeblurbid ASC, i.ingredientid ASC, s.stepid ASC, rm.recipemediaid ASC",
    )
    rows = cur_recipes.fetchall()
    all_recipes = {}

    for row in rows:
        recipe_id = row['recipeid']
        if recipe_id not in all_recipes:
            all_recipes[recipe_id] = {
                'recipeid': row['recipeid'],
                'recipe_name': row['recipename'],
                'recipe_filename': row['recipe_filename'],
                'recipe_alt': row['recipe_alt'],
                'recipe_owner': row['recipe_owner'],
                'owner_filename': row['user_filename'],
                'owner_alt': row['user_alt'],
                'username': row['username'],
                'fullname': row['fullname'],
                'origin': row['origin'],
                'source': row['source'],
                'category': row['category'],
                'blurbs': [],
                'ingredients': [],
                'steps': [],
                'medias': []
            }
        if 'recipeblurbid' in row and row['recipeblurbid']:
            existing_blurb_ids = {blurb['blurb_id'] for blurb in all_recipes[recipe_id]['blurbs']}
            if row['recipeblurbid'] not in existing_blurb_ids:
                all_recipes[recipe_id]['blurbs'].append({
                    'blurb_text': row['rb_blurb'],
                    'blurb_id': row['recipeblurbid']
                })
        if row['ingredientid'] and row['ingredientid']:
            existing_ingredient_ids = {ingredient['ingredient_id'] for ingredient in all_recipes[recipe_id]['ingredients']}
            if row['ingredientid'] not in existing_ingredient_ids:
                all_recipes[recipe_id]['ingredients'].append({
                    'ingredient': row['ingredient'],
                    'ingredient_id': row['ingredientid']
                })
        if row['stepid'] and row['stepid']:
            existing_step_ids = {step['step_id'] for step in all_recipes[recipe_id]['steps']}
            if row['stepid'] not in existing_step_ids:
                all_recipes[recipe_id]['steps'].append({
                    'step': row['step'],
                    'step_id': row['stepid']
                })
        if row['recipemediaid'] and row['recipemediaid']:
            existing_media_ids = {media['media_id'] for media in all_recipes[recipe_id]['medias']}
            if row['recipemediaid'] not in existing_media_ids:
                all_recipes[recipe_id]['medias'].append({
                    'media_filename': row['recipe_media'],
                    'media_alt': row['recipe_media_alt'],
                    'media_id': row['recipemediaid']
                })

    all_recipes = list(all_recipes.values())

    context = {
        "logname": logname, 
        "users": users,
        "recipes": all_recipes
    }
    return flask.render_template("recipes.html", **context)

@ccp.app.route('/recipes/<path:filename>')
def download_recipe_file(filename):
    """Display /uploads/ route."""
    # if 'username' not in flask.session:
    #    flask.abort(403)
    return send_from_directory(
        ccp.app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )

