from flask import Flask, render_template, request, redirect
from file_proc import pievienot, lasitRindinas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/kontakti')
def kontakti():
    status = request.args.get('status')
    return render_template('kontakti.html', veiksmigi = status)

@app.route('/parmani')
def parmani():
    return render_template('parmani.html')

@app.route('/jaunumi')
def jaunumi():
    return render_template('jaunumi.html')

@app.route('/postData', methods = ['POST', 'GET'])
def postData():
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        #print(request.form)
        vards = request.form.get('vards')
        pievienot(vards)
        return redirect('/kontakti?status=1')
    else:
        return "This method not supported!"

@app.route('/lasitDatus')
def lasitDatus():
    rindinas = lasitRindinas()
    dati = []
    dati2 = []
    for rindina in rindinas:
        ieraksts = rindina.split(',')
        #print(rindina)
        #print(ieraksts)
        dati.append(ieraksts)
        dati2.append({'vards':ieraksts[0], 'uzvards':ieraksts[1], 'hobijs':ieraksts[2]})

    #print(dati)
    return render_template("dati.html", rindinas = dati, rindinas2 = dati2)


if __name__ == '__main__':
    app.run(port=80, debug=True)