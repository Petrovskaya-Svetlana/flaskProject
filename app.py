from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):  # put application's code here
    return 'Hello, from user page ' + name + '-' + str(id)


if __name__ == '__main__':
    app.run(debug=True)


