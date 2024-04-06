"""
CCP travel view.

URLs include:
/travel/
"""
import flask
from flask import send_from_directory
import ccp

ccp.app.secret_key = (
    b'w\xb7\xc5\xd4\x98D\xe8v\xa7\xd0\x9b{\xd7Uq' +
    b'\x14\x0c\xae\xca\xc8\xca\xd9r\x01'
)


@ccp.app.route("/travel/")
def show_travels():
    """Travel page default view."""
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

    cur_travels = connection.execute(
        "SELECT "
        "t.travelid, "
        "t.owner AS travel_owner, "
        "t.travelname AS travel_name, "
        "t.location, "
        "m.mainid, "
        "m.still, "
        "m.moving, "
        "m.alt AS main_alt, "
        "u.filename AS user_filename, "
        "u.alt AS user_alt, "
        "u.username, "
        "u.fullname, "
        "tb.travelblurbid, "
        "tb.text AS tb_blurb, "
        "tm.travelmediaid, "
        "tm.filename AS travel_media, "
        "tm.alt AS travel_media_alt, "
        "tm.caption AS travel_media_caption "
        "FROM travel t "
        "LEFT JOIN travel_main m ON t.travelid = m.travelid "
        "LEFT JOIN travel_blurbs tb ON t.travelid = tb.travelid "
        "LEFT JOIN travel_media tm on t.travelid = tm.travelid "
        "JOIN users u ON t.owner = u.username "
        "ORDER BY t.travelid DESC, tb.travelblurbid ASC, tm.travelmediaid ASC",
    )
    rows = cur_travels.fetchall()
    all_travels = {}

    for row in rows:
        travelid = row['travelid']
        if travelid not in all_travels:
            all_travels[travelid] = {
                'travelname': row['travel_name'], 
                'location': row['location'],
                'mainid': row['mainid'],
                'still': row['still'],
                'moving': row['moving'],
                'main_alt': row['main_alt'],
                'travel_owner': row['travel_owner'],
                'owner_filename': row['user_filename'],
                'owner_alt': row['user_alt'],
                'username': row['username'],
                'fullname': row['fullname'],
                'blurbs': [],
                'medias': []
            }
        if row['travelblurbid'] and row['travelblurbid']:
            existing_blurb_ids = {blurb['blurb_id'] for blurb in all_travels[travelid]['blurbs']}
            if row['travelblurbid'] not in existing_blurb_ids:
                all_travels[travelid]['blurbs'].append({
                    'blurb_text': row['tb_blurb'],
                    'blurb_id': row['travelblurbid']
                })
        if row['travelmediaid'] and row['travelmediaid']:
            existing_media_ids = {media['media_id'] for media in all_travels[travelid]['medias']}
            if row['travelmediaid'] not in existing_media_ids:
                all_travels[travelid]['medias'].append({
                    'media_filename': row['travel_media'],
                    'media_alt': row['travel_media_alt'],
                    'media_id': row['travelmediaid'],
                    'caption': row['travel_media_caption']
                })

    all_travels = list(all_travels.values())

    context = {
        "logname": logname, 
        "users": users,
        "travels": all_travels
    }
    return flask.render_template("travel.html", **context)


@ccp.app.route('/travel/<path:filename>')
def download_travel_file(filename):
    """Display /uploads/ route."""
    # if 'username' not in flask.session:
    #    flask.abort(403)
    return send_from_directory(
        ccp.app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )