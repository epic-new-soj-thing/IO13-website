from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def hello_world():
	return "hello world"

from flask import Flask, request, render_template

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}, POST request received"
    return render_template('name.html')

if __name__ == '__main__':
    app.run(host="217.174.245.131")