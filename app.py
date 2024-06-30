from flask import Flask, render_template, redirect, url_for
from forms import DataCollectionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/information')
def information():
    return render_template('information.html')


@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()
    if form.validate_on_submit():
        # 处理表单数据，例如保存到文件
        with open('data.txt', 'a') as file:
            file.write(f"Name: {form.name.data}\n")
            file.write(f"Age: {form.age.data}\n")
            file.write(f"Email: {form.email.data}\n")
            file.write(f"Grades: {form.grades.data}\n")
            file.write(f"Feedback: {form.feedback.data}\n")
            file.write(f'Satisfaction:{form.satisfaction.data}\n\n')
        return redirect(url_for('data_collection'))
    return render_template('data_collection.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
