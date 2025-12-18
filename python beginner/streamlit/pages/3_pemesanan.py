# ============================================================
# HALAMAN PEMESANAN - 3_Pemesanan.py
# Tugas Kelompok: Aplikasi Pemesanan Restoran
# Anggota: 4 Orang
# ============================================================
# Halaman ini untuk melakukan pemesanan dan checkout
# ============================================================

import streamlit as st
from datetime import datetime
import menu_data
import utils

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title=f"{menu_data.NAMA_RESTORAN} - Pemesanan",
    page_icon="🛒",
    layout="wide"
)

# ============================================================
# INISIALISASI SESSION STATE
# ============================================================
# VARIABEL: Keranjang dan riwayat pesanan
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

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
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .order-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .item-row {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid #eee;
    }
    .total-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    .form-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .success-message {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
    .empty-cart {
        text-align: center;
        padding: 3rem;
        background: #f8f9fa;
        border-radius: 15px;
        margin: 2rem 0;
    }
    .discount-badge {
        background: #28a745;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER HALAMAN
# ============================================================
st.markdown(f"""
<div class="page-header">
    <h1>🛒 Pemesanan</h1>
    <p>Konfirmasi dan selesaikan pesanan Anda</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LOGIKA: Cek apakah keranjang kosong
# ============================================================
if len(st.session_state.keranjang) == 0:
    st.markdown("""
    <div class="empty-cart">
        <h2>🛒 Keranjang Kosong</h2>
        <p>Silakan pilih menu terlebih dahulu</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📋 Lihat Menu", type="primary"):
        st.switch_page("pages/2_Menu.py")

else:
    # ============================================================
    # LAYOUT 2 KOLOM
    # ============================================================
    col_order, col_form = st.columns([1, 1])
    
    # ============================================================
    # KOLOM KIRI: DAFTAR PESANAN
    # ============================================================
    with col_order:
        st.markdown("### 📋 Daftar Pesanan")
        
        st.markdown('<div class="order-card">', unsafe_allow_html=True)
        
        # VARIABEL: Untuk menyimpan subtotal
        subtotal = 0
        
        # LOOPING: Menampilkan setiap item di keranjang
        for i, item in enumerate(st.session_state.keranjang):
            # Menghitung total per item menggunakan FUNCTION
            total_item = utils.hitung_total_item(item["harga"], item["jumlah"])
            subtotal += total_item
            
            col_item, col_qty, col_price, col_action = st.columns([3, 2, 2, 1])
            
            with col_item:
                st.markdown(f"**{item['nama']}**")
                st.caption(f"{item['kategori']}")
            
            with col_qty:
                # Input untuk mengubah jumlah
                new_qty = st.number_input(
                    "Qty",
                    min_value=0,
                    max_value=99,
                    value=item["jumlah"],
                    key=f"qty_{i}",
                    label_visibility="collapsed"
                )
                
                # LOGIKA: Update jumlah jika berubah
                if new_qty != item["jumlah"]:
                    if new_qty == 0:
                        st.session_state.keranjang = utils.hapus_item_keranjang(
                            st.session_state.keranjang, 
                            item["id"]
                        )
                        st.rerun()
                    else:
                        st.session_state.keranjang[i]["jumlah"] = new_qty
                        st.rerun()
            
            with col_price:
                st.markdown(f"**{utils.format_rupiah(total_item)}**")
            
            with col_action:
                if st.button("🗑️", key=f"del_{i}"):
                    st.session_state.keranjang = utils.hapus_item_keranjang(
                        st.session_state.keranjang, 
                        item["id"]
                    )
                    st.rerun()
            
            st.markdown("---")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # ============================================================
        # RINGKASAN PEMBAYARAN
        # ============================================================
        st.markdown("### 💰 Ringkasan Pembayaran")
        
        # VARIABEL: Diskon dan pajak
        diskon = 0
        persen_diskon = 0
        
        # Input kode promo
        kode_promo = st.text_input("🎁 Kode Promo (opsional)", placeholder="Masukkan kode promo...")
        
        # LOGIKA: Validasi kode promo
        if kode_promo:
            if kode_promo.upper() == "MEMBER10":
                persen_diskon = menu_data.DISKON_MEMBER
                st.success(f"✅ Kode promo valid! Diskon {persen_diskon}%")
            elif kode_promo.upper() == "PROMO15":
                persen_diskon = menu_data.DISKON_PROMO
                st.success(f"✅ Kode promo valid! Diskon {persen_diskon}%")
            else:
                st.error("❌ Kode promo tidak valid")
        
        # Menghitung diskon menggunakan FUNCTION
        diskon = utils.hitung_diskon(subtotal, persen_diskon)
        
        # VARIABEL: Subtotal setelah diskon
        subtotal_setelah_diskon = subtotal - diskon
        
        # Menghitung pajak menggunakan FUNCTION
        pajak = utils.hitung_pajak(subtotal_setelah_diskon)
        
        # Menghitung total akhir menggunakan FUNCTION
        total_akhir = utils.hitung_total_akhir(subtotal, diskon, pajak)
        
        # Menampilkan ringkasan
        st.markdown(f"""
        <div class="order-card">
            <div class="item-row">
                <span>Subtotal</span>
                <span>{utils.format_rupiah(subtotal)}</span>
            </div>
        """, unsafe_allow_html=True)
        
        # LOGIKA: Tampilkan diskon jika ada
        if diskon > 0:
            st.markdown(f"""
            <div class="item-row" style="color: #28a745;">
                <span>Diskon ({persen_diskon}%)</span>
                <span>-{utils.format_rupiah(diskon)}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="item-row">
                <span>Pajak ({menu_data.PAJAK}%)</span>
                <span>{utils.format_rupiah(pajak)}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="total-section">
            <h2 style="margin: 0; text-align: center;">Total: {utils.format_rupiah(total_akhir)}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # ============================================================
    # KOLOM KANAN: FORM PEMESANAN
    # ============================================================
    with col_form:
        st.markdown("### 📝 Data Pemesanan")
        
        st.markdown('<div class="form-section">', unsafe_allow_html=True)
        
        # Form input
        with st.form("form_pemesanan"):
            # Input nama pelanggan
            nama_pelanggan = st.text_input(
                "👤 Nama Pelanggan",
                placeholder="Masukkan nama Anda..."
            )
            
            # Input nomor meja
            nomor_meja = st.number_input(
                "🪑 Nomor Meja",
                min_value=1,
                max_value=20,
                value=1
            )
            
            # Input catatan
            catatan = st.text_area(
                "📝 Catatan Khusus (opsional)",
                placeholder="Contoh: Tidak pedas, tanpa bawang..."
            )
            
            # Metode pembayaran
            metode_pembayaran = st.selectbox(
                "💳 Metode Pembayaran",
                ["Tunai", "Kartu Debit", "Kartu Kredit", "E-Wallet"]
            )
            
            # Tombol submit
            submitted = st.form_submit_button("✅ Konfirmasi Pesanan", type="primary", use_container_width=True)
            
            # LOGIKA: Proses pemesanan
            if submitted:
                # Validasi nama menggunakan FUNCTION
                valid_nama, pesan_nama = utils.validasi_nama(nama_pelanggan)
                
                # Validasi meja menggunakan FUNCTION
                valid_meja, pesan_meja = utils.validasi_meja(nomor_meja)
                
                # LOGIKA: Cek validasi
                if not valid_nama:
                    st.error(f"❌ {pesan_nama}")
                elif not valid_meja:
                    st.error(f"❌ {pesan_meja}")
                else:
                    # Generate ID pesanan menggunakan FUNCTION
                    id_pesanan = utils.generate_id_pesanan()
                    
                    # VARIABEL: Data pesanan baru
                    pesanan_baru = {
                        "id_pesanan": id_pesanan,
                        "nama_pelanggan": nama_pelanggan,
                        "nomor_meja": nomor_meja,
                        "catatan": catatan,
                        "metode_pembayaran": metode_pembayaran,
                        "items": st.session_state.keranjang.copy(),
                        "subtotal": subtotal,
                        "diskon": diskon,
                        "pajak": pajak,
                        "total": total_akhir,
                        "waktu_pesan": datetime.now(),
                        "status": "Menunggu"
                    }
                    
                    # Simpan ke riwayat pesanan
                    st.session_state.riwayat_pesanan.append(pesanan_baru)
                    
                    # Kosongkan keranjang
                    st.session_state.keranjang = []
                    
                    # Set flag untuk menampilkan pesan sukses
                    st.session_state.pesanan_sukses = pesanan_baru
                    
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Tombol kembali ke menu
        if st.button("◀️ Kembali ke Menu"):
            st.switch_page("pages/2_Menu.py")

# ============================================================
# LOGIKA: Tampilkan pesan sukses jika ada
# ============================================================
if "pesanan_sukses" in st.session_state and st.session_state.pesanan_sukses:
    pesanan = st.session_state.pesanan_sukses
    
    st.markdown(f"""
    <div class="success-message">
        <h1>✅ Pesanan Berhasil!</h1>
        <h2>ID Pesanan: {pesanan['id_pesanan']}</h2>
        <p>Terima kasih, <strong>{pesanan['nama_pelanggan']}</strong>!</p>
        <p>Pesanan Anda sedang diproses. Silakan tunggu di meja <strong>{pesanan['nomor_meja']}</strong></p>
        <p>Total Pembayaran: <strong>{utils.format_rupiah(pesanan['total'])}</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tampilkan detail pesanan
    st.markdown("### 📋 Detail Pesanan")
    
    # Menggunakan FUNCTION untuk membuat ringkasan
    ringkasan = utils.buat_ringkasan_pesanan(pesanan)
    st.code(ringkasan)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📋 Lihat Menu Lagi", use_container_width=True):
            st.session_state.pesanan_sukses = None
            st.switch_page("pages/2_Menu.py")
    
    with col2:
        if st.button("📊 Lihat Riwayat Pesanan", use_container_width=True):
            st.session_state.pesanan_sukses = None
            st.switch_page("pages/4_Riwayat.py")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: gray; padding: 1rem;">
    <p>© 2024 {menu_data.NAMA_RESTORAN}</p>
</div>
""", unsafe_allow_html=True)
