from flask import Flask, render_template

app = Flask('UniversalWebMailClient')


@app.route('/')
def root():
    return '<h1>Universal Web Mail Client</h1>'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
