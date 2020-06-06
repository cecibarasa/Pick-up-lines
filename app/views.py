from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''

    message = 'Pitches'
    return render_template('index.html', message=message)
    
@app.route('/pitch/<int:pitch_id')
def pitch(pitch_id):
    '''
    view pitch function that returns pitch categories
    '''

    return render_template('pitch.html', id = pitch_id)    