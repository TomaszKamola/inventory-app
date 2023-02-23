from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

@app.route("/")
@app.route("/home")
def hello():
    return render_template(
        'home.html'
    )

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)