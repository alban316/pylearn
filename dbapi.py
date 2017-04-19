# -*- coding: utf-8 -*-
import adodbapi as ado



host = "CSGTAMLT38"
database = "WideWorldImporters"
user = "sa"
password = "Withersp00n"

connStr = "Provider=SQLOLEDB.1;User ID={0};Password={1};Initial Catalog={2};Data Source={3}".format(user, password, database, host)
conn = ado.connect(connStr)

with conn.cursor() as cur:
    sql = "SELECT l.OrderId, l.StockItemId, l.Description, l.Quantity, l.UnitPrice, o.OrderDate \
    FROM Sales.Orders o JOIN Sales.OrderLines l ON o.OrderId = l.OrderId"
    cur.execute(sql)

    #print rowcount to console    
    print(cur.rowcount)

    #print column names & attributes to console
    for col in cur.description:
        print(col)

    #extract 10 rows from our so-called cursor
    for row in cur.fetchmany(10):
        print(row)