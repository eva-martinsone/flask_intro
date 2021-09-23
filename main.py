from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Sveiki!!!'

@app.route('/kontakti')
def kontakti():
    return '<html><h1>Kontakti</h1><p>Eva Martinsone</p></html>'

if __name__ == '__main__':
    app.run(port=80, debug=True)
