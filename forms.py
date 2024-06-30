from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class DataCollectionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    grades = StringField('Grades Obtained')
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction',
                               choices=[
                                   ('very_satisfied', 'Very Satisfied'),
                                   ('satisfied', 'Satisfied'),
                                   ('neutral', 'Neutral'),
                                   ('unsatisfied', 'Unsatisfied'),
                                   ('very-unsatisfied', 'Very Unsatisfied')
                               ],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')
