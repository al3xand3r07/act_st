#pip install python-nmap
import nmap

inicia = 79
termina = 80
target = '10.100.224.1'
scanner = nmap.PortScanner()

with open('result.txt', 'w+', encoding='utf-8') as txt:
    for i in range(inicia,termina+1): 
        res = scanner.scan(target,str(i))
        for x,y in res.items():
            temp = x,y
            txt.seek(2)
            txt.write('\n')
            txt.write(str(temp))
        res = res['scan'][target]['tcp'][i]['state'] 
        txt.write(f'port {i} is {res}.')
    txt.close()