from flask import Flask, render_template, request, session, redirect, url_for, flash
from dataclasses import dataclass
from bootstrap import ERROR


app = Flask('UniversalWebMailClient')
app.secret_key = b'JKtZv7NG,E%5$TJ5]BT:T}NJRU9VTaMe'


@dataclass
class User:
    userid: str
    name: str


@app.route('/')
def mailbox():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    return render_template('mailbox.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    session.pop('user', None)
    if request.method == 'POST':
        user = log_user_in(request.form['uid'], request.form['pwd'])
        if user:
            session['user'] = user
            return redirect(url_for('mailbox'))
        flash('Invalid login.', ERROR)
    return render_template('login.html')


def log_user_in(userid, password):
    # TODO: need a real login implementation
    if userid == password:
        return User(userid, userid.capitalize())
    return None


if __name__ == '__main__':
    app.run()
