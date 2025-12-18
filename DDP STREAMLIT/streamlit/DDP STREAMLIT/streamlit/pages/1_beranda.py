# ============================================================
# HALAMAN BERANDA - 1_Beranda.py
# Tugas Kelompok: Aplikasi Pemesanan Restoran
# Anggota: 4 Orang
# ============================================================
# Halaman ini menampilkan informasi restoran dan welcome page
# ============================================================

import streamlit as st
import menu_data
import utils

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title=f"{menu_data.NAMA_RESTORAN} - Beranda",
    page_icon="🍽️",
    layout="wide"
)

# ============================================================
# STYLING CSS
# ============================================================
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    .feature-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        height: 100%;
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .promo-banner {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 2rem 0;
    }
    .stats-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stats-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER UTAMA
# ============================================================
st.markdown(f"""
<div class="main-header">
    <h1>🍽️ {menu_data.NAMA_RESTORAN}</h1>
    <p>Cita Rasa Nusantara yang Autentik</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# DESKRIPSI RESTORAN
# ============================================================
st.markdown("### Selamat Datang!")
st.markdown(f"""
<div class="info-card">
    {menu_data.DESKRIPSI_RESTORAN}
</div>
""", unsafe_allow_html=True)

# ============================================================
# INFORMASI RESTORAN - Menggunakan Columns
# ============================================================
st.markdown("### 📍 Informasi Restoran")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="info-card">
        <h4>📍 Alamat</h4>
        <p>{menu_data.ALAMAT_RESTORAN}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="info-card">
        <h4>📞 Telepon</h4>
        <p>{menu_data.TELEPON_RESTORAN}</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="info-card">
        <h4>🕐 Jam Buka</h4>
        <p>{menu_data.JAM_BUKA}</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# BANNER PROMO
# ============================================================
st.markdown(f"""
<div class="promo-banner">
    <h2>🎉 PROMO SPESIAL!</h2>
    <p>Dapatkan diskon {menu_data.DISKON_MEMBER}% untuk member setia kami!</p>
    <p>Gunakan kode: <strong>MEMBER10</strong></p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FITUR APLIKASI - Menggunakan LOOPING
# ============================================================
st.markdown("### ✨ Fitur Aplikasi")

# VARIABEL: Data fitur aplikasi
fitur_list = [
    {"icon": "📋", "judul": "Menu Lengkap", "deskripsi": "Lihat semua menu makanan dan minuman dengan harga terjangkau"},
    {"icon": "🛒", "judul": "Pemesanan Mudah", "deskripsi": "Pesan menu favorit Anda dengan mudah dan cepat"},
    {"icon": "📊", "judul": "Riwayat Pesanan", "deskripsi": "Pantau status dan riwayat pesanan Anda kapan saja"},
    {"icon": "💰", "judul": "Harga Transparan", "deskripsi": "Harga jelas tanpa biaya tersembunyi"}
]

# Menggunakan LOOPING untuk menampilkan fitur
cols = st.columns(4)
for i, fitur in enumerate(fitur_list):
    with cols[i]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{fitur['icon']}</div>
            <h4>{fitur['judul']}</h4>
            <p>{fitur['deskripsi']}</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# STATISTIK MENU - Menggunakan FUNCTION dan LOOPING
# ============================================================
st.markdown("### 📊 Statistik Menu")

# Menggunakan FUNCTION dari modul menu_data
semua_menu = menu_data.get_semua_menu()

# VARIABEL: Menghitung statistik
total_menu = len(semua_menu)
total_makanan_utama = len(menu_data.menu_makanan_utama)
total_makanan_ringan = len(menu_data.menu_makanan_ringan)
total_minuman = len(menu_data.menu_minuman)
total_dessert = len(menu_data.menu_dessert)

# Menampilkan statistik
stat_cols = st.columns(5)

statistik_data = [
    {"label": "Total Menu", "value": total_menu, "icon": "🍽️"},
    {"label": "Makanan Utama", "value": total_makanan_utama, "icon": "🍛"},
    {"label": "Makanan Ringan", "value": total_makanan_ringan, "icon": "🍟"},
    {"label": "Minuman", "value": total_minuman, "icon": "🥤"},
    {"label": "Dessert", "value": total_dessert, "icon": "🍨"}
]

# LOOPING: Menampilkan statistik
for i, stat in enumerate(statistik_data):
    with stat_cols[i]:
        st.markdown(f"""
        <div class="stats-card">
            <div style="font-size: 2rem;">{stat['icon']}</div>
            <div class="stats-number">{stat['value']}</div>
            <p>{stat['label']}</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# MENU POPULER - Menggunakan LOOPING dan LOGIKA
# ============================================================
st.markdown("### 🔥 Menu Populer")

# VARIABEL: Menu populer (3 item pertama dari makanan utama)
menu_populer = menu_data.menu_makanan_utama[:3]

cols = st.columns(3)

# LOOPING: Menampilkan menu populer

for i, menu in enumerate(menu_populer):
    with cols[i]:
        st.image(
            menu["gambar"],
            use_container_width=True
        )

        st.markdown(f"""
        <div class="quick-menu">
            <h4>{menu['nama']}</h4>
            <p style="color:#666;">{menu['deskripsi']}</p>
            <h3 style="color:#667eea;">
                {utils.format_rupiah(menu['harga'])}
            </h3>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# CARA PEMESANAN
# ============================================================
st.markdown("### 📝 Cara Pemesanan")

langkah_pemesanan = [
    "Buka halaman **Menu** untuk melihat daftar makanan dan minuman",
    "Pilih menu yang diinginkan dan masukkan ke keranjang",
    "Buka halaman **Pemesanan** untuk mengisi data dan konfirmasi pesanan",
    "Pantau status pesanan di halaman **Riwayat Pesanan**"
]

# LOOPING: Menampilkan langkah-langkah
for i, langkah in enumerate(langkah_pemesanan, 1):
    st.markdown(f"**{i}.** {langkah}")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: gray; padding: 1rem;">
    <p>© 2024 {menu_data.NAMA_RESTORAN} - Tugas Kelompok Pemrograman Python</p>
    <p>Dibuat dengan ❤️ menggunakan Streamlit</p>
</div>
""", unsafe_allow_html=True)
