import pyautogui

#print(pyautogui.position())     

print(pyautogui.KEYBOARD_KEYS)


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
'''
pyautogui.moveTo(10,388)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(35, 425)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(67, 877)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(85, 910)
pyautogui.click()
time.sleep(2)
#pyautogui.alert("então")
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
file = r"J:\Meu Drive\Valduga\Novos desenvolvimentos\Linx\Estoques\ESTOQUE_11_070_2.CSV"
pyautogui.write(file)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
for i in range(0,15):
    pyautogui.press('tab')
    time.sleep(1)
time.sleep(1)
pyautogui.write('E')
time.sleep(1)
pyautogui.press('enter')
for i in range(0,12):
    pyautogui.press('tab')
    time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
pyautogui.alert("that's it folks")
pyautogui.hotkey('alt','f4')
'''
print('foi')