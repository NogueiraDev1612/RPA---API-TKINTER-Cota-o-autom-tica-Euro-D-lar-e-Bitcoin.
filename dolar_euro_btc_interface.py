import requests
from tkinter import *

# dolar_euro_btc_interface


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    #print(texto) - ao usar isso, seria para printar o codigo no temrminal
    texto_cotacao["text"] = texto




janela = Tk()                            # cria um arquivo janela
janela.title('Cotação Atual das moeda')  #cria um título para a janela

#coloca o texto na tela e seleciona o local de retorno
texto_orientacao = Label(janela,text='Clique no botão para ver as cotações das moedas')
#tem várias maneira de colocar um elemento na janela em uma certa localização. Porém, vamos usar o método grid.
texto_orientacao.grid(column=0,row=0,padx=50,pady=50) #colunm e row representqa a linha e coluna, padx e pady representa os espaços

#cria botão
botao = Button(janela,text="Busca cotações Dólar/Euro/BTC", command=pegar_cotacoes)
botao.grid(column=0,row=1)


#criar texto dinamico
texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column=0,row=3)

from tkinter import * # importa o modulo de interface

janela = Tk()
'''acesse = Label(janela,text='Acesse sua conta')
acesse.grid(column=1,row=1,padx=10,pady=10)'''

#Criamos o código
def button_command():
    print("test")
    return None

#how to get the entr contents
def button_command2():
    text = entry1.get()
    print(text)
    return None

#how to add contents to the entry
def button_command3():
    text = "this is another test"
    entry1.insert(0,text)
    return None

#how to clear the entry
def button_command4():
    entry1.delete(0,END) #o primeiro argumento é o começo da string e o segundo é até onde ela vai. Se fosse atá 2, seria o interiro 2
    return None


entry1 = Entry(janela,width=20) #CRIA UMA ESPAÇO DE DIGITAÇÃO NA JANELA
entry1.pack()
#Cria um botao e chama a função button_command
Button(janela,text="Button",command=button_command).pack()
    

#how to get the entr contents
#Cria um botao e chama a função button_command
Button(janela,text="Button Entry - call fuction",command=button_command2).pack()

#how to add contents to the entry
Button(janela,text="Button Entry - Add content",command=button_command3).pack()

#how to delete string in space
Button(janela,text="Button Entry - Delete",command=button_command4).pack()




janela.mainloop()        # mantem a hanela aberta obs, deve ser sempre a utima linha de código do tk
