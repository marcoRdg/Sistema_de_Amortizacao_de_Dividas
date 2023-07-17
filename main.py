import tkinter

from library import series_amortizacao as fc
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

print(fc.met_americano(6000,0.040093,7))

#global Var


#cores
cor1 = '#242323'

# Tamanho Label/Entry
w_label=10
h_label=2
t_entry=10

# funcao obter
def obter_dados():
    divida = float(entry_divida.get())
    taxa_juros = float(entry_juros.get())
    periodos = int(entry_periodo.get())
    modelo = modelo_amortizacao.get()


    """label_divida_rep['text'] = divida
    label_juros_rep['text'] = taxa_juros
    label_periodo_rep['text'] = periodos"""

    entry_divida.delete(0,END)
    entry_juros.delete(0, END)
    entry_periodo.delete(0, END)

    adicionar_dados(divida,taxa_juros,periodos,modelo)




def adicionar_dados(divida,taxa_juros,periodos, modelo):
    # Apaga a tabela atual
    for row in treeview.get_children():
        treeview.delete(row)

    # Atualiza o df ao modelo escolhido
    if modelo == "Americano":
        df = fc.met_americano(divida,taxa_juros,periodos)
    elif modelo == "Francês (Price)":
        df = fc.met_frances(divida,taxa_juros,periodos)
    else:
        df = fc.met_hamburgues(divida,taxa_juros,periodos)


    for i,j,a,p,d in df.values:
        treeview.insert("","end", values=(i,j,a,p,d))



janela = Tk()
janela.title("Olá Mundo")
janela.geometry('700x300')
janela.config(bg=cor1)

# Altera icone da janela
#janela.iconphoto(False, PhotoImage(file=''))
#janela.resizable(width=False, height=False)

frame_opcoes = Frame(janela, width=200, height=550)
frame_opcoes.grid(row=0,column=0)
frame_df = Frame(janela, width=800, height=550)
frame_df.grid(row=0,column=1)

#Entrada Dados -----------------------------------------
label_title = Label(frame_opcoes, width=18, height=h_label+2, text='Amortização de Dividas ', bg='white')
label_title.grid(row=0, column=0, padx=10,pady=5)
# Divida
label_divida = Label(frame_opcoes, width=w_label, height=h_label, text='Dívida: ', bg='white')
label_divida.grid(row=1, column=0, padx=5,pady=5, sticky=NSEW)
entry_divida = Entry(frame_opcoes, width=w_label, font=('ComicSan 10'))
entry_divida.grid(row=1, column=1, padx=10, pady=5, sticky=NSEW)

# Taxa de Juros
label_juros = Label(frame_opcoes, width=w_label, height=h_label, text='Taxa de Juros: ', bg='white')
label_juros.grid(row=2, column=0, padx=5,pady=5, sticky=NSEW)
entry_juros = Entry(frame_opcoes, width=w_label, font=('ComicSan 10'))
entry_juros.grid(row=2, column=1, padx=10, pady=5, sticky=NSEW)

# periodo
label_periodo = Label(frame_opcoes, width=w_label, height=h_label, text='Períodos: ', bg='white')
label_periodo.grid(row=3, column=0, padx=5,pady=5, sticky=NSEW)
entry_periodo = Entry(frame_opcoes, width=w_label, font=('ComicSan 10'))
entry_periodo.grid(row=3, column=1, padx=10, pady=5, sticky=NSEW)

# Criando comboBox
modelo_amortizacao = ttk.Combobox(frame_opcoes)
modelo_amortizacao['values']=('Americano', 'Francês (Price)', 'Hamburguês')
modelo_amortizacao.current(0)
modelo_amortizacao.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

#botoeira
botao = Button(frame_opcoes, command=obter_dados, width=8, height=1, text='Calcular', relief='raised', fg='#fcb603', bg='#4b13ab')
botao.grid(row=5, column=0, padx=5, pady=10)


"""#figura
figura = plt.Figure(figsize=(8,4), dpi=60)
grafico = figura.add_subplot(111)

canva = FigureCanvasTkAgg(figura, janela)
canva.get_tk_widget().grid(row=5,column=0)"""

# Criar tabela
treeview = ttk.Treeview(frame_df, columns=("periodo","juros","amortizacao","pagamento","divida"), show='headings')
treeview.column('periodo', minwidth=0,width=80)
treeview.heading('periodo', text='Periodo')
treeview.column('juros', minwidth=0,width=80)
treeview.heading('juros', text='Juros')
treeview.column('amortizacao', minwidth=0,width=100)
treeview.heading('amortizacao', text='Amortização')
treeview.column('pagamento', minwidth=0,width=80)
treeview.heading('pagamento', text='Pagamento')
treeview.column('divida', minwidth=0,width=80)
treeview.heading('divida', text='Dívida')
treeview.pack()


#Saida Dados -----------------------------------------

"""# Divida
label_divida_rep = Label(janela, width=w_label, height=h_label, text='', bg='white')
label_divida_rep.place(x=50, y=70)
# Periodos
label_periodo_rep = Label(janela, width=w_label, height=h_label, text='', bg='white')
label_periodo_rep.grid(row=6, column=1, padx=10,pady=5, sticky=NSEW)
# Taxa de Juros
label_juros_rep = Label(janela, width=w_label, height=h_label, text='', bg='white')
label_juros_rep.grid(row=6, column=2, padx=10,pady=5, sticky=NSEW)"""

janela.mainloop()