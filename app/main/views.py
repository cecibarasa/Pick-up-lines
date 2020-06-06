from flask import render_template
from . import main

#Views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''

    title = 'Home - Welcome to The Pitches of The Century'
    return render_template('index.html', title = title)
    
@main.route('/pitch', methods=['GET', 'POST'])
@login_required
def pitch():
    '''
    view pitch function that returns pitch categories
    '''

    return render_template('pitch.html')    