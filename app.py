from flask import Flask, render_template, redirect, url_for
from forms import DataCollectionForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for CSRF protection


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/information')
def information():
    return render_template('information.html')


@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()  # Creating an instance of DataCollectionForm
    if form.validate_on_submit():  # If the form is submitted and passes validation
        # Handling form data, for example, saving it to a file
        with open('data.txt', 'a') as file:
            file.write(f"Name: {form.name.data}\n")
            file.write(f"Age: {form.age.data}\n")
            file.write(f"Email: {form.email.data}\n")
            file.write(f"Grades: {form.grades.data}\n")
            file.write(f"Feedback: {form.feedback.data}\n")
            file.write(f'Satisfaction:{form.satisfaction.data}\n\n')
        return redirect(url_for('data_collection'))
    # Redirects back to the data_collection route
    return render_template('data_collection.html', form=form)


# Renders the data_collection.html template with the form object

if __name__ == '__main__':
    app.run(debug=True)
