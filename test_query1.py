"""    CONNECTION INTO A SQL ESRVER DB USING SQLServerToPandasDataFrame LIBRARY,
                AND CREATE A QUERY INTO A PANDAS DATAFRAME
"""
from SQLServerToPandasDataFrame import createConnection, runQuery
from pipesql import  upload

Base_Query = "select prod.nombre, COUNT(inv.id) 'Cantidad Total' FROM productos prod JOIN inventarios inv ON inv.id_prod = prod.id GROUP BY prod.nombre"
    
server = "localhost"
user = "sa"
password = "Pass12345"
    
conn = createConnection("company", server, user, password)
query1 = runQuery(Base_Query, conn)

upload(query1,'Cantidad')