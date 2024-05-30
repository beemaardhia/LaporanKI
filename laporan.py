import streamlit as st
from PIL import Image

st.markdown(
    """
    <style>
    .watermark {
        position: fixed;
        bottom: 10px;
        left: 10px;
        opacity: 0.5;
        z-index: 99;
        font-size: 24px; /* Ukuran font watermark */
        font-family: 'Times New Roman', serif;
        color: #808080; /* Warna abu-abu */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="watermark">bimaardhiavardhan</p>', unsafe_allow_html=True)


# --- JUDUL ---
st.title("Kunjungan Industri SMKN 1 Surabaya")

st.image("banner.jpg")

# --- DESKRIPSI UMUM ---
st.write("""
Kunjungan industri merupakan bagian penting dari pembelajaran di SMKN 1 Surabaya. 
Kegiatan ini memberikan kesempatan bagi siswa untuk:

*   **Melihat secara langsung:** Proses produksi, teknologi, dan lingkungan kerja di industri.
*   **Belajar dari praktisi:** Mendapatkan wawasan dari para ahli dan praktisi di bidang masing-masing.
*   **Membangun jaringan:** Menjalin hubungan dengan perusahaan dan profesional di industri.
*   **Menemukan inspirasi:** Memperoleh gambaran nyata tentang karier masa depan.
""")



# --- NAVBAR ---
page = st.selectbox("Pilih Hari:", ["Day 1", "Day 2", "Day 3"])

# --- KONTEN DINAMIS BERDASARKAN PILIHAN NAVBAR ---

if page == "Day 1":
    st.subheader("Day 1")

    st.header("1. AMIKOM Yogyakarta")
    st.image(Image.open("amikom1.jpg"), use_column_width=True)
    st.write("Universitas AMIKOM Yogyakarta adalah sebuah perguruan tinggi swasta yang terletak di Yogyakarta. Universitas ini dikenal dengan program studi di bidang teknologi informasi dan komputer.")
  # Menyesuaikan lebar foto dengan kolom

    # Foto-foto Kecil
    st.subheader("Pemateri")
    col1, col2, col3 = st.columns(3)  # Membuat 3 kolom
    with col1:
        st.image(Image.open("amikomlab3.jpg") , caption="Sambutan SMKN 1")
    with col2:
        st.image(Image.open("Amikomlab1.jpg"), caption="Materi Amikom")
    with col3:
        st.image(Image.open("amikomlab2.jpg"), caption="Materi RPL")

elif page == "Day 2":
    st.subheader("Day 2")

    st.header("1. Kaos Gareng")
    st.image(Image.open("gareng.jpg"), use_column_width=True)
    st.write("""
    Kaos Gareng adalah merek kaos lokal Yogyakarta yang terkenal dengan desain-desain unik, kreatif, dan nyentrik. 
    Menggunakan bahan berkualitas tinggi dan teknik sablon yang baik, Kaos Gareng menjadi pilihan populer 
    bagi mereka yang mencari gaya kasual yang berbeda.
    """)
    # Tambahkan foto-foto Kaos Gareng di sini
    col1, col2 = st.columns(2)  # Membuat 3 kolom
    with col1:
        st.image(Image.open("gareng1.jpeg"))
    with col2:
        st.image(Image.open("gareng2.jpeg"))

    st.header("2. Studio Alam Gamplong")
    st.image(Image.open("gamplong.jpg"), use_column_width=True)

    st.write("""
    Studio Alam Gamplong adalah studio film terbuka yang terletak di Sleman, Yogyakarta. 
    Terkenal sebagai lokasi syuting film-film kolosal seperti Bumi Manusia dan Sultan Agung, 
    studio ini menawarkan replika bangunan-bangunan bersejarah yang megah dan suasana pedesaan yang asri.
    """)
    # Tambahkan foto-foto Studio Gamplong di sini

    st.header("3. Jeep Lava Tour Merapi")
    st.image(Image.open("lava.jpg"), use_column_width=True)
    st.write("""
    Jeep Lava Tour Merapi adalah salah satu aktivitas wisata petualangan yang paling populer di Yogyakarta. 
    Menggunakan jeep terbuka, pengunjung diajak menjelajahi medan offroad di sekitar Gunung Merapi, 
    menyaksikan sisa-sisa erupsi, dan menikmati pemandangan alam yang menakjubkan.
    """)
    col1, col2, col3 = st.columns(3)  # Membuat 3 kolom
    with col1:
        st.image(Image.open("jeep.jpg") )
    with col2:
        st.image(Image.open("Bunker.jpg"))
    with col3:
        st.image(Image.open("Jeep2.jpg"))
    # Tambahkan foto-foto Jeep Lava Tour di sini

    st.header("4. Gala Dinner di Aji Saka Resto")
    st.image(Image.open("ajisaka.jpg"), use_column_width=True)
    st.write("""
    Ajisaka Resto dan Oleh-Oleh Yogyakarta adalah dua toko yang sangat populer di Yogyakarta, terkenal dengan kuliner dan oleh-olehnya yang berkualitas. Dengan adanya produk IKM Magetan yang dipasarkan di kedua tempat tersebut, diharapkan dapat memberikan variasi dan pilihan baru bagi pengunjung.
    """)
    # Tambahkan foto-foto Gala Dinner di Aji Saka Resto di sini

elif page == "Day 3":
    st.subheader("Day 3")

    st.header("1. Bakpia Pathok 25")
    st.image(Image.open("bakpia.jpg"), use_column_width=True)
    st.write("""
    Bakpia Pathok 25 adalah salah satu produsen bakpia paling terkenal di Yogyakarta. 
    Terletak di kawasan Pathuk, toko ini menawarkan berbagai varian rasa bakpia, 
    mulai dari yang klasik seperti kacang hijau hingga yang inovatif seperti keju dan coklat. 
    Kunjungan ke Bakpia Pathok 25 memberikan kesempatan untuk melihat proses pembuatan bakpia secara langsung 
    dan tentu saja, mencicipi kelezatannya!
    """)
    # Tambahkan foto-foto Bakpia Pathok 25 di sini

    st.header("2. Rumah Kreatif Sleman & Dekranasda")
    st.image(Image.open("sleman.jpg"), use_column_width=True)
    st.write("""
    Rumah Kreatif Sleman adalah pusat pengembangan kreativitas dan inovasi di Kabupaten Sleman. 
    Di sini, pengunjung dapat melihat berbagai produk kerajinan dan karya seni dari para perajin lokal. 
    Dekranasda (Dewan Kerajinan Nasional Daerah) Sleman juga berperan penting dalam membina dan mempromosikan 
    kerajinan khas Sleman, menjadikannya tempat yang tepat untuk belajar tentang kekayaan budaya lokal.
    """)
    # Tambahkan foto-foto Rumah Kreatif Sleman & Dekranasda di sini

    st.header("3. Berijalan Yogyakarta")
    st.image(Image.open("berijalan.jpg"), use_column_width=True)
    st.write("""
    Berijalan adalah perusahaan teknologi yang berfokus pada penyediaan solusi bisnis berbasis digital. 
    Melalui layanan Operations Center, Telephony Center, dan Techno Center, Berijalan membantu perusahaan 
    dalam mengelola operasional, komunikasi, dan teknologi informasi mereka. 
    Kunjungan ke Berijalan memberikan wawasan tentang bagaimana teknologi dapat diterapkan 
    untuk meningkatkan efisiensi dan efektivitas bisnis.
    """)
    # Tambahkan foto-foto Berijalan Yogyakarta di sini
