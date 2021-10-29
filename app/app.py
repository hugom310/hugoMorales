
import os
from sys import getallocatedblocks
from flask import Flask, render_template, request, flash, redirect, jsonify, session
from db import get_db, insert_datos
import yagmail
import utils
from formulario import Contactenos
from message import mensajes
from smtplib import SMTP
import sqlite3
from sqlite3 import Error
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape


app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def index(): 
    return render_template('principal.html')




@app.route('/register', methods=('GET', 'POST'))
def register():
    
    
    if request.method=="POST":
        print('Entrar')
        username = request.form['username']
        password = request.form['password']
        email = request.form['correo']
        name=request.form['nombre']
        password2 = request.form['password2']
        if password != password2:
            error = "Las contraseñas no coinciden"
            flash(error)
            return render_template('register.html')
        else:
            hash_clave = generate_password_hash(password)
            try:
                db= get_db()
                error=None

                print('conexion exitosa')
                print(username)
                print(hash_clave)
                print(email)


                
                if not name: 
                        error= "Debes ingresar el nombre del usuario"
                        flash(error)

                if not utils.isUsernameValid(username):
                    error="El usuario debe ser alfanumerico"
                    flash(error)

                if not utils.isPasswordValid(password):
                    error="La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres"
                    flash(error)
                    return render_template('register.html')

                if not utils.isEmailVaid(email):
                    error="Correo Invalido"
                    flash(error)
                    return render_template('register.html')
                if db.execute('SELECT id FROM usuario2021 WHERE correo = ?', [email]).fetchone()is not None: 
                    error = " El Correo ya existe".format(email)
                    flash(error)
                    return render_template('register.html')
                print(error)

                db.execute('INSERT INTO usuario2021(nombre,usuario, correo,contrasena) VALUES (?,?,?,?)',(name,username,email,hash_clave))
                db.cursor()
                db.commit()
                
                yag=yagmail.SMTP('hugonew20212020@gmail.com', 'new20212020' )
                yag.send(to=email, subject='Activa Tu Cuenta', 
                contents='Bienvenido, usa este link para activar tu cuenta')
                return render_template('login.html')
            except:
                return render_template('register.html')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    try: 
        if request.method=='POST':
          
            db = get_db()
            error=None
            username= request.form['username']
            password= request.form['password']
            print('login')
            print(username)
            print(password)

            if not username: 
                error= " Debes Ingresar el usuario"
                flash( error )
                return render_template('login.html')

            if not password: 
                error= "Debes Ingresar el password"
                flash( error )
                return render_template('/login.html')
            
            user = db.execute('SELECT * FROM usuario2021 WHERE usuario = ? AND contrasena = ?', 
            (username,password)).fetchone()

            print(user)

            if user is None: 
                error = "Usuario o contraseña inválidos"
            else:
                return redirect ('message')
            flash( error )
        return render_template ('login.html')

    except: 
        return render_template ('login.html')



@app.route('/message', methods=['GET', 'POST'])
def message(): 
    print("Recibimos información")
    flash("Bienvenido Has iniciado Sesion")
    return render_template('principal.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto(): 
    form = Contactenos()
    flash('Mensaje enviado')
    return render_template('contacto.html', titulo='Contactenos', form=form,)
    
    
@app.route('/principal', methods=('GET', 'POST'))
def principal():
    try:
        if request.method=='POST':
            busqueda_input = request.form["busqueda_input"]
            rer= len(busqueda_input)
            if rer == 3 :
                error= "debes ingresar mas de 3 letras"
                flash(error)
                return render_template('principal.html')
            else:
                if busqueda_input == 'producto 1':
                    return render_template('articulo1.html')
                if busqueda_input == 'producto 2':
                    return render_template('articulo2.html')
                if busqueda_input == 'producto 3':
                    return render_template('articulo3.html')
    except:
        return render_template('principal.html')
    return render_template('principal.html')


@app.route('/gestionarProductos', methods=('GET', 'POST'))
def gestionarProductos():
    return render_template('gestionarProductos.html')

@app.route('/articulo1', methods=('GET', 'POST'))
def articulo1():
    return render_template('articulo1.html')


@app.route('/articulo2', methods=('GET', 'POST'))
def articulo2():
    return render_template('articulo2.html')


@app.route('/articulo3', methods=('GET', 'POST'))
def articulo3():
    return render_template('articulo3.html')


@app.route("/deseo/list", methods=['GET','POST'])
def deseo_list():
        try:
            with sqlite3.connect('cuatro.db') as con: 
                con.row_factory=sqlite3.Row # Convierte la respuesta de la BD en un diccionario
                cur = con.cursor()  #manipular la conxion de la BD
                cur.execute('SELECT * FROM producto')
                row = cur.fetchall()
                return render_template('listarDeseo.html', row = row)
               
        except Error: 
            print(Error)
        return "ok"

@app.route("/producto/get", methods=['GET','POST'])
def estudiante_get(): 
    if request.method == 'POST':
        name2= principal(input("busqueda_input"))
        print(name2)
        if name2 == '':
            render_template('')
        else:
            flash('Producto no se encuentra en la base de datos')


@app.route('/SeccionEmpleados',methods=['GET','POST'])
def SeccionEmpleados():
    if request.method == 'POST':
        user = escape(request.form['usuario'])
        password = escape(request.form['contrasena'])
        
        try:
            with sqlite3.connect("cuatro.db") as con:
                cur = con.cursor()
                query=cur.execute("SELECT contrasena FROM usuario2021 WHERE usuario=?",[user]).fetchone()
                if query!=None:
                    if check_password_hash(query[0],password):
                        session['user']=user
                        return redirect("/principal.html") 
                    else:
                        return "Credenciales incorrectas"
                else:
                    return "El usuario NO existe"
        except Error:
            print(Error)

    if 'user' in session:
        return redirect('/principal.html')
    else:
        return render_template('login.html')



if __name__=='__main__':
    app.run(debug=True)
