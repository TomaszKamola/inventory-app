from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# table_data = {
#     'name': [
#         'Random1',
#         'Random2',
#         'Random3'
#     ],
#     'value': [
#         12.34,
#         34.56,
#         56.78
#     ],
#     'description': [
#         'Some text for random1',
#         'Some text for random2',
#         'Some text for random3'
#     ]
# }

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
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