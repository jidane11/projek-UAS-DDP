# ============================================================
# MODUL DATA MENU - menu_data.py
# Tugas Kelompok: Aplikasi Pemesanan Restoran
# Anggota: 4 Orang
# ============================================================
# Modul ini berisi VARIABEL untuk menyimpan data menu restoran
# ============================================================

# VARIABEL: Informasi Restoran
NAMA_RESTORAN = "Warung Nusantara"
ALAMAT_RESTORAN = "Jl. Merdeka No. 123, Jakarta Pusat"
TELEPON_RESTORAN = "(021) 1234-5678"
JAM_BUKA = "10:00 - 22:00"
DESKRIPSI_RESTORAN = """
Warung Nusantara menyajikan berbagai masakan khas Indonesia 
dengan cita rasa autentik dan bahan-bahan berkualitas tinggi.
Nikmati pengalaman kuliner terbaik bersama keluarga tercinta.
"""

# VARIABEL: Kategori Menu
KATEGORI_MENU = ["Makanan Utama", "Makanan Ringan", "Minuman", "Dessert"]

# VARIABEL: Data Menu Makanan Utama (List of Dictionary)
menu_makanan_utama = [
    {
        "id": "MU001",
        "nama": "Nasi Goreng Spesial",
        "harga": 35000,
        "deskripsi": "Nasi goreng dengan telur, ayam, dan sayuran segar",
        "kategori": "Makanan Utama",
        "tersedia": True,
        "gambar": "assets/images/nasigoreng.jpg"
    },
    {
        "id": "MU002",
        "nama": "Mie Goreng Seafood",
        "harga": 40000,
        "deskripsi": "Mie goreng dengan udang, cumi, dan sayuran",
        "kategori": "Makanan Utama",
        "tersedia": True,
        "gambar": "assets/images/miegoreng_seafood.jpg"
    },
    {
        "id": "MU003",
        "nama": "Ayam Bakar Madu",
        "harga": 45000,
        "deskripsi": "Ayam bakar dengan saus madu khas rumahan",
        "kategori": "Makanan Utama",
        "tersedia": True,
        "gambar": "assets/images/ayambakar.jpg"
    },
    {
        "id": "MU004",
        "nama": "Soto Ayam",
        "harga": 30000,
        "deskripsi": "Soto ayam kuah bening dengan pelengkap lengkap",
        "kategori": "Makanan Utama",
        "tersedia": True,
        "gambar": "assets/images/soto.jpg"
    },
    {
        "id": "MU005",
        "nama": "Rendang Daging",
        "harga": 55000,
        "deskripsi": "Rendang daging sapi empuk khas Padang",
        "kategori": "Makanan Utama",
        "tersedia": True,
        "gambar": "assets/images/rendang.jpg"
    },
    {
        "id": "MU006",
        "nama": "Gado-Gado",
        "harga": 28000,
        "deskripsi": "Sayuran segar dengan saus kacang spesial",
        "kategori": "Makanan Utama",
        "tersedia": True,
        "gambar": "assets/images/gado.jpg"
    }
]

# VARIABEL: Data Menu Makanan Ringan (List of Dictionary)
menu_makanan_ringan = [
    {
        "id": "MR001",
        "nama": "Pisang Goreng",
        "harga": 15000,
        "deskripsi": "Pisang goreng renyah dengan topping keju/coklat",
        "kategori": "Makanan Ringan",
        "tersedia": True,
        "gambar": "assets/images/pisang.jpg"
    },
    {
        "id": "MR002",
        "nama": "Tahu Crispy",
        "harga": 12000,
        "deskripsi": "Tahu goreng crispy dengan saus pedas",
        "kategori": "Makanan Ringan",
        "tersedia": True,
        "gambar": "assets/images/tahu.jpg"
    },
    {
        "id": "MR003",
        "nama": "Kentang Goreng",
        "harga": 18000,
        "deskripsi": "Kentang goreng renyah dengan saus sambal/mayo",
        "kategori": "Makanan Ringan",
        "tersedia": True,
        "gambar": "assets/images/kentang.jpg"
    },
    {
        "id": "MR004",
        "nama": "Lumpia Sayur",
        "harga": 15000,
        "deskripsi": "Lumpia isi sayuran dengan saus manis",
        "kategori": "Makanan Ringan",
        "tersedia": True,
        "gambar": "assets/images/lumpia.jpg"
    }
]

# VARIABEL: Data Menu Minuman (List of Dictionary)
menu_minuman = [
    {
        "id": "MN001",
        "nama": "Es Teh Manis",
        "harga": 8000,
        "deskripsi": "Teh manis segar dengan es batu",
        "kategori": "Minuman",
        "tersedia": True,
        "gambar": "assets/images/esteh.jpg"
    },
    {
        "id": "MN002",
        "nama": "Es Jeruk",
        "harga": 10000,
        "deskripsi": "Jus jeruk segar dengan es batu",
        "kategori": "Minuman",
        "tersedia": True,
        "gambar": "assets/images/esjeruk.jpg"
    },
    {
        "id": "MN003",
        "nama": "Kopi Susu",
        "harga": 15000,
        "deskripsi": "Kopi robusta dengan susu creamy",
        "kategori": "Minuman",
        "tersedia": True,
        "gambar": "assets/images/kopi.jpg"
    },
    {
        "id": "MN004",
        "nama": "Jus Alpukat",
        "harga": 18000,
        "deskripsi": "Jus alpukat segar dengan susu kental manis",
        "kategori": "Minuman",
        "tersedia": True,
        "gambar": "assets/images/alpukat.jpg"
    },
    {
        "id": "MN005",
        "nama": "Es Campur",
        "harga": 20000,
        "deskripsi": "Es campur dengan berbagai topping manis",
        "kategori": "Minuman",
        "tersedia": True,
        "gambar": "assets/images/escampur.jpg"
    }
]

# VARIABEL: Data Menu Dessert (List of Dictionary)
menu_dessert = [
    {
        "id": "DS001",
        "nama": "Es Krim",
        "harga": 15000,
        "deskripsi": "Es krim vanilla/coklat/strawberry",
        "kategori": "Dessert",
        "tersedia": True,
        "gambar": "assets/images/eskrim.jpg"
    },
    {
        "id": "DS002",
        "nama": "Puding Coklat",
        "harga": 12000,
        "deskripsi": "Puding coklat lembut dengan vla vanilla",
        "kategori": "Dessert",
        "tersedia": True,
        "gambar": "assets/images/puding.jpg"
    },
    {
        "id": "DS003",
        "nama": "Pisang Ijo",
        "harga": 18000,
        "deskripsi": "Pisang ijo khas Makassar dengan saus durian",
        "kategori": "Dessert",
        "tersedia": True,
        "gambar": "assets/images/pisangijo.jpg"
    }
]

# VARIABEL: Persentase Diskon
DISKON_MEMBER = 10  # Diskon 10% untuk member
DISKON_PROMO = 15   # Diskon 15% untuk promo tertentu
PAJAK = 10          # Pajak 10%

# VARIABEL: Status Pesanan
STATUS_PESANAN = ["Menunggu", "Diproses", "Siap", "Selesai", "Dibatalkan"]


# ============================================================
# FUNCTION: Mengambil semua menu dalam satu list
# ============================================================
def get_semua_menu():
    """
    Menggabungkan semua menu menjadi satu list
    Menggunakan LOOPING untuk iterasi
    """
    semua_menu = []
    
    # LOOPING: Menambahkan setiap item dari berbagai kategori
    for item in menu_makanan_utama:
        semua_menu.append(item)
    
    for item in menu_makanan_ringan:
        semua_menu.append(item)
    
    for item in menu_minuman:
        semua_menu.append(item)
    
    for item in menu_dessert:
        semua_menu.append(item)
    
    return semua_menu


# FUNCTION: Mengambil menu berdasarkan kategori
def get_menu_by_kategori(kategori):
    """
    Mengambil menu berdasarkan kategori tertentu
    Menggunakan LOGIKA kondisional
    """
    # LOGIKA: Pengecekan kategori
    if kategori == "Makanan Utama":
        return menu_makanan_utama
    elif kategori == "Makanan Ringan":
        return menu_makanan_ringan
    elif kategori == "Minuman":
        return menu_minuman
    elif kategori == "Dessert":
        return menu_dessert
    else:
        return []


# FUNCTION: Mencari menu berdasarkan ID
def get_menu_by_id(menu_id):
    """
    Mencari menu berdasarkan ID
    Menggunakan LOOPING dan LOGIKA
    """
    semua_menu = get_semua_menu()
    
    # LOOPING: Iterasi semua menu
    for menu in semua_menu:
        # LOGIKA: Pengecekan ID
        if menu["id"] == menu_id:
            return menu
    
    return None


# FUNCTION: Mencari menu berdasarkan nama
def cari_menu(keyword):
    """
    Mencari menu berdasarkan keyword nama
    Menggunakan LOOPING dan LOGIKA
    """
    semua_menu = get_semua_menu()
    hasil = []
    
    # LOOPING: Iterasi semua menu
    for menu in semua_menu:
        # LOGIKA: Pengecekan apakah keyword ada di nama menu
        if keyword.lower() in menu["nama"].lower():
            hasil.append(menu)
    
    return hasil


