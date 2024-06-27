import datetime
import streamlit as st

st.title("Entrada de OS",help="OS: Ordem de Serviços")
st.page_link("app.py",label=":gray[Não quero dar entrada agora. Quero retornar ao Inicial]")

tab1, tab2, tab3, tab4 = st.tabs([":green[Criar nova OS]",":green[Dados do Cliente]",":green[Informações do produto]",":blue[Validar dados]"])

with tab1:
    st.subheader(":blue[Dados de abertura da OS]")
    dtEntOS = st.date_input("Confirme a data de abertura da OS:",format="DD/MM/YYYY")
    hrEntOS = st.time_input("Confirme a hora de entrada da OS:")

with tab2:
    st.subheader(":blue[Dados do cliente]")
    nomeCli = st.text_input("Nome do cliente:",placeholder="Nome completo ou parcial")
    cpfCli = st.text_input("CPF:",placeholder="somente 11 caracteres")
    telCli = st.text_input("Número do celular:",placeholder="DDD e números")

with tab3:
    st.subheader(":blue[Dados do produto]")
    nomeProd = st.text_input("Descrição do produto:",placeholder="Nome que determina o produto")
    idProd = st.text_input("Identificação do produto:",placeholder="Número de série ou do modelo")
    txtProd = st.text_area("Detalhes do defeito:",placeholder="Escreva o motivo do mau funcionamento do produto")

with tab4:
    def criaNumOS():
        tempo = datetime.datetime.now().strftime("%X")
        hr = tempo[:2]
        min = tempo[3:5]
        seg = tempo[6:]
        num = hr+min+seg
        return num[:3]+"."+num[3:]

    st.write(":gray[Verificando...]")
    tudoOK = True
    txt = "Dados do cliente: Faltou "
    txt2 = ""
    # verifica se todos os campos acima foram digitados.
    if nomeCli == "":
        txt2 += "NOME / "
    if cpfCli == "":
        txt2 += "CPF / "
    if telCli == "":
        txt2 += "TELEFONE / "
    if txt2:    
        txt += txt2
        tudoOK = False
        st.write(txt)

    txt = "Dados do produto: Faltou "
    txt2 = ""
    # verifica se todos os campos acima foram digitados.
    if nomeProd == "":
        txt2 += "NOME / "
    if idProd == "":
        txt2 += "IDENTIFICAÇÃO / "
    if txtProd == "":
        txt2 += "DETALHES / "
    if txt2:    
        txt += txt2
        tudoOK = False
        st.write(txt)

    if tudoOK:
        # cria o numero da OS: hora min seg
        numOS = criaNumOS() #000.000 
        st.write("Criada a OS número: ",numOS)

        # grava isso na tabela

        # link para retorno ao inicial:
        st.page_link("app.py",label=":violet[Retornar ao Inicial]")
    else:
        st.write(":red[ERRO nos dados informados.]"," Verifique as abas acima: Dados do Cliente e Informações do Produto.")


