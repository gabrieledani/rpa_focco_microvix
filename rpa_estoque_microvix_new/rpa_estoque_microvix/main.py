import pyautogui
import time


url ='https://erp.microvix.com.br/'

'''https://erp.microvix.com.br/
usuário: modelovencedor
senha: Modelo1875
'''
pyautogui.press('winleft')
pyautogui.write('firefox')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(url)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('modelovencedor.casavalduga')
pyautogui.press('tab')
pyautogui.write('Modelo1875')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(10)
#posição do mouse pra clicar em Suprimentos
#print(pyautogui.position())
#https://linx.microvix.com.br:8371/gestor_web/produtos/balanco/envia_balanco.asp

print('foi')