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
        # "gambar": "assets/images/nasigoreng.jpg"
        "gambar": "https://images.unsplash.com/photo-1680674814945-7945d913319c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bmFzaSUyMGdvcmVuZ3xlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "id": "MU002",
        "nama": "Mie Goreng Seafood",
        "harga": 40000,
        "deskripsi": "Mie goreng dengan udang, cumi, dan sayuran",
        "kategori": "Makanan Utama",
        "tersedia": True,
        # "gambar": "assets/images/miegoreng_seafood.jpg"
        "gambar": "https://images.unsplash.com/photo-1645696329525-8ec3bee460a9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bWllJTIwZ29yZW5nfGVufDB8fDB8fHww"
    },
    {
        "id": "MU003",
        "nama": "Ayam Bakar Madu",
        "harga": 45000,
        "deskripsi": "Ayam bakar dengan saus madu khas rumahan",
        "kategori": "Makanan Utama",
        "tersedia": True,
        # "gambar": "assets/images/ayambakar.jpg"
        "gambar": "https://images.unsplash.com/photo-1645066803665-d16a79a21566?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YXlhbSUyMGJha2FyfGVufDB8fDB8fHww"
    },
    {
        "id": "MU004",
        "nama": "Soto Ayam",
        "harga": 30000,
        "deskripsi": "Soto ayam kuah bening dengan pelengkap lengkap",
        "kategori": "Makanan Utama",
        "tersedia": True,
        # "gambar": "assets/images/soto.jpg"
        "gambar": "https://images.unsplash.com/photo-1677029969063-23ecbb98d0af?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c290byUyMGF5YW18ZW58MHx8MHx8fDA%3D"
    },
    {
        "id": "MU005",
        "nama": "Rendang Daging",
        "harga": 55000,
        "deskripsi": "Rendang daging sapi empuk khas Padang",
        "kategori": "Makanan Utama",
        "tersedia": True,
        # "gambar": "assets/images/rendang.jpg"
        "gambar": "https://images.unsplash.com/photo-1622198678447-47d574f474e6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8cmVuZGFuZ3xlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "id": "MU006",
        "nama": "Gado-Gado",
        "harga": 28000,
        "deskripsi": "Sayuran segar dengan saus kacang spesial",
        "kategori": "Makanan Utama",
        "tersedia": True,
        # "gambar": "assets/images/gado.jpg"
        "gambar": "https://images.unsplash.com/photo-1707269561481-a4a0370a980a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z2FkbyUyMGdhZG98ZW58MHx8MHx8fDA%3D"
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
        # "gambar": "assets/images/pisang.jpg"
        "gambar": "https://th.bing.com/th/id/OIP.MfBZ77OKC6LX44uxdyY8JwHaE7?w=247&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1"
    },
    {
        "id": "MR002",
        "nama": "Tahu Crispy",
        "harga": 12000,
        "deskripsi": "Tahu goreng crispy dengan saus pedas",
        "kategori": "Makanan Ringan",
        "tersedia": True,
        # "gambar": "assets/images/tahu.jpg"
        "gambar": "https://images.unsplash.com/photo-1754636218780-5216f7470f6b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dGFodSUyMGNyaXNweXxlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "id": "MR003",
        "nama": "Kentang Goreng",
        "harga": 18000,
        "deskripsi": "Kentang goreng renyah dengan saus sambal/mayo",
        "kategori": "Makanan Ringan",
        "tersedia": True,
        # "gambar": "assets/images/kentang.jpg"
        "gambar": "https://plus.unsplash.com/premium_photo-1672498329467-b27e2a97d29b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8a2VudGFuZyUyMGdvcmVuZ3xlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "id": "MR004",
        "nama": "Lumpia Sayur",
        "harga": 15000,
        "deskripsi": "Lumpia isi sayuran dengan saus manis",
        "kategori": "Makanan Ringan",
        "tersedia": True,
        # "gambar": "assets/images/lumpia.jpg"
        "gambar": "https://images.unsplash.com/photo-1695712641569-05eee7b37b6d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bHVtcGlhfGVufDB8fDB8fHww"
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
        # "gambar": "assets/images/esteh.jpg"
        "gambar": "data:image/webp;base64,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"
    },
    {
        "id": "MN002",
        "nama": "Es Jeruk",
        "harga": 10000,
        "deskripsi": "Jus jeruk segar dengan es batu",
        "kategori": "Minuman",
        "tersedia": True,
        # "gambar": "assets/images/esjeruk.jpg"
        "gambar": "https://th.bing.com/th/id/OIP.PMoZG9UtA_rlPpsAmVbfuQHaE3?w=227&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1"
    },
    {
        "id": "MN003",
        "nama": "Kopi Susu",
        "harga": 15000,
        "deskripsi": "Kopi robusta dengan susu creamy",
        "kategori": "Minuman",
        "tersedia": True,
        # "gambar": "assets/images/kopi.jpg"
        "gambar": "https://images.unsplash.com/photo-1681366074674-13850edc6d6c?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "id": "MN004",
        "nama": "Jus Alpukat",
        "harga": 18000,
        "deskripsi": "Jus alpukat segar dengan susu kental manis",
        "kategori": "Minuman",
        "tersedia": True,
        # "gambar": "assets/images/alpukat.jpg"
        "gambar": "data:image/webp;base64,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"
    },
    {
        "id": "MN005",
        "nama": "Es Campur",
        "harga": 20000,
        "deskripsi": "Es campur dengan berbagai topping manis",
        "kategori": "Minuman",
        "tersedia": True,
        # "gambar": "assets/images/escampur.jpg"
        "gambar": "data:image/webp;base64,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"
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
        # "gambar": "assets/images/eskrim.jpg"
        "gambar": "https://images.unsplash.com/photo-1501443762994-82bd5dace89a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGljZSUyMGNyZWFtfGVufDB8fDB8fHww"
    },
    {
        "id": "DS002",
        "nama": "Puding Coklat",
        "harga": 12000,
        "deskripsi": "Puding coklat lembut dengan vla vanilla",
        "kategori": "Dessert",
        "tersedia": True,
        # "gambar": "assets/images/puding.jpg"
        "gambar": "https://th.bing.com/th/id/OIP.iLIV-FSd6TsEPG7jzRbiHAHaEK?w=278&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1"
    },
    {
        "id": "DS003",
        "nama": "Pisang Ijo",
        "harga": 18000,
        "deskripsi": "Pisang ijo khas Makassar dengan saus durian",
        "kategori": "Dessert",
        "tersedia": True,
        # "gambar": "assets/images/pisangijo.jpg"
        "gambar": "https://th.bing.com/th/id/OIP.2bgWLp86tyGpOKQDkEg1BQHaFk?w=228&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1"
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


