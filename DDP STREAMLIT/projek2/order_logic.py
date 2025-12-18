# # functions.py
# from data import MENU
# import streamlit as st

# # Function: Menghitung total biaya pesanan
# def hitung_total(pesanan):
#     """
#     Menghitung total harga dari list pesanan.
#     :param pesanan: Dict of {nama_menu: jumlah_pesanan}
#     :return: Total harga (int)
#     """
#     total = 0
#     # Looping: Melakukan iterasi pada pesanan untuk menghitung total
#     for item, jumlah in pesanan.items():
#         if item in MENU:
#             total += MENU[item] * jumlah
#     return total

# # Function: Menyimpan pesanan ke State
# def simpan_pesanan(menu_item, jumlah):
#     """
#     Menyimpan atau memperbarui pesanan pelanggan di session state.
#     """
#     if 'keranjang' not in st.session_state:
#         st.session_state.keranjang = {}
    
#     # Logika: Jika jumlah > 0, simpan. Jika 0, hapus dari keranjang.
#     if jumlah > 0:
#         st.session_state.keranjang[menu_item] = jumlah
#     elif menu_item in st.session_state.keranjang:
#         del st.session_state.keranjang[menu_item]
        
#     st.success(f"Pesanan {menu_item} sebanyak {jumlah} berhasil diperbarui.")

# order_logic.py (Modul untuk Logika)


from data_model import MENU

def hitung_total_pesanan(pesanan):
    """
    Function untuk menghitung total biaya dari pesanan.
    
    Arg:
        pesanan (dict): Dictionary dengan format {nama_item: jumlah, ...}
    """
    total = 0
    
    # Logika untuk mencari harga dari MENU dan menghitung total
    for kategori, items in MENU.items():
        # Looping melalui setiap kategori dan item
        for item in items:
            if item["nama"] in pesanan:
                jumlah = pesanan[item["nama"]]
                harga_item = item["harga"]
                total += jumlah * harga_item
                
    return total

def tampilkan_detail_pesanan(pesanan):
    """
    Function untuk menampilkan detail pesanan.
    """
    detail = []
    
    for kategori, items in MENU.items():
        for item in items:
            if item["nama"] in pesanan and pesanan[item["nama"]] > 0:
                nama = item["nama"]
                jumlah = pesanan[nama]
                harga = item["harga"]
                subtotal = jumlah * harga
                detail.append([nama, f"{jumlah}x", f"Rp {harga:,}", f"Rp {subtotal:,}"])
                
    return detail