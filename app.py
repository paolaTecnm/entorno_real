from flask import Flask

#crear instancia
app= Flask(__name__)

#ruta raíz
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'

if __name__== '__main__':
    app.run(debug=True)