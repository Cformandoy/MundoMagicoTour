from crypt import methods
from urllib import request
from flask import Flask, render_template, request, url_for, redirect
import eel


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

app = Flask(__name__)
app.config['SECRET_KEY'] = "cp209182793"

#GOOGLE API

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']


credenciales = ServiceAccountCredentials.from_json_keyfile_name('./static/gs/gs-credentials.json', scope)

cliente = gspread.authorize(credenciales)

service = discovery.build('sheets', 'v4', credentials=credenciales)

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


@app.route('/home')
@app.route('/')
@app.route('/login')
@app.route('/admin')
@app.route('/login-finanzas')
def login_finanzas():
    return render_template('login-finanzas.html')

@app.route('/index-finanzas')
def index_finanzas():
    return render_template('index-finanzas.html')

@app.route('/index-cuentas-ingresar')
def index_cuentas_ingresar():
    return render_template('index-cuentas-ingresar.html')

@app.route('/index-cuentas-verificar')
def index_cuentas_verificar():
    return render_template('index-cuentas-verificar.html')

@app.route('/index-pagar')
def index_pagar():
    return render_template('index-pagar.html')

@app.route('/insertgasto', methods =['POST', "GET"])
def insertgasto():
    output = request.form.to_dict()
    
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
    data = [[tipo,detalle,metodo,fechaNew,monto]]

    salida = service.spreadsheets().values().append(spreadsheetId='10iwQfOkhsCcQZ2vrPG3Rpjj_h23PsdH22DvPALzvnMs', range='Sheet1!A1:E1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    
    return redirect(url_for("index_cuentas_ingresar"))

@app.route('/insertingreso', methods =['POST', "GET"])
def insertingreso():
    output = request.form.to_dict()
    
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
    data = [[tipo,detalle,metodo,fechaNew,monto]]

    salida = service.spreadsheets().values().append(spreadsheetId='1OmoQaTmJyi6y6B5W7xakoEwvpsALBU-P5W0ELVanaZE', range='Sheet1!A1:E1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={"values":data}).execute()
    
    return redirect(url_for("index_cuentas_ingresar"))
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5757)

@eel.expose
def reporteCuentas():
    print('Aqui se generara el reporte')
    


#