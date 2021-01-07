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
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import tabula
import pandas as pd
import io
import math

pd.options.display.max_colwidth = 1000
pd.options.display.max_rows = None
filename = "Padrao_TISS_Componente_Organizacional__202012.pdf"

# # Table 30

# +
page = 79
top = 132.87
left = 134.41
bottom = top + 83.1
right = left + 212.2
col_boundary = 201.75

df = tabula.read_pdf(filename,
                     pages=page,
                     guess=False,
                     area=[top, left, bottom, right],
                     columns=[col_boundary])[0]
df
# -

df.to_csv('table-30.csv', index=False)

# # Table 32

# +
page = 85
top = 147.08
left = 136.12
bottom = top + 54.73
right = left + 177.02
col_boundary = 169.6

df = tabula.read_pdf(filename,
                     pages=page,
                     guess=False,
                     area=[top, left, bottom, right],
                     columns=[col_boundary])[0]
df
# -

df.to_csv('table-32.csv', index=False)

# # Table 31

first_page = 79
last_page = 84 + 1  # need to add 1 since end index is exclusive
pages = list(range(first_page, last_page))
dfs = tabula.read_pdf(filename, pages=pages)[1:]

dfs[0]

# Fix the first dataframe (which contains the header)
df = dfs[0]
headers = df.iloc[0]
dfs[0]  = pd.DataFrame(df.values[1:], columns=headers)
dfs[0]


# +
# Set the headers in the remaining dataframes

def set_headers(df, headers):
    new_df = pd.read_csv(io.StringIO(df.to_csv(index=False)), header=None)
    return pd.DataFrame(new_df.values, columns=headers)

for i in range(1, len(dfs)):
    dfs[i] = set_headers(dfs[i], headers)
# -

df = pd.concat(dfs, ignore_index=True)

df.columns

df

# +
'''
Tabula does not deal well with entries that take up more
than one line in the PDF.
We need to scan the df in order to find these entries
and fix them up.
'''

def fix_entries(df):
    new_df = pd.DataFrame(columns=df.columns)
    i = 1
    while i < df.shape[0]:
        row = df.iloc[i-1].copy()
        x = df.iloc[i]['Descrição da categoria']
        if isinstance(x, float) and math.isnan(x):
            suffix = df.iloc[i]['Código']
            row['Descrição da categoria'] += ' {}'.format(suffix)
            i += 1
        new_df = new_df.append(row, ignore_index=True)
        i += 1
        
    row = df.iloc[df.shape[0]-1].copy()  # copy last row
    new_df.append(row, ignore_index=True)
    return new_df

new_df = fix_entries(df)
# -

# We can now export to CSV
new_df.to_csv('table-31.csv', index=False)
