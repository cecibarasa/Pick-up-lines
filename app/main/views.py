from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .forms import Pitch_Form, Update_Profile,CommentsForm
from .. import db, photos
from flask_login import login_required,current_user

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
    general = Pitch.query.all()
        # return redirect(url_for('main.index'))

    return render_template('pitch.html', general=general)
    
@main.route('/interview')
def interview():
    comment = Comment.query.all()
    interview = Pitch.query.filter_by(category='Interview Pitch').all()
    return render_template('interview.html', comment=comment)

@main.route('/promotion')
def promotion():
    comment = Comment.query.all()
    promotion = Pitch.query.filter_by(category = 'Promotion Pitch').all()
    return render_template('promotion.html',promotion=promotion,comment=comment)

@main.route('/product')
def product():
    comment = Comment.query.all()
    product = Pitch.query.filter_by(category = 'Product Pitch').all()
    return render_template('product.html',product=product,comment=comment)
@main.route('/pickup')
def pickup():
    comments = Comment.query.all()
    pickup = Pitch.query.filter_by(category = 'Pickup Lines').all()
    return render_template('pickup.html', pickup=pickup,comments=comment)        
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username = name).first()
    if user is None:
        abort(404)

    form = Update_Profile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

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

@main.route('/comments/<int:pitch_id>/comment',methods=['GET','POST'])
@login_required
def comment(pitch_id):

    form = CommentsForm()    
    pitch = Pitch.query.filter_by(id=pitch_id).first()
    comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    user = current_user.username
    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data,user_id = current_user.id,pitch_id = pitch.id)
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('main.comment',pitch_id=pitch_id))
    
    return render_template('comments.html', comments=comments, form = form,pitch=pitch,pitch_id=pitch_id,user=user)

@main.route('/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = Pitch_Form()    

    if form.validate_on_submit():
        pitch = Pitch(title = form.title.data, category =form.category.data, content = form.content.data,upvote = 0,downvote = 0,user_id=current_user.id)

        pitch.save_pitch()
        
        return redirect(url_for('main.pitch'))
    
    return render_template('new_pitch.html', pitch_form = form)  



# @main.route('/like/<int:id>',methods = ['POST','GET'])
# @login_required
# def like(id):
#     get_pitches = Upvote.get_upvotes(id)
#     valid_string = f'{current_user.id}:{id}'
#     for pitch in get_pitches:
#         to_str = f'{pitch}'
#         print(valid_string+" "+to_str)
#         if valid_string == to_str:
#             return redirect(url_for('main.index',id=id))
#         else:
#             continue
#     new_vote = Upvote(user = current_user, pitch_id=id)
#     new_vote.save()
#     return redirect(url_for('main.index',id=id))

# @main.route('/dislike/<int:id>',methods = ['POST','GET'])
# @login_required
# def dislike(id):
#     pitch = Downvote.get_downvotes(id)
#     valid_string = f'{current_user.id}:{id}'
#     for p in pitch:
#         to_str = f'{p}'
#         print(valid_string+" "+to_str)
#         if valid_string == to_str:
#             return redirect(url_for('main.index',id=id))
#         else:
#             continue
#     new_downvote = Downvote(user = current_user, pitch_id=id)
#     new_downvote.save()
#     return redirect(url_for('main.index',id = id))
