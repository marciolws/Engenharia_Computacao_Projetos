import streamlit as st
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4  # Importando A4 corretamente

# Dados de rede credenciada simulados
rede_completa = {
    "Amil": [
        {"hospital": "Hospital São Luiz", "cidade": "São Paulo", "especialidades": ["Cardiologia", "Ortopedia"]},
        {"hospital": "Clínica ABC", "cidade": "Santo André", "especialidades": ["Pediatria"]}
    ],
    "Bradesco": [
        {"hospital": "Hospital Albert Einstein", "cidade": "São Paulo", "especialidades": ["Oncologia", "Neurologia"]}
    ],
    "NotreDame": [
        {"hospital": "Hospital Santa Joana", "cidade": "Recife", "especialidades": ["Ginecologia", "Obstetrícia"]}
    ]
}

# Função para gerar PDF
def gerar_pdf(nome, idade, cidade, operadora, valor, consultor_nome, consultor_telefone, logo_path):
    nome_arquivo = f"proposta_{nome.replace(' ', '_')}.pdf"
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    story = []
    styles = getSampleStyleSheet()

    # Logo e dados do consultor
    if os.path.exists(logo_path):
        img = Image(logo_path, width=80, height=80)
        story.append(img)

    style_center = styles['Normal'].clone('centered')
    style_center.alignment = TA_CENTER
    story.append(Paragraph(f"<b>{consultor_nome}</b><br/>{consultor_telefone}", style_center))
    story.append(Spacer(1, 12))

    # Título
    story.append(Paragraph("<b>Proposta de Plano de Saúde</b>", styles['Title']))
    story.append(Spacer(1, 12))

    # Dados do cliente
    story.append(Paragraph(f"<b>Nome:</b> {nome}", styles['Normal']))
    story.append(Paragraph(f"<b>Idade:</b> {idade}", styles['Normal']))
    story.append(Paragraph(f"<b>Cidade:</b> {cidade}", styles['Normal']))
    story.append(Paragraph(f"<b>Operadora:</b> {operadora}", styles['Normal']))
    story.append(Paragraph(f"<b>Valor:</b> R$ {valor:.2f}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Detalhes do plano
    story.append(Paragraph("<b>Detalhes do Plano:</b>", styles['Heading3']))
    detalhes = [
        "Tipo de acomodação: Apartamento",
        "Cobertura: Nacional",
        "Carência: Reduzida conforme contrato",
        "Exames: Inclusos para consultas gerais",
        "Procedimentos: Inclusos conforme tabela"
    ]
    for item in detalhes:
        story.append(Paragraph(f"- {item}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Rede credenciada
    story.append(Paragraph("<b>Rede Credenciada:</b>", styles['Heading3']))
    hospitais = rede_completa.get(operadora, [])
    dados_tabela = [["Hospital", "Cidade", "Especialidades"]]
    for h in hospitais:
        dados_tabela.append([h['hospital'], h['cidade'], ", ".join(h['especialidades'])])

    tabela = Table(dados_tabela, colWidths=[150, 100, 200])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#14b8a6")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(tabela)

    doc.build(story)
    return nome_arquivo

# Interface Streamlit
st.set_page_config(page_title="Cotação de Plano de Saúde", layout="wide")
st.title("📄 Cadastrar Nova Proposta")

# Logo da empresa (atualize o caminho conforme necessário)
logo_path = "images.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

# Dados do consultor
consultor_nome = "Samuel Vital Marques"
consultor_telefone = "(11) 94658-9430"

# Formulário de cadastro
with st.container():
    st.subheader("📋 Preencha os Dados para Gerar a Proposta")

    with st.form("form_proposta", clear_on_submit=True):
        col1, col2 = st.columns([1, 2])  # Definir o layout com colunas
        with col1:
            nome = st.text_input("Nome completo")
            idade = st.selectbox("Idade", list(range(0, 91)))  # Idades de 0 a 90
            cidade = st.text_input("Cidade")
        with col2:
            operadora = st.selectbox("Operadora", list(rede_completa.keys()))
            valor = st.number_input("Valor da proposta (R$)", min_value=0.0, format="%.2f")
            telefone = st.text_input("Telefone (DDD+Número)")

        enviar = st.form_submit_button("Gerar Proposta")

    if enviar:
        # Gerar o PDF
        pdf = gerar_pdf(nome, idade, cidade, operadora, valor, consultor_nome, consultor_telefone, logo_path)
        
        # Mostrar prévia da proposta antes do download
        with open(pdf, "rb") as file:
            st.download_button("📄 Baixar PDF da Proposta", file, file_name=pdf)
        
        st.success("Proposta gerada com sucesso!")
