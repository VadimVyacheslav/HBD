import streamlit as st
from datetime import datetime
import pytz # Import library pytz

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Menunggu Hari Spesial...",
    page_icon="💖"
)

# --- LOGIKA PENGECEKAN TANGGAL (VERSI AKURAT DENGAN TIMEZONE) ---

# 1. Tentukan zona waktu Jakarta
tz_jakarta = pytz.timezone("Asia/Jakarta")

# 2. Ambil waktu saat ini dan konversikan ke zona waktu Jakarta
hari_ini_jakarta = datetime.now(tz_jakarta)

# 3. Ambil hanya tanggalnya saja
hari_ini = hari_ini_jakarta.date()

# 4. Tentukan tanggal ulang tahun di tahun ini
tanggal_ultah = datetime(hari_ini.year, 12, 4).date()


# --- TAMPILAN WEBSITE BERDASARKAN TANGGAL ---

# KONDISI 1: JIKA HARI INI SEBELUM TANGGAL ULANG TAHUN
if hari_ini < tanggal_ultah:
    
    st.title("Menghitung Hari...")
    st.header("❤️ MENUJU ULTAH BUBBYY!! ❤️") # Menggunakan header dari screenshot Anda
    
    # Hitung sisa hari
    sisa_waktu = tanggal_ultah - hari_ini
    sisa_hari = sisa_waktu.days
    
    st.markdown("---")
    
    # Tampilan metric countdown
    st.metric(label="Sisa Hari Lagi", value=f"⏳ {sisa_hari} Hari")
    
    st.markdown("---")
    st.info("Ada Surprais loh nanti...") # Menggunakan teks dari screenshot Anda


# KONDISI 2: JIKA HARI INI ADALAH HARI H ATAU SESUDAHNYA
else:
    # Ganti judul halaman dan ikonnya
    st.set_page_config(
        page_title="Selamat Ulang Tahun!!!",
        page_icon="🎉"
    )
    st.balloons()
    st.title("🎉 SELAMAT ULANG TAHUN, BUBBYY! 🎉")
    st.header(f"4 Desember {hari_ini.year}")

    st.markdown("---")

    # Tampilkan gambar/GIF yang meriah
    st.image(
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExamlsNDR1cmVzZmxlaDR1ZjhoOGt0OW9xemc1bm02MmtqeHA4ZDF2ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W1hd3uXRIbddu/giphy.gif",
        caption="KITTHHH!!!"
    )

    st.markdown("---")

    # Pesan personal
    st.success(
        """
        **Untuk Bubbyku yangg selalu sayangg,**

        Selamat Ulang Tahun! Semoga Kamu bisa dapet apa yang kamu mau,
        Contohnya kayak kuromi trus kentang trus seblak trus wow spageti.

        Terima kasih udah nemenin aku ya selama iniii

        LOFYUUUUUU! ❤️
        """
    )