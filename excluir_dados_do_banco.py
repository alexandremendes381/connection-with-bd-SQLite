from email.errors import InvalidDateDefect
import sqlite3
print('banco de dados')
nome = str(input('Qual nome gostaria de deletar da lista : '))

try:  
    banco = sqlite3.connect('primeiro_banco.db') #objeto de conexao com banco

    cursor = banco.cursor()
    cursor.execute("DELETE FROM pessoas WHERE nome = '{}' ".format(nome))
    
    banco.commit()
    banco.close()
    print('os dados foram removidos com sucesso')

except sqlite3.Error as erro:
    print('erro ao tentar excluir os dados',erro)
    