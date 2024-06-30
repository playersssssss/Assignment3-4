from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class DataCollectionForm(FlaskForm):
    # Define fields for the form
    name = StringField('Name', validators=[DataRequired()])  # Text field for name, required
    age = IntegerField('Age', validators=[DataRequired()])  # Integer field for age, required
    email = EmailField('Email', validators=[DataRequired(), Email()])  # Email field, required and validated
    grades = StringField('Grades Obtained')  # Text field for grades obtained, optional
    feedback = TextAreaField('Feedback', validators=[DataRequired()])  # Text area for feedback, required
    satisfaction = SelectField('Overall Satisfaction',
                               choices=[
                                   ('very_satisfied', 'Very Satisfied'),  # Choices for satisfaction level
                                   ('satisfied', 'Satisfied'),
                                   ('neutral', 'Neutral'),
                                   ('unsatisfied', 'Unsatisfied'),
                                   ('very-unsatisfied', 'Very Unsatisfied')
                               ],
                               validators=[DataRequired()])  # Dropdown selection, required
    submit = SubmitField('Submit')
