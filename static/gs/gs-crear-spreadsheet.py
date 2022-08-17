import gspread
from oauth2client.service_account import ServiceAccountCredentials
import eel

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

credenciales = ServiceAccountCredentials.from_json_keyfile_name("/Volumes/GoogleDrive/.shortcut-targets-by-id/1hWP14ufuayDlqEN5qYsaIpyWVdOtswr9/Administración muebleria /Bots/ActualizacionDePrecios/gs/gs-credentials.json", scope)

cliente = gspread.authorize(credenciales)

# Creacion de sheets

# sheet_finanzas_gastos = cliente.create("finanzas-gastos")
# sheet_finanzas_ingresos = cliente.create("finanzas-ingresos")

# sheet_finanzas_gastos.share('cformandoy@gmail.com', perm_type='user', role='writer')
# sheet_finanzas_ingresos.share('cformandoy@gmail.com', perm_type='user', role='writer')



sheet = cliente.open('finanzas-gastos').sheet1

sheet.update('')