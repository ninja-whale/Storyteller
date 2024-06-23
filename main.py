from flask import Flask, render_template, request
from app import inputer

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])

def basic():
    if request.method == 'POST':
        input_link = request.form['input_link']
        caption = inputer(input_link)
        return render_template('index.html', output=caption)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)