from flask import Flask, render_template, flash, redirect, url_for, session, logging, request


from datetime import datetime

app = Flask(__name__, static_url_path='/static')


### Home Route ###
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',)

### About Route ###
@app.route('/about')
def about():
    title = "About"
    return render_template('about.html', title=title)

### Resume Route ###
@app.route('/resume')
def resume():
    title = "Resume"
    return render_template('resume.html', title=title)

### Projects Route ###
@app.route('/projects')
def projects():
    title = "Projects"
    return render_template('projects.html', title=title)

### IoT Health Kit ###
@app.route('/projects/healthkit')
def healthkit():
    title = "IoT Health Kit Monitoring System"
    return render_template('healthkit.html', title=title)


if __name__ == '__main__':
    app.secret_key='mysecretkey'
    app.run(debug=True)
