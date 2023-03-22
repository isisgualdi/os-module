import os

os.getcwd()

os.path.join(os.getcwd(), 'pasta')

# Retorna a última pasta contida no caminho
os.path.basename(os.getcwd())
os.getcwd().split('/')[-1]

os.path.dirname(os.getcwd())   

# Para ver a data
curr_dir = os.getcwd()
lt = os.path.getmtime(curr_dir)

from datetime import datetime
print(datetime.utcfromtimestamp(lt))

# Para saber se é um arquivo
os.path.isfile(curr_dir)