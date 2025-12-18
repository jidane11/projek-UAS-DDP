# # import streamlit as st

# # st.title("Aplikasi Streamlit Pertama")
# # st.write("Selamat datang di Streamlit")
# # st.write("made in FTSL")

# # with st.form("form_data_diri"):
# #     nama = st.text_input("Masukkan Nama Anda")
# #     alamat = st.text_area("Masukkan Alamat Anda")
# #     umur = st.number_input("Masukkan Umur Anda", min_value=0, max_value=120, step=1)
# #     submit_button = st.form_submit_button("submit")

# #     if submit_button:
# #         st.success(f"Terimakasih {nama} telah mengisi data diri ")
# #         st.write(f"Nama : {nama}")
# #         st.write(f"Alamat : {alamat}")
# #         st.write(f"Usia : {umur}")


# # app.py

# import streamlit as st
# from data_menu import MENU_RESTORAN, DAFTAR_HARGA # <-- Modul (Anggota 2)

# # --- Function (Anggota 3) ---

# # app.py (Pastikan di awal file, di bagian Variabel/Session State - Anggota 2)

# if 'keranjang' not in st.session_state:
#     st.session_state.keranjang = {} 

# # Inisialisasi variabel transaksi_terakhir
# if 'transaksi_terakhir' not in st.session_state:
#     st.session_state.transaksi_terakhir = None 

# # Inisialisasi flag checkout_sukses
# if 'checkout_sukses' not in st.session_state:
#     st.session_state.checkout_sukses = False
    
# def hitung_subtotal(keranjang):
#     """Fungsi untuk menghitung total biaya dari keranjang."""
#     total = 0
#     # Looping (Anggota 4) untuk menjumlahkan harga semua item di keranjang
#     for item_nama, detail in keranjang.items():
#         total += detail['harga'] * detail['jumlah']
#     return total

# # app.py (di bagian atas, bersama fungsi-fungsi lainnya)
# # app.py (Perbarui fungsi konfirmasi_pembayaran)

# def konfirmasi_pembayaran(nama_pembeli, no_hp, alamat):
#     """Fungsi untuk menyelesaikan transaksi, mereset keranjang, dan menyimpan detail pelanggan."""
    
#     # 1. Simpan detail transaksi ke session state (sebelum di-reset)
#     st.session_state.transaksi_terakhir = {
#         'keranjang': st.session_state.keranjang.copy(),
#         'pelanggan': {
#             'nama': nama_pembeli,
#             'hp': no_hp,
#             'alamat': alamat
#         }
#     }
    
#     # 2. Reset variabel keranjang (Variabel - Anggota 2)
#     st.session_state.keranjang = {} 
    
#     # 3. Set flag sukses
#     st.session_state.checkout_sukses = True

# def terapkan_diskon(total):
#     """Fungsi Logika (Anggota 4) untuk memberikan diskon."""
#     # Logika (Anggota 4): Jika total melebihi Rp 100.000, dapat diskon 10%
#     if total >= 100000:
#         diskon = total * 0.10
#         total_akhir = total - diskon
#         return total_akhir, diskon
#     return total, 0

# def tambah_ke_keranjang(nama_item, harga, jumlah):
#     """Fungsi (Anggota 3) untuk menambah item ke session_state keranjang."""
#     # Logika (Anggota 1) untuk memastikan input valid
#     if jumlah > 0:
#         if nama_item in st.session_state.keranjang:
#             st.session_state.keranjang[nama_item]['jumlah'] += jumlah
#         else:
#             st.session_state.keranjang[nama_item] = {
#                 'harga': harga,
#                 'jumlah': jumlah
#             }
#         st.success(f"'{nama_item}' ({jumlah} porsi) ditambahkan ke keranjang!")
#     else:
#         st.warning("Jumlah pemesanan harus lebih dari 0.")

# # --- Variabel/Session State (Anggota 2) ---
# if 'keranjang' not in st.session_state:
#     # Variabel utama untuk menyimpan keranjang pemesanan
#     st.session_state.keranjang = {} 


# # --- Pages (Anggota 1) ---

# st.set_page_config(
#     page_title="Aplikasi Pemesanan Restoran",
#     layout="wide"
# )

# st.title("🍽️ Aplikasi Pemesanan Restoran Streamlit")

# # Pilihan navigasi sidebar (Pages - Anggota 1)
# page_select = st.sidebar.radio(
#     "Navigasi",
#     ["Menu Restoran", "Keranjang Anda"]
# )


# def tampilkan_struk_pembelian(data_transaksi):
#     """Fungsi untuk menampilkan struk pembelian yang rapi."""
#     """Fungsi untuk menampilkan struk pembelian yang rapi."""
#     # Pastikan data_transaksi bukan None atau kosong
#     if not data_transaksi:
#         st.error("Data transaksi tidak ditemukan.")
#         return
#     st.subheader("🧾 Struk Pembelian / Pesanan")
    
    
#     # Ambil data
#     keranjang = data_transaksi['keranjang']
#     pelanggan = data_transaksi['pelanggan']
    
#     # Hitung total
#     subtotal = hitung_subtotal(keranjang)
#     total_akhir, diskon = terapkan_diskon(subtotal)
    
#     # --- Detail Pelanggan ---
#     st.markdown("---")
#     st.markdown("**Detail Pemesan**")
#     col_p1, col_p2 = st.columns(2)
#     col_p1.write(f"Nama: **{pelanggan['nama']}**")
#     col_p1.write(f"No. HP: **{pelanggan['hp']}**")
#     col_p2.write(f"Alamat: **{pelanggan['alamat']}**")
#     st.markdown("---")
    
#     # --- Detail Pesanan (Looping Anggota 4) ---
#     st.markdown("**Item yang Dipesan**")
#     col_t1, col_t2, col_t3 = st.columns([4, 2, 2])
#     col_t1.write("Item")
#     col_t2.write("Jumlah")
#     col_t3.write("Harga")
    
#     total_item = 0
#     for nama_item, detail in keranjang.items():
#         subtotal_item = detail['harga'] * detail['jumlah']
#         total_item += subtotal_item
        
#         col_i1, col_i2, col_i3 = st.columns([4, 2, 2])
#         col_i1.write(nama_item)
#         col_i2.write(f"x{detail['jumlah']}")
#         col_i3.write(f"Rp {subtotal_item:,.0f}")
        
#     st.markdown("---")
    
#     # --- Detail Total ---
#     st.write(f"Subtotal Pesanan: **Rp {subtotal:,.0f}**")
    
#     if diskon > 0:
#         st.success(f"Diskon (10%): - Rp {diskon:,.0f}")
    
#     st.metric(
#         label="TOTAL YANG HARUS DIBAYAR", 
#         value=f"Rp {total_akhir:,.0f}"
#     )
    
#     st.info("Terima kasih atas pesanan Anda. Pesanan akan segera diantar!")
# # --- Logika Halaman Menu (Anggota 3) ---
# if page_select == "Menu Restoran":
#     st.header("Pilih Menu Makanan & Minuman")

#     # Looping (Anggota 4) untuk menampilkan menu berdasarkan kategori
#     for kategori, items in MENU_RESTORAN.items():
#         st.subheader(f"--- {kategori} ---")
        
#         col1, col2, col3 = st.columns([3, 1, 1])
        
#         col1.write("**Nama Menu**")
#         col2.write("**Harga**")
#         col3.write("**Jumlah**")
#         st.markdown("---")
        
#         for item in items:
#             nama = item['nama']
#             harga = item['harga']
            
#             with st.form(key=f'form_{nama}'):
                
#                 col_item, col_harga, col_input = st.columns([3, 1, 1])
                
#                 # Menampilkan nama dan harga
#                 col_item.write(nama)
#                 col_harga.write(f"Rp {harga:,.0f}")
                
#                 # Input Jumlah
#                 jumlah = col_input.number_input(
#                     'Jumlah',
#                     min_value=0,
#                     value=0,
#                     step=1,
#                     key=f'input_{nama}',
#                     label_visibility="collapsed"
#                 )

#                 # Tombol Submit Form
#                 st.form_submit_button(
#                     label="Tambah", 
#                     on_click=tambah_ke_keranjang, 
#                     args=(nama, harga, jumlah) # Argumen untuk Fungsi (Anggota 3)
#                 )


# # app.py (Perbarui bagian ini sepenuhnya)

# elif page_select == "Keranjang Anda":
#     st.header("🛒 Keranjang Pemesanan Anda")
    
#     # 1. Tampilan Struk Pembelian (jika transaksi baru saja sukses)
#     if st.session_state.get('checkout_sukses', False):
#         st.balloons()
        
#         # Panggil fungsi tampilkan_struk_pembelian
#         tampilkan_struk_pembelian(st.session_state.transaksi_terakhir)
        
#         # Reset flag sukses agar pesan hanya tampil sekali
#         st.session_state.checkout_sukses = False
#         # Jangan tampilkan bagian input/keranjang di bawah jika struk ditampilkan
#         st.stop()
        
#     # 2. Tampilan Keranjang Normal
    
#     keranjang_kosong = not st.session_state.keranjang
    
#     if keranjang_kosong:
#         st.info("Keranjang Anda masih kosong. Silakan pesan dari halaman Menu Restoran.")
#     else:
#         # --- (Bagian Tampilan Detail Item Keranjang SAMA seperti sebelumnya) ---

#         # Header Tabel
#         col_h1, col_h2, col_h3, col_h4 = st.columns([4, 2, 2, 1])
#         col_h1.write("**Item**")
#         col_h2.write("**Jumlah**")
#         col_h3.write("**Subtotal**")
#         col_h4.write("**Hapus**")
#         st.markdown("---")
        
#         subtotal_keranjang = 0
#         for nama_item, detail in st.session_state.keranjang.copy().items():
#             subtotal = detail['harga'] * detail['jumlah']
#             subtotal_keranjang += subtotal
            
#             # Baris Item Keranjang
#             col_i1, col_i2, col_i3, col_i4 = st.columns([4, 2, 2, 1])
#             col_i1.write(nama_item)
#             col_i2.write(f"{detail['jumlah']} porsi")
#             col_i3.write(f"Rp {subtotal:,.0f}")
            
#             # Tombol Hapus Item
#             if col_i4.button("🗑️", key=f'hapus_{nama_item}'):
#                 del st.session_state.keranjang[nama_item]
#                 st.rerun() 

#         st.markdown("---")
        
#         # --- Total Perhitungan ---
#         total_akhir, diskon = terapkan_diskon(subtotal_keranjang)

#         st.subheader("Rincian Pembayaran")
#         st.write(f"Subtotal Pesanan: **Rp {subtotal_keranjang:,.0f}**")
#         if diskon > 0:
#             st.success(f"🎉 Diskon Spesial (10%): - **Rp {diskon:,.0f}**")
#         st.metric(label="TOTAL AKHIR", value=f"Rp {total_akhir:,.0f}")
        
#         st.markdown("---")

#         # --- Input Data Pelanggan dan Konfirmasi Pembayaran ---
#         st.subheader("Data Pelanggan")

#         with st.form("form_data_pelanggan"):
            
#             # Input data pelanggan (Variabel / Logika Anggota 1)
#             nama_pembeli = st.text_input("Nama Pembeli", key="nama_pembeli")
#             no_hp = st.text_input("Nomor HP", key="no_hp")
#             alamat = st.text_area("Alamat Pengiriman (Opsional)", key="alamat_kirim")

#             submitted = st.form_submit_button("💰 Konfirmasi & Bayar", type="primary")

#             if submitted:
#                 # Logika (Anggota 1) untuk validasi
#                 if not nama_pembeli or not no_hp:
#                     st.error("Nama Pembeli dan Nomor HP wajib diisi untuk konfirmasi.")
#                 else:
#                     # Panggil Fungsi (Anggota 3) saat tombol diklik
#                     konfirmasi_pembayaran(nama_pembeli, no_hp, alamat)
#                     st.rerun() # Wajib Rerun untuk menampilkan struk
#         # app.py (Tambahkan fungsi baru ini di bagian atas)

        