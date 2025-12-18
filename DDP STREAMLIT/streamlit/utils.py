# ============================================================
# MODUL UTILITAS - utils.py
# Tugas Kelompok: Aplikasi Pemesanan Restoran
# Anggota: 4 Orang
# ============================================================
# Modul ini berisi FUNCTION helper untuk berbagai operasi
# ============================================================

from datetime import datetime
import menu_data

# ============================================================
# FUNCTION: Format Mata Uang Rupiah
# ============================================================
def format_rupiah(angka):
    """
    Mengubah angka menjadi format Rupiah
    Contoh: 50000 -> Rp 50.000
    """
    return f"Rp {angka:,.0f}".replace(",", ".")


# ============================================================
# FUNCTION: Hitung Total Harga Item
# ============================================================
def hitung_total_item(harga, jumlah):
    """
    Menghitung total harga untuk satu item
    Menggunakan operasi matematika sederhana
    """
    total = harga * jumlah
    return total


# ============================================================
# FUNCTION: Hitung Subtotal Pesanan
# ============================================================
def hitung_subtotal(daftar_pesanan):
    """
    Menghitung subtotal dari semua item pesanan
    Menggunakan LOOPING untuk iterasi
    """
    subtotal = 0
    
    # LOOPING: Iterasi setiap item pesanan
    for item in daftar_pesanan:
        subtotal = subtotal + (item["harga"] * item["jumlah"])
    
    return subtotal


# ============================================================
# FUNCTION: Hitung Diskon
# ============================================================
def hitung_diskon(subtotal, persen_diskon):
    """
    Menghitung nilai diskon berdasarkan persentase
    Menggunakan LOGIKA untuk validasi
    """
    # LOGIKA: Validasi persentase diskon
    if persen_diskon < 0:
        persen_diskon = 0
    elif persen_diskon > 100:
        persen_diskon = 100
    
    diskon = subtotal * (persen_diskon / 100)
    return diskon


# ============================================================
# FUNCTION: Hitung Pajak
# ============================================================
def hitung_pajak(subtotal_setelah_diskon):
    """
    Menghitung pajak berdasarkan persentase tetap
    """
    pajak = subtotal_setelah_diskon * (menu_data.PAJAK / 100)
    return pajak


# ============================================================
# FUNCTION: Hitung Total Akhir
# ============================================================
def hitung_total_akhir(subtotal, diskon, pajak):
    """
    Menghitung total akhir setelah diskon dan pajak
    """
    total_akhir = subtotal - diskon + pajak
    return total_akhir


# ============================================================
# FUNCTION: Validasi Jumlah Pesanan
# ============================================================
def validasi_jumlah(jumlah):
    """
    Memvalidasi jumlah pesanan
    Menggunakan LOGIKA kondisional
    """
    # LOGIKA: Pengecekan kondisi
    if jumlah <= 0:
        return False, "Jumlah pesanan harus lebih dari 0"
    elif jumlah > 99:
        return False, "Jumlah pesanan maksimal 99"
    else:
        return True, "Jumlah valid"


# ============================================================
# FUNCTION: Validasi Nama Pelanggan
# ============================================================
def validasi_nama(nama):
    """
    Memvalidasi nama pelanggan
    Menggunakan LOGIKA kondisional
    """
    # LOGIKA: Pengecekan kondisi
    if nama == "" or nama is None:
        return False, "Nama tidak boleh kosong"
    elif len(nama) < 2:
        return False, "Nama minimal 2 karakter"
    elif len(nama) > 50:
        return False, "Nama maksimal 50 karakter"
    else:
        return True, "Nama valid"


# ============================================================
# FUNCTION: Validasi Nomor Meja
# ============================================================
def validasi_meja(nomor_meja):
    """
    Memvalidasi nomor meja
    Menggunakan LOGIKA kondisional
    """
    # LOGIKA: Pengecekan kondisi
    if nomor_meja < 1:
        return False, "Nomor meja tidak valid"
    elif nomor_meja > 20:
        return False, "Nomor meja maksimal 20"
    else:
        return True, "Nomor meja valid"


# ============================================================
# FUNCTION: Generate ID Pesanan
# ============================================================
def generate_id_pesanan():
    """
    Membuat ID pesanan unik berdasarkan waktu
    """
    waktu = datetime.now()
    id_pesanan = waktu.strftime("ORD%Y%m%d%H%M%S")
    return id_pesanan


# ============================================================
# FUNCTION: Format Waktu Pesanan
# ============================================================
def format_waktu(waktu=None):
    """
    Format waktu menjadi string yang mudah dibaca
    """
    if waktu is None:
        waktu = datetime.now()
    
    return waktu.strftime("%d %B %Y, %H:%M:%S")


# ============================================================
# FUNCTION: Format Waktu Singkat
# ============================================================
def format_waktu_singkat(waktu=None):
    """
    Format waktu menjadi string singkat
    """
    if waktu is None:
        waktu = datetime.now()
    
    return waktu.strftime("%d/%m/%Y %H:%M")


# ============================================================
# FUNCTION: Buat Ringkasan Pesanan
# ============================================================
def buat_ringkasan_pesanan(pesanan):
    """
    Membuat ringkasan pesanan dalam format teks
    Menggunakan LOOPING dan STRING formatting
    """
    ringkasan = []
    ringkasan.append(f"ID Pesanan: {pesanan['id_pesanan']}")
    ringkasan.append(f"Nama: {pesanan['nama_pelanggan']}")
    ringkasan.append(f"Meja: {pesanan['nomor_meja']}")
    ringkasan.append("-" * 30)
    ringkasan.append("Daftar Pesanan:")
    
    # LOOPING: Iterasi setiap item
    for item in pesanan['items']:
        ringkasan.append(f"  - {item['nama']} x{item['jumlah']} = {format_rupiah(item['harga'] * item['jumlah'])}")
    
    ringkasan.append("-" * 30)
    ringkasan.append(f"Subtotal: {format_rupiah(pesanan['subtotal'])}")
    
    # LOGIKA: Tampilkan diskon jika ada
    if pesanan['diskon'] > 0:
        ringkasan.append(f"Diskon: -{format_rupiah(pesanan['diskon'])}")
    
    ringkasan.append(f"Pajak (10%): {format_rupiah(pesanan['pajak'])}")
    ringkasan.append(f"TOTAL: {format_rupiah(pesanan['total'])}")
    
    return "\n".join(ringkasan)


# ============================================================
# FUNCTION: Hitung Jumlah Item di Keranjang
# ============================================================
def hitung_jumlah_keranjang(keranjang):
    """
    Menghitung total jumlah item di keranjang
    Menggunakan LOOPING
    """
    total = 0
    
    # LOOPING: Iterasi setiap item
    for item in keranjang:
        total = total + item["jumlah"]
    
    return total


# ============================================================
# FUNCTION: Cek Apakah Item Ada di Keranjang
# ============================================================
def cek_item_keranjang(keranjang, menu_id):
    """
    Mengecek apakah item sudah ada di keranjang
    Menggunakan LOOPING dan LOGIKA
    """
    # LOOPING: Iterasi keranjang
    for i, item in enumerate(keranjang):
        # LOGIKA: Pengecekan ID
        if item["id"] == menu_id:
            return True, i
    
    return False, -1


# ============================================================
# FUNCTION: Update Jumlah Item di Keranjang
# ============================================================
def update_item_keranjang(keranjang, menu_id, jumlah_baru):
    """
    Update jumlah item di keranjang
    Menggunakan LOOPING dan LOGIKA
    """
    # LOOPING: Iterasi keranjang
    for i, item in enumerate(keranjang):
        # LOGIKA: Pengecekan ID
        if item["id"] == menu_id:
            # LOGIKA: Hapus jika jumlah 0 atau kurang
            if jumlah_baru <= 0:
                keranjang.pop(i)
            else:
                keranjang[i]["jumlah"] = jumlah_baru
            return keranjang
    
    return keranjang


# ============================================================
# FUNCTION: Hapus Item dari Keranjang
# ============================================================
def hapus_item_keranjang(keranjang, menu_id):
    """
    Menghapus item dari keranjang
    Menggunakan LOOPING dan LOGIKA
    """
    keranjang_baru = []
    
    # LOOPING: Filter item yang tidak dihapus
    for item in keranjang:
        # LOGIKA: Pengecekan ID
        if item["id"] != menu_id:
            keranjang_baru.append(item)
    
    return keranjang_baru


# ============================================================
# FUNCTION: Kosongkan Keranjang
# ============================================================
def kosongkan_keranjang():
    """
    Mengembalikan keranjang kosong
    """
    return []


# ============================================================
# FUNCTION: Hitung Statistik Pesanan
# ============================================================
def hitung_statistik_pesanan(daftar_pesanan):
    """
    Menghitung statistik dari daftar pesanan
    Menggunakan LOOPING dan LOGIKA
    """
    total_pesanan = len(daftar_pesanan)
    total_pendapatan = 0
    pesanan_selesai = 0
    pesanan_dibatalkan = 0
    
    # LOOPING: Iterasi semua pesanan
    for pesanan in daftar_pesanan:
        total_pendapatan = total_pendapatan + pesanan["total"]
        
        # LOGIKA: Hitung berdasarkan status
        if pesanan["status"] == "Selesai":
            pesanan_selesai = pesanan_selesai + 1
        elif pesanan["status"] == "Dibatalkan":
            pesanan_dibatalkan = pesanan_dibatalkan + 1
    
    return {
        "total_pesanan": total_pesanan,
        "total_pendapatan": total_pendapatan,
        "pesanan_selesai": pesanan_selesai,
        "pesanan_dibatalkan": pesanan_dibatalkan
    }
