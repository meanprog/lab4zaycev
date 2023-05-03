from flask import Flask, render_template, request
import cmath
import mymath

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        num_1 = int(request.form.get('num_1'))
        num_2 = int(request.form.get('num_2'))
        num_3 = int(request.form.get('num_3'))
    return render_template('index.html', sol=mymath.quadratic_equation(num_1, num_2, num_3))


if __name__ == '__main__':
    app.run()