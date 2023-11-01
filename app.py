import pyautogui
from time import sleep

# NO PROMPT DE COMANDO DO PC, DIGITE:
# python
# from mouseinfo import mouseInfo
# mouseInfo()

# 1- CLICAR E DIGITAR MEU USUARIO
pyautogui.click()
pyautogui.write('Mariana')
# 2- CLICAR E DIGITAR MINHA SENHA
pyautogui.click()
pyautogui.write('123456')

# 3- CLICAR EM "ENTRAR"
pyautogui.click()

# 4- EXTRAIR CADA PRODUTO
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 1- Clicar e digitar o produto
        pyautogui.click()
        pyautogui.write(produto)
        # 2- Clicar e registrar a quantidade
        pyautogui.click()
        pyautogui.write(quantidade)
        # 3- Clicar e registrar o preço
        pyautogui.click()
        pyautogui.write(preco)
        # 4- Clicar em registrar tudo
