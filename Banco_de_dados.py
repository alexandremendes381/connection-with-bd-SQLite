from cmath import e
from pickle import TRUE
import sqlite3
continuar = TRUE
while continuar == TRUE:
    nome = str(input('qual o seu nome : '))
    idade = int(input('qual sua idade : '))
    email_ = str(input('qual o seu email : '))
    tel = int(input('qual seu numero telefonico :'))

    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()
    #cursor.execute("CREATE TABLE pessoas (nome text, idade interger, email_ text, tel interger)")

    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+", '"+email_+"', '"+str(tel)+"')")

    banco.commit()

    cursor.execute("SELECT * FROM pessoas")
    #print(cursor.fetchall())
    recebe = int(input('Deseja fazer uma busca novamente:'
             '1 = (sim) \n'
             '2 = (não)\n''Qual das opções ? '))
    if recebe == 1:
        continuar = True
        print('ok iremos reiniciar nosso sistema')
    if recebe == 2:
        continuar = False
        print('OK, muito obrigado por usar o nosso sitema nos agradecemos!!')
