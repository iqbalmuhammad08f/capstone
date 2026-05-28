# **Petunjuk**

Anda harus melanjutkan notebook yang sudah ada yakni:

C:\Users\Lenovo LOQ\Documents\coding\dicoding\tes\capstone\notebook.ipynb

1. ## **Kriteria**

Terdapat 4 kriteria utama yang harus Anda penuhi dalam mengerjakan proyek akhir ini.

### **Kriteria 1: Menggunakan Salah Satu dari Dataset yang Telah Disediakan**

Pada proyek ini, Anda harus melakukan proses analisis menggunakan dataset yang telah diberikan yakni 

C:\Users\Lenovo LOQ\Documents\coding\dicoding\tes\capstone\dataset

### **Kriteria 2: Melakukan Seluruh Proses Analisis Data**

Anda harus melakukan seluruh proses analisis data mulai dari mendefinisikan pertanyaan hingga membuat rekomendasi action item dari hasil analisis.

Proyek analisis data yang Anda buat harus memenuhi ketentuan berikut.

**1\. Menentukan Pertanyaan Bisnis**

* Minimal terdapat 2 buah pertanyaan bisnis (pertanyaan analisis) yang ingin dijawab melalui proses analisis data.  
* Pertanyaan tersebut haruslah menerapkan metode SMART Question.  
  * **Spesific (Spesifik)**  
    Pertanyaan Anda harus jelas, fokus pada sebuah topik tertentu, dan tidak bermakna ganda. Hindari pertanyaan yang terlalu luas.  
    * Salah: Bagaimana cara meningkatkan penjualan?  
    * Benar: Faktor apa saja yang memengaruhi penurunan penjualan produk kategori elektronik di wilayah Jakarta selama kuartal terakhir?  
  * **Measurable (Terukur)**  
    Pertanyaan Anda harus bisa dijawab dengan angka atau matrix yang konkret. Anda harus tahu apa yang akan dihitung.  
    * Salah: Apakah pelanggan senang dengan layanan kita?  
    * Benar: Berapa skor rata-rata Customer Satisfaction untuk layanan purna jual bulan ini dibandingkan bulan lalu?  
  * **Action-Oriented (Berorientasi Aksi)**  
    Hasil dari pertanyaan Anda harus bisa memberikan arahan untuk melakukan tindakan nyata. Jika pertanyaan terjawab, stakeholder harus tahu apa langkah selanjutnya.  
    * Salah: Mengapa orang suka berbelanja?  
    * Benar: Fitur apa pada aplikasi yang paling sering digunakan sebelum pengguna memutuskan untuk melakukan checkout?  
  * **Relevant (Relevan)**  
    Hasil dari pertanyaan Anda harus sejalan dengan tujuan utama bisnis atau masalah yang sedang dihadapi.  
    * Salah: Menanyakan tentang stok gudang saat masalah utamanya adalah efektivitas kampanye media sosial.  
    * Benar: Apakah kampanye iklan di Instagram memberikan Return on Ad Spend (ROAS) yang lebih tinggi dibandingkan iklan di TikTok?  
  * **Time-bound (Terikat Waktu)**  
    Pertanyaan Anda harus ada batasan waktu yang jelas agar analisis memiliki konteks yang tepat.  
    * Salah: Berapa banyak pengguna baru kita?  
    * Benar: Berapa tingkat pertumbuhan pengguna baru secara bulanan (Month-over-Month) sepanjang tahun 2025?

**Contoh pertanyaan bisnis yang memenuhi seluruh elemen SMART**

"Faktor apa saja yang memengaruhi penurunan conversion rate pada pengguna aplikasi Android di wilayah Jabodetabek sebesar 5% selama periode Flash Sale Maret 2026?"

Keterangan:

* **Specific**: Fokus pada "penurunan conversion rate" untuk "aplikasi Android" di "Jabodetabek". Bukan sekadar penjualan turun.  
* **Measurable**: Ada angka konkret yang ingin dianalisis, yaitu penurunan sebesar "5%".  
* **Action-Oriented**: Dengan mengetahui faktor penyebabnya misalnya bug pada versi Android tertentu atau kendala logistik di Jabodetabek, tim bisa langsung melakukan perbaikan teknis atau operasional.  
* **Relevant**: Penurunan konversi saat Flash Sale adalah masalah kritis bagi bisnis retail/e-commerce.  
* **Time-bound**: Dibatasi pada periode spesifik "Flash Sale Maret 2026".

**3\. Exploratory Data Analysis (EDA)**

Anda harus melakukan eksplorasi data guna menjawab pertanyaan bisnis.

* Minimal terdapat 2 pertanyaan bisnis yang ingin diselesaikan melalui proses EDA.  
* Anda dapat menggunakan berbagai method dan function dalam library Python untuk memahami data, seperti melihat rangkuman statistik, melakukan grouping dan agregasi untuk mendapatkan informasi tertentu, dan sebagainya.

Tahap selanjutnya ditujukan untuk melengkapi dan memperkuat proses eksplorasi Anda, yaitu melalui visualisasi data.

**4\. Visualization & Explanatory Analysis**

* Minimal terdapat 2 buah visualisasi data untuk menjawab pertanyaan bisnis yang telah dibuat.  
* Pastikan setiap pertanyaan bisnis terjawab oleh minimal 1 visualisasi.

**5\. Conclusion & Recommendation**

* Minimal terdapat 2 buah kesimpulan dari hasil visualisasi data yang sekaligus menjawab pertanyaan bisnis yang telah dibuat.  
* Pastikan ada kesimpulan untuk setiap pertanyaan bisnis.  
* Buat minimal 1 rekomendasi akhir berupa action item dari kesimpulan yang telah didapatkan.

### **Kriteria 3: Proses Analisis Dibuat dalam Notebook yang Rapi**

Pada submission ini, Anda harus mengerjakan proyek analisis data menggunakan templat proyek yang telah disediakan. Tujuannya supaya proyek yang dibuat terdokumentasi dengan rapi. Untuk file template nya yakni:
C:\Users\Lenovo LOQ\Documents\coding\dicoding\tes\capstone\template_notebook.ipynb

### **Kriteria 4: Membuat Dashboard Sederhana Menggunakan Streamlit**

Setelah melakukan proses analisis, selanjutnya Anda wajib membuat dashboard sebagai media untuk menyampaikan hasil analisis data secara interaktif. Pada proyek ini, Anda dapat membuat dashboard dengan streamlit mirip seperti materi latihan sebelumnya. Selain itu, pastikan bahwa dashboard Anda buat dapat berjalan dengan lancar di *local*.

2. ## **Ketentuan Berkas**

pastikan untuk menulis **penjelasan atau tujuan** dari **teknik analisis** yang dilakukan dalam **markdown/text cell** pada berkas Jupyter Notebook atau Colab Notebook.

Berikut merupakan struktur direktori submission yang kami sarankan.  
submission

├───dashboard

| └───dashboard.py

├───notebook.ipynb

