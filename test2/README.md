# Test 2 - Extracting tables from PDF with Tabula

In this test we extract three tables from a PDF using
the [Tabula](https://tabula-py.readthedocs.io/en/latest/) module.
This library uses [Pandas](https://pandas.pydata.org) to store the tables internally.
Tabula is implemented in Java, so make sure to have it installed.

First, install the dependencies

```bash
$ pip install pandas tabula-py
```

Now run the [notebook](2.ipynb) or execute the [script](../scripts/test2/2.py).

The results are stored in CSV files, which are compacted in a ZIP file.