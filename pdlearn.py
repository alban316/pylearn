# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:49:10 2017

@author: jbrugger
"""
import pandas as pd


rs = []
map(lambda i:rs.append(i), range(26))
print(rs)


# a dictionary of dictionaries
d = {}
d.update({"first": {"name":"Jason", "species":"Human", "gender":"Male"}})
d.update({"second": {"name":"Kathy", "species":"Human", "gender":"Female"}})
d.update({"third": {"name":"Smacks", "species":"Cat", "gender":"Female"}})
d.update({"fourth": {"name":"Fredo", "species":"Dog", "gender":"Male"}})

print(d["third"])

df = pd.DataFrame.from_dict(d, orient="index")

print(df)