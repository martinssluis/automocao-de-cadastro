import pyautogui
from time import sleep

# 1 clicar e digitar meu usuario
pyautogui.click(673,383,duration=1)
pyautogui.write('lilico')
# 2 clicar e digitar minha senha
pyautogui.click(675,410,duration=1)
pyautogui.write('1234')
# 3 clicar em entrar
pyautogui.click(589,439,duration=1)
# 4 extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 1 clicar e digitar produto
        pyautogui.click(398,372,duration=1)
        pyautogui.write(produto)
        # 2 clicar e digitar quantidade
        pyautogui.click(397,396,duration=1)
        pyautogui.write(quantidade)
        # 3 clicar e digitar preço
        pyautogui.click(397,422,duration=1)
        pyautogui.write(preco)
        # 4 clicar em registarar
        pyautogui.click(309,579,duration=1)
        sleep(1)