# n = int(input("n = "))
# s = 0
# for i in range(1, n + 1):
#     s += i ** i
# print("Yig'indi =", s)
# a=int(input("Yoshingizni kiriting !"))
# for i in range(1,201):
#     print(i)
#     if i==a:
#         print("Sizning yoshingiz !")
#         break
# for i in range(100, 1000):
#     a = i // 100
#     b = (i // 10) % 10
#     c = i % 10
#     if (a == b and b != c) or \
#        (a == c and a != b) or \
#        (b == c and a != b):
#         print(i, end=" ")

# yosh = int(input("Yosh: "))
# yil = int(input("Obunada bo'lish yillari: "))
# narx = 15
# print("Asosiy narx: $15")
# if yosh > 50:
#     narx = narx * 0.80
#     print("Yosh bo'yicha chegirma: 20%")
# else:
#     print("Yosh bo'yicha chegirma: 0%")
# if yil > 5:
#     narx = narx * 0.85
#     print("Obuna davomiyligi bo'yicha chegirma: 15%")
# elif yil > 3:
#     narx = narx * 0.90
#     print("Obuna davomiyligi bo'yicha chegirma: 10%")
# else:
#     print("Obuna davomiyligi bo'yicha chegirma: 0%")
# print(f"Yakuniy narx: ${narx:.2f}")


# while True:
#     parol = input("Parol: ")
#     if len(parol) < 8:
#         print("Parol juda qisqa.")
#     elif parol == parol.lower():
#         print("Katta harf yetishmayapti.")

#     elif parol.isalpha():
#         print("Raqam yetishmayapti.")

#     elif parol.isalnum():
#         print("Maxsus belgi yetishmayapti.")
#     else:
#         print("Parol kuchli!")
#         break


# for i in range(1, 4):
#     kompaniya = input(f"Kompaniya {i}: ")
#     narx = float(input("Narx: "))

#     if narx > 100:
#         print(f"{kompaniya} aksiyasi qimmat.")
#     elif narx < 50:
#         print(f"{kompaniya} aksiyasi arzon.")
#     else:
#         print(f"{kompaniya} aksiyasi o'rtacha.")
