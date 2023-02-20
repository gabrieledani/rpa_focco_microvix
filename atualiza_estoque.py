from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import create_files
import time
import os
from datetime import datetime
import logging

#empresas = {'12':'2','13':'3','21':'5','41':'6','61':'7','71':'4','91':'8'}

def open_web():
    opcoes = webdriver.ChromeOptions()

    #opcoes.headless = True

    #opcoes.add_argument('--headless')
    #opcoes.add_argument('--disable-software-rasterizer')
    #opcoes.add_argument('--disable-gpu')
    #opcoes.add_argument('--remote-debugging-port=9222')
    #--disable-software-rasterizer
    '''
    chrome \
    --headless \                   # Runs Chrome in headless mode.
    --disable-gpu \                # Temporarily needed if running on Windows.
    --remote-debugging-port=9222 \
    https://www.chromestatus.com   # URL to open. Defaults to about:blank.    
    '''
    servico = Service(ChromeDriverManager().install())
    opcoes.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(service=servico,options=opcoes)


def carrega_arquivo(emp_focco,emp_microvix):
    logging.basicConfig(filename='application.log',level=logging.INFO,format='%(asctime)s - %(message)s')
    try:
        file = create_files.execute(emp_focco)

        logging.info(datetime.now().strftime("%H:%M:%S - ") + "Abrindo Microvix")
        navegador = open_web()
        #navegador.maximize_window()
        
        navegador.get("https://erp.microvix.com.br/")
        time.sleep(10)
        #print('site')

        usuario = navegador.find_element(By.ID,'f_login')
        usuario.send_keys('modelovencedor.casavalduga')
        time.sleep(3)
        #print('login')

        senha = navegador.find_element(By.ID,'f_senha')
        senha.send_keys('Modelo#1875')
        time.sleep(3)
        #print('senha')

        navegador.find_element(By.ID,"form_login").submit()
        time.sleep(10)
        #print('submete')
        
        navegador.find_element(By.XPATH,'//*[@id="frm_selecao_empresa_login"]/div/div/button').click()
        time.sleep(3)
        #print('clica lista')

        empresa = navegador.find_element(By.CSS_SELECTOR,"input.form-control")
        empresa.send_keys(emp_microvix)
        #print('informa empresa',emp_microvix)
        time.sleep(3)
        
        navegador.find_element(By.XPATH,'//*[@id="frm_selecao_empresa_login"]/div/div/div/div[2]/ul/li/a').click()
        time.sleep(3)
        #print('clica na empresa informada')

        navegador.find_element(By.ID,'btnselecionar_empresa').click()
        #print('submete')
        time.sleep(10)

        #pagina de entrada de arquivo de estoque
        url = navegador.current_url
        url = url[:url.find('v4')]

        navegador.get(url+"gestor_web/produtos/balanco/envia_balanco.asp")
        #print('pagina balanco')
        time.sleep(10)

        diretorio = os.getcwd()
        file = os.path.join(diretorio,file.name)

        logging.info(datetime.now().strftime("%H:%M:%S - ") + "Enviando arquivo")
        arquivos = navegador.find_element(By.ID,"fileinput")
        arquivos.send_keys(file)
        #print('arquivo',arquivos)
        time.sleep(5)
        
        navegador.find_element(By.NAME,'B1').click()
        #print('enviar arquivo')
        time.sleep(20)
        
        actions = ActionChains(navegador) 
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        #print('clique aqui')
        time.sleep(10)

        navegador.find_element(By.NAME,'f_deposito').click()
        #print('opcao deposito')
        time.sleep(3)

        #Define deposito estoque
        deposito = navegador.find_element(By.NAME,'f_deposito')
        deposito.send_keys('E')
        time.sleep(3)
        navegador.find_element(By.NAME,'Prosseguir').click()
        #print('botao prosseguir')
        time.sleep(10)

        logging.info(datetime.now().strftime("%H:%M:%S - ") + "Processando balanço!")
        WebDriverWait(navegador, 10).until(EC.alert_is_present())
        navegador.switch_to.alert.accept()
        #print('alerta')
        time.sleep(10)
        
        navegador.find_element(By.XPATH,'//*[@id="AutoNumber1"]/tbody/tr[3]/td/form/p[1]/input').click()
        #print('botao não sei')
        time.sleep(10)
        
        navegador.find_element(By.ID,'bt_balanco').click()
        #print('ultimo botao')
        time.sleep(20)
        
        logging.info(datetime.now().strftime("%H:%M:%S - ") + "Processo para setar estoque completo")
        navegador.close()
    except:
        logging.info(datetime.now().strftime("%H:%M:%S - ") + "Erro"+emp_focco+emp_microvix)
        print('Error',emp_focco,emp_microvix)