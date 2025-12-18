# # data_menu.py

# # Dikelola oleh Anggota 2 (Data & Variabel)

# def dapatkan_menu():
#     """Mengembalikan struktur data menu restoran."""
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
#     """Mengembalikan daftar harga datar (dict) untuk perhitungan cepat."""
#     daftar_harga = {}
#     for items in dapatkan_menu().values():
#         for item in items:
#             daftar_harga[item["nama"]] = item["harga"]
#     return daftar_harga

# # Variabel utama yang bisa di-import (Anggota 2)
# MENU_RESTORAN = dapatkan_menu()
# DAFTAR_HARGA = dapatkan_daftar_harga()


# data_model.py (Modul untuk Data)

MENU = {
    "Makanan Utama": [
        {"nama": "Nasi Goreng Spesial", "harga": 35000},
        {"nama": "Mie Ayam Bakso", "harga": 28000},
        {"nama": "Sate Ayam Madura", "harga": 40000},
    ],
    "Minuman": [
        {"nama": "Es Teh Manis", "harga": 8000},
        {"nama": "Jus Alpukat", "harga": 15000},
        {"nama": "Kopi Latte Panas", "harga": 25000},
    ]
}

RESTORAN_NAMA = "Restoran 4 Sekawan"