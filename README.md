# NutriScan MBG - Analisis Gizi Seimbang & Segmentasi Makanan

**NutriScan MBG** adalah platform analisis data dan segmentasi citra makanan berbasis AI untuk mengawasi serta menjamin keseimbangan porsi nutrisi pada program nasional **Makan Bergizi Gratis (MBG)** di Indonesia. Menggunakan segmentasi semantik, platform ini mendeteksi komponen-komponen makanan dalam kotak ompreng dan mengevaluasi kepatuhannya terhadap kriteria piring sehat gizi seimbang.

---

##  Prasyarat & Instalasi

Pastikan Anda memiliki **Python 3.8+** yang sudah terinstal di sistem Anda.

1.  **Clone Repository:**
    ```bash
    git clone https://github.com/iqbalmuhammad08f/NutriScan-MBG
    ```

2.  **Buat Virtual Environment (opsional):**
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

## Cara Menjalankan

### 1. Jupyter Notebook (Analisis Data & Preprocessing)
Untuk menjalankan atau meninjau proses data preprocessing, eksplorasi data, dan visualisasi:
```bash
jupyter notebook
```
Buka berkas `notebook.ipynb` pada peramban (browser) Anda dan jalankan sel-sel kode secara berurutan.

### 2. Streamlit Dashboard (Visualisasi Interaktif & Peninjau Masker)
Untuk meluncurkan dashboard premium interaktif guna meninjau performa dan sebaran seimbang nutrisi makanan:
```bash
streamlit run dashboard/dashboard.py
```

---
