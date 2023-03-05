from playwright.sync_api import sync_playwright
import time
import pyautogui

with sync_playwright() as p:
    navegador = p.firefox.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://erp.microvix.com.br/")
    time.sleep(5)
    pagina.fill('xpath=//*[@id="f_login"]','modelovencedor.casavalduga')
    pagina.fill('xpath=//*[@id="f_senha"]', 'Vencedor1875')
    pagina.locator('xpath=/html/body/div/div/div/div/div[2]/div/div/div[2]/form/button[1]').click()
    time.sleep(5)
    #escolher empresa
    pagina.locator('xpath=/html/body/div/div[3]/div/form/div/div/button').click()
    time.sleep(5)
    pagina.fill('xpath=/html/body/div/div[3]/div/form/div/div/div/div[1]/input','1')
    pagina.keyboard.down("Enter")
    pagina.locator('xpath=//*[@id="btnselecionar_empresa"]').click()
    time.sleep(5)
    #pagina.locator('xpath=//*[@id="notification"]').click()
    time.sleep(5)
    #pagina de entrada de arquivo de estoque
    pagina.goto("https://linx.microvix.com.br:8371/gestor_web/produtos/balanco/envia_balanco.asp")
    time.sleep(3)
    #//*[@id="fileinput"]
    file = r"J:\Meu Drive\Valduga\Novos desenvolvimentos\Linx\Estoques\ESTOQUE_11_070_2.CSV"
    pagina.locator('xpath=//*[@id="fileinput"]').set_input_files(file)
    time.sleep(1)
    pagina.locator('xpath=/html/body/div[4]/form/div[6]/table/tbody/tr[1]/td/input').click()
    time.sleep(2)
    pagina.locator('xpath=/ html / body / table[1] / tbody / tr / td / div[2] / p / font / a[1]').click()
    time.sleep(2)
    #Define deposito estoque
    pagina.locator('xpath=/html/body/table/tbody/tr[3]/td[2]/form/table/tbody/tr[11]/td[2]/font/select').click()
    pagina.keyboard.down('E')
    time.sleep(1)
    pagina.keyboard.down('Enter')
    time.sleep(1)
    #print('oi')
    pagina.locator('xpath=/html/body/table/tbody/tr[3]/td[2]/form/table/tbody/tr[20]/td[2]/font/input').click()
    #for i in range(0,12):
    #    pagina.keyboard.down("Tab")
    #    time.sleep(2)
    time.sleep(2)
    pyautogui.press('enter')
    #pagina.keyboard.down('Enter')
    time.sleep(2)
    pyautogui.press('enter')
    #pagina.keyboard.down('Enter')
    time.sleep(2)
    pagina.locator('xpath=/html/body/table[3]/tbody/tr[3]/td/form/p[1]/input').click()
    time.sleep(2)
    pagina.locator('xpath=// *[ @ id = "bt_balanco"]').click()
    time.sleep(10)
