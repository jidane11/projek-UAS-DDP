# pages/menu_order.py
import streamlit as st
from data_model import MENU, RESTORAN_NAMA
from order_logic import hitung_total_pesanan

def run():
    st.title("🍜 Menu dan Pemesanan")
    st.header("Pilih Menu Anda")

    col1, col2, col3 = st.columns(3)
    
    # Looping melalui Kategori Menu
    for kategori, items in MENU.items():
        st.subheader(f"***{kategori}***")
        
        # Looping melalui Item dalam Kategori
        for item in items:
            nama = item["nama"]
            harga = item["harga"]
            
            # Logika untuk menampilkan input dan menyimpan pesanan
            key = f"input_{nama.replace(' ', '_')}"
            
            # Mendapatkan jumlah pesanan saat ini (Variabel dari session state)
            initial_value = st.session_state.pesanan.get(nama, 0)
            
            # Input untuk jumlah item
            jumlah = st.number_input(
                f"{nama} (Rp {harga:,})",
                min_value=0,
                max_value=10,
                value=initial_value,
                step=1,
                key=key
            )
            
            # Update Variabel pesanan di session_state
            if jumlah > 0:
                st.session_state.pesanan[nama] = jumlah
            elif nama in st.session_state.pesanan:
                # Logika menghapus item jika jumlah 0
                del st.session_state.pesanan[nama]

    st.markdown("---")
    
    # Logika untuk menghitung dan menampilkan subtotal saat ini
    total = hitung_total_pesanan(st.session_state.pesanan)
    st.session_state.total_harga = total # Update Variabel Total
    
    st.metric(label="Total Belanja Saat Ini", value=f"Rp {total:,}")

    if st.button("Lanjut ke Review Pesanan"):
        st.switch_page("pages/review.py")

run()