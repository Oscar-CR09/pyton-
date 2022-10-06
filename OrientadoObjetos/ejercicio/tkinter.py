from  flask import Flask, render_template



app=Flask(__name__)

@app.route('/')
def index():

    cursos = ['php', 'python', 'java', 'kotlin', 'dart', 'java script' ]
    data={
        "titulo": "Index123",
        "bienvenido":"Saludos",
        "cursos":cursos,
        'numero_cursos':len(cursos)
    }
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True,port=5000)#para que se actualice sin salir
