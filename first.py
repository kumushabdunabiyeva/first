# hajm = float(input("Fayl hajmi (MB): "))
# tezlik = float(input("Tezlik (Mb/s): "))
# vaqt = (hajm * 8) / tezlik
# print("Fayl", vaqt, "soniyada yuklanadi")
# # 2
# son = int(input("Son: "))
# yuzlik = son // 100
# onlik = son // 10 % 10
# birlik = son % 10
# print("Raqamlar yig'indisi:", yuzlik + onlik + birlik)
# # 3
# soch = int(input("Soch olasizmi?\n1.Ha\n0.Yo'q\n"))
# soqol = int(input("Soqol olasizmi?\n1.Ha\n0.Yo'q\n"))
# jami = soch * 25000 + soqol * 10000
# print("Jami to'lov:", jami, "so'm")
# # 4
# ism = input()
# print("@" + ism.lower())
# # 5
# n = int(input())
# jami = n * 40000
# print("Jami to'lov:", jami, "so'm")
# print("Har bir kishi:", jami // n, "so'm")
# # 6
# s = input()
# print("Birinchi harf:", s[0])
# print("Oxirgi harf:", s[-1])
# # 7
# ism = input()
# parol = ism[:2] + ism[-2:]
# print(parol * 3)
# # 8
# kitob = input()
# print(f"{kitob.title():^30}")
# # 9
# sms = input()
# print("SMS uzunligi:", len(sms), "ta belgi")
# # 10
# h = input()
# kod = ord(h)
# print(f"Kod: {kod} → {kod + 3} → {chr(kod + 3)}")
# # 11
# s = input()
# print(s[::-1])
# # 12
# parol = input()
# uzunlik = len(parol)
# print(f"Parol uzunligi: {uzunlik} belgi — {uzunlik >= 8}")
# # 13
# tel = input()
# tel = tel.replace("+", "").replace("-", "")
# print(tel)
# # 14
# s = input()
# print("Faqat harfmi?", s.isalpha())
# print("Faqat raqammi?", s.isdigit())
# print("Harf+raqammi?", s.isalnum())
# # 15
# ism = input()
# a = ord(ism[0])
# b = ord(ism[1])
# c = ord(ism[2])
# print(ism[0], "→", a)
# print(ism[1], "→", b)
# print(ism[2], "→", c)
# print("Jami:", a + b + c)