from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['get'])
def calcoloGeo():
  return render_template("due_2.html") 

@app.route('/risultato',methods=['post'])
def risultato():
    latoQ = float(request.form['latoQ'])
    calcolo = latoQ * latoQ
    return render_template('due_2Risultato.html',calcolo=calcolo)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)