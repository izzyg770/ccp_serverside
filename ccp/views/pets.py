"""
CCP pet view.

URLs include:
/pets/
"""
import flask
from flask import send_from_directory
import ccp

ccp.app.secret_key = (
    b'w\xb7\xc5\xd4\x98D\xe8v\xa7\xd0\x9b{\xd7Uq' +
    b'\x14\x0c\xae\xca\xc8\xca\xd9r\x01'
)


@ccp.app.route("/pets/")
def show_pets():
    """Pets page default view."""
    # if 'username' not in flask.session:
    #    return flask.redirect(flask.url_for('show_login'))
    
    connection = ccp.model.get_db()
    logname = flask.session['username']
    cur_user = connection.execute(
        "SELECT username, fullname, filename, alt "
        "FROM users "
        "WHERE username != ?",
        (logname, )
    )
    users = cur_user.fetchall()

    cur_pets = connection.execute(
        "SELECT "
        "p.petid, "
        "p.owner AS pet_owner, " 
        "p.petname AS pet_name, "
        "p.filename AS pet_filename, "
        "p.alt AS pet_alt, "
        "u.filename AS user_filename, "
        "u.alt AS user_alt, "
        "u.username, "
        "u.fullname, "
        "pl.petlikeid, "
        "pl.text AS pl_like, "
        "pb.petblurbid, "
        "pb.text AS pb_blurb, "
        "pm.petmediaid, "
        "pm.filename AS pet_media, "
        "pm.alt AS pet_media_alt "
        "FROM pets p "
        "LEFT JOIN pet_likes pl ON p.petid = pl.petid "
        "LEFT JOIN pet_blurbs pb ON p.petid = pb.petid "
        "LEFT JOIN pet_media pm on p.petid = pm.petid "
        "JOIN users u ON p.owner = u.username "
        # "GROUP BY p.petid, p.owner, p.petname, p.filename, p.alt, u.filename, u.alt, u.username, u.fullname "
        "ORDER BY p.petid ASC, pl.petlikeid ASC, pb.petblurbid ASC, pm.petmediaid ASC",
    )
    rows = cur_pets.fetchall()
    all_pets = {}
    for row in rows:
        pet_id = row['petid']
        if pet_id not in all_pets:
            all_pets[pet_id] = {
                'pet_id': pet_id,
                'pet_name': row['pet_name'],
                'pet_filename': row['pet_filename'],
                'pet_alt': row['pet_alt'],
                'likes': [],
                'blurbs': [],
                'medias': []
            }
        if row['petlikeid'] and row['petlikeid'] not in (like['like_id'] for like in all_pets[pet_id]['likes']):
            all_pets[pet_id]['likes'].append({
                'like_text': row['pl_like'],
                'like_id': row['petlikeid']
            })
        if row['petblurbid'] and row['petblurbid'] not in (blurb['blurb_id'] for blurb in all_pets[pet_id]['blurbs']):
            all_pets[pet_id]['blurbs'].append({
                'blurb_text': row['pb_blurb'],
                'blurb_id': row['petblurbid']
            })
        if row['petmediaid'] and row['petmediaid'] not in (media['media_id'] for media in all_pets[pet_id]['medias']):
            all_pets[pet_id]['medias'].append({
                'media_filename': row['pet_media'],
                'media_alt': row['pet_media_alt'],
                'media_id': row['petmediaid']
            })

    all_pets = list(all_pets.values())

    context = {
        "logname": logname, 
        "users": users,
        "pets": all_pets
    }
    return flask.render_template("pets.html", **context)

@ccp.app.route('/pets/<path:filename>')
def download_pet_file(filename):
    """Display /uploads/ route."""
    # if 'username' not in flask.session:
    #    flask.abort(403)
    return send_from_directory(
        ccp.app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )
