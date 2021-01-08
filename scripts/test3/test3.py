# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     comment_magics: true
#     split_at_heading: true
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3.8.2 64-bit
#     metadata:
#       interpreter:
#         hash: 20bf69066c0dd38d51965b69d5e1b6e387082e3198ba56e97997ac55f4e50ad0
#     name: python3
# ---

import psycopg2
from os import listdir

DB = 'test3'
USER = 'breno'
PORT = 5433  # typically 5432


# +
def startup(database, user, port):
    conn = psycopg2.connect(database=database, user=user, port=port)
    cur = conn.cursor()
    return (conn, cur)

(conn, cur) = startup(DB, USER, PORT)


# -

# Next we create the tables according to the formats
# found in the CSV files.

# +
def create_accounting_table(conn, cur):
    create_accounting_table_query = (
    '''
    CREATE TABLE accounting (
        data DATE,
        reg_ans INT,
        cd_conta_contabil INT,
        descricao VARCHAR(255),
        vl_saldo_final FLOAT
        );
    '''
    )
    cur.execute('set datestyle to iso;')
    cur.execute(create_accounting_table_query)
    conn.commit()
    
def create_companies_table(conn, cur):
    create_companies_table_query = (
    '''
    CREATE TABLE companies (
        reg_ans INT,
        cnpj VARCHAR(15),
        razao_social VARCHAR(255),
        nome_fantasia VARCHAR(255),
        modalidade VARCHAR(255),
        logradouro VARCHAR(255),
        numero VARCHAR(255),
        complemento VARCHAR(255),
        bairro VARCHAR(255),
        cidade VARCHAR(255),
        uf VARCHAR(255),
        cep VARCHAR(255),
        ddd VARCHAR(255),
        telefone VARCHAR(255),
        fax VARCHAR(255),
        email VARCHAR(255),
        representante VARCHAR(255),
        cargo_representante VARCHAR(255),
        data_registro_ans date
        );
    '''
    )
    cur.execute('set datestyle to dmy;')
    cur.execute(create_companies_table_query)
    conn.commit()


def create_tables(conn, cur,):
    create_accounting_table(conn, cur)
    create_companies_table(conn, cur)


# -

# only run this if the tables have not been created already
create_tables(conn, cur)


# We now need to read the provided CSVs into the tables.

def load_csvs(conn, cur, dir, companies_csv):
    filenames = [dir + filename for filename in listdir(dir)]
    copy_csv_query = (lambda table, filename:
    '''COPY {}
    FROM \'{}\'
    DELIMITER \';\'
    ENCODING \'latin1\'
    CSV HEADER;
    '''.format(table, filename)
    )

    cur.execute(copy_csv_query('companies', companies_csv))

    for filename in filenames:
        cur.execute(copy_csv_query('accounting', filename))
    conn.commit()


# only run this if data has not been loaded
# check the filenames
dir = '/Users/breno/Documents/intuitive-care/test3/'
companies_csv = dir + 'Relatorio_cadop-2.csv'
load_csvs(conn, cur, dir + 'processed-data/', companies_csv)


def fetch_results(description, start_date, end_date):
    query = (
    '''
    select reg_ans,
    sum (vl_saldo_final)
    from accounting
    where descricao=\'{}\'
    and data >= \'{}\'
    and data <  \'{}\'
    group by reg_ans
    order by sum (vl_saldo_final) desc;
    '''.format(description, start_date, end_date)
    )

    cur.execute(query)
    results = cur.fetchall()
    return results


def fetch_companies(results):
    tuples = []
    for (code, value) in results:
        query = (
            'select razao_social from companies where reg_ans={};'
            .format(code)
        )
        cur.execute(query)
        fetch = cur.fetchone()
        name = fetch[0] if fetch else fetch
        tuples.append((name, code, value))
    return tuples


# First query: over the last year
description = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
start_date = '2020-01-01'
end_date = '2021-01-01'
output_filename = 'query-year.csv'
results = fetch_results(description, start_date, end_date)[:10]
companies = fetch_companies(results)
with open(output_filename, 'w') as f:
    s = 'Razão Social, Registro ANS, Valor Total'
    print(s)
    f.write(s + '\n')
    for company in companies:
        s = '{}, {}, {}'.format(*company)
        print(s)
        f.write(s + '\n')

# Second query: over the last trimester
description = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
start_date = '2020-07-01'
end_date = '2020-10-01'
output_filename = 'query-trimester.csv'
results = fetch_results(description, start_date, end_date)[:10]
companies = fetch_companies(results)
with open(output_filename, 'w') as f:
    s = 'Razão Social, Registro ANS, Valor Total'
    print(s)
    f.write(s + '\n')
    for company in companies:
        s = '{}, {}, {}'.format(*company)
        print(s)
        f.write(s + '\n')


def shutdown(conn, cur):
    cur.close()
    conn.close()


shutdown(conn, cur)
