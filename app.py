from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Colunm(db.Integer, primary_key=True)
    title = db.Column(db.Sring(100), nullable=False)
    intro = db.Column(db.Sring(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


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
