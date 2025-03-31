# backup-s-processo
Realizando os backup's em python de forma pratica e rapida com otimização na memoria gerando arquivos de kb em vez de mb ou gb

# Consulta de Operações no PostgreSQL e Exportação para JSON
Isso é um modelo de backup para mensagens bancarias tipo de uma psti com select focado nos campos de uma mensageria do bacen

## Descrição
Este script Python conecta-se a um banco de dados PostgreSQL, executa uma consulta SQL para obter operações dentro de um intervalo de tempo específico, e exporta os resultados para um arquivo JSON.

## Tecnologias Utilizadas
- Python 3
- Biblioteca `psycopg2` para conexão com PostgreSQL
- Biblioteca `json` para manipulação dos dados

## Requisitos
Antes de executar o script, certifique-se de ter:
- Python 3 instalado
- Biblioteca `psycopg2` instalada (`pip install psycopg2` ou `pip install psycopg2-binary`)
- Um banco de dados PostgreSQL acessível

## Configuração
Atualize os parâmetros de conexão no script:
```python
conexao = psycopg2.connect(
    host="seu host de base",
    port="sua porta especifica",
    database="sua database",
    user="o usuario da sua base",
    password="senha de acesso a base"
)
```

## Execução
Execute o script com o comando:
```sh
python script.py
```

## Estrutura da Saída JSON
O resultado será salvo no arquivo `resultado_consolid_msgid.json` com a seguinte estrutura:
```json
{
    "consulta": "Lista de operacoes com STATUSOP especificado",
    "intervalo_tempo": {},
    "status_operacao": [106, 107, 108, 111, 112, 204, 205],
    "resultado": [
        {
            "msgid": "<valor>",
            "codmsg": "<valor>",
            "nuop": "<valor>",
            "ts_inclusao": "YYYY-MM-DD HH:MM:SS",
            "consolid": "<valor>"
        }
    ]
}
```

## Observações
- Certifique-se de ter as permissões necessárias para acessar o banco de dados.
- Caso ocorram erros, verifique a conexão e os parâmetros de acesso.

## Autor
Vinicius Costa de Paula
