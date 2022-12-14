from crypt import methods
import email
from urllib import request
from flask import Flask, render_template, request, url_for, redirect
import eel
import flask
import flask_login

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

#GOOGLE API

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']


credenciales = ServiceAccountCredentials.from_json_keyfile_name('./static/gs/gs-credentials.json', scope)

cliente = gspread.authorize(credenciales)

service = discovery.build('sheets', 'v4', credentials=credenciales)

app = Flask(__name__)
app.config['SECRET_KEY'] = "cp209182793"


login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'ignacio.soto': {'password': 'ignacio'},
         'cristopher.pozas': {'password': 'Cp209182793'},
         'natacha.soto': {'password': '0321'},
         'scarlett.soto': {'password': 'scarlett'},
         'amador.soto': {'password': 'amador'},
         'leonardo.maulen': {'password': 'leonardo2346'},}

def meses(numero):
    mes = ''
    if numero == '01':
        mes = 'Ene'
    elif numero == '02':
        mes = 'Feb'
    elif numero == '03':
        mes = 'Mar'
    elif numero == '04':
        mes = 'Abr'
    elif numero == '05':
        mes = 'May'
    elif numero == '06':
        mes = 'Jun'
    elif numero == '07':
        mes = 'Jul'
    elif numero == '08':
        mes = 'Ago'
    elif numero == '09':
        mes = 'Sep'
    elif numero == '10':
        mes = 'Oct'
    elif numero == '11':
        mes = 'Nov'
    elif numero == '12':
        mes = 'Dic'
    
    return mes

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        
        email = flask.request.form['email']
        if email in users and flask.request.form['password'] == users[email]['password']:
            user = User()
            user.id = email
            flask_login.login_user(user)
            return flask.redirect(flask.url_for('index_finanzas'))
        else:
            return redirect(url_for('login'))
    if flask.request.method == 'GET':
        return render_template('login.html')

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('login'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))

@app.route("/settings")
@flask_login.login_required
def settings():
    pass



@app.route('/index-finanzas')
@flask_login.login_required
def index_finanzas():
    return render_template("index-finanzas.html", name= flask_login.current_user.id)


@app.route('/index-cuentas-ingresar')
@flask_login.login_required
def index_cuentas_ingresar():
    
    return render_template('index-cuentas-ingresar.html',name= flask_login.current_user.id)

@app.route('/index-cuentas-verificar')
@flask_login.login_required
def index_cuentas_verificar():
    return render_template('index-cuentas-verificar.html',name= flask_login.current_user.id)

@app.route('/index-pagar')
@flask_login.login_required
def index_pagar():
    return render_template('index-pagar.html')

@app.route('/insertgasto', methods =['POST', "GET"])
@flask_login.login_required
def insertgasto():
    output = request.form.to_dict()
    
    user = output["usuario_gasto"]
    tipo = output["tipo_gasto"]
    detalle = output["detalle_gasto"]
    metodo = output["metodo_gasto"]
    fecha = output["fecha_gasto"]
    monto = output["monto_gasto"]
    
    dia = (fecha.split("-", 1))[0]
    mes = ((fecha.split("-", 1))[1].split('-',1))[0]
    age = ((fecha.split("-", 1))[1].split('-',1))[1]
    
    mesNew = meses(mes)
    
    fechaNew = dia +'-'+ mesNew +'-'+ age
    data = [[user,tipo,detalle,metodo,fechaNew,monto]]

    if user=="Natacha Soto":
        service.spreadsheets().values().append(spreadsheetId='10iwQfOkhsCcQZ2vrPG3Rpjj_h23PsdH22DvPALzvnMs', range='natacha!A1:F1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Cristopher Pozas":
        service.spreadsheets().values().append(spreadsheetId='10iwQfOkhsCcQZ2vrPG3Rpjj_h23PsdH22DvPALzvnMs', range='cristopher!A1:F1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Ignacio Soto":
        service.spreadsheets().values().append(spreadsheetId='10iwQfOkhsCcQZ2vrPG3Rpjj_h23PsdH22DvPALzvnMs', range='ignacio!A1:F1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Leonardo Maulen":
        service.spreadsheets().values().append(spreadsheetId='10iwQfOkhsCcQZ2vrPG3Rpjj_h23PsdH22DvPALzvnMs', range='leonardo!A1:F1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Scarlett Soto":
        service.spreadsheets().values().append(spreadsheetId='10iwQfOkhsCcQZ2vrPG3Rpjj_h23PsdH22DvPALzvnMs', range='scarlett!A1:F1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Amador Soto":
        service.spreadsheets().values().append(spreadsheetId='10iwQfOkhsCcQZ2vrPG3Rpjj_h23PsdH22DvPALzvnMs', range='amador!A1:F1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()

    salida = service.spreadsheets().values().append(spreadsheetId='10iwQfOkhsCcQZ2vrPG3Rpjj_h23PsdH22DvPALzvnMs', range='general!A1:F1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    
    return redirect(url_for("index_cuentas_ingresar"))

@app.route('/insertingreso', methods =['POST', "GET"])
@flask_login.login_required
def insertingreso():
    output = request.form.to_dict()
    
    user = output["usuario_ingreso"]
    cli = output["cliente_ingreso"]
    tipo = output["tipo_ingreso"]
    detalle = output["detalle_ingreso"]
    metodo = output["metodo_ingreso"]
    fecha = output["fecha_ingreso"]
    monto = output["monto_ingreso"]
    
    dia = (fecha.split("-", 1))[0]
    mes = ((fecha.split("-", 1))[1].split('-',1))[0]
    age = ((fecha.split("-", 1))[1].split('-',1))[1]
    
    mesNew = meses(mes)
    
    fechaNew = dia +'-'+ mesNew +'-'+ age
    data = [[user,cli,tipo,detalle,metodo,fechaNew,monto]]

    if user=="Natacha Soto":
        service.spreadsheets().values().append(spreadsheetId='1OmoQaTmJyi6y6B5W7xakoEwvpsALBU-P5W0ELVanaZE', range='natacha!A1:G1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Cristopher Pozas":
        service.spreadsheets().values().append(spreadsheetId='1OmoQaTmJyi6y6B5W7xakoEwvpsALBU-P5W0ELVanaZE', range='cristopher!A1:G1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Ignacio Soto":
        service.spreadsheets().values().append(spreadsheetId='1OmoQaTmJyi6y6B5W7xakoEwvpsALBU-P5W0ELVanaZE', range='ignacio!A1:G1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Leonardo Maulen":
        service.spreadsheets().values().append(spreadsheetId='1OmoQaTmJyi6y6B5W7xakoEwvpsALBU-P5W0ELVanaZE', range='leonardo!A1:G1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Scarlett Soto":
        service.spreadsheets().values().append(spreadsheetId='1OmoQaTmJyi6y6B5W7xakoEwvpsALBU-P5W0ELVanaZE', range='scarlett!A1:G1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    elif user =="Amador Soto":
        service.spreadsheets().values().append(spreadsheetId='1OmoQaTmJyi6y6B5W7xakoEwvpsALBU-P5W0ELVanaZE', range='amador!A1:G1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()

    salida = service.spreadsheets().values().append(spreadsheetId='1OmoQaTmJyi6y6B5W7xakoEwvpsALBU-P5W0ELVanaZE', range='general!A1:G1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    return redirect(url_for("index_cuentas_ingresar"))
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5757)

@eel.expose
def reporteCuentas():
    print('Aqui se generara el reporte')
    



