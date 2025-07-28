import streamlit as st
from datetime import date

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Menunggu Hari Spesial...",
    page_icon="💖"
)

# --- LOGIKA PENGECEKAN TANGGAL ---

# Dapatkan tanggal hari ini (tanpa informasi waktu)
hari_ini = date.today()

# Tentukan tanggal ulang tahun di tahun ini
# Menggunakan hari_ini.year agar dinamis setiap tahun
tanggal_ultah = date(hari_ini.year, 12, 4)


# --- TAMPILAN WEBSITE BERDASARKAN TANGGAL ---

# KONDISI 1: JIKA HARI INI SEBELUM TANGGAL ULANG TAHUN
if hari_ini < tanggal_ultah:
    
    # --- HALAMAN HITUNG MUNDUR ---
    
    st.title("Menghitung Hari...")
    st.header("❤️ MENUJU ULTAH BUBBYY!!! ❤️")
    
    # Hitung sisa hari
    sisa_waktu = tanggal_ultah - hari_ini
    sisa_hari = sisa_waktu.days
    
    st.markdown("---")
    
    # Gunakan kolom untuk membuat tampilan metric lebih rapi di tengah
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.metric(label="Sisa Hari Lagi", value=f"⏳ {sisa_hari} Hari")
    
    st.markdown("---")
    st.info("Ada Surprais loh nanti...")


# KONDISI 2: JIKA HARI INI ADALAH HARI H ATAU SESUDAHNYA
else:
    
    # --- HALAMAN PERAYAAN ULANG TAHUN ---
    
    # Ganti judul halaman dan ikonnya
    st.set_page_config(
        page_title="Selamat Ulang Tahun!!!",
        page_icon="🎉"
    )
    
    # Tampilkan efek balon!
    st.balloons()
    
    # Judul Perayaan
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