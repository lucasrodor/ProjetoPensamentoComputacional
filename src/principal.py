import pandas as pd
from meuPacote.meuModulo import tratar_df, filtrar_df, acharemails, enviar_emails

dados = {
    0: {'nome': 'Pastel Frito', 'vendas': 3000},
    1: {'nome': 'Massa da Mama', 'vendas': 5000},
    2: {'nome': 'Pizza do Tio', 'vendas': 10000},
    3: {'nome': 'Rodizio Mineiro', 'vendas': 3900},
    4: {'nome': 'Restaurante para Todos', 'vendas': 6000},
    5: {'nome': 'Bom Prato', 'vendas': 9000},
    6: {'nome': 'Yakisoba Delicia', 'vendas': 3000},
    7: {'nome': 'Doceria Feliz', 'vendas': 8000},
    8: {'nome': 'Bolo Gostoso', 'vendas': 8900},
    9: {'nome': 'Carne Assada', 'vendas': 7400},
    10: {'nome': 'Panqueca na Hora', 'vendas': 10743},
    11: {'nome': 'Quibe Bem Feito', 'vendas': 8733},
    12: {'nome': 'Coxinha da Tia', 'vendas': 2999},
    13: {'nome': 'Brigadeiro do Ceu', 'vendas': 4500},
    14: {'nome': 'Feijoada Preta', 'vendas': 9022},
    15: {'nome': 'Sushi Baiano', 'vendas': 8444},
    16: {'nome': 'Peixe Grelhado', 'vendas': 19000},
    17: {'nome': 'Porco no Rolete', 'vendas': 4000},
    18: {'nome': 'Lanche Seja Feliz', 'vendas': 8000}
}
dados[19] = {'nome': 'Churrasco Legal', 'vendas': 10000}
dados[20] = {'nome': 'Espiha delícia', 'vendas': 8500}

tratar_df(dados)
df_tratado = tratar_df(dados)
df_doces, df_salgados = filtrar_df(df_tratado)

# Impressão dos resultados
print("Fornecedores de doces:")
print(df_doces)

print("\nFornecedores de salgados:")
print(df_salgados)


emails = acharemails(df_doces, df_salgados)
assunto = "Parabéns pelos seus resultados!"
corpo = "Gostaríamos de parabenizá-los pelas suas vendas excepcionais. Continuem com o ótimo trabalho!"
enviar_emails(emails, assunto, corpo)

print(f'Os principais emails são:')
for i in emails:
    print(i)



