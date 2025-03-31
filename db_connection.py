import psycopg2
import json

# Parâmetros de conexão ao banco de dados PostgreSQL
conexao = psycopg2.connect(
    host="seu host de base",
    port="sua porta especifica",
    database="sua database",
    user="o usuario da sua base",
    password="senha de acesso a base"
)

# Executar a consulta SQL
consulta_sql = """
WITH params AS (
  SELECT 
      '2024-07-09 05:00:00.000'::timestamp AS dt_inicio,
      '2024-07-09 10:59:59.999'::timestamp AS dt_fim,
       08357240 AS ispb
),
msg_limits AS (
  SELECT 
      min(msgid) AS min_msgid, 
      max(msgid) AS max_msgid
  FROM csspi.operacao, params
  WHERE ts_inclusao >= params.dt_inicio
    AND ts_inclusao <= params.dt_fim
)
SELECT 
  msgid, 
  codmsg, 
  nuop, 
  ts_inclusao, 
  msgop
FROM csspi.operacao
JOIN params
  ON csspi.operacao.ispb = params.ispb
WHERE STATUSOP IN (106, 107, 108, 111, 112, 204, 205)
  AND ts_inclusao >= params.dt_inicio
  AND ts_inclusao <= params.dt_fim;
"""

# Abrir o cursor para executar a consulta
cursor = conexao.cursor()
cursor.execute(consulta_sql)

# Obter o resultado da consulta (múltiplas linhas)
resultado = cursor.fetchall()  # fetchall() para capturar todos os resultados

# Depuração: Exibir o resultado para ver o que está retornando
print("Resultado da consulta:", resultado)

# Fechar o cursor e a conexão
cursor.close()
conexao.close()

# Preparar os dados em formato de lista de dicionários para serem convertidos em JSON
dados_json = {
    "consulta": "Lista de operacoes com STATUSOP especificado",
    "intervalo_tempo": {
       # "inicio": "2023-05-01 00:00:00",
       # "fim": "2023-05-03 23:59:59"
    },
    "status_operacao": [106, 107, 108, 111, 112, 204, 205],
    "resultado": [
        {
            "msgid": linha[0],
            "codmsg": linha[1],
            "nuop": linha[2],
            "ts_inclusao": linha[3].strftime('%Y-%m-%d %H:%M:%S'),  # Convertendo timestamp para string
            "consolid": linha[4]  # msgop como 'consolid'
        }
        for linha in resultado
    ]
}

# Salvar os dados em um arquivo JSON
with open('resultado_consolid_msgid.json', 'w') as json_file:
    json.dump(dados_json, json_file, indent=4)

print("Arquivo JSON 'resultado_consolid_msgid.json' criado com sucesso!")
