import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

YAHOO_EMAIL = os.getenv("YAHOO_EMAIL")
YAHOO_PASSWORD = os.getenv("YAHOO_PASSWORD")

def tratar_df(fornecedores):
    df = pd.DataFrame.from_dict(fornecedores, orient='index')
    df['nome'] = df['nome'].str.lower()
    df['email'] = df['nome'].str.replace(' ', '_') + '@gmail.com'
    df['repasse'] = df['vendas'] * 0.5
    df['tipo'] = df['nome'].apply(
        lambda x: 'doces' if 'bolo' in x or 'doceria' in x or 'brigadeiro' in x else 'salgados')
    return df

def filtrar_df(df_tratado):
    df_doces = df_tratado[df_tratado['tipo'] == 'doces']
    df_salgados = df_tratado[df_tratado['tipo'] == 'salgados']
    return df_doces, df_salgados

def acharemails(dfdoce, dfsalgado):
    """função para encontrar os emails dos fornecedores que mais venderam

    Args:
        top3 salgados e top 1 doces: encontra os fornecedores que mais venderam doces ou salgados
        emailsalgados/doc = adiciona o item do dicionario para a lista
        emails = cria a lista com os emails

    Returns:
        lista com emails selecionados
    """
    top3_salgados = dfsalgado.nlargest(3, 'vendas')
    top1_doce = dfdoce.nlargest(1, 'vendas')
    emailsalgados = top3_salgados['email'].tolist()
    emailsdoce = top1_doce['email'].tolist()
    emails = emailsalgados + emailsdoce + ['lucasgomessr10@gmail.com']
    return emails

def enviar_emails(destinatarios, assunto, corpo):
    """função para enviar os emails

    Args:
        destinatarios - quais emails serao enviados
        assunto - assunto do email
        corpo - texto do email
    """
    smtp_server = "smtp.mail.yahoo.com"
    port = 465

    msg = MIMEMultipart()
    msg['From'] = YAHOO_EMAIL
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(YAHOO_EMAIL, YAHOO_PASSWORD)
            for destinatario in destinatarios:
                msg['To'] = destinatario
                server.sendmail(YAHOO_EMAIL, destinatario, msg.as_string())
        print("Emails enviados com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar os emails: {e}")