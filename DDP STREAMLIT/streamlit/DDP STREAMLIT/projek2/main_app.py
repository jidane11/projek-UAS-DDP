# # app.py

# import streamlit as st
# # Modul (Anggota 1)
# from pages import PAGES 

# # --- Setup Awal & Session State (Anggota 2: Variabel) ---
# st.set_page_config(
#     page_title="Aplikasi Pemesanan Restoran",
#     layout="wide"
# )

# # Inisialisasi Session State (Anggota 2)
# if 'keranjang' not in st.session_state:
#     st.session_state.keranjang = {} 
# if 'transaksi_terakhir' not in st.session_state:
#     st.session_state.transaksi_terakhir = None 
# if 'page_select' not in st.session_state:
#     st.session_state.page_select = "Menu Utama" 

# # --- Tampilan Utama (Anggota 1: Pages Navigasi) ---

# st.title("🍽️ Aplikasi Pemesanan Restoran Streamlit")
# st.markdown("---")

# # Pilihan navigasi sidebar (Anggota 1)
# st.sidebar.radio(
#     "Navigasi",
#     list(PAGES.keys()),
#     index=list(PAGES.keys()).index(st.session_state.page_select), 
#     key="page_select" # Menggunakan key yang sama dengan session state agar mudah diakses di modul lain
# )

# # Panggil fungsi halaman yang dipilih (Anggota 1)
# PAGES[st.session_state.page_select]()

# main_app.py
import streamlit as st
from data_model import RESTORAN_NAMA
from order_logic import hitung_total_pesanan, tampilkan_detail_pesanan

# Menggunakan Streamlit Page Configuration
st.set_page_config(
    page_title=RESTORAN_NAMA,
    page_icon="🍽️",
    layout="wide"
)

# --- 1. Variabel dan Logika Inisialisasi Sesi ---
if 'pesanan' not in st.session_state:
    # Variabel session_state untuk menyimpan pesanan
    st.session_state.pesanan = {}

if 'total_harga' not in st.session_state:
    # Variabel session_state untuk menyimpan total harga
    st.session_state.total_harga = 0

# --- 2. Navigasi Halaman (Pages) ---

# Streamlit kini mendukung navigasi multi-page melalui struktur file di folder 'pages/'
# Kita hanya perlu memastikan setiap file page memiliki fungsi `run()` atau menggunakan struktur file otomatis.
# Karena kita menggunakan folder 'pages', Streamlit akan otomatis menampilkan sidebar navigasi.

# Tampilan Halaman Utama (Bisa dipindahkan ke pages/home.py, tapi untuk contoh ini kita taruh di sini)
st.title(f"Selamat Datang di {RESTORAN_NAMA} 🍽️")
st.markdown("Pesan makanan favorit Anda dengan mudah dan cepat.")

# Tampilan Sidebar (Menu Navigasi)
st.sidebar.title("Menu Utama")
st.sidebar.page_link("pages/menu_order.py", label="🍜 Menu & Order")
st.sidebar.page_link("pages/review.py", label="🛒 Review Order")
st.sidebar.page_link("pages/about.py", label="ℹ️ About Us")

# Logika Sederhana untuk Tampilan Pesanan di Sidebar
if st.session_state.pesanan:
    total = hitung_total_pesanan(st.session_state.pesanan)
    st.session_state.total_harga = total
    st.sidebar.info(f"**Total Pesanan Anda:**\n\n**Rp {total:,}**")
else:
    st.sidebar.info("Keranjang Anda kosong.")

# Catatan: Kode Streamlit Pages sisanya akan berada di folder `pages/`