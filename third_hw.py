# lst=[1,7,8,False,6,"salom"]
# sanoq = 0
# for son in lst:
#     if type(son) == int:
#         sanoq += 1
# print(sanoq)
# lst=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12,22]
# new=[]
# for son in lst:
#     if type(son) in (int, float):
#         new.append(son)
# print(max(new))
# lst=['abc', 'xyz', "bo'lib", 'aba', '1221']
# count =0
# for i in lst:
#     if len(i)>=2 and i[0]==i[-1]:
#         print(i)
#         count+=1
# print(count)
# lst=[True, "Salom", 5, 5.6]
# bool_t=[]
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
# royxat = ['p', 'q']
# n = 5
# natija = []
# for i in range(1, n + 1):
#     for element in royxat:
#         natija.append(element + str(i))
# print(natija)
# lst = list(map(int, input("Sonlarni kiriting: ").split()))
# if lst == sorted(lst):
#     print("O'sish")
# elif lst == sorted(lst, reverse=True):
#     print("Kamayish")
# else:
#     print("Tartibsiz")
# lst = [3,1,0,0,7,0,1,0,4,0,0,8,0]
# n=lst.count(0)
# for i in range(n):
#     lst.remove(0)
# for i in range(n):
#     lst.append(0)
# print(lst)
# royxat = [[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]
# for qator in royxat:
#     for i in range(len(qator)):
#         if i % 2 == 1:
#             qator[i] = qator[i] ** 2
# print(royxat)
# royxat = [[1, 2, 3], [4000, 5000, 6000], [8000, 9000]]
# for qator in royxat:
#     if 6000 in qator:
#         qator.insert(qator.index(6000) + 1, 7000)
# print(royxat)
