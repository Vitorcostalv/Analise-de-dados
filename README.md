# Analise de dados



### **Objetivo do Projeto**
O objetivo deste projeto é criar uma aplicação em Python que permita carregar um arquivo PDF, extrair dados dele e exibi-los de forma interativa através de uma interface gráfica. Esse estudo tem como base a manipulação de dados usando **Pandas**, a extração de texto e tabelas de PDFs com **pdfplumber**, e a criação de uma interface gráfica com **Tkinter**.

### **Como o Projeto Funciona**

1. **Carregar e Extrair Dados do PDF**:
   - Para carregar o PDF, eu utilizei a biblioteca **pdfplumber**, que facilita a extração de texto e dados de tabelas de arquivos PDF. Quando o usuário escolhe um arquivo PDF, o conteúdo é extraído página por página.
   - A função `carregar_pdf()` abre o PDF e usa o `pdfplumber` para coletar o texto das páginas e armazená-lo em uma variável.

2. **Análise de Dados com Pandas**:
   - Depois de extrair os dados do PDF, eu usei **Pandas** para converter as informações extraídas em uma tabela manipulável. O objetivo aqui é transformar o texto bruto em um formato estruturado que facilite a análise.
   - A função `analisar_dados()` pega as linhas de texto extraídas e as organiza em um DataFrame do Pandas. A primeira linha é considerada como o cabeçalho das colunas da tabela, e as demais linhas são os dados.

3. **Exibição na Interface Gráfica**:
   - A interface gráfica foi construída com **Tkinter**, que é uma biblioteca do Python para criar interfaces de usuário. O **Treeview** de Tkinter foi utilizado para exibir os dados de forma tabular, permitindo que o usuário visualize e interaja com os dados carregados do PDF.
   - A função `exibir_tabela()` limpa qualquer dado anterior na tabela e atualiza com os dados extraídos e analisados.

### **Como Usar**

1. **Instalar as Dependências**:
   Primeiro, você precisa instalar as bibliotecas necessárias. Abra o terminal ou prompt de comando e execute:

   ```bash
   pip install pandas pdfplumber
   ```

   **Nota**: O Tkinter geralmente vem instalado por padrão com o Python, então não é necessário instalá-lo separadamente.

2. **Rodar o Código**:
   - Copie o código em um arquivo Python (por exemplo, `analise_pdf.py`).
   - Execute o arquivo no terminal ou no seu ambiente de desenvolvimento. A interface gráfica abrirá e permitirá que você carregue um arquivo PDF para análise.
   
3. **Interagir com a Interface**:
   - Clique no botão **"Carregar PDF"** para selecionar um arquivo PDF em seu computador.
   - Após o arquivo ser carregado, ele será processado, e os dados extraídos serão exibidos em uma tabela na interface gráfica.
   
### **Como Baixar e Usar o Código**

1. **Baixar o Código**:
   - Copie o código fornecido e cole-o em um novo arquivo Python no seu editor de código.
   - Salve o arquivo com a extensão `.py` (exemplo: `analise_pdf.py`).

2. **Executar o Projeto**:
   - Abra o terminal ou o Prompt de Comando.
   - Navegue até o diretório onde o arquivo Python foi salvo.
   - Execute o código com o comando:

     ```bash
     python analise_pdf.py
     ```

3. **Carregar e Visualizar os Dados**:
   - Após rodar o código, uma janela de interface gráfica será aberta. Nela, você verá um botão para carregar um arquivo PDF. Depois de carregar o PDF, os dados extraídos serão exibidos na tabela.

### **Por que eu fiz isso**

Este estudo foi uma forma de aprofundar meu conhecimento nas bibliotecas **Pandas**, **pdfplumber** e **Tkinter**, explorando como essas ferramentas podem ser combinadas para analisar dados de arquivos PDF. Aprendi a usar o **Pandas** para manipulação de dados e o **Tkinter** para criar interfaces gráficas interativas, o que é uma habilidade valiosa para projetos que envolvem visualização de dados em Python.

