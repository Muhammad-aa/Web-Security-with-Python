# vulnerable_app.py
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used to sign session cookies

@app.route('/')
def index():
    if 'username' in session:
        return f'''
            <h1>Welcome, {session["username"]}!</h1>
            <p>You are logged in.</p>
            <a href="/logout">Logout</a>
        '''
    return '''
        <h1>You are not logged in.</h1>
        <a href="/login">Login</a>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # For simplicity, no password verification
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <h1>Login</h1>
        <form method="post">
            <input type="text" name="username" placeholder="Enter username" required>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Running on HTTP on port 5000
    app.run(debug=True, port=5000)
