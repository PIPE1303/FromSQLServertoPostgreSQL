###SCRIPT DESIGNED TO PRINT A FORMATED STRING WITH A SPECIFIED QUERY TO SOLVE THE CASE STUDY

inventory = [
    [23.7, 24.6, 66.6, 77.8, 88.9],
    [11.1, 22.2, 33.3, 44.4, 55.5],
    [26.7, 14.6, 86.6, 97.8, 8.9],
    [1.5, 23.7, 84.6, 76.6, 47.7, 98.9],
    [23.6, 23.7, 24.6, 66.6, 77.8, 88.6]
]

QUERY_INSERT = 'INSERT INTO "dbo"."inventarios" VALUES '

count = 0
values = []

for idx, product in enumerate(inventory):
    for idj, j in enumerate(product):
        count += 1
        values.append(f"({count},{idx+1},{j})")

imp = QUERY_INSERT + ",".join(values)
print(imp)