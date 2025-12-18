# ============================================================
# FILE UTAMA APLIKASI - app.py
# Tugas Kelompok: Aplikasi Pemesanan Restoran
# Anggota: 4 Orang
# ============================================================
# File ini adalah entry point aplikasi Streamlit
# ============================================================

import streamlit as st
import menu_data
import utils

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title=menu_data.NAMA_RESTORAN,
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# INISIALISASI SESSION STATE
# ============================================================
# VARIABEL: Keranjang belanja
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# VARIABEL: Riwayat pesanan
if "riwayat_pesanan" not in st.session_state:
    st.session_state.riwayat_pesanan = []

# ============================================================
# STYLING CSS GLOBAL
# ============================================================
st.markdown("""
<style>
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    .hero-section {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .hero-subtitle {
        font-size: 1.3rem;
        opacity: 0.9;
        margin-bottom: 1.5rem;
    }
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .feature-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 0.5rem;
    }
    .feature-desc {
        color: #666;
        font-size: 0.9rem;
    }
    .info-section {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
    }
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    .promo-banner {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 5px 20px rgba(240, 147, 251, 0.4);
    }
    .quick-menu {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    .menu-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        border-bottom: 1px solid #eee;
    }
    .menu-item:last-child {
        border-bottom: none;
    }
            
    .menu-populer-img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-bottom: 1px solid #eee;
    }
    .cta-button {
        display: inline-block;
        background: white;
        color: #667eea;
        padding: 1rem 2rem;
        border-radius: 30px;
        font-weight: bold;
        text-decoration: none;
        margin-top: 1rem;
        transition: transform 0.2s;
    }
    .cta-button:hover {
        transform: scale(1.05);
    }
    .sidebar-info {
        padding: 1rem;
        background: #f0f2f6;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        margin-top: 3rem;
        border-top: 1px solid #eee;
            
    
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown(f"## 🍽️ {menu_data.NAMA_RESTORAN}")
    st.markdown("---")
    
    # Info keranjang
    jumlah_keranjang = utils.hitung_jumlah_keranjang(st.session_state.keranjang)
    
    st.markdown('<div class="sidebar-info">', unsafe_allow_html=True)
    st.markdown(f"### 🛒 Keranjang: {jumlah_keranjang} item")
    
    # LOGIKA: Tampilkan subtotal jika ada item
    if jumlah_keranjang > 0:
        subtotal = utils.hitung_subtotal(st.session_state.keranjang)
        st.markdown(f"**Subtotal:** {utils.format_rupiah(subtotal)}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📍 Navigasi")
    st.markdown("""
    - **Beranda** - Halaman utama
    - **Menu** - Lihat daftar menu
    - **Pemesanan** - Checkout pesanan
    - **Riwayat** - Lihat riwayat pesanan
    """)
    
    st.markdown("---")
    st.markdown("### ℹ️ Informasi")
    st.markdown(f"""
    **Alamat:**  
    {menu_data.ALAMAT_RESTORAN}
    
    **Telepon:**  
    {menu_data.TELEPON_RESTORAN}
    
    **Jam Buka:**  
    {menu_data.JAM_BUKA}
    """)

# ============================================================
# KONTEN UTAMA - HERO SECTION
# ============================================================
st.markdown(f"""
<div class="hero-section">
    <div class="hero-title">🍽️ {menu_data.NAMA_RESTORAN}</div>
    <div class="hero-subtitle">Cita Rasa Nusantara yang Autentik</div>
    <p>{menu_data.DESKRIPSI_RESTORAN}</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# TOMBOL NAVIGASI CEPAT
# ============================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Beranda", use_container_width=True):
        st.switch_page("pages/1_Beranda.py")

with col2:
    if st.button("📋 Lihat Menu", use_container_width=True, type="primary"):
        st.switch_page("pages/2_Menu.py")

with col3:
    if st.button("🛒 Pemesanan", use_container_width=True):
        st.switch_page("pages/3_Pemesanan.py")

with col4:
    if st.button("📊 Riwayat", use_container_width=True):
        st.switch_page("pages/4_Riwayat.py")

# ============================================================
# BANNER PROMO
# ============================================================
st.markdown(f"""
<div class="promo-banner">
    <h2>🎉 PROMO SPESIAL HARI INI!</h2>
    <p>Dapatkan diskon {menu_data.DISKON_MEMBER}% untuk member setia!</p>
    <p>Gunakan kode: <strong>MEMBER10</strong></p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FITUR APLIKASI - Menggunakan LOOPING
# ============================================================
st.markdown("## ✨ Fitur Aplikasi")

# VARIABEL: Data fitur
fitur_list = [
    {
        "icon": "📋",
        "judul": "Menu Lengkap",
        "deskripsi": "Lihat semua menu makanan dan minuman dengan harga terjangkau"
    },
    {
        "icon": "🛒",
        "judul": "Pemesanan Mudah",
        "deskripsi": "Pesan menu favorit Anda dengan mudah dan cepat"
    },
    {
        "icon": "📊",
        "judul": "Riwayat Pesanan",
        "deskripsi": "Pantau status dan riwayat pesanan Anda kapan saja"
    },
    {
        "icon": "💰",
        "judul": "Harga Transparan",
        "deskripsi": "Harga jelas tanpa biaya tersembunyi"
    }
]

# Menampilkan fitur dengan LOOPING
cols = st.columns(4)
for i, fitur in enumerate(fitur_list):
    with cols[i]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{fitur['icon']}</div>
            <div class="feature-title">{fitur['judul']}</div>
            <div class="feature-desc">{fitur['deskripsi']}</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# MENU POPULER - Menggunakan LOOPING dan FUNCTION
# ============================================================
st.markdown("## 🔥 Menu Populer")

# menu_populer = menu_data.menu_makanan_utama[:3]
# MENU POPULER DIPILIH MANUAL (TIDAK BERURUTAN)
id_menu_populer = ["MU001", "MU002", "MU003"]  
# Gado-Gado, Ayam Bakar Madu, Nasi Goreng Spesial

menu_populer = [
    menu for menu in menu_data.menu_makanan_utama
    if menu["id"] in id_menu_populer
]
cols = st.columns(3)

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
# INFORMASI RESTORAN
# ============================================================
st.markdown("## 📍 Tentang Kami")

col_info1, col_info2 = st.columns([2, 1])

with col_info1:
    st.markdown(f"""
    <div class="info-section">
        <h3>Selamat Datang di {menu_data.NAMA_RESTORAN}</h3>
        <p>{menu_data.DESKRIPSI_RESTORAN}</p>
        <br>
        <h4>Mengapa Memilih Kami?</h4>
        <ul>
            <li>Bahan-bahan berkualitas tinggi</li>
            <li>Resep tradisional autentik</li>
            <li>Harga terjangkau</li>
            <li>Pelayanan ramah dan cepat</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_info2:
    st.markdown(f"""
    <div class="info-card">
        <h4>📍 Alamat</h4>
        <p>{menu_data.ALAMAT_RESTORAN}</p>
        <br>
        <h4>📞 Telepon</h4>
        <p>{menu_data.TELEPON_RESTORAN}</p>
        <br>
        <h4>🕐 Jam Buka</h4>
        <p>{menu_data.JAM_BUKA}</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# STATISTIK MENU - Menggunakan FUNCTION dan LOOPING
# ============================================================
st.markdown("## 📊 Statistik Menu Kami")

# Menggunakan FUNCTION dari modul
semua_menu = menu_data.get_semua_menu()

# VARIABEL: Data statistik
statistik_menu = [
    {"label": "Total Menu", "value": len(semua_menu), "icon": "🍽️"},
    {"label": "Makanan Utama", "value": len(menu_data.menu_makanan_utama), "icon": "🍛"},
    {"label": "Makanan Ringan", "value": len(menu_data.menu_makanan_ringan), "icon": "🍟"},
    {"label": "Minuman", "value": len(menu_data.menu_minuman), "icon": "🥤"},
    {"label": "Dessert", "value": len(menu_data.menu_dessert), "icon": "🍨"}
]

cols = st.columns(5)

# LOOPING: Menampilkan statistik
for i, stat in enumerate(statistik_menu):
    with cols[i]:
        st.metric(
            label=f"{stat['icon']} {stat['label']}",
            value=stat['value']
        )

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer">
    <h4>📚 Tugas Kelompok - Aplikasi Pemesanan Restoran</h4>
    <p>Dibuat dengan Python dan Streamlit</p>
    <p>Elemen yang digunakan: Pages, Variabel, Logika, Looping, Function, dan Modul</p>
    <br>
    <p>© 2024 Warung Nusantara - Semua Hak Dilindungi</p>
</div>
""", unsafe_allow_html=True)
