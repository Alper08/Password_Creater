import random
# Characters
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# Password Length
parola_uzunlugu = int(input("Parolanın uzunluğunu girin: "))
# Password
parola = ""
# Random
for _ in range(parola_uzunlugu):
    rastgele_karakter = random.choice(karakterler)
    parola += rastgele_karakter
# Printing to Console
print("Oluşturulan parola:", parola)
