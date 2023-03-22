from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def calcoloGeo():
  return render_template("uno_1.html", methods = ['GET']) 

@app.route('/risultato',methods=['get'])
def risultato():
    latoQ = float(request.args.get('latoQ'))
    calcolo = latoQ * latoQ
    return render_template('uno_2Risultato.html',calcolo=calcolo)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)