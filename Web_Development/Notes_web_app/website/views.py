# for the main views or url end points

from flask import Blueprint,render_template , request ,flash ,jsonify      # defining this file is a blueprint of out application which mean it contains multiple routes in it
from flask_login import  login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views',__name__)  # 

@views.route('/', methods=['Get','POST'])    # defining a route
@login_required
def home():          # home page route   
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash ('Note is too Short!', category='error')
        else :
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash ("Note Added!", category='success' )

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
