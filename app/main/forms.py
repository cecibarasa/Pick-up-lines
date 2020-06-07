from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,RadioField
from wtforms.validators import Required

class Pitch_Form(FlaskForm):
    title = StringField('Title', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    content = TextAreaField('Write Pitch', validators=[Required()])  
    category = RadioField('Pick Category', choices=[('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Interview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promotion Pitch', 'Promotion Pitch')], validators=[Required()])  
    submit = SubmitField('Submit')

class Update_Profile(FlaskForm):
    bio = TextAreaField('Add something more about Yourself...', validators = [Required()])
    submit = SubmitField('Submit')
class CommentsForm(FlaskForm):
   comment = TextAreaField('comment on the post',validators=[Required()])
   submit = SubmitField('Add Comment')