from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def calcoloGeo():
  return render_template("tre_3.html", methods = ['GET']) 

@app.route('/risultato',methods=['get'])
def risultato():
    latoQ = float(request.args.get('latoQ'))
    calcolo = latoQ * latoQ
    calcolo2 = (latoQ**2) + (latoQ**2)
    tipo = int(request.args.get('primo'))

    def doppietta(a):
        if tipo == 0:
             calcolo = a * a
        elif tipo == 1:
            calcolo = (a**2) + (a**2)
        return calcolo

    return render_template('tre_3Risultato.html',calcolo=doppietta(latoQ))
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)