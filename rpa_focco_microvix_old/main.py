from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import create_files
import datetime
import time
import os


def open_web():
    opcoes = webdriver.ChromeOptions()
    #opcoes.add_argument('--headless')
    servico = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=servico,options=opcoes)


if __name__ == '__main__':
    while True:
        print(datetime.datetime.today().hour)
        
        if datetime.datetime.today().hour > 8 and datetime.datetime.today().hour < 20:
            #empresas = {'91':'8'}#{'12':'2','13':'3','21':'5','41':'6','61':'7','71':'4','91':'8'}
            empresas = {'12':'2','13':'3','21':'5','41':'6','61':'7','71':'4','91':'8'}
        else:
            empresas = {}
        
        #empresas = {'12':'2','13':'3','21':'5','41':'6','61':'7','71':'4','91':'8'}
        for emp_focco,emp_microvix in empresas.items():
            file = create_files.execute(emp_focco)

            navegador = open_web()
            navegador.get("https://erp.microvix.com.br/")
            time.sleep(5)

            usuario = navegador.find_element(By.ID,'f_login')
            usuario.send_keys('modelovencedor.casavalduga')
            senha = navegador.find_element(By.ID,'f_senha')
            senha.send_keys('Vencedor1875')
            navegador.find_element(By.ID,"form_login").submit()
            time.sleep(5)
            
            #navegador.find_element(By.ID,"sel_empresa_portal_usuario").click()
            navegador.find_element(By.XPATH,'//*[@id="frm_selecao_empresa_login"]/div/div/button').click()
            
            empresa = navegador.find_element(By.CSS_SELECTOR,"input.form-control")
            empresa.send_keys(emp_microvix)
            #navegador.find_element(By.CLASS_NAME,"dropdown-item active").click()
            navegador.find_element(By.XPATH,'//*[@id="frm_selecao_empresa_login"]/div/div/div/div[2]/ul/li/a').click()
            navegador.find_element(By.ID,'btnselecionar_empresa').click()
            time.sleep(5)

            #pagina de entrada de arquivo de estoque
            url = navegador.current_url
            url = url[:url.find('v4')]
            print(url)

            navegador.get(url+"gestor_web/produtos/balanco/envia_balanco.asp")
            time.sleep(3)

            diretorio = os.getcwd()
            file = os.path.join(diretorio,file.name)
            print(file)

            arquivos = navegador.find_element(By.ID,"fileinput")
            arquivos.send_keys(file)
            time.sleep(5)
            
            navegador.find_element(By.NAME,'B1').click()
            time.sleep(5)

            navegador.get(url+"gestor_web/produtos/balanco/relatorio_balanco.asp?seq_balanco=8&tipo_leitura_arquivo=1")
            time.sleep(5)

            navegador.find_element(By.NAME,'f_deposito').click()
            time.sleep(3)

            #Define deposito estoque
            deposito = navegador.find_element(By.NAME,'f_deposito')
            deposito.send_keys('E')
            
            navegador.find_element(By.NAME,'Prosseguir').click()
            time.sleep(3)

            WebDriverWait(navegador, 10).until(EC.alert_is_present())
            navegador.switch_to.alert.accept()
            time.sleep(10)
            
            
            navegador.find_element(By.XPATH,'//*[@id="AutoNumber1"]/tbody/tr[3]/td/form/p[1]/input').click()
            time.sleep(10)
            
            navegador.find_element(By.ID,'bt_balanco').click()
            time.sleep(10)

            print('END!')
            navegador.close()
            print(datetime.datetime.now())
            time.sleep(5)
        time.sleep(500)
