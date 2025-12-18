# pages/review.py
import streamlit as st
from order_logic import hitung_total_pesanan, tampilkan_detail_pesanan

def run():
    st.title("🛒 Tinjauan Pesanan Anda")

    # Logika Cek Keranjang Kosong
    if not st.session_state.pesanan:
        st.warning("Keranjang Anda kosong! Silakan pesan menu terlebih dahulu.")
        if st.button("Pesan Sekarang"):
            st.switch_page("pages/menu_order.py")
        return

    # Menghitung total dan menampilkan detail
    total = hitung_total_pesanan(st.session_state.pesanan)
    details = tampilkan_detail_pesanan(st.session_state.pesanan)

    st.subheader("Detail Pesanan:")
    
    # Menampilkan detail pesanan dalam bentuk Tabel
    st.table(details)
    
    st.markdown("---")
    
    st.success(f"**TOTAL AKHIR PEMBAYARAN: Rp {total:,}**")
    
    st.markdown("---")

    col_back, col_confirm = st.columns(2)
    
    with col_back:
        if st.button("◀️ Ubah Pesanan"):
            st.switch_page("pages/menu_order.py")

    with col_confirm:
        # Logika Konfirmasi Pemesanan
        if st.button("✅ Konfirmasi Pesanan & Bayar", type="primary"):
            st.balloons()
            st.success("🎉 **Pesanan Anda telah berhasil dikonfirmasi!**")
            st.info("Anda akan dihubungi oleh staf kami. Terima kasih telah memesan.")
            # Reset Variabel pesanan setelah konfirmasi
            st.session_state.pesanan = {}

run()