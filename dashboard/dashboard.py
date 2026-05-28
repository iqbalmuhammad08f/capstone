import os
import json
import random
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from PIL import Image, ImageOps
import streamlit as st


# 1. Page Configuration & Theme

st.set_page_config(
    page_title="NutriScan MBG - Dashboard Analisis Gizi Seimbang",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium UI Styling Custom CSS (Dark-mode optimized, custom font, sleek cards, hover effects)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Sleek Dark Mode Background */
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #1a1e29 100%);
        color: #e2e8f0;
    }
    
    /* Header Gradient Styling */
    .header-container {
        padding: 1.8rem;
        background: rgba(30, 41, 59, 0.45);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(12px);
        text-align: center;
    }
    
    .header-title {
        background: #FFF;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
        font-weight: 300;
    }
    
    /* Premium Glassmorphism Cards */
    .glass-card {
        padding: 1.5rem;
        background: rgba(30, 41, 59, 0.35);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(8px);
        margin-bottom: 1rem;
        transition: transform 0.3s ease, border 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-4px);
        border: 1px solid rgba(129, 140, 248, 0.3);
    }
    
    /* Custom Badges */
    .badge {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        color: white;
        display: inline-block;
        margin: 2px;
    }
    
    .badge-buah { background-color: #ff3232; }
    .badge-karbohidrat { background-color: #ffc832; color: #1e293b; }
    .badge-protein { background-color: #3296ff; }
    .badge-sayur { background-color: #32c832; }
    .badge-susu { background-color: #b432ff; }
    
    /* Streamlit widget tweaks */
    div[data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 700;
        color: #f8fafc;
    }
    
    div[data-testid="stMetricLabel"] {
        font-size: 0.95rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    </style>
    """, unsafe_allow_html=True)


# 2. Path Settings & Data Loading

DASHBOARD_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(DASHBOARD_DIR)
STATS_PATH = os.path.join(WORKSPACE_DIR, "dataset", "metadata", "analyzed_stats.json")
DATASET_DIR = os.path.join(WORKSPACE_DIR, "dataset")

class_mapping = {
    0: "background",
    1: "buah",
    2: "karbohidrat",
    3: "protein",
    4: "sayur",
    5: "susu"
}

COLORS = {
    1: [255, 50, 50],     # buah - merah
    2: [255, 200, 50],    # karbohidrat - kuning
    3: [50, 150, 255],    # protein - biru
    4: [50, 200, 50],     # sayur - hijau
    5: [180, 50, 255]     # susu - ungu
}

@st.cache_data
def load_stats(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

stats_data = load_stats(STATS_PATH)

if stats_data is None:
    st.error(f"File stats `{STATS_PATH}` tidak ditemukan! Pastikan Anda telah menjalankan analisis data terlebih dahulu.")
    st.stop()

# Helper function to convert data list to DataFrame
@st.cache_data
def get_dataframe(data):
    rows = []
    for split, items in data.items():
        for item in items:
            row = {
                'split': split,
                'filename': item['filename'],
                'total_food_pixels': item['total_food_pixels'],
                'num_categories': item['num_categories'],
                'buah_pixels': item['counts']['1'],
                'karbohidrat_pixels': item['counts']['2'],
                'protein_pixels': item['counts']['3'],
                'sayur_pixels': item['counts']['4'],
                'susu_pixels': item['counts']['5']
            }
            rows.append(row)
    df = pd.DataFrame(rows)
    # Calculate percentage contributions
    for col in ['buah', 'karbohidrat', 'protein', 'sayur', 'susu']:
        df[f'{col}_pct'] = (df[f'{col}_pixels'] / df['total_food_pixels']) * 100
    df['is_balanced'] = df['num_categories'] >= 4
    return df

df = get_dataframe(stats_data)


# 3. Sidebar Navigation & Interactive Filters

with st.sidebar:
    st.markdown("### Navigasi Dashboard")
    view_mode = st.radio(
        "Pilih Tampilan:",
        ["Analisis Statistik", "Peninjau Masker Segmentasi"]
    )
    
    st.markdown("---")
    st.markdown("### Filter Data")
    
    # Selection of split
    selected_split = st.selectbox(
        "Pilih Split Dataset:",
        ["Semua Split", "train", "valid", "test"],
        format_func=lambda x: "Semua Split" if x == "Semua Split" else f"{x.capitalize()} Split"
    )
    
    # Filter by number of food categories present
    min_cats, max_cats = st.slider(
        "Filter Jumlah Kategori Nutrisi:",
        min_value=3, max_value=5, value=(3, 5)
    )

# Filter dataframe based on selections
filtered_df = df.copy()
if selected_split != "Semua Split":
    filtered_df = filtered_df[filtered_df['split'] == selected_split]

filtered_df = filtered_df[
    (filtered_df['num_categories'] >= min_cats) & 
    (filtered_df['num_categories'] <= max_cats)
]


# 4. Header Section

st.markdown("""
    <div class="header-container">
        <div class="header-title">NutriScan MBG</div>
        <div class="header-subtitle">Dashboard Deteksi Dini Risiko Pola Makan Tidak Seimbang Melalui Analisis Visual Makanan</div>
    </div>
    """, unsafe_allow_html=True)


# 5. VIEW MODE: Analisis Statistik

if view_mode == "Analisis Statistik":
    
    # Key Performance Metrics row
    col1, col2 = st.columns(2)
    
    total_samples = len(filtered_df)
    balanced_meals = len(filtered_df[filtered_df['is_balanced'] == True])
    compliance_rate = (balanced_meals / total_samples * 100) if total_samples > 0 else 0
    
    avg_sayur = filtered_df['sayur_pct'].mean() if total_samples > 0 else 0
    avg_buah = filtered_df['buah_pct'].mean() if total_samples > 0 else 0
    
    with col1:
        st.markdown(f"""
            <div class="glass-card">
                <div>TOTAL SAMPEL</div>
                <div style="font-size: 2.2rem; font-weight:700; color:#38bdf8;">{total_samples}</div>
                <div style="color: #94a3b8; font-size:0.85rem; margin-top:0.4rem;">Wadah Makanan (Ompreng)</div>
            </div>
            """, unsafe_allow_html=True)
            
    with col2:
        badge_text = "SEIMBANG" if compliance_rate >= 90 else "TINGKATKAN"
        st.markdown(f"""
            <div class="glass-card">
                <div>TINGKAT KEPATUHAN</div>
                <div style="font-size: 2.2rem; font-weight:700; color:#818cf8;">{compliance_rate:.1f}%</div>
                <div style="color: #94a3b8; font-size:0.85rem; margin-top:0.4rem;">{badge_text}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Plots Section
    left_plot, right_plot = st.columns(2)
    
    with left_plot:
        st.markdown("### Persentase Area Porsi Gizi vs Ambang Batas Sehat")
        
        # Calculate averages for plot
        categories = ['buah', 'karbohidrat', 'protein', 'sayur', 'susu']
        avg_vals = [filtered_df[f'{cat}_pct'].mean() for cat in categories]
        
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="#1e293b")
        ax.set_facecolor("#1e293b")
        
        # Create gradient colors for plot
        colors = ['#ef4444', '#f59e0b', '#3b82f6', '#10b981', '#a855f7']
        bars = ax.bar([c.capitalize() for c in categories], avg_vals, color=colors, edgecolor='white', alpha=0.9, width=0.6)
        
        # Style grid & labels
        ax.tick_params(colors='white', labelsize=11)
        ax.xaxis.grid(False)
        ax.yaxis.grid(True, color='white', alpha=0.1, ls='--')
        
        # Line for 15% threshold
        ax.axhline(15, color='#f43f5e', ls='--', linewidth=2, label='Ideal Min 15%')
        
        ax.set_ylabel("Rata-rata Persentase Area Piksel (%)", color='white', fontsize=12)
        ax.set_title("Distribusi Rata-rata Porsi Area Gizi", color='white', fontsize=14, fontweight='bold', pad=15)
        ax.set_ylim(0, 40)
        
        # Value tags
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.1f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', color='white', fontweight='bold')
            
        ax.legend(loc='upper right', facecolor='#1e293b', edgecolor='white', labelcolor='white')
        
        # Remove spines
        for spine in ['top', 'right', 'left', 'bottom']:
            ax.spines[spine].set_color('none')
            
        st.pyplot(fig)
        
    with right_plot:
        st.markdown("### Distribusi Kelengkapan Menu Nutrisi per Sajian")
        
        # Pie chart / Donut Chart for number of categories present
        cat_counts = filtered_df['num_categories'].value_counts().sort_index()
        
        if len(cat_counts) > 0:
            fig, ax = plt.subplots(figsize=(8, 8), facecolor="#1e293b")
            ax.set_facecolor("#1e293b")
            
            # Palette
            colors = sns.color_palette('viridis_r', len(cat_counts))
            explode = [0.08 if x < 4 else 0.0 for x in cat_counts.index]
            
            wedges, texts, autotexts = ax.pie(
                cat_counts.values,
                labels=[f'{x} Kategori' for x in cat_counts.index],
                autopct='%1.1f%%',
                startangle=140,
                colors=colors,
                explode=explode,
                shadow=False,
                textprops=dict(color="white", fontsize=11, weight="bold")
            )
            
            # Change color of autopct labels for readability
            for autotext in autotexts:
                autotext.set_color('white')
                
            # Draw a circle in the center to make it a donut chart
            centre_circle = plt.Circle((0,0),0.55,fc='#1e293b')
            ax.add_artist(centre_circle)
            
            ax.set_title("Tingkat Kelengkapan Variasi Komponen Gizi", color='white', fontsize=14, fontweight='bold', pad=15)
            st.pyplot(fig)
        else:
            st.info("Tidak ada data yang memenuhi filter saat ini.")
            
    st.markdown("---")
    
    # Data Table View
    st.markdown("### Daftar Sampel Makanan Terfilter")
    show_df = filtered_df[['filename', 'split', 'num_categories', 'buah_pct', 'karbohidrat_pct', 'protein_pct', 'sayur_pct', 'susu_pct', 'is_balanced']]
    
    st.dataframe(
        show_df.style.format({
            'buah_pct': '{:.2f}%',
            'karbohidrat_pct': '{:.2f}%',
            'protein_pct': '{:.2f}%',
            'sayur_pct': '{:.2f}%',
            'susu_pct': '{:.2f}%'
        }).background_gradient(subset=['sayur_pct', 'buah_pct'], cmap='Greens', vmin=0, vmax=30),
        use_container_width=True
    )


# 6. VIEW MODE: Peninjau Masker Segmentasi (Visualizer)

else:
    st.markdown("### Segmentasi Masker Gizi & Visualizer Interaktif")
    st.markdown("Fitur ini memungkinkan Anda memuat gambar asli dan mencocokkannya secara dinamis dengan masker segmentasi semantik hasil label ground-truth.")

    # Control row
    col_ctrl1, col_ctrl2 = st.columns([1, 2])
    
    # Active split selection for sampling
    with col_ctrl1:
        split_sample = st.selectbox(
            "Pilih Split Gambar:",
            ["train", "valid", "test"],
            index=0
        )
        
        # Load a random file from this split
        images_dir = os.path.join(DATASET_DIR, "images", split_sample)
        masks_dir = os.path.join(DATASET_DIR, "masks", split_sample)
        
        if not os.path.exists(images_dir) or not os.path.exists(masks_dir):
            st.error(f"Folder dataset tidak lengkap di path: `{images_dir}`")
            st.stop()
            
        all_imgs = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
        
        if not all_imgs:
            st.warning("Tidak ada file gambar ditemukan di folder split terpilih.")
            st.stop()
            
        # Use session state to persist selected image across transparency adjustments
        if "selected_img" not in st.session_state or "last_split" not in st.session_state or st.session_state.last_split != split_sample:
            st.session_state.selected_img = random.choice(all_imgs)
            st.session_state.last_split = split_sample
            
        if st.button("Muat Sampel Gambar Acak Baru"):
            st.session_state.selected_img = random.choice(all_imgs)

    with col_ctrl2:
        alpha_slider = st.slider(
            "Transparansi Masker Overlay (Alpha):",
            min_value=0.0, max_value=1.0, value=0.5, step=0.05
        )
        
    st.markdown("---")
    
    # Load selected image and corresponding mask
    img_name = st.session_state.selected_img
    img_path = os.path.join(images_dir, img_name)
    
    mask_name = os.path.splitext(img_name)[0] + ".png"
    mask_path = os.path.join(masks_dir, mask_name)
    
    if not os.path.exists(mask_path):
        st.error(f"Masker `{mask_name}` tidak ditemukan di `{masks_dir}`!")
        st.stop()
        
    # Read Image using OpenCV and convert to RGB
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Read mask
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    
    # Create colored mask representation
    colored_mask = np.zeros((*mask.shape, 3), dtype=np.uint8)
    for cat_id, color in COLORS.items():
        colored_mask[mask == cat_id] = color
        
    # Create overlay (alpha blend)
    # Resize mask or image if there's any dimension mismatch, though they should be 640x640
    if img_rgb.shape[:2] != mask.shape[:2]:
        mask_resized = cv2.resize(mask, (img_rgb.shape[1], img_rgb.shape[0]), interpolation=cv2.INTER_NEAREST)
        colored_mask = np.zeros((*mask_resized.shape, 3), dtype=np.uint8)
        for cat_id, color in COLORS.items():
            colored_mask[mask_resized == cat_id] = color
            
    overlay = cv2.addWeighted(img_rgb, 1.0 - alpha_slider, colored_mask, alpha_slider, 0)
    
    # Calculate pixel breakdown for this specific image on the fly!
    unique, counts = np.unique(mask, return_counts=True)
    counts_dict = dict(zip(unique, counts))
    total_food_pixels = sum(counts_dict.get(c, 0) for c in range(1, 6))
    
    # Display columns
    img_col, overlay_col = st.columns(2)
    
    with img_col:
        st.markdown("#### Gambar Asli (Original)")
        st.image(img_rgb, use_container_width=True)
        
        
    with overlay_col:
        st.markdown("#### Masker Overlay Semantik")
        st.image(overlay, use_container_width=True)
        
    # Breakdown section
    st.markdown("### Analisis Kandungan Wadah Makanan Terpilih")
    
    cols = st.columns(5)
    for idx, (cat_id, cat_name) in enumerate(class_mapping.items()):
        if cat_id == 0:
            continue
            
        pixel_count = counts_dict.get(cat_id, 0)
        pct = (pixel_count / total_food_pixels * 100) if total_food_pixels > 0 else 0
        
        with cols[idx-1]:
            card_class = f"badge-{cat_name}"
            # Render a mini card for each category
            if pixel_count > 0:
                st.markdown(f"""
                    <div style="background: rgba(30, 41, 59, 0.4); padding: 15px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05); text-align:center;">
                        <span class="badge {card_class}" style="font-size:1rem; padding: 6px 12px;">{cat_name.capitalize()}</span>
                        <div style="font-size: 1.6rem; font-weight:700; margin-top:8px; color:white;">{pct:.1f}%</div>
                        <div style="color: #94a3b8; font-size:0.8rem;">{pixel_count:,} Piksel</div>
                    </div><br>
                    """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="background: rgba(30, 41, 59, 0.2); padding: 15px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.02); text-align:center; opacity: 0.5;">
                        <span class="badge" style="background-color:#475569; font-size:1rem; padding: 6px 12px;">{cat_name.capitalize()}</span>
                        <div style="font-size: 1.6rem; font-weight:700; margin-top:8px; color:#64748b;">0.0%</div>
                        <div style="color: #64748b; font-size:0.8rem;">Tidak Ada</div>
                    </div><br>
                    """, unsafe_allow_html=True)
                    
    # Nutrition balanced verification
    num_cats_present = sum(1 for c in range(1, 6) if counts_dict.get(c, 0) > 0)
    is_bal = num_cats_present >= 4
    
    if is_bal:
        st.success(f"**GIZI SEIMBANG LENGKAP ({num_cats_present} Kategori)**")
    else:
        st.warning(f"**RISIKO POLA MAKAN TIDAK SEIMBANG ({num_cats_present} Kategori)**")
