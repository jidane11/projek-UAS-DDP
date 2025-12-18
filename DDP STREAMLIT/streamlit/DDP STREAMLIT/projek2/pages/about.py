# pages/about.py
import streamlit as st
from data_model import RESTORAN_NAMA

def run():
    st.title(f"ℹ️ Tentang {RESTORAN_NAMA}")
    st.markdown("Restoran 4 Sekawan didirikan oleh 4 anggota tim yang bersemangat untuk menyajikan pengalaman kuliner terbaik.")
    
    st.subheader("Tim Kami:")
    st.markdown("* **Anggota 1:** Ahli Struktur dan Desain Antarmuka")
    st.markdown("* **Anggota 2:** Penjaga Data dan Kreator Konten")
    st.markdown("* **Anggota 3:** Master Logika dan Fungsi Pemesanan")
    st.markdown("* **Anggota 4:** Validator Pesanan dan Manajer Tinjauan")
    
    st.info("Alamat: Jl. Kode Program No. 4, Kota Streamlit")

run()