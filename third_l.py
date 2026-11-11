# lst = []

# for i in range(int(input("Nechta son: "))):
#     son = int(input(">>> "))
#     lst.append(son)

# for son in lst:
#     if son % 2 == 0:
#         print(son)

# ---------------------------------

# lst = ["Salom", "exam", "chopilasan", "uxlasen", "Baraka", "TOPGUR!"]
# new = []
# for soz in lst:
#     if soz[0].isupper():
#         new.append(soz)
# print(new)

# ---------------------------------

# lst = ["salom", 45, "kiyiK", 12, True, "Olma", "amma", 11, True, 45]
# bool_t = []
# str_t = []
# int_t = []
# for i in lst:
#     if type(i) == str and i not in str_t:
#         str_t.append(i)
#     elif type(i) == int and i not in int_t:
#         int_t.append(i)
#     elif type(i) == bool and i not in bool_t:
#         bool_t.append(i)
# print(bool_t)
# print(int_t)
# print(str_t)


# lst = ["salom", "Maktab"]
# lst.insert(1, "malina")
# print(lst)


# lst = ["salom", "Maktab"]
# lst.extend("abc")
# lst.extend([12,34,10])
# lst.append([12,34,"salom"])
# print(lst)

# ------------------------------

# lst = [23, 12, 10, 23, 9, 7, 6, 23]
# lst.clear()

# for i in range(lst.count(23)):
#     lst.remove(23)
# print(lst)

# for son in lst.copy():
#     if son % 2:
#         lst.remove(son)
# print(lst)


# lst = ["kiyik", "olma", "poliz"]

# for index, soz in enumerate(lst):
#     if soz == soz[::-1]:
#         lst[index] = "polindrom soz bor edi"

# print(lst)

# -------------------------

# lst = [23, 12, 43, 23, True]
# lst.sort()
# lst.sort(reverse=True)


# lst = ["abb", "aaa", "abc", "z", "az"]
# lst.sort()
# print(lst)

# -------------------------

# lst = [23, 12, 4, 64, 7]
# max(lst) # 64
# min(lst) # 4
# sum(lst) # 110


# lst = [[1,5,4], [2,4], [1,1,1]]
# new = []
# for royxat in lst:
#     new.append(sum(royxat))
# print(new)
# ------------------------------------------------------------
# lst =[True,"salom",5,5.6]
# bool_t = []
# str_t=[]
# int_t=[]
# float_t=[]
# for i in lst:
#     if type(i)==str:
#         print("<class'string'>")
#     elif type(i)==bool:
#         print("<class'bool'>")
#     elif type(i)==int:
#         print("<class'int'>")
#     elif type(i)==float:
#         print("<class'float'>")
# lst=[7,8,1,3,4,5,6,9]
# new=[]
# for i in lst:
#     if i%2:
#        new.append(i*i)
#     elif i%2==0:
#         new.append(i*i*i)
# print(new)
# lst = [3,1,0,0,7,0,1,0,4,0,0,8,0]
# n=lst.count(0)
# for i in range(n):
#     lst.remove(0)
# for i in range(n):
#     lst.append(0)
# print(lst)
# lst=[2,1,0,-8,9,9,7]
# lst.sort()
# for i in range(lst.count(9)):
#     lst.remove(9)
# print(lst[-1])
# lst=[1,1,4,7,8,7,9,5,5,6,6]
# tozalangan=[]
# lst.sort()
# for i in lst:
#     if i not in tozalangan:
#         tozalangan.append(i)
# print(tozalangan)
# lst =[11,33,50]
# new=""
# for son in lst:
#     new+=str(son)
# print(int(new))
# a = [12, 4, 3, 2, 1, 10]
# b = [5, 3, 2, 1, 2, 4]
# c = a + b
# print(sum(c) / len(c))
# lst=[False,"ada",4,454,"aziza"]
# for  soz in lst:
#     if type(soz)==str and soz == soz[::-1]:
#       print(soz,"Palindrom soz")
#     elif type(soz)==str and soz !=soz[::-1]:
#        print(soz,"Palindrom soz emas")






