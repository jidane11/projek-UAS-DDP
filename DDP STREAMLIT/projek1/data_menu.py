# # data_menu.py

# # Modul ini berisi data menu dan harga restoran
# # Dikelola oleh Anggota 2 (Variabel & Modul)

# def dapatkan_menu():
#     """Mengembalikan daftar menu makanan dan minuman."""
#     menu = {
#         "Makanan Utama": [
#             {"nama": "Nasi Goreng Spesial", "harga": 30000},
#             {"nama": "Mie Goreng Jawa", "harga": 28000},
#             {"nama": "Ayam Geprek", "harga": 35000},
#         ],
#         "Minuman Segar": [
#             {"nama": "Es Teh Manis", "harga": 8000},
#             {"nama": "Es Jeruk", "harga": 10000},
#             {"nama": "Jus Alpukat", "harga": 15000},
#         ]
#     }
#     return menu

# def dapatkan_daftar_harga():
#     """Mengembalikan daftar harga datar untuk perhitungan cepat."""
#     daftar_harga = {}
#     for kategori, items in dapatkan_menu().items():
#         for item in items:
#             daftar_harga[item["nama"]] = item["harga"]
#     return daftar_harga

# # Variabel utama yang bisa di-import
# MENU_RESTORAN = dapatkan_menu()
# DAFTAR_HARGA = dapatkan_daftar_harga()