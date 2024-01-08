from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz', methods=['POST'])
def quiz():
    score = 0
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']

    if q1 == '1147':
        score += 1
    if q2.lower() == 'париж':
        score += 1
    if q3.lower() == 'раскольников':
        score += 1

    return render_template('quiz.html', score=score)


if __name__ == '__main__':
    app.run(debug=True)
