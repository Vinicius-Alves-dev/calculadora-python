#importando tkinter
from tkinter import *
from tkinter import ttk


#definindo algumas cores (peguei do color picker)
cor_fundo = "#0D0B0D" #Preto rosado
cor_display = "#181318" #preto acinzentado
cor_numeros = "#FFB6D9" #Rosa pastel
cor_operadores = "#FF1493" #Pink
cor_botao = "#EBB5C8" #Rosa bebê
cor_texto = "#FFF0F7" #Branco rosado


janela = Tk()
janela.title("🎀Calculadora🎀")

#ajustando a largura e comprimento
janela.geometry("235x310")

#mudando a cor da pagina inteira
janela.config(bg=cor_fundo)


#para dividir em partes, vamos usar o frame
frame_display = Frame(janela, width=235, height=50, bg=cor_display)
frame_display.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)



#variavel todos valores
todos_valores = ''

valor_texto = StringVar()

#criando funcao, do que a gente clicar aparecer no display
def entrar_valores(event):

    global todos_valores

    #concatenacao
    todos_valores = todos_valores + str(event)

    #passando valor para display
    valor_texto.set(todos_valores)



#funcao para calcular os valores armazenados em "todos_valores"

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))


#criando a funcao limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")



#criando label

app_label = Label(frame_display, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=cor_display, fg=cor_texto)
app_label.place(x=0, y=0)


#criando botoes
botao_clean = Button(frame_corpo, text="C", width=11, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=limpar_tela)
botao_clean.place(x=0, y=0)
botao_resto_da_divisao = Button(frame_corpo, text="%", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('%'))
botao_resto_da_divisao.place(x=118, y=0)
botao_divisao = Button(frame_corpo, text="/", width=5, height=2, bg=cor_operadores, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('/'))
botao_divisao.place(x=177, y=0)


botao_numero_7 = Button(frame_corpo, text="7", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('7'))
botao_numero_7.place(x=0, y=52)
botao_numero_8 = Button(frame_corpo, text="8", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('8'))
botao_numero_8.place(x=60, y=52)
botao_numero_9 = Button(frame_corpo, text="9", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('9'))
botao_numero_9.place(x=118, y=52)
botao_da_multiplicacao = Button(frame_corpo, text="*", width=5, height=2, bg=cor_operadores, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('*'))
botao_da_multiplicacao.place(x=177, y=52)


botao_numero_4 = Button(frame_corpo, text="4", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('4'))
botao_numero_4.place(x=0, y=104)
botao_numero_5 = Button(frame_corpo, text="5", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('5'))
botao_numero_5.place(x=60, y=104)
botao_numero_6 = Button(frame_corpo, text="6", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('6'))
botao_numero_6.place(x=118, y=104)
botao_da_subtracao = Button(frame_corpo, text="-", width=5, height=2, bg=cor_operadores, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('-'))
botao_da_subtracao.place(x=177, y=104)


botao_numero_1 = Button(frame_corpo, text="1", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('1'))
botao_numero_1.place(x=0, y=156)
botao_numero_2 = Button(frame_corpo, text="2", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('2'))
botao_numero_2.place(x=60, y=156)
botao_numero_3 = Button(frame_corpo, text="3", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('3'))
botao_numero_3.place(x=118, y=156)
botao_da_adicao = Button(frame_corpo, text="+", width=5, height=2, bg=cor_operadores, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('+'))
botao_da_adicao.place(x=177, y=156)


botao_numero_0 = Button(frame_corpo, text="0", width=11, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('0'))
botao_numero_0.place(x=0, y=208)
botao_ponto = Button(frame_corpo, text=".", width=5, height=2, bg=cor_botao, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('.'))
botao_ponto.place(x=118, y=208)
botao_igual = Button(frame_corpo, text="=", width=5, height=2, bg=cor_operadores, fg=cor_texto, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command= calcular)
botao_igual.place(x=177, y=208)




#permite executarmos a nossa janela
janela.mainloop()