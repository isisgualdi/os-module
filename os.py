import os

os.getcwd() # Mostra o caminho até esse documento

os.listdir() # Lista tudo que está nessa pasta
os.listdir('/Users/isisg/OneDrive/Área de Trabalho')

os.chdir('/Users/isisg/OneDrive/Área de Trabalho') # Troca o diretório em que o código está sendo executado

os.mkdir('Pasta') # Cria uma nova pasta

os.rename('teste.txt', 'teste2.txt') # Mudar nome de pastas e arquivos

os.remove('teste.csv') # Deletar arquivos
os.rmdir('teste') # Deletar diretório

# Para acessar funções que não estão disponiveis no módulo, mas que funcionam no terminal
cmd = 'date' # Comando date
os.system(cmd)

