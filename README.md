# Projeto Integrador I - Cotação de Plano de Saúde

Este projeto tem como objetivo simular a criação de uma proposta de plano de saúde através de um formulário em **Streamlit**. O sistema permite que o usuário preencha os dados necessários (nome, idade, cidade, operadora de saúde, valor da proposta) e gere um PDF com as informações inseridas, que pode ser baixado. O sistema também permite a visualização prévia do PDF e oferece a possibilidade de gerar o link para envio via WhatsApp.

## Funcionalidades

- **Formulário de Cadastro**: O usuário pode cadastrar uma nova proposta de plano de saúde, inserindo dados como nome, idade, cidade, operadora, valor da proposta e telefone.
- **Geração de PDF**: Após o cadastro, um PDF com todos os dados do cliente e da proposta é gerado e disponibilizado para download.
- **Prévia do PDF**: O usuário pode visualizar uma prévia da proposta antes de realizar o download do arquivo PDF.
- **Design Responsivo**: A interface foi desenvolvida para ser simples e intuitiva, com um design focado em um visual futurista e profissional.
- **Seleção de Idade**: O usuário pode selecionar a idade de 0 a 90 anos para personalizar a proposta.

## Tecnologias Utilizadas

- **Streamlit**: Framework para construção de interfaces web interativas.
- **ReportLab**: Biblioteca para geração de PDFs a partir dos dados informados.
- **Python 3.x**: Linguagem de programação utilizada no desenvolvimento da aplicação.
- **Matplotlib e Seaborn**: Bibliotecas auxiliares para visualização de dados (não utilizadas diretamente na versão atual, mas poderiam ser usadas para gráficos no futuro).

## Pré-requisitos

Antes de rodar o projeto, é necessário ter o Python instalado na sua máquina. Além disso, você precisará instalar as dependências do projeto.

### Instalar Dependências
