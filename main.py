import yfinance
import pyautogui
import pyperclip
import time
from tkinter import *
from tkinter import ttk
from dados import *

def fEnviar(destinatario, assunto, mensagem):

    pyautogui.PAUSE = 2

    pyautogui.click(x=8, y=878)
    pyperclip.copy("brave")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("enter")
    pyautogui.hotkey("ctrl", "t")
    pyperclip.copy("www.gmail.com")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("enter")
    pyautogui.click(x=102, y=160)
    pyperclip.copy(destinatario)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("tab")
    pyperclip.copy(assunto)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("tab")
    pyperclip.copy(mensagem)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("ctrl", "enter")


# time.sleep(5)
# posicao = pyautogui.position()
# print(posicao)


def fTeste(x):
    nomeEmpresa = x
    nomeEmpresa = nomeEmpresa.upper()
    acao = empresa[nomeEmpresa]
    dados = yfinance.Ticker(acao)
    tabela = dados.history("6mo")
    fechamento = tabela.Close

    maxima = fechamento.max()
    minima = fechamento.min()
    atual = fechamento[-1]

    destinatario = "dev.python003@gmail.com"
    assunto = f"Analise Semestral {nomeEmpresa}"
    mensagem = f"""
    Bom dia!
    Seguem os valores de fechamento dos ultimos 6 meses da carteira {nomeEmpresa} ({acao}):
    Máxima: R${round(maxima, 2)}
    Minima: R${round(minima, 2)}
    Atual:  R${round(atual, 2)}
    
    Dúvidas fico a disposição!
    
    Att.
    
    Murilo Oliveira
    """
    fEnviar(destinatario, assunto, mensagem)

corBg = "#cecece"
corFg = "#000"
janela = Tk()
janela.title("Gerador de E-mails")
janela.geometry("250x200")
janela.configure(bg=corBg)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)
style = ttk.Style(janela)
style.theme_use('default')

topoTitulo = Label(janela, text="Automatização de E-mails", anchor=CENTER, relief="flat", font="Verdana 10 bold",
               bg=corBg, fg=corFg)
topoTitulo.place(x=28, y=10)
ticker = Label(janela, text="Empresa: ", font="Verdana 10", bg=corBg, fg=corFg)
ticker.place(x=40, y=50)

tickerEntrada = Entry(janela, width=17
                      )
tickerEntrada.place(x=107, y=52)

button = Button(janela, text="Enviar", width=18, padx=20, command=lambda:fTeste(tickerEntrada.get()))
button.place(x=40, y=95)

janela.mainloop()
