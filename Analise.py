import pandas as pd
import pdfplumber
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

def carregar_pdf():
    arquivo_pdf = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("PDF files", "*.pdf")]
    )
    
    if arquivo_pdf:
        try:
            with pdfplumber.open(arquivo_pdf) as pdf:
                texto = ""
                for page in pdf.pages:
                    texto += page.extract_text() + "\n"
            
            analisar_dados(texto)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível processar o PDF: {e}")

def analisar_dados(texto):
    # Exemplo: Converter texto em DataFrame simples
    linhas = texto.split("\n")
    dados = [linha.split(",") for linha in linhas if linha.strip()]
    df = pd.DataFrame(dados[1:], columns=dados[0])  # Usa a primeira linha como cabeçalho
    
    exibir_tabela(df)

def exibir_tabela(df):
    # Limpar tabela anterior
    for i in tabela.get_children():
        tabela.delete(i)

    # Configurar novas colunas
    tabela["columns"] = list(df.columns)
    tabela["show"] = "headings"

    for col in df.columns:
        tabela.heading(col, text=col)

    # Inserir dados na tabela
    for row in df.to_numpy():
        tabela.insert("", "end", values=row)

# Configuração da interface
root = tk.Tk()
root.title("Analisador de Dados PDF")

frame = ttk.Frame(root, padding="10")
frame.pack(fill="both", expand=True)

btn_carregar = ttk.Button(frame, text="Carregar PDF", command=carregar_pdf)
btn_carregar.pack(pady=5)

tabela = ttk.Treeview(frame)
tabela.pack(fill="both", expand=True)

root.mainloop()
