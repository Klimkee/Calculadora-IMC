from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from tkinter.tix import ButtonBox


#cores ------------------------------
co0 = '#000000' # preto
co1 = '#ffffff' # branco
co2 = '#3fb5a3' # verde
co3 = '#38576b' # azul ciano
co4 = '#403d3d' # cinza

janela = Tk()
janela.title('')
janela.geometry('300x230')
janela.configure(bg=co1)

# ----------------- dividindo a janela em duas partes

frame_cima = Frame(janela,width=295,height=50,bg=co1,relief="flat")
frame_cima.grid(row=0, column=0,padx=1,sticky=NSEW)

frame_baixo = Frame(janela,width=295,height=180,bg=co1,relief="flat")
frame_baixo.grid(row=1,column=0,padx=1,sticky=NSEW)

# _____configurando frame cima_______

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co1, fg=co0)
app_nome.place(x=0, y=0) 

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co2,  fg=co2)
app_linha.place(x=0, y=35) 

#________________função calcular_____________
def calcular():

    peso = float(l_peso.get())
    altura = float(l_altura.get())

    imc = peso / altura ** 2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"

    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = "Seu IMC é: Normal"

    elif resultado >= 25 and resultado < 30:
        l_resultado_texto['text'] = "Seu IMC é: Sobrepeso"

    else: 
        l_resultado_texto['text'] = 'Seu IMC é: Obesidade'


    l_resultado['text'] = "{:.{}f}".format(resultado, 2)


#___________configurando frame baixo______________

l_peso = Entry(frame_baixo,width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
l_peso.grid (row=0, column= 2, sticky=NSEW, pady=10, padx=3 )
e_peso = Label(frame_baixo, text='Insira seu peso:',height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
e_peso.grid (row=0, column=1, sticky=NSEW, pady=10, padx=3 ) 


l_altura = Entry(frame_baixo,text='---', width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
l_altura.grid (row=2, column=2, sticky=NSEW, pady=10, padx=3 ) 
e_altura = Label(frame_baixo, text='Insira sua altura:',height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
e_altura.grid (row=2, column=1, sticky=NSEW, pady=10, padx=3 ) 


l_resultado = Label(frame_baixo,text='---',width=6, height=1, padx=6,pady=12,  relief='solid',anchor='center', font=('Ivy 24 bold'), bg= co2, fg=co1)
l_resultado.place(x=175, y=10) 

l_resultado_texto= Label(frame_baixo,text='',width=37, height=1, padx=0,pady=12,  relief='flat',anchor='center', font=('Ivy 10 bold'), bg= co1, fg=co0)
l_resultado_texto.place(x=0, y=80) 

b_calcular= Button(frame_baixo, command=calcular, text='Calcular',width=34 , height=1,overrelief=SOLID, relief='raised',anchor='center', font=('Ivy 10 bold'), bg= co2, fg=co1)
b_calcular.grid (row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=80) 


janela.mainloop()   
