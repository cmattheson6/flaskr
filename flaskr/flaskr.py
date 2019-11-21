from flask import Flask, url_for, session, render_template, flash, request, redirect

# configuration
DATABASE = ''
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'change me'

app = Flask(__name__)
app.config.from_pyfile('_config.py')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """user login/authentication/session management"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """user logout/authentication/session management"""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

