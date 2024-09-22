import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Criar a conexão com o banco de dados
conn = sqlite3.connect("controle_pagamentos")

# Criar um cursor
c = conn.cursor()

# Criar a tabela solicitatne
c.execute('''CREATE TABLE IF NOT EXISTS solicitante (
          empresa_solicitante TEXT PRIMARY KEY,
          email TEXT,
          telefone TEXT
          )''')

c.execute('''CREATE TABLE IF NOT EXISTS titulo (
          codigo_titulo TEXT PRIMARY KEY,
          tipo_titulo TEXT,
          beneficiario_credor TEXT, 
          parcelamento INTEGER,
          solicitante_empresa_solicitante TEXT,
          FOREIGN KEY(solicitante_empresa_solicitante) REFERENCES solicitante(empresa_solicitante)
          )''')

c.execute('''CREATE TABLE IF NOT EXISTS pagamento (
          motivo_pagamento TEXT,
          descriminacao_parcela TEXT,
          valor REAL,
          parcela INTEGER,
          data_pagamento DATE,
          vencimento_fatal DATE,
          observacoes TEXT,
          forma_pagamento TEXT,
          pagamento BOOLEAN,
          data_comprovante DATE,
          inclusao BOOLEAN,
          acordo_descumprido BOOLEAN,
          solicitante_empresa_solicitante TEXT,
          titulo_codigo_titulo TEXT,
          PRIMARY KEY(solicitante_empresa_solicitante,titulo_codigo_titulo,parcela)
          )''')

c.execute("PRAGMA table_info(titulo)")

rows = c.fetchall()
for row in rows:
    print(row)

#Cria interface gráfica
root = Tk()

#Cria widget Notebook
notebook = ttk.Notebook(root)
notebook.grid()

#Cria abas
aba_solicitante = Frame(notebook)
aba_titulo = Frame(notebook)
aba_pagamento = Frame(notebook)

notebook.add(aba_solicitante, text='Setor Solicitante')
notebook.add(aba_titulo, text='Título')
notebook.add(aba_pagamento, text='Informações de pagamento')

#Cria entradas
empresa_solicitante_lable = Label(aba_solicitante, text="Área Solicitante")
empresa_solicitante_lable.grid(row=0, column=0)
empresa_solicitante_entry = Entry(aba_solicitante)
empresa_solicitante_entry.grid(row=0, column=1)

empresa_solicitante_lable = Label(aba_titulo, text="Área Solicitante")
empresa_solicitante_lable.grid(row=0, column=0)
empresa_solicitante_entry = Entry(aba_titulo)
empresa_solicitante_entry.grid(row=0, column=1)

empresa_solicitante_lable = Label(aba_pagamento, text="Área Solicitante")
empresa_solicitante_lable.grid(row=0, column=0)
empresa_solicitante_entry = Entry(aba_pagamento)
empresa_solicitante_entry.grid(row=0, column=1)

codigo_titulo_lable = Label(aba_titulo, text="Código do Título")
codigo_titulo_lable.grid(row=1, column=0)
codigo_titulo_entry = Entry(aba_titulo, width=50)
codigo_titulo_entry.grid(row=1, column=1)

codigo_titulo_lable = Label(aba_pagamento, text="Código do Título")
codigo_titulo_lable.grid(row=1, column=0)
codigo_titulo_entry = Entry(aba_pagamento, width=50)
codigo_titulo_entry.grid(row=1, column=1)

email_lable = Label(aba_solicitante, text="E-mail")
email_lable.grid(row=1, column=0)
email_entry = Entry(aba_solicitante, width=50)
email_entry.grid(row=1, column=1)

telefone_lable = Label(aba_solicitante, text="Telefone")
telefone_lable.grid(row=2, column=0)
telefone_entry = Entry(aba_solicitante, width=14)
telefone_entry.grid(row=2, column=1)

tipo_titulo_lable = Label(aba_titulo, text="Tipo do título")
tipo_titulo_lable.grid(row=2, column=0)
tipo_titulo_entry = Entry(aba_titulo, width=30)
tipo_titulo_entry.grid(row=2, column=1)

beneficiario_credor_lable = Label(aba_titulo, text="Beneficiário/Credor")
beneficiario_credor_lable.grid(row=3, column=0)
beneficiario_credor_entry = Entry(aba_titulo, width=40)
beneficiario_credor_entry.grid(row=3, column=1)

parcelamento_lable = Label(aba_titulo, text="Quantidade total de parcelas")
parcelamento_lable.grid(row=4, column=0)
parcelamento_entry = Entry(aba_titulo, width=3)
parcelamento_entry.grid(row=4, column=1)

motivo_pagamento_lable = Label(aba_pagamento, text="Motivo do Pagamento")
motivo_pagamento_lable.grid(row=2, column=0)
motivo_pagamento_entry = Entry(aba_pagamento, width=30)
motivo_pagamento_entry.grid(row=1, column=1)

descriminacao_parcela_lable = Label(aba_pagamento, text="Descrição do Pagamento")
descriminacao_parcela_lable.grid(row=3, column=0)
descriminacao_parcela_entry = Entry(aba_pagamento, width=40)
descriminacao_parcela_entry.grid(row=3, column=1)

valor_lable = Label(aba_pagamento, text="Valor")
valor_lable.grid(row=4, column=0)
valor_entry = Entry(aba_pagamento, width=15)
valor_entry.grid(row=4, column=1)

parcela_lable = Label(aba_pagamento, text="Parcela")
parcela_lable.grid(row=5, column=0)
parcela_entry = Entry(aba_pagamento, width=3)
parcela_entry.grid(row=5, column=1)

data_pagamento_lable = Label(aba_pagamento, text="Data do Pagamento")
data_pagamento_lable.grid(row=6, column=0)
data_pagamento_entry = Entry(aba_pagamento, width=10)
data_pagamento_entry.grid(row=6, column=1)

vencimento_fatal_lable = Label(aba_pagamento, text="Vencimento Fatal")
vencimento_fatal_lable.grid(row=7, column=0)
vencimento_fatal_entry = Entry(aba_pagamento, width=10)
vencimento_fatal_entry.grid(row=7, column=1)

observacoes_lable = Label(aba_pagamento, text="Observações")
observacoes_lable.grid(row=8, column=0)
observacoes_entry = Entry(aba_pagamento, width=50)
observacoes_entry.grid(row=8, column=1)

forma_pagamento_lable = Label(aba_pagamento, text="Forma de Pagamento")
forma_pagamento_lable.grid(row=9, column=0)
forma_pagamento_entry = Entry(aba_pagamento, width=20)
forma_pagamento_entry.grid(row=9, column=1)

data_comprovante_lable = Label(aba_pagamento, text="Data do Comprovante")
data_comprovante_lable.grid(row=10, column=0)
data_comprovante_entry = Entry(aba_pagamento, width=10)
data_comprovante_entry.grid(row=10, column=1)

pagamento = BooleanVar()
pagamento_check = Checkbutton(aba_pagamento, text="Pago", variable=pagamento)
pagamento_check.grid(row=11, column=0)

inclusao = BooleanVar()
inclusao_check = Checkbutton(aba_pagamento, text="Incluído", variable=inclusao)
inclusao_check.grid(row=12, column=0)

acordo_descumprido = BooleanVar()
acordo_descumprido_check = Checkbutton(aba_pagamento, text="Acordo descumprido", variable=acordo_descumprido)
acordo_descumprido_check.grid(row=13, column=0)

#Função para adicionardados ao banco de dados
def add_data_solicitante():              
    empresa_solicitante = empresa_solicitante_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()

    c.execute('INSERT INTO solicitante (empresa_solicitante, email, telefone) VALUES (?, ?, ?)', (empresa_solicitante, email, telefone))
    
    conn.commit()

    empresa_solicitante_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    telefone_entry.delete(0, 'end')

#Mensagem de confirmação
    messagebox.showinfo("Dados inserido")

def add_data_titulo():
    codigo_titulo = codigo_titulo_entry.get()
    tipo_titulo = tipo_titulo_entry.get()
    beneficiario_credor = beneficiario_credor_entry.get()
    parcelamento = parcelamento_entry.get()
    empresa_solicitante = empresa_solicitante_entry.get()

    c.execute('INSERT INTO titulo (codigo_titulo, tipo_titulo, beneficiario_credor, parcelamento, solicitante_empresa_solicitante) VALUES (?, ?, ?, ?, ?)', (codigo_titulo, tipo_titulo, beneficiario_credor, parcelamento, empresa_solicitante))

    conn.commit()

    codigo_titulo_entry.delete(0, 'end')
    tipo_titulo_entry.delete(0, 'end')
    beneficiario_credor_entry.delete(0, 'end')
    parcelamento_entry.delete(0, 'end')
    empresa_solicitante_entry.delete(0, 'end')
#Mensagem de confirmação
    messagebox.showinfo("Dados inserido", "Inserção de dados")


def add_data_pagamento():
    motivo_pagamento = motivo_pagamento_entry.get()
    descriminacao_parcela = descriminacao_parcela_entry.get()
    valor = valor_entry.get()
    parcela = parcela_entry.get()
    data_pagamento = data_pagamento_entry.get()
    vencimento_fatal = vencimento_fatal_entry.get()
    observacoes = observacoes_entry.get()
    forma_pagamento = forma_pagamento_entry.get()
    pagamento = pagamento_check
    data_comprovante = data_comprovante_entry.get()
    inclusao = inclusao_check
    acordo_descumprido = acordo_descumprido_check
    empresa_solicitante = empresa_solicitante_entry.get()
    codigo_titulo = codigo_titulo_entry.get()

    c.execute('INSERT INTO pagamento (motivo_pagamento, descriminacao_parecela, valor, parcela, data_pagamento, vencimento_fatal, observacoes, forma_pagamento, pagamento, data_comprovante, inclusao, acordo_descumprido, solicitante_empresa_solicitante, titulo_codigo_titulo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (motivo_pagamento, descriminacao_parcela, valor, parcela, data_pagamento, vencimento_fatal, observacoes, forma_pagamento, pagamento, data_comprovante, inclusao, acordo_descumprido, empresa_solicitante, codigo_titulo))
    
    conn.commit()

    motivo_pagamento_entry.delete(0, 'end')
    descriminacao_parcela_entry.delete(0, 'end')
    valor_entry.delete(0, 'end')
    parcela_entry.delete(0, 'end')
    data_pagamento_entry.delete(0, 'end')
    vencimento_fatal_entry.delete(0, 'end')
    observacoes_entry.delete(0, 'end')
    forma_pagamento_entry.delete(0, 'end')
    data_comprovante_entry.delete(0, 'end')   
    empresa_solicitante_entry.delete(0, 'end')
    codigo_titulo_entry.delete(0, 'end')

#Mensagem de confirmação
    messagebox.showinfo("Dados inserido")

#Cria botão de envio
submit_btn = Button(aba_solicitante, text="Adicionar ao Banco de Dados", command=add_data_solicitante)
submit_btn.grid(row=4, column=1)

submit_btn = Button(aba_titulo, text="Adicionar ao Banco de Dados", command=add_data_titulo)
submit_btn.grid(row=6, column=1)

submit_btn = Button(aba_pagamento, text="Adicionar ao Banco de Dados", command=add_data_pagamento)
submit_btn.grid(row=15, column=1)

root.mainloop()

#Fecah a conexão com o banco de dados
conn.close()
