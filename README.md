# NutriScan MBG 🍱 - Dashboard Analisis Gizi Seimbang & Segmentasi Makanan

**NutriScan MBG** adalah platform analisis data dan segmentasi citra makanan berbasis AI untuk mengawasi serta menjamin keseimbangan porsi nutrisi pada program nasional **Makan Bergizi Gratis (MBG)** di Indonesia. Menggunakan segmentasi semantik, platform ini mendeteksi komponen-komponen makanan dalam kotak ompreng dan mengevaluasi kepatuhannya terhadap kriteria piring sehat gizi seimbang.

---

## 📁 Struktur Proyek (Project Structure)

*   `notebook.ipynb`: Notebook utama berisi data wrangling (COCO parsing), pembersihan data, *stratified split*, preprocessing (auto-orient, pad-resize), augmentasi gambar, Exploratory Data Analysis (EDA), visualisasi porsi, serta kesimpulan bisnis.
*   `dashboard/`
    *   `dashboard.py`: Aplikasi dashboard interaktif berbasis Streamlit yang mengintegrasikan statistik data gizi dan **peninjau segmentasi masker interaktif** dengan transparansi slider.
*   `dataset/`: Berkas dataset yang telah dipreproses dan dipecah ke dalam split `train`, `valid`, dan `test` (berisi subdirektori `images` dan `masks`).
*   `ompreng_mbg_coco/`: Berkas anotasi citra mentah dalam format COCO.
*   `requirements.txt`: Daftar pustaka Python yang dibutuhkan proyek ini.

---

## 🛠️ Prasyarat & Instalasi (Prerequisites & Installation)

Pastikan Anda memiliki **Python 3.8+** yang sudah terinstal di sistem Anda.

1.  **Clone / Buka Direktori Proyek:**
    ```bash
    cd c:\Users\Lenovo LOQ\Documents\coding\dicoding\tes\capstone
    ```

2.  **Buat Virtual Environment (Sangat Direkomendasikan):**
    ```bash
    python -m venv .venv
    ```

3.  **Aktifkan Virtual Environment:**
    *   **Windows (PowerShell/CMD):**
        ```powershell
        .venv\Scripts\activate
        ```
    *   **macOS / Linux:**
        ```bash
        source .venv/bin/activate
        ```

4.  **Instal Seluruh Dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Cara Menjalankan (How to Run)

### 📓 1. Jupyter Notebook (Analisis Data & Preprocessing)
Untuk menjalankan atau meninjau proses data preprocessing, eksplorasi data, dan visualisasi:
```bash
jupyter notebook
```
Buka berkas `notebook.ipynb` pada peramban (browser) Anda dan jalankan sel-sel kode secara berurutan.

### 📊 2. Streamlit Dashboard (Visualisasi Interaktif & Peninjau Masker)
Untuk meluncurkan dashboard premium interaktif guna meninjau performa dan sebaran seimbang nutrisi makanan:
```bash
streamlit run dashboard/dashboard.py
```
Setelah dijalankan, dashboard akan terbuka secara otomatis di browser Anda di:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 📈 Ringkasan Wawasan Data (Data Analysis Insights)

*   **Porsi Karbohidrat Dominan**: Karbohidrat mengambil area visual terbesar di wadah makan dengan rata-rata **32.35%**, diikuti Protein (**24.90%**), dan Sayur (**20.70%**).
*   **Kepatuhan Gizi Seimbang Sangat Tinggi**: Lebih dari **94.91%** sampel kotak makan pada training set telah memenuhi standar gizi seimbang dengan menghadirkan minimal 4 kategori nutrisi penting.
*   **Peluang Peningkatan Porsi Buah**: Rata-rata porsi buah saat ini baru menyentuh **13.86%** piksel makanan. Disarankan untuk meningkatkan porsi visual buah agar melampaui ambang batas ideal minimal 15% gizi seimbang.
