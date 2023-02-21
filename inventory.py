from flask import Flask, render_template


table_data = {
    'name': [
        'Random1',
        'Random2',
        'Random3'
    ],
    'value': [
        12.34,
        34.56,
        56.78
    ],
    'description': [
        'Some text for random1',
        'Some text for random2',
        'Some text for random3'
    ]
}

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template(
        'home.html', 
        table_data=table_data, 
        table_len=len(table_data)
    )

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)