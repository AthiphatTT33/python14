fruits = ("apple","orange","rose apple")
print(fruits[2])
fruits = ("apple","orange","jujude","pear","custard apple")
print(fruits[2:5])
print(fruits[:5])
print(fruits[2:])
#เพิ่มค่าใน tuple
h = ("apple","orange","rose apple")
k = list(h) #แปลงเป็น list ในค่า y
k[0] = "grape"
h = tuple(k)
#แปลงlistเป็นtupleแล้วกลับมาที่ค่าx
print(h)
#ลบค่าในtuple
h = ("apple","orange","rose apple")
k = list(h)
k.remove("orange")
h = tuple(k)
print(h)
#join
tuple1 = ("i","j","k")
tuple2 = (4,5,6)
tuple3 = tuple1 +tuple2
print(tuple3)
h = range(2, 8)
for n in h:
    print(n)
h = range(2, 18 , 1)
for n in h:
    print("doraemon",n)
    #นายอธิพัชร์ อภิมงคล เลขที่ 27