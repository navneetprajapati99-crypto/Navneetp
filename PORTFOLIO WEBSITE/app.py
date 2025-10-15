from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/work')
def work():
    return render_template('work.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/service')
def service():
    return render_template('service.html')


if __name__ == '__main__':
    app.run(debug=True)
