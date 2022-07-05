#การแสดงคำในlist
movies = ["doraemon","godzilla","mission impossible","kingsman","ninja turtles"]
print(movies[1])
#เปลี่ยนค่าในlist
movies[1] = "resident evil"
print(movies[1])
#เปลี่ยนค่าlistหลายตำแหน่ง
movies[1:3] = ["marvel","dc","xmen"]
print(movies)
#การเพิ่มค่าในlist
movies.append("minions")
print(movies)
movies.insert(0,"kung fu panda")
print(movies)
action = ["top gun maverick","avengers","green lantern"]
movies.extend(action)
print(movies)
#ลบคำในlist
movies.remove("ninja turtles")
movies.pop(5)
#del movies
movies.sort(reverse=True)
print(movies)
#อธิพัชร์ อภิมงคล เลขที่ 27