# Test 3 - PostgreSQL Queries with Psycopg2

[PostgreSQL](https://www.postgresql.org)

In this test we extract data from tables using SQL queries.
For this the [Psycopg2](https://www.psycopg.org/docs/) Python library is used.

To install the dependencies

```bash
$ pip install psycopg2-binary
```

The code is contained in the [notebook](test3.ipynb).
Alternatively, the [script](../scripts/test3/3.py) can be
used to execute the operations.
The database name, user, and Postgres port number need to be
correctly setup in the script.

## Data

The data is available at.
- http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
- http://www.ans.gov.br/externo/site_novo/informacoes_avaliacoes_oper/lista_cadop.asp

The files are arranged as follows:
```
.
├── Relatorio_cadop-2.csv
├── data
│   ├── 1T2019.csv
│   ├── 1T2020.csv
│   ├── 2T2019.csv
│   ├── 2T2020.csv
│   ├── 3T2019.csv
│   ├── 3T2020.csv
│   └── 4T2019.csv
├── processed-data
│   ├── 1T2019.csv
│   ├── 1T2020.csv
│   ├── 2T2019.csv
│   ├── 2T2020.csv
│   ├── 3T2019.csv
│   ├── 3T2020.csv
│   └── 4T2019.csv
```

Due to locale configuration, we need to substitute `,` with `.` in decimal values stored in the CSV files.
This is done in the `process_data.sh` script, which processes the files in `./data`
and places them in `./processed-data`. File from the latter are used in the Python program.

## Results

Results over the last year (from 2020-01-01 to 2021-01-01 - right exclusive).
```
Razão Social, Registro ANS, Valor Total
BRADESCO SAÚDE S.A., 5711, 29238637561.910004
AMIL ASSISTÊNCIA MÉDICA INTERNACIONAL S.A., 326305, 22239265407.1
SUL AMERICA COMPANHIA DE SEGURO SAÚDE, 6246, 19134861006.79
NOTRE DAME INTERMÉDICA SAÚDE S.A., 359017, 8717609226.0
CAIXA DE ASSISTÊNCIA DOS FUNCIONÁRIOS DO BANCO DO BRASIL, 346659, 6701591952.419999
CENTRAL NACIONAL UNIMED - COOPERATIVA CENTRAL, 339679, 5532110614.25
UNIMED-RIO COOPERATIVA DE TRABALHO MEDICO DO RIO DE JANEIRO, 393321, 5449561080.42
HAPVIDA ASSISTENCIA MEDICA LTDA, 368253, 5296308468.6
UNIMED BELO HORIZONTE COOPERATIVA DE TRABALHO MÉDICO, 343889, 4305426998.96
GEAP AUTOGESTÃO EM SAÚDE, 323080, 4262564672.2299995
```

Results over the last available trimester (from 2020-01-01 to 2021-01-01 - right exclusive).

```
Razão Social, Registro ANS, Valor Total
BRADESCO SAÚDE S.A., 5711, 14689350312.67
AMIL ASSISTÊNCIA MÉDICA INTERNACIONAL S.A., 326305, 10928531414.16
SUL AMERICA COMPANHIA DE SEGURO SAÚDE, 6246, 9498661307.98
NOTRE DAME INTERMÉDICA SAÚDE S.A., 359017, 4402526741.07
CAIXA DE ASSISTÊNCIA DOS FUNCIONÁRIOS DO BANCO DO BRASIL, 346659, 3337556927.0299997
CENTRAL NACIONAL UNIMED - COOPERATIVA CENTRAL, 339679, 2770465180.87
UNIMED-RIO COOPERATIVA DE TRABALHO MEDICO DO RIO DE JANEIRO, 393321, 2754253192.49
HAPVIDA ASSISTENCIA MEDICA LTDA, 368253, 2629132597.67
UNIMED BELO HORIZONTE COOPERATIVA DE TRABALHO MÉDICO, 343889, 2211589474.5299997
GEAP AUTOGESTÃO EM SAÚDE, 323080, 2062436242.9
```