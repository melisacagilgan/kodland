from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField
from wtforms.validators import DataRequired


class InfoForm(FlaskForm):
    fullname = StringField('What is your name?', validators=[DataRequired()])
    color = RadioField('What is your favorite color?', validators=[DataRequired()], choices=[
        ('1', 'Red'), ('2', 'Blue'), ('3', 'Green')])
    animal = RadioField('What is your favorite animal?', validators=[DataRequired()], choices=[
        ('1', 'Dog'), ('2', 'Cat'), ('3', 'Parrot')])
    hobbies = TextAreaField('Describe your hobbies or interests:', validators=[DataRequired()], render_kw={
        'style': 'text-align: left; width: 300px; height: 100px; resize: both;'})
    submit = SubmitField('Submit Answers')


class QuizForm(FlaskForm):
    q1 = RadioField("Which library is most commonly used for AI development in Python?", validators=[DataRequired()], default="1", choices=[
        ('1', 'NumPy'),
        ('2', 'Pandas'),
        ('3', 'TensorFlow'),
        ('4', 'Requests')
    ])

    q2 = RadioField("Which library is widely used for computer vision tasks in Python?", validators=[DataRequired()], default="1", choices=[
        ('1', 'Matplotlib'),
        ('2', 'OpenCV'),
        ('3', 'Scikit-learn'),
        ('4', 'Flask')
    ])

    q3 = RadioField("Which library is commonly used for natural language processing in Python?", validators=[DataRequired()], default="1", choices=[
        ('1', 'NLTK'),
        ('2', 'BeautifulSoup'),
        ('3', 'Flask'),
        ('4', 'Requests')
    ])

    q4 = RadioField("What is a common method to evaluate machine learning models in Python?", validators=[DataRequired()], default="1", choices=[
        ('1', 'Cross-validation'),
        ('2', 'Debugging'),
        ('3', 'Profiling'),
        ('4', 'Code review')
    ])

    q5 = RadioField("Which technique is used to avoid overfitting in machine learning models?", validators=[DataRequired()], default="1", choices=[
        ('1', 'Regularization'),
        ('2', 'Feature scaling'),
        ('3', 'Data augmentation'),
        ('4', 'Hyperparameter tuning')
    ])
