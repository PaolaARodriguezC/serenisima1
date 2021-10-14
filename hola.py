from flask import Flask
from flask import render_template as render

listado_roles=["Superadministrador","administrador","empleado"]
listado_usuario=["empleado1","empleado2","empleado3","empleado3"]

app = Flask(__name__)
@app.route('/')
def login():
    return render('login.html', methods=["GET", "POST"])




@app.route('/listado/<id_rol>', methods=["GET"])
def listado(id_rol):
    if id_rol == "administrador" or id_rol == "Superadministrador":
       return render('listado.html')           
    else:
       return "no tiene acceso" 

    
@app.route('/visualizar/<id_rol>' , methods=["GET", "POST"])
def visualizar(id_rol):
    if id_rol == "Superadministrador" :
        return render('visualizar.html')
    elif id_rol =="administrador":
        return render('visualizar.html')
    else:
        return render('visualizar.html')


@app.route('/editar', methods=["GET", "POST"])
def editar():
    return render('editar.html')
     
    