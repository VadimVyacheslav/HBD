import streamlit as st
from datetime import datetime
import pytz
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Menunggu Harinya Bubbyku...",
    page_icon="💖"
)

# --- LOGIKA PENGECEKAN TANGGAL & WAKTU ---
tz_jakarta = pytz.timezone("Asia/Jakarta")
waktu_sekarang_jakarta = datetime.now(tz_jakarta)
waktu_target_ultah = tz_jakarta.localize(datetime(waktu_sekarang_jakarta.year, 12, 4, 0, 0, 0))

# --- TAMPILAN WEBSITE BERDASARKAN WAKTU ---
if waktu_sekarang_jakarta < waktu_target_ultah:
    
    st.title("Waktu Ultah Bubbyku!")
    st.header("❤️ ULTAH BUBBYY!! ❤️")
    st.markdown("---")

    placeholder = st.empty()

    while True:
        sisa_waktu = waktu_target_ultah - datetime.now(tz_jakarta)

        if sisa_waktu.total_seconds() <= 0:
            placeholder.empty()
            st.balloons()
            st.success("Waktunya Tiba! Halaman akan dimuat ulang...")
            time.sleep(2)
            st.rerun()
            break

        sisa_hari = sisa_waktu.days
        sisa_jam = sisa_waktu.seconds // 3600
        sisa_menit = (sisa_waktu.seconds % 3600) // 60
        sisa_detik = sisa_waktu.seconds % 60

        with placeholder.container():
            col1, col2, col3, col4 = st.columns(4)
            
            col1.metric("Hari", f"{sisa_hari}")
            col2.metric("Jam", f"{sisa_jam}")
            col3.metric("Menit", f"{sisa_menit}")
            col4.metric("Detik", f"{sisa_detik}")

            # --- DITAMBAHKAN DI SINI ---
            st.markdown("---")
            st.info("Ada Surprais loh nanti...")

        time.sleep(1)

else:
    # --- HALAMAN PERAYAAN ULANG TAHUN ---
    st.set_page_config(
        page_title="Selamat Ulang Tahun!!!",
        page_icon="🎉"
    )
    st.balloons()
    st.title("🎉 SELAMAT ULANG TAHUN, BUBBYY! 🎉")
    st.header(f"4 Desember {waktu_sekarang_jakarta.year}")
    
    st.markdown("---")
    
    st.image(
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExamlsNDR1cmVzZmxlaDR1ZjhoOGt0OW9xemc1bm02MmtqeHA4ZDF2ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W1hd3uXRIbddu/giphy.gif",
        caption="KITTHHH!!!"
    )
    
    st.markdown("---")
    
    st.success(
        """
        **Untuk Bubbyku yangg selalu sayangg,**

        Selamat Ulang Tahun! Semoga Kamu bisa dapet apa yang kamu mau,
        Contohnya kayak kuromi trus kentang trus seblak trus wow spageti.
        
        Terima kasih udah nemenin aku ya selama iniii
        
        LOFYUUUUUU! ❤️
        """
    )