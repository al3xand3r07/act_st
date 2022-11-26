#pip install python-nmap
import nmap

inicia = 79
termina = 80
target = '192.168.1.10'
scanner = nmap.PortScanner()


for i in range(inicia,termina+1):
    with open('result.txt', 'w+', encoding='utf-8') as txt:
        txt.seek(2)
        res = scanner.scan(target,str(i))
        for x,y in res.items():
            temp = x,y
            txt.write('\n')
            txt.write(str(temp))
        res = res['scan'][target]['tcp'][i]['state'] 
        txt.write(f'port {i} is {res}.')