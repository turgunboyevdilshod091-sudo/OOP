# class Book :

#     def __init__(self,author,title,cost):
#         self.muallif=author
#         self.nomi=title
#         self.narx=cost

# book1=Book("Shukrullo","Kafansiz ko'milganlar",56000)
# print(book1.muallif)
# print(book1.nomi)
# print(book1.narx)

# class Person:

#     def __init__(self,name,age,xobby):
#         self.ism=name
#         self.yosh=age
#         self.mashgulot=xobby

# person1=Person("Dilshod",17,"Fudbol va kitob o'qish")
# print(person1.ism)
# print(person1.yosh)
# print(person1.mashgulot)

# class Rectangle:
     
#     def __init__(self,length,width):
#           self.uzunlik=length
#           self.kenglik=width

# maydon1=Rectangle(15,20)
# print(maydon1.uzunlik*maydon1.kenglik)

# class Oquvchi:

#     def __init__(self,name,surname,age,group):
#         self.ism=name
#         self.familya=surname
#         self.yosh=age
#         self.guruh=group

# oquvchi1=Oquvchi("Dilshod","Tur'unboyev",17,"Ra-04-24")

# print(oquvchi1.ism)
# print(oquvchi1.familya)
# print(oquvchi1.yosh)
# print(oquvchi1.guruh)


class Avtomobil:

    def __init__(self,brand,model,color):
        self.nomi=brand
        self.modeli=model
        self.rang=color

avtomobil1=Avtomobil("BMW","M5","Black")
avtomobil2=Avtomobil("Porshe","911","Blue")

print(avtomobil1.nomi)
print(avtomobil1.modeli)
print(avtomobil1.rang)
print(avtomobil2.nomi)
print(avtomobil2.modeli)
print(avtomobil2.rang)