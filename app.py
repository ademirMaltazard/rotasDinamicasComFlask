from flask import Flask, render_template
from data import dados, media, addCarros

app = Flask(__name__)

mediaIdade = media('idade')
tag = 'Familia'

@app.route('/')
def homePage():
    return render_template(
        'homePage.html',
        dados=dados,
        mediaIdade=mediaIdade,
        tag=tag,
        carros=addCarros()
    )

@app.route('/curriculo')
def showCurriculo():
    return render_template('index.html')

@app.route('/add/contato/')
def adicionarContato():
    return 'page'

if __name__ == "__main__":
    app.run(debug=True)
