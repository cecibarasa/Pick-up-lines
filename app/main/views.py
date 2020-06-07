from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment,Upvote,Downvote
from .form import UpdateProfile, PitchForm, CommentForm
from .. import db,photos

#Views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    pithes = Pitch.query.all()
    pickuplines = Pitch.query.filter_by(category='Pick up lines').all()
    productpitch = Pitch.query.filter_by(category='Product Pitch').all()
    interviewpitch = Pitch.query.filter_by(category='Interview Pitch').all()
    promotionpitch = Pitch.query.filter_by(category='Promotion Pitch').all()

    title = 'Home - Welcome to The Pitches of The Century'
    return render_template('index.html', title = title, pickuplines = pickuplines,productpitch = productpitch,interviewpitch = interviewpitch,promotionpitch = promotionpitch)
    
@main.route('/pitch', methods=['GET', 'POST'])
@login_required
def pitch():
    '''
    view pitch function that returns pitch categories
    '''
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current

    return render_template('pitch.html')


@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))           