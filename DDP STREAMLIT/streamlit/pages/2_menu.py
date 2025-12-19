# ============================================================
# HALAMAN MENU - 2_Menu.py
# Tugas Kelompok: Aplikasi Pemesanan Restoran
# Anggota: 4 Orang
# ============================================================
# Halaman ini menampilkan daftar menu makanan dan minuman
# ============================================================

import streamlit as st
import menu_data
import utils


# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title=f"{menu_data.NAMA_RESTORAN} - Menu",
    page_icon="📋",
    layout="wide"
)

# ============================================================
# INISIALISASI SESSION STATE
# ============================================================
# VARIABEL: Keranjang belanja dalam session state
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# ============================================================
# STYLING CSS
# ============================================================
st.markdown("""
<style>
    .page-header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .menu-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: transform 0.2s;
        height: 100%;
    }
    .menu-card:hover {
        transform: translateY(-5px);
    }
    .menu-image img {
    border-radius: 15px;
    object-fit: cover;
    height: 180px;
    width: 100%;
    margin-bottom: 0.75rem;
    }     
    .menu-name {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 0.5rem;
    }
    .menu-desc {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    .menu-price {
        font-size: 1.1rem;
        font-weight: bold;
        color: #11998e;
    }
    .kategori-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0 1rem 0;
    }
    .keranjang-badge {
        background: #f5576c;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
    }
    .search-box {
        margin-bottom: 1.5rem;
    }
    .filter-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
    }
    .status-tersedia {
        color: #28a745;
        font-size: 0.8rem;
    }
    .status-habis {
        color: #dc3545;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER HALAMAN
# ============================================================
# VARIABEL: Menghitung jumlah item di keranjang
jumlah_keranjang = utils.hitung_jumlah_keranjang(st.session_state.keranjang)

st.markdown(f"""
<div class="page-header">
    <h1>📋 Daftar Menu</h1>
    <p>Pilih menu favorit Anda</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# INFO KERANJANG
# ============================================================
col_info1, col_info2 = st.columns([3, 1])

with col_info1:
    st.markdown(f"### 🛒 Keranjang Anda: **{jumlah_keranjang}** item")

with col_info2:
    # LOGIKA: Tampilkan tombol lihat keranjang jika ada item
    if jumlah_keranjang > 0:
        if st.button("🛒 Lihat Keranjang", type="primary"):
            st.switch_page("pages/3_Pemesanan.py")

# ============================================================
# FILTER DAN PENCARIAN
# ============================================================
st.markdown('<div class="filter-section">', unsafe_allow_html=True)

col_search, col_filter = st.columns([2, 1])

with col_search:
    # VARIABEL: Input pencarian
    keyword_pencarian = st.text_input("🔍 Cari Menu", placeholder="Ketik nama menu...")

with col_filter:
    # VARIABEL: Filter kategori
    kategori_terpilih = st.selectbox(
        "📂 Filter Kategori",
        ["Semua"] + menu_data.KATEGORI_MENU
    )

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# FUNCTION: Menambah item ke keranjang
# ============================================================
def tambah_ke_keranjang(menu_item, jumlah):
    """
    Menambahkan item ke keranjang
    Menggunakan LOGIKA dan LOOPING
    """
    # Cek apakah item sudah ada di keranjang
    ada, index = utils.cek_item_keranjang(st.session_state.keranjang, menu_item["id"])
    
    # LOGIKA: Update atau tambah item
    if ada:
        # Update jumlah jika sudah ada
        st.session_state.keranjang[index]["jumlah"] += jumlah
    else:
        # Tambah item baru
        item_baru = {
            "id": menu_item["id"],
            "nama": menu_item["nama"],
            "harga": menu_item["harga"],
            "kategori": menu_item["kategori"],
            "jumlah": jumlah
        }
        st.session_state.keranjang.append(item_baru)


# ============================================================
# FUNCTION: Menampilkan kartu menu
# ============================================================
def tampilkan_menu_card(menu_item, col_key):
    
    """
    Menampilkan kartu menu individual
    Menggunakan LOGIKA untuk status ketersediaan
    """
    with st.container():
         # Tampilkan gambar
        gambar = menu_item.get("gambar", "../assets/images/default.jpg")
        st.image(gambar, use_container_width=True)
        st.markdown(f"""
        <div class="menu-card">
            <div class="menu-name">{menu_item['nama']}</div>
            <div class="menu-desc">{menu_item['deskripsi']}</div>
            <div class="menu-price">{utils.format_rupiah(menu_item['harga'])}</div>
        </div>
        """, unsafe_allow_html=True)

        
        # LOGIKA: Cek ketersediaan
        if menu_item['tersedia']:
            col_qty, col_btn = st.columns([1, 1])
            with col_qty:
                qty = st.number_input(
                    "Jumlah",
                    min_value=1,
                    max_value=10,
                    value=1,
                    key=f"qty_{col_key}_{menu_item['id']}"
                )
            with col_btn:
                if st.button("➕ Tambah", key=f"add_{col_key}_{menu_item['id']}"):
                    tambah_ke_keranjang(menu_item, qty)
                    st.success(f"✅ {menu_item['nama']} ditambahkan!")
                    st.rerun()
        else:
            st.markdown('<span class="status-habis">❌ Stok Habis</span>', unsafe_allow_html=True)


# ============================================================
# MENAMPILKAN MENU - Menggunakan LOOPING dan LOGIKA
# ============================================================

# LOGIKA: Filter berdasarkan pencarian atau kategori
if keyword_pencarian:
    # Menggunakan FUNCTION dari modul menu_data
    menu_tampil = menu_data.cari_menu(keyword_pencarian)
    st.markdown(f"### Hasil Pencarian: '{keyword_pencarian}'")
    
    # LOGIKA: Cek hasil pencarian
    if len(menu_tampil) == 0:
        st.warning("❌ Menu tidak ditemukan. Coba kata kunci lain.")
    else:
        # LOOPING: Menampilkan hasil pencarian
        cols = st.columns(3)
        for i, menu in enumerate(menu_tampil):
            with cols[i % 3]:
                tampilkan_menu_card(menu, f"search_{i}")

elif kategori_terpilih != "Semua":
    # Menggunakan FUNCTION dari modul menu_data
    menu_tampil = menu_data.get_menu_by_kategori(kategori_terpilih)
    
    st.markdown(f"""
    <div class="kategori-header">
        <h3>{kategori_terpilih}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # LOOPING: Menampilkan menu berdasarkan kategori
    cols = st.columns(3)
    for i, menu in enumerate(menu_tampil):
        with cols[i % 3]:
            tampilkan_menu_card(menu, f"cat_{i}")

else:
    # Tampilkan semua menu berdasarkan kategori
    # LOOPING: Iterasi setiap kategori
    for kategori in menu_data.KATEGORI_MENU:
        st.markdown(f"""
        <div class="kategori-header">
            <h3>{kategori}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Menggunakan FUNCTION dari modul menu_data
        menu_kategori = menu_data.get_menu_by_kategori(kategori)
        
        # LOOPING: Menampilkan menu dalam kategori
        cols = st.columns(3)
        for i, menu in enumerate(menu_kategori):
            with cols[i % 3]:
                tampilkan_menu_card(menu, f"{kategori}_{i}")
        
        st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# SIDEBAR: KERANJANG MINI
# ============================================================
with st.sidebar:
    st.markdown("### 🛒 Keranjang Belanja")
    st.markdown("---")
    
    # LOGIKA: Cek apakah keranjang kosong
    if len(st.session_state.keranjang) == 0:
        st.info("Keranjang masih kosong")
    else:
        # VARIABEL: Hitung subtotal
        subtotal = 0
        
        # LOOPING: Tampilkan item di keranjang
        for item in st.session_state.keranjang:
            total_item = item["harga"] * item["jumlah"]
            subtotal += total_item
            
            st.markdown(f"""
            **{item['nama']}**  
            {item['jumlah']} x {utils.format_rupiah(item['harga'])} = {utils.format_rupiah(total_item)}
            """)
            st.markdown("---")
        
        # Tampilkan subtotal
        st.markdown(f"### Subtotal: {utils.format_rupiah(subtotal)}")
        
        # Tombol aksi
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Kosongkan"):
                st.session_state.keranjang = []
                st.rerun()
        with col2:
            if st.button("📝 Pesan"):
                st.switch_page("pages/3_Pemesanan.py")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: gray; padding: 1rem;">
    <p>© 2024 {menu_data.NAMA_RESTORAN}</p>
</div>
""", unsafe_allow_html=True)

