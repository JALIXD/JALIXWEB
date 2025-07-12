from flask import Flask, render_template, request
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    cancion = request.form['cancion']
    dedicatoria = request.form['dedicatoria']
    mensaje = request.form['mensaje']
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar los datos en un archivo CSV
    with open('peticiones.csv', 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([fecha, nombre, cancion, dedicatoria, mensaje])

    return render_template('gracias.html')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

@app.route('/ver-peticiones')
def ver_peticiones():
    peticiones = []
    try:
        with open('peticiones.csv', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                peticiones.append(fila)
    except FileNotFoundError:
        pass

    return render_template('ver_peticiones.html', peticiones=peticiones)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
