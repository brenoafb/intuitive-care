# coding=utf-8
import psycopg2
import sys
import argparse
from os import listdir

parser = argparse.ArgumentParser(description='Process SQL queries')
parser.add_argument('database', metavar='-d', type=str, nargs='?', default='test')
parser.add_argument('user', metavar='-u', type=str, nargs='?', default='postgres')
parser.add_argument('port', metavar='-p', type=int, nargs='?', default=5432)
parser.add_argument('-l', action=argparse.BooleanOptionalAction)

def main():
    args = parser.parse_args()
    print('args: {}'.format(args))

    # descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    # query = 'select * from test where descricao=\'{}\' order by vl_saldo_final desc;'.format(descricao)

    # cur.execute(query)

    # dir = '/Users/breno/Documents/intuitive-care/test3/processed-data/'

def startup(database, user, port):
    conn = psycopg2.connect(database=database, user=user, port=port)
    cur = conn.cursor()

def create_table():
    create_table_query = (
    '''
    CREATE TABLE test (
        data DATE,
        reg_ans INT,
        cd_conta_contabil INT,
        descricao VARCHAR(255),
        vl_saldo_final FLOAT
        );
    '''
    )
    cur.execute(create_table_query)
    cur.commit()

def load_csvs(dir):
    filenames = [dir + filename for filename in listdir(dir)]
    copy_csv_query = (lambda x:
    '''COPY test
    FROM \'{}\'
    DELIMITER \';\'
    ENCODING \'latin1\'
    CSV HEADER;
    '''.format(x)
    )
    for filename in filenames:
        cur.execute(copy_csv_query(filename))
    cur.commit()

if __name__ == '__main__':
    main()
