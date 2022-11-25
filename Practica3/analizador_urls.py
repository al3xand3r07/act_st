from openpyxl import Workbook
import requests
import re
import datetime

def analizar(key, archivo):
    wb=Workbook()
    page = wb.active
    page['A1']="URL"
    page['B1']="Fecha de analisis"
    page['C1']="Total análisis"
    page['D1']="Análisis positivos"
    page['E1']="Clasificacion"

    api_key = str(key)
    urls = open(archivo, 'r')
    read_urls = urls.read()

    api = "https://www.virustotal.com/vtapi/v2/url/report"
    pagina_re = re.compile('(https?:W(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9]+[a-zA-Z0-9]\.[^\s]{2,}|https?:W(?:wwww\.|(?!wwww))[a-zA-Z0-9]+\.[^\s]')
    pagina_e = pagina_re.findall(read_urls)

    for i in range(len(pagina_e)):
        page[f'A{i+2}'] = pagina_e[i]
        page[f'B{i+2}'] = datetime.datetime.now()
        link = pagina_e[i]
        req = requests.get(link)

        if req.status_code == 200:
            parametros = {
                'apikey': api_key,
                'resource': link
            }
            analisis = requests.get(api, params=parametros)
            json = analisis.json()
            page[f'C{i+2}'] = json['total']
            page[f'D{i+2}'] = json['psotives']

            if json['positives'] < 3:
                page[f'E{i+2}'] = "Baja"
            elif json['positives'] >=3 and json['positives'] < 10:
                page[f'{i+2}'] = "Media"
            else:
                page[f'E{i+2}'] = "Alta"
        else:
            page[f'A{i+2}'] = "Pagina no encontrada"
        
    wb.save("Reporte_analizador_urls.xlsx")    

if __name__=='__main__':
    #llave cambiada por seguridad
    key='24d019ced34088b4dd6838115f985830bc5d57d6f626052c426e5d5d05'
    arch="links.txt"
    analizar(key, arch)