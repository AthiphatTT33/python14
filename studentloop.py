student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for i in student :
    if i['score']>= 80:
        print(i['name'],i['score'],"4")
for k in student :
    if k['score']== 70:
        print(k['name'],k['score'],"3")
for o in student :
    if o['score']== 65:
        print(o['name'],o['score'],"2")
for l in student :
    if l['score']== 51:
        print(l['name'],l['score'],"1")
for u in student :
    if u['score']< 50:
        print(u['name'],u['score'],"0")