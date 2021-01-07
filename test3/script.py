# coding=utf-8
import psycopg2
import sys
import argparse
from os import listdir

# parser = argparse.ArgumentParser(description='Process SQL queries')
# parser.add_argument('database', metavar='-d', type=str, nargs='?', default='test')
# parser.add_argument('user', metavar='-u', type=str, nargs='?', default='postgres')
# parser.add_argument('port', metavar='-p', type=int, nargs='?', default=5432)
# parser.add_argument('-l', action=argparse.BooleanOptionalAction)
# args = parser.parse_args()
# print('args: {}'.format(args))

dir = '/Users/breno/Documents/intuitive-care/test3/processed-data/'

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

def fetch_results(start_date, end_date):
    descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
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
    '''.format(descricao, start_date, end_date)
    )

    cur.execute(query)
    results = cur.fetchall()
    return results

def main():
    return

def startup(database, user, port):
    conn = psycopg2.connect(database=database, user=user, port=port)
    cur = conn.cursor()
    return (conn, cur)

def shutdown(conn, cur):
    cur.close()
    conn.close()

def create_tables(conn, cur,):
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

    cur.execute('set datestyle to iso;')
    cur.execute(create_accounting_table_query)
    cur.execute('set datestyle to dmy;')
    cur.execute(create_companies_table_query)
    conn.commit()

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

if __name__ == '__main__':
    main()
