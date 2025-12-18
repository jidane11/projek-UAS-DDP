# a = "reza"
# while a<=5:
# #  if true
#     print(a)
#     a+=1

# # if false
# print("program selesai")


# for i in range (1,10,3):
#    print(i)



# j=1
# while j<=10:
    
#     k=1
#     while k<=10: 
#         print(j*k, end="")
#         k+=1
#     print()
#     j+=1



# for i in range(1,11):
#     for j in range(1,11):
#         k = i*j
#         print (k, end=' ')
#     print()




# a = 20
# while a>=0:
# #  if true
#     print(a)
#     a-=2



# password_benar = "pyhton123"
# password_input = ""

# while password_input != password_benar:
#     password_input = input("Masukkan Password: ")

# print("Password Benar! Akses diberikan.")

daftar_nama = []
print("Masukkan 5 Nama Teman: ")

for i in range(5):
    nama = input(f"Nama teman ke-{i+1}: ")
    daftar_nama.append(nama)
print("Daftar nama yang sudah di masukkan: ")
for nama in daftar_nama:
    print("-" + nama)