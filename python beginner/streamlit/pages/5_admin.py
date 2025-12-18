# ============================================================
# HALAMAN ADMIN - 5_Admin.py
# Tugas Kelompok: Aplikasi Pemesanan Restoran
# Anggota: 4 Orang
# ============================================================
# Halaman ini untuk admin mengelola menu dan pesanan
# ============================================================

import streamlit as st
from datetime import datetime
import menu_data
import utils
import database

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title=f"{menu_data.NAMA_RESTORAN} - Admin",
    page_icon="⚙️",
    layout="wide"
)

# ============================================================
# INISIALISASI DATABASE DAN SESSION STATE
# ============================================================
database.init_database()

if "riwayat_pesanan" not in st.session_state:
    st.session_state.riwayat_pesanan = []

if "menu_tambahan" not in st.session_state:
    st.session_state.menu_tambahan = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# Sinkronisasi dengan database
pesanan_db = database.get_semua_pesanan()
if len(pesanan_db) > 0:
    st.session_state.riwayat_pesanan = pesanan_db

menu_db = database.get_menu_tambahan()
if len(menu_db) > 0:
    st.session_state.menu_tambahan = menu_db

# ============================================================
# STYLING CSS
# ============================================================
st.markdown("""
<style>
    .page-header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .admin-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .stats-row {
        display: flex;
        justify-content: space-around;
        margin: 1rem 0;
    }
    .stat-item {
        text-align: center;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 10px;
        min-width: 150px;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #3498db;
    }
    .login-box {
        max-width: 400px;
        margin: 2rem auto;
        padding: 2rem;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .menu-table {
        width: 100%;
        border-collapse: collapse;
    }
    .menu-table th, .menu-table td {
        padding: 0.75rem;
        text-align: left;
        border-bottom: 1px solid #eee;
    }
    .menu-table th {
        background: #f8f9fa;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER HALAMAN
# ============================================================
st.markdown(f"""
<div class="page-header">
    <h1>⚙️ Panel Admin</h1>
    <p>Kelola menu dan pesanan restoran</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LOGIKA: Cek login admin
# ============================================================
if not st.session_state.admin_logged_in:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("### 🔐 Login Admin")
    
    with st.form("form_login"):
        username = st.text_input("Username", placeholder="Masukkan username...")
        password = st.text_input("Password", type="password", placeholder="Masukkan password...")
        
        submitted = st.form_submit_button("Login", type="primary", use_container_width=True)
        
        # LOGIKA: Validasi login
        if submitted:
            # VARIABEL: Kredensial admin (untuk demo)
            ADMIN_USERNAME = "admin"
            ADMIN_PASSWORD = "admin123"
            
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.toast("✅ Login berhasil!", icon="🎉")
                st.rerun()
            else:
                st.error("❌ Username atau password salah!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.info("💡 Hint: Username: admin, Password: admin123")

else:
    # ============================================================
    # TOMBOL LOGOUT
    # ============================================================
    col_title, col_logout = st.columns([4, 1])
    
    with col_logout:
        if st.button("🚪 Logout", type="secondary"):
            st.session_state.admin_logged_in = False
            st.toast("👋 Logout berhasil!", icon="✅")
            st.rerun()
    
    # ============================================================
    # STATISTIK DASHBOARD
    # ============================================================
    st.markdown("### 📊 Dashboard")
    
    # VARIABEL: Menghitung statistik
    total_menu = len(menu_data.get_semua_menu()) + len(st.session_state.menu_tambahan)
    total_pesanan = len(st.session_state.riwayat_pesanan)
    
    # Menghitung total pendapatan menggunakan LOOPING
    total_pendapatan = 0
    pesanan_aktif = 0
    for pesanan in st.session_state.riwayat_pesanan:
        total_pendapatan += pesanan["total"]
        # LOGIKA: Hitung pesanan aktif
        if pesanan["status"] in ["Menunggu", "Diproses", "Siap"]:
            pesanan_aktif += 1
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📋 Total Menu", total_menu)
    
    with col2:
        st.metric("🧾 Total Pesanan", total_pesanan)
    
    with col3:
        st.metric("⏳ Pesanan Aktif", pesanan_aktif)
    
    with col4:
        st.metric("💰 Total Pendapatan", utils.format_rupiah(total_pendapatan))
    
    st.markdown("---")
    
    # ============================================================
    # TAB UNTUK FITUR ADMIN
    # ============================================================
    tab1, tab2, tab3 = st.tabs(["📋 Kelola Menu", "🧾 Kelola Pesanan", "➕ Tambah Menu Baru"])
    
    # ============================================================
    # TAB 1: KELOLA MENU
    # ============================================================
    with tab1:
        st.markdown("### 📋 Daftar Menu")
        
        # Filter kategori
        kategori_filter = st.selectbox(
            "Filter Kategori",
            ["Semua"] + menu_data.KATEGORI_MENU,
            key="admin_kategori_filter"
        )
        
        # LOOPING: Menampilkan menu berdasarkan kategori
        for kategori in menu_data.KATEGORI_MENU:
            # LOGIKA: Filter kategori
            if kategori_filter != "Semua" and kategori != kategori_filter:
                continue
            
            st.markdown(f"#### {kategori}")
            
            # Ambil menu berdasarkan kategori
            menu_list = menu_data.get_menu_by_kategori(kategori)
            
            # LOOPING: Menampilkan setiap menu
            for i, menu in enumerate(menu_list):
                col_info, col_price, col_status, col_action = st.columns([3, 2, 2, 1])
                
                with col_info:
                    st.markdown(f"**{menu['nama']}**")
                    st.caption(menu['deskripsi'])
                
                with col_price:
                    st.markdown(utils.format_rupiah(menu['harga']))
                
                with col_status:
                    # LOGIKA: Status ketersediaan
                    if menu['tersedia']:
                        st.success("Tersedia")
                    else:
                        st.error("Habis")
                
                with col_action:
                    # Toggle ketersediaan
                    if st.button("🔄", key=f"toggle_{kategori}_{i}", help="Toggle Status"):
                        menu['tersedia'] = not menu['tersedia']
                        status = "tersedia" if menu['tersedia'] else "habis"
                        st.toast(f"Status {menu['nama']} diubah menjadi {status}", icon="✅")
                        st.rerun()
                
                st.markdown("---")
        
        # Menampilkan menu tambahan dari session state
        if len(st.session_state.menu_tambahan) > 0:
            st.markdown("#### 🆕 Menu Tambahan (Baru)")
            
            for i, menu in enumerate(st.session_state.menu_tambahan):
                col_info, col_price, col_status, col_action = st.columns([3, 2, 2, 1])
                
                with col_info:
                    st.markdown(f"**{menu['nama']}**")
                    st.caption(menu['deskripsi'])
                
                with col_price:
                    st.markdown(utils.format_rupiah(menu['harga']))
                
                with col_status:
                    if menu['tersedia']:
                        st.success("Tersedia")
                    else:
                        st.error("Habis")
                
                with col_action:
                    if st.button("🗑️", key=f"del_new_{i}", help="Hapus Menu"):
                        database.hapus_menu_tambahan(menu["id"])
                        st.session_state.menu_tambahan.pop(i)
                        st.toast("Menu berhasil dihapus!", icon="🗑️")
                        st.rerun()
                
                st.markdown("---")
    
    # ============================================================
    # TAB 2: KELOLA PESANAN
    # ============================================================
    with tab2:
        st.markdown("### 🧾 Daftar Pesanan")
        
        # LOGIKA: Cek apakah ada pesanan
        if len(st.session_state.riwayat_pesanan) == 0:
            st.info("Belum ada pesanan")
        else:
            # Filter status
            status_filter = st.selectbox(
                "Filter Status",
                ["Semua"] + menu_data.STATUS_PESANAN,
                key="admin_status_filter"
            )
            
            # LOOPING: Menampilkan pesanan
            for i, pesanan in enumerate(st.session_state.riwayat_pesanan):
                # LOGIKA: Filter status
                if status_filter != "Semua" and pesanan["status"] != status_filter:
                    continue
                
                with st.expander(f"🧾 {pesanan['id_pesanan']} - {pesanan['nama_pelanggan']} ({pesanan['status']})"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.markdown(f"""
                        **ID:** {pesanan['id_pesanan']}  
                        **Nama:** {pesanan['nama_pelanggan']}  
                        **Meja:** {pesanan['nomor_meja']}  
                        **Waktu:** {utils.format_waktu(pesanan['waktu_pesan'])}
                        """)
                        
                        st.markdown("**Item Pesanan:**")
                        for item in pesanan['items']:
                            st.markdown(f"- {item['nama']} x{item['jumlah']}")
                    
                    with col2:
                        st.markdown(f"**Total:** {utils.format_rupiah(pesanan['total'])}")
                        
                        # Dropdown untuk update status
                        new_status = st.selectbox(
                            "Update Status",
                            menu_data.STATUS_PESANAN,
                            index=menu_data.STATUS_PESANAN.index(pesanan['status']),
                            key=f"status_{i}"
                        )
                        
                        if new_status != pesanan['status']:
                            if st.button("💾 Simpan", key=f"save_{i}"):
                                st.session_state.riwayat_pesanan[i]["status"] = new_status
                                database.update_status_pesanan(pesanan["id_pesanan"], new_status)
                                st.toast(f"Status pesanan diubah menjadi {new_status}", icon="✅")
                                st.rerun()
    
    # ============================================================
    # TAB 3: TAMBAH MENU BARU
    # ============================================================
    with tab3:
        st.markdown("### ➕ Tambah Menu Baru")
        
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        
        with st.form("form_tambah_menu"):
            nama_menu = st.text_input("Nama Menu", placeholder="Masukkan nama menu...")
            
            col1, col2 = st.columns(2)
            
            with col1:
                harga_menu = st.number_input("Harga (Rp)", min_value=1000, max_value=1000000, value=25000, step=1000)
            
            with col2:
                kategori_menu = st.selectbox("Kategori", menu_data.KATEGORI_MENU)
            
            deskripsi_menu = st.text_area("Deskripsi", placeholder="Deskripsi singkat menu...")
            
            tersedia_menu = st.checkbox("Menu Tersedia", value=True)
            
            submitted = st.form_submit_button("➕ Tambah Menu", type="primary", use_container_width=True)
            
            # LOGIKA: Proses tambah menu
            if submitted:
                # Validasi
                if not nama_menu:
                    st.error("❌ Nama menu tidak boleh kosong!")
                elif not deskripsi_menu:
                    st.error("❌ Deskripsi tidak boleh kosong!")
                else:
                    # Generate ID menu baru
                    new_id = f"NEW{datetime.now().strftime('%H%M%S')}"
                    
                    # VARIABEL: Menu baru
                    menu_baru = {
                        "id": new_id,
                        "nama": nama_menu,
                        "harga": harga_menu,
                        "deskripsi": deskripsi_menu,
                        "kategori": kategori_menu,
                        "tersedia": tersedia_menu
                    }
                    
                    # Simpan ke session state
                    st.session_state.menu_tambahan.append(menu_baru)
                    
                    # Simpan ke database
                    database.simpan_menu_tambahan(menu_baru)
                    
                    st.toast(f"✅ Menu '{nama_menu}' berhasil ditambahkan!", icon="🎉")
                    st.success(f"✅ Menu '{nama_menu}' berhasil ditambahkan!")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: gray; padding: 1rem;">
    <p>© 2024 {menu_data.NAMA_RESTORAN} - Panel Admin</p>
</div>
""", unsafe_allow_html=True)
