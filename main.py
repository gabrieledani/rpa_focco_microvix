import atualiza_estoque
import datetime

while True:
    empresas = {'12':'2','13':'3','21':'5','41':'6','61':'7','71':'4','91':'8'}
    for emp_focco, emp_linx in empresas.items():
        if datetime.datetime.today().hour >= 8 and datetime.datetime.today().hour <= 20:
            print(emp_linx,emp_focco,datetime.datetime.now())
            atualiza_estoque.carrega_arquivo(emp_focco,emp_linx)
            print(emp_linx,emp_focco,datetime.datetime.now())

