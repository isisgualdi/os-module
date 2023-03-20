import os

os.getcwd() # Mostra o caminho até esse documento

os.listdir() # Lista tudo que está nessa pasta
os.listdir('/Users/isisg/OneDrive/Área de Trabalho')

os.chdir('/Users/isisg/OneDrive/Área de Trabalho') # Troca o diretório em que o código está sendo executado

actual_dir = os.getcwd
os.chdir(actual_dir)

os.mkdir('Pasta') # Cria uma nova pasta

os.rename('teste.txt', 'teste2.txt')