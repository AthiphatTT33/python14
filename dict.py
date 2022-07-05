japanesetown = {"name": "nagoya",
    "thebesttouristplace": "nagoyacastle",
    "population": "2millionpeople"
}
print(japanesetown["population"])
print(japanesetown)
l = japanesetown.keys()
print(l)
#เพิ่มค่าในdict
japanesetown["sizeofthetown"] = "large"
print(japanesetown)
#แก้ค่าในdict
japanesetown["sizeofthetown"] = "small"
print(japanesetown)
#การupdate dic
japanesetown.update({"GDP":"1400million"})
print(japanesetown)
#ลบค่าdict
japanesetown.pop("population")
print(japanesetown)
del japanesetown["sizeofthetown"]
#เพิ่มค่าdictแบบlist
japanesetown.update({"livestyle":{"shopping","travel","entertainment"}})
print(japanesetown)
#เพิ่มค่าdictแบบ Nested dic
myfavouritemovies = {
    "movie1" : {
        "name" : "Vanhelsing",
        "year" : 2009
},
    "movie2" : {
        "name" : "underworld",
        "year" : 2002
},
    "movie3" : {
        "name" : "titanic",
        "year" : 1997
}
}
print(myfavouritemovies)