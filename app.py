from flask import Flask

#crear instancia
app= Flask(__name__)

#ruta raíz
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'

#ruta raíz
@app.route('/alumnos')
def getAlumnos():
    return 'Aquí van los alumnos'

if __name__== '__main__':
    app.run(debug=True)