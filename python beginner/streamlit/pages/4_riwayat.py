# ============================================================
# HALAMAN RIWAYAT PESANAN - 4_Riwayat.py
# Tugas Kelompok: Aplikasi Pemesanan Restoran
# Anggota: 4 Orang
# ============================================================
# Halaman ini menampilkan riwayat pesanan pelanggan
# ============================================================

import streamlit as st
from datetime import datetime
import menu_data
import utils

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title=f"{menu_data.NAMA_RESTORAN} - Riwayat Pesanan",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# INISIALISASI SESSION STATE
# ============================================================
# VARIABEL: Riwayat pesanan
if "riwayat_pesanan" not in st.session_state:
    st.session_state.riwayat_pesanan = []

# ============================================================
# STYLING CSS
# ============================================================
st.markdown("""
<style>
    .page-header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .order-history-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    .order-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #eee;
    }
    .order-id {
        font-size: 1.1rem;
        font-weight: bold;
        color: #667eea;
    }
    .status-badge {
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .status-menunggu {
        background: #ffc107;
        color: #000;
    }
    .status-diproses {
        background: #17a2b8;
        color: white;
    }
    .status-siap {
        background: #28a745;
        color: white;
    }
    .status-selesai {
        background: #6c757d;
        color: white;
    }
    .status-dibatalkan {
        background: #dc3545;
        color: white;
    }
    .stats-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stats-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #667eea;
    }
    .stats-label {
        color: #666;
        font-size: 0.9rem;
    }
    .empty-history {
        text-align: center;
        padding: 3rem;
        background: #f8f9fa;
        border-radius: 15px;
        margin: 2rem 0;
    }
    .filter-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
    }
    .item-list {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER HALAMAN
# ============================================================
st.markdown(f"""
<div class="page-header">
    <h1>📊 Riwayat Pesanan</h1>
    <p>Pantau status dan riwayat pesanan Anda</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LOGIKA: Cek apakah ada riwayat pesanan
# ============================================================
if len(st.session_state.riwayat_pesanan) == 0:
    st.markdown("""
    <div class="empty-history">
        <h2>📋 Belum Ada Pesanan</h2>
        <p>Anda belum memiliki riwayat pesanan</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📋 Mulai Pesan", type="primary"):
        st.switch_page("pages/2_Menu.py")

else:
    # ============================================================
    # STATISTIK PESANAN - Menggunakan FUNCTION
    # ============================================================
    st.markdown("### 📈 Statistik Pesanan")
    
    # Menggunakan FUNCTION untuk menghitung statistik
    statistik = utils.hitung_statistik_pesanan(st.session_state.riwayat_pesanan)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{statistik['total_pesanan']}</div>
            <div class="stats-label">Total Pesanan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{utils.format_rupiah(statistik['total_pendapatan'])}</div>
            <div class="stats-label">Total Transaksi</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{statistik['pesanan_selesai']}</div>
            <div class="stats-label">Pesanan Selesai</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{statistik['pesanan_dibatalkan']}</div>
            <div class="stats-label">Pesanan Dibatalkan</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ============================================================
    # FILTER PESANAN
    # ============================================================
    st.markdown("### 🔍 Filter Pesanan")
    
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    
    col_filter1, col_filter2 = st.columns(2)
    
    with col_filter1:
        # VARIABEL: Filter status
        filter_status = st.selectbox(
            "Filter Status",
            ["Semua"] + menu_data.STATUS_PESANAN
        )
    
    with col_filter2:
        # VARIABEL: Urutan
        urutan = st.selectbox(
            "Urutkan",
            ["Terbaru", "Terlama", "Total Tertinggi", "Total Terendah"]
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============================================================
    # FUNCTION: Filter dan urutkan pesanan
    # ============================================================
    def filter_pesanan(daftar_pesanan, status, urutan):
        """
        Filter dan urutkan daftar pesanan
        Menggunakan LOOPING dan LOGIKA
        """
        hasil = []
        
        # LOOPING: Filter berdasarkan status
        for pesanan in daftar_pesanan:
            # LOGIKA: Cek status
            if status == "Semua" or pesanan["status"] == status:
                hasil.append(pesanan)
        
        # LOGIKA: Urutkan berdasarkan pilihan
        if urutan == "Terbaru":
            hasil.sort(key=lambda x: x["waktu_pesan"], reverse=True)
        elif urutan == "Terlama":
            hasil.sort(key=lambda x: x["waktu_pesan"])
        elif urutan == "Total Tertinggi":
            hasil.sort(key=lambda x: x["total"], reverse=True)
        elif urutan == "Total Terendah":
            hasil.sort(key=lambda x: x["total"])
        
        return hasil
    
    # ============================================================
    # FUNCTION: Mendapatkan class status
    # ============================================================
    def get_status_class(status):
        """
        Mendapatkan class CSS berdasarkan status
        Menggunakan LOGIKA kondisional
        """
        # LOGIKA: Mapping status ke class
        if status == "Menunggu":
            return "status-menunggu"
        elif status == "Diproses":
            return "status-diproses"
        elif status == "Siap":
            return "status-siap"
        elif status == "Selesai":
            return "status-selesai"
        elif status == "Dibatalkan":
            return "status-dibatalkan"
        else:
            return ""
    
    # ============================================================
    # DAFTAR PESANAN - Menggunakan LOOPING
    # ============================================================
    st.markdown("### 📋 Daftar Pesanan")
    
    # Filter pesanan menggunakan FUNCTION
    pesanan_filtered = filter_pesanan(
        st.session_state.riwayat_pesanan,
        filter_status,
        urutan
    )
    
    # LOGIKA: Cek hasil filter
    if len(pesanan_filtered) == 0:
        st.info("Tidak ada pesanan dengan kriteria tersebut")
    else:
        # LOOPING: Menampilkan setiap pesanan
        for i, pesanan in enumerate(pesanan_filtered):
            # Menggunakan FUNCTION untuk format waktu
            waktu_format = utils.format_waktu_singkat(pesanan["waktu_pesan"])
            status_class = get_status_class(pesanan["status"])
            
            with st.expander(f"🧾 {pesanan['id_pesanan']} - {pesanan['nama_pelanggan']} ({waktu_format})"):
                col_info, col_action = st.columns([3, 1])
                
                with col_info:
                    st.markdown(f"""
                    **ID Pesanan:** {pesanan['id_pesanan']}  
                    **Nama:** {pesanan['nama_pelanggan']}  
                    **Meja:** {pesanan['nomor_meja']}  
                    **Waktu:** {utils.format_waktu(pesanan['waktu_pesan'])}  
                    **Status:** <span class="status-badge {status_class}">{pesanan['status']}</span>
                    """, unsafe_allow_html=True)
                    
                    # Menampilkan catatan jika ada
                    if pesanan.get("catatan"):
                        st.markdown(f"**Catatan:** {pesanan['catatan']}")
                
                with col_action:
                    st.markdown(f"**Total:**")
                    st.markdown(f"### {utils.format_rupiah(pesanan['total'])}")
                
                # Menampilkan daftar item
                st.markdown("**Daftar Item:**")
                st.markdown('<div class="item-list">', unsafe_allow_html=True)
                
                # LOOPING: Menampilkan setiap item
                for item in pesanan["items"]:
                    total_item = item["harga"] * item["jumlah"]
                    st.markdown(f"• {item['nama']} x{item['jumlah']} = {utils.format_rupiah(total_item)}")
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Ringkasan pembayaran
                st.markdown("**Ringkasan Pembayaran:**")
                col_pay1, col_pay2, col_pay3 = st.columns(3)
                
                with col_pay1:
                    st.metric("Subtotal", utils.format_rupiah(pesanan["subtotal"]))
                
                with col_pay2:
                    # LOGIKA: Tampilkan diskon jika ada
                    if pesanan["diskon"] > 0:
                        st.metric("Diskon", f"-{utils.format_rupiah(pesanan['diskon'])}")
                    else:
                        st.metric("Diskon", "Rp 0")
                
                with col_pay3:
                    st.metric("Pajak (10%)", utils.format_rupiah(pesanan["pajak"]))
                
                st.markdown(f"**Metode Pembayaran:** {pesanan.get('metode_pembayaran', 'Tunai')}")
                
                # Tombol update status (untuk simulasi)
                st.markdown("---")
                st.markdown("**Update Status:**")
                col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4)
                
                with col_btn1:
                    if st.button("⏳ Diproses", key=f"proses_{i}"):
                        st.session_state.riwayat_pesanan[i]["status"] = "Diproses"
                        st.rerun()
                
                with col_btn2:
                    if st.button("✅ Siap", key=f"siap_{i}"):
                        st.session_state.riwayat_pesanan[i]["status"] = "Siap"
                        st.rerun()
                
                with col_btn3:
                    if st.button("🏁 Selesai", key=f"selesai_{i}"):
                        st.session_state.riwayat_pesanan[i]["status"] = "Selesai"
                        st.rerun()
                
                with col_btn4:
                    if st.button("❌ Batal", key=f"batal_{i}"):
                        st.session_state.riwayat_pesanan[i]["status"] = "Dibatalkan"
                        st.rerun()
    
    # ============================================================
    # TOMBOL AKSI
    # ============================================================
    st.markdown("---")
    
    col_action1, col_action2 = st.columns(2)
    
    with col_action1:
        if st.button("📋 Pesan Lagi", type="primary", use_container_width=True):
            st.switch_page("pages/2_Menu.py")
    
    with col_action2:
        if st.button("🗑️ Hapus Semua Riwayat", use_container_width=True):
            st.session_state.riwayat_pesanan = []
            st.rerun()

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: gray; padding: 1rem;">
    <p>© 2024 {menu_data.NAMA_RESTORAN}</p>
</div>
""", unsafe_allow_html=True)
