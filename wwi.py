# -*- coding: utf-8 -*-

#==============================================================================
# Created on Tue Apr 18 12:22:57 2017
# 
# @author: jbrugger
# 
# Goals:
# 1. shape the data into a pandas dataframe
# 2. do aggregations on the columns using numpy
# 3. do visualizations using matplotlib
# 
#==============================================================================

import adodbapi as ado
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

host = "localhost"
database = "WideWorldImporters"
user = "junk"
password = "fred"
connStr = "Provider=SQLOLEDB.1;User ID={0};Password={1};Initial Catalog={2};Data Source={3}".format(user, password, database, host)
conn = ado.connect(connStr)


with conn.cursor() as cur:
    sql = """
    WITH sg
    AS (
    	SELECT StockItemId
    		,StockGroupId
    		,ROW_NUMBER() OVER (PARTITION BY StockItemId ORDER BY StockGroupId) AS RowNum
    	FROM Warehouse.StockItemStockGroups
    )
    SELECT l.OrderLineId
    ,l.OrderId
    ,CONVERT(varchar(256), l.Description) AS [Description]
    ,l.Quantity
    ,l.UnitPrice
    ,o.OrderDate
    ,CONVERT(varchar(256), g.StockGroupName) AS [DefaultStockGroupName]
    ,CONVERT(varchar(256), c.CustomerName) AS [CustomerName]
    ,CONVERT(varchar(256), sp.SalesTerritory) AS [SalesTerritory]
    ,CONVERT(varchar(256), p.FullName) AS [SalesPersonFullName]
    FROM Sales.Orders o
    JOIN Sales.OrderLines l ON o.OrderId = l.OrderId
    JOIN sg ON l.StockItemID = sg.StockItemID AND RowNum = 1
    JOIN Warehouse.StockGroups g ON sg.StockGroupID = g.StockGroupID
    JOIN Sales.Customers c ON c.CustomerID = o.CustomerID
    JOIN Application.Cities ci ON ci.CityID = c.PostalCityID
    JOIN Application.StateProvinces sp ON sp.StateProvinceID = ci.StateProvinceID
    JOIN Application.People p ON o.SalespersonPersonID = p.PersonID
    ORDER BY l.OrderLineId
    """
    
    cur.execute(sql)

    #can't seem to create df directly from ado cursor
    #it returns "not-iterable"
    #so we use list comprehensions
    data = [row for row in cur.fetchall()]
    columns = [col[0] for col in cur.description]

    #create the dataframe
    df = pd.DataFrame.from_records(data=data, columns=columns, index="OrderLineId")

#==============================================================================
#     #some other operations examples
#     #some quick aggregations
#     print df.OrderId.count()
#     print df.Quantity.sum()
#     print df["Quantity"].std() #alternate syntax
#     
#     #group by SalesTerritory, describe Quantity
#     print df.groupby("SalesTerritory").Quantity.sum()
#     print df.groupby("SalesTerritory")["Quantity"].describe()
#     
#     #unique items
#     df.SalesTerritory.unique()
#==============================================================================
    
    #returns a dictionary which consists of lists of series grouped by SalesTerritory
    stgrp = df.groupby("SalesTerritory").apply(lambda x: [x.Quantity]).to_dict()
  
    #just returns an array or arrays
    plotdata = [stgrp[i][0].values for i in stgrp]
    
    #plots it, simply showing that most quantities are below 50
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(plotdata)
    plt.show()



#==============================================================================
# #some alternate ways of processing the data fram from adodbapi    
# #method 1 (dict of dict)
# tbl = {}
# map(lambda row:tbl.update({row["OrderLineId"]:{"quantity":row["Quantity"], "unitPrice":row["UnitPrice"]}} ), cur.fetchmany(10))
# df = pd.DataFrame.from_dict(tbl, orient="index")
# print(df)
# 
# #method 2 (using map to build a list--redundant approach)
# rows = []
# map(lambda row:rows.append(row), cur.fetchmany(10))
# df = pd.DataFrame.from_records(rows)
# print(df)
# 
#==============================================================================
