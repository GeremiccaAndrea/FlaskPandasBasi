from flask import Flask, request, render_template
app = Flask(__name__)

import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep = ";")


@app.route('/')
def home():
    lingue = list(set(df['Language'])) #creiamo una lista con tutte le lingue e togliamo i duplicati con set 
    return render_template('index.html', lista = lingue)

@app.route('/Es1')
def Es1():
    dfFilmInglesi = df[df['Language'] == 'English'][['Title']].to_html() # trasforma il dataframe di python in una tabella html
    return render_template('risultato.html', tabella = dfFilmInglesi)


@app.route('/Es2', methods = ['GET'])
def Es2():
    InserisciLingua = request.args.get('lingua')
    dflinguaUtente = df[df['Language'] == InserisciLingua][['Title']].to_html()
    return render_template('risultato.html', tabella = dflinguaUtente)


@app.route('/Es3', methods = ['GET'])
def Es3():
    InserisciLinguaRadio = request.args.get('lingueRadio')
    dflinguaUtenteRadio = df[df['Language'] == InserisciLinguaRadio][['Title']].to_html()
    return render_template('risultato.html', tabella = dflinguaUtenteRadio)


@app.route('/Es4', methods = ['GET'])
def Es4():
    InserisciLinguaCheckBox = request.args.getlist('lingueCheckBox') #getlist perchè posso selezionare una o più lingue
    dflinguaUtenteCheckBox = df[df['Language'].isin(InserisciLinguaCheckBox)][['Title']].to_html() #.isin serve per confrontare le lingue scelte nella checkbox (conforonto degli elementi di una lista)
    return render_template('risultato.html', tabella = dflinguaUtenteCheckBox)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)