# # 1
# lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# count = 0
# for x in lst:
#     if type(x) == int:
#         count += 1
# print(count)  # 6
# # 2
# lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# sonlar = []
# for x in lst:
#     if type(x) == int or type(x) == float:
#         sonlar.append(x)
# print(max(sonlar))  # 7
# # 3
# lst = ['abc', 'xyz', "bo'lib", 'aba', '1221']
# count = 0
# for s in lst:
#     if len(s) >= 2 and s[0] == s[-1]:
#         count += 1
# print(count)  
# # 4
# lst = [True, "Salom", 5, 5.6]
# natija = []
# for x in lst:
#     natija.append(type(x))
# print(natija)
# # 5
# lst = [7, 8, 1, 3, 4, 6, 7, 5]
# nusxa = lst.copy()
# for i in range(len(nusxa)):
#     if i % 2 == 0:
#         nusxa[i] = nusxa[i] ** 2
#     else:
#         nusxa[i] = nusxa[i] ** 3
# print(nusxa)
# # 6
# lst = [2, 1, -4, -9, 0, -5, 8, 3]
# lst2 = sorted(set(lst))
# print(lst2[-2])  
# # 7
# a = [1, 1, 3, 4, 4, 5, 6, 7]
# b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# hammasi = a + b
# print(sum(hammasi) / len(hammasi))  
# # 8
# lst = ["ada", 212, False, 4567, "aziza"]
# for x in lst:
#     s = str(x)
#     if s == s[::-1]:
#         print(x, "-> palindrom")
#     else:
#         print(x, "-> palindrom emas")
# # 9
# lst = ['p', 'q']
# n = 5
# yangi = []
# for i in range(1, n + 1):
#     for x in lst:
#         yangi.append(x + str(i))
# print(yangi)
# # 10
# lst = [5, 3, 8, 1]
# if lst == sorted(lst):
#     print("o'sish")
# elif lst == sorted(lst, reverse=True):
#     print("kamayish")
# else:
#     print("tartibsiz")
# # 11
# lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# yangi = []
# nol = 0
# for x in lst:
#     if x == 0:
#         nol += 1
#     else:
#         yangi.append(x)
# yangi = yangi + [0] * nol
# print(yangi)
# # 12
# lst = [[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]
# for qator in lst:
#     for i in range(1, len(qator), 2):
#         qator[i] = qator[i] ** 2
# print(lst)
# # 13
# lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# lst[2][2].append(7000)
# print(lst)