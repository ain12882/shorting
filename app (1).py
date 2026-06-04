# app.py - Aplikasi Manajemen Toko
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Manajemen Toko", layout="wide", page_icon="🏪")

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Import Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Background utama ── */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}

/* ── Judul utama ── */
h1 {
    background: linear-gradient(90deg, #00f2fe, #4facfe, #a18cd1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700 !important;
    font-size: 2.2rem !important;
    margin-bottom: 0.5rem !important;
}

/* ── Subheader ── */
h2, h3 {
    color: #e0e0ff !important;
    font-weight: 600 !important;
}

/* ── Tab navigasi ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    color: #a0a0c8 !important;
    font-weight: 500;
    padding: 8px 20px;
    transition: all 0.2s;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(102,126,234,0.4);
}

/* ── Card / Block container ── */
.stForm {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 16px !important;
    padding: 1.5rem !important;
    backdrop-filter: blur(10px);
}

/* ── Input fields ── */
.stTextInput input, .stNumberInput input, .stSelectbox select {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 10px !important;
    color: white !important;
    font-family: 'Inter', sans-serif;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 2px rgba(102,126,234,0.3) !important;
}

/* ── Label input ── */
label, .stTextInput label, .stNumberInput label, .stSelectbox label {
    color: #b0b0d8 !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
}

/* ── Tombol utama (form submit) ── */
.stFormSubmitButton button, button[kind="primary"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    border: none !important;
    border-radius: 10px !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 15px rgba(102,126,234,0.4) !important;
}
.stFormSubmitButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(102,126,234,0.6) !important;
}

/* ── Tombol biasa (hapus dll) ── */
button[kind="secondary"] {
    background: rgba(255,80,80,0.15) !important;
    border: 1px solid rgba(255,80,80,0.4) !important;
    border-radius: 8px !important;
    color: #ff8080 !important;
    font-weight: 500 !important;
    transition: all 0.2s !important;
}
button[kind="secondary"]:hover {
    background: rgba(255,80,80,0.3) !important;
    transform: scale(1.05);
}

/* ── Metric (sidebar) ── */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    padding: 0.8rem 1rem !important;
    margin-bottom: 0.5rem !important;
}
[data-testid="metric-container"] label {
    color: #9090c0 !important;
    font-size: 0.8rem !important;
}
[data-testid="metric-container"] [data-testid="metric-value"] {
    color: #00f2fe !important;
    font-weight: 700 !important;
    font-size: 1.4rem !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(15,12,41,0.95) !important;
    border-right: 1px solid rgba(255,255,255,0.08) !important;
}
[data-testid="stSidebar"] h2 {
    color: #a18cd1 !important;
}

/* ── Success / Warning / Error / Info box ── */
.stSuccess {
    background: rgba(0,230,118,0.12) !important;
    border: 1px solid rgba(0,230,118,0.35) !important;
    border-radius: 10px !important;
    color: #00e676 !important;
}
.stWarning {
    background: rgba(255,193,7,0.12) !important;
    border: 1px solid rgba(255,193,7,0.35) !important;
    border-radius: 10px !important;
    color: #ffc107 !important;
}
.stError {
    background: rgba(255,82,82,0.12) !important;
    border: 1px solid rgba(255,82,82,0.35) !important;
    border-radius: 10px !important;
    color: #ff5252 !important;
}
.stInfo {
    background: rgba(79,172,254,0.12) !important;
    border: 1px solid rgba(79,172,254,0.35) !important;
    border-radius: 10px !important;
    color: #4facfe !important;
}

/* ── Divider ── */
hr {
    border-color: rgba(255,255,255,0.1) !important;
    margin: 1rem 0 !important;
}

/* ── Teks paragraph ── */
p, .stMarkdown p {
    color: #c8c8e8 !important;
}

/* ── Caption ── */
.stCaption, small {
    color: #8080b0 !important;
}

/* ── Selectbox dropdown ── */
[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 10px !important;
}
[data-baseweb="select"] span {
    color: white !important;
}

/* ── Number input buttons ── */
[data-testid="stNumberInput"] button {
    background: rgba(102,126,234,0.3) !important;
    border-color: rgba(102,126,234,0.5) !important;
    color: white !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); }
::-webkit-scrollbar-thumb { background: rgba(102,126,234,0.5); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(102,126,234,0.8); }
</style>
""", unsafe_allow_html=True)

st.title("🏪 Manajemen Toko")

# ── Inisialisasi session state ─────────────────────────────────────────────────
if "produk" not in st.session_state:
    st.session_state.produk = []
if "transaksi" not in st.session_state:
    st.session_state.transaksi = []
if "id_counter" not in st.session_state:
    st.session_state.id_counter = 1

# ── Sidebar: Statistik ─────────────────────────────────────────────────────────
st.sidebar.header("📊 Statistik")
total_produk = len(st.session_state.produk)
total_stok = sum(p["stok"] for p in st.session_state.produk)
total_pendapatan = sum(t["total"] for t in st.session_state.transaksi)
total_transaksi = len(st.session_state.transaksi)

st.sidebar.metric("Total Produk", total_produk)
st.sidebar.metric("Total Stok", total_stok)
st.sidebar.metric("Pendapatan", f"Rp {total_pendapatan:,.0f}")
st.sidebar.metric("Jumlah Transaksi", total_transaksi)

stok_tipis = [p for p in st.session_state.produk if p["stok"] <= 5]
if stok_tipis:
    st.sidebar.warning(f"⚠️ {len(stok_tipis)} produk stok menipis!")
    for p in stok_tipis:
        st.sidebar.write(f"- {p['nama']} (stok: {p['stok']})")

# ── Tab utama ──────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["📦 Produk", "💰 Transaksi", "📋 Riwayat"])

# ── TAB 1: Produk ──────────────────────────────────────────────────────────────
with tab1:
    st.subheader("Tambah Produk Baru")
    with st.form("form_produk"):
        col1, col2 = st.columns(2)
        with col1:
            nama = st.text_input("Nama Produk")
            kategori = st.selectbox("Kategori", ["Pakaian", "Makanan", "Elektronik", "Lainnya"])
        with col2:
            harga = st.number_input("Harga (Rp)", min_value=0, step=500)
            stok = st.number_input("Stok", min_value=0, step=1)
        submitted = st.form_submit_button("➕ Tambah Produk")
        if submitted:
            if not nama:
                st.error("Nama produk tidak boleh kosong!")
            else:
                st.session_state.produk.append({
                    "id": st.session_state.id_counter,
                    "nama": nama,
                    "kategori": kategori,
                    "harga": harga,
                    "stok": stok,
                })
                st.session_state.id_counter += 1
                st.success(f"✅ Produk '{nama}' berhasil ditambahkan!")
                st.rerun()

    st.divider()
    st.subheader("🗂️ Daftar Produk")

    if not st.session_state.produk:
        st.info("Belum ada produk. Tambahkan produk di atas.")
    else:
        for i, p in enumerate(st.session_state.produk):
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 1])
            with col1:
                st.markdown(f"**{p['nama']}**")
                st.caption(p["kategori"])
            with col2:
                st.markdown(f"<span style='color:#4facfe;font-weight:600'>Rp {p['harga']:,.0f}</span>", unsafe_allow_html=True)
            with col3:
                if p["stok"] > 10:
                    st.success(f"Stok: {p['stok']}")
                elif p["stok"] > 3:
                    st.warning(f"Stok: {p['stok']}")
                else:
                    st.error(f"Stok: {p['stok']}")
            with col4:
                new_stok = st.number_input(
                    "Update stok", value=p["stok"], min_value=0,
                    key=f"stok_{p['id']}", label_visibility="collapsed"
                )
                if new_stok != p["stok"]:
                    st.session_state.produk[i]["stok"] = new_stok
                    st.rerun()
            with col5:
                if st.button("🗑️", key=f"del_{p['id']}"):
                    st.session_state.produk.pop(i)
                    st.rerun()

# ── TAB 2: Transaksi ───────────────────────────────────────────────────────────
with tab2:
    st.subheader("Catat Penjualan")

    produk_tersedia = [p for p in st.session_state.produk if p["stok"] > 0]

    if not produk_tersedia:
        st.warning("Tidak ada produk tersedia. Tambahkan produk di tab Produk.")
    else:
        with st.form("form_transaksi"):
            col1, col2 = st.columns([3, 1])
            with col1:
                pilihan = st.selectbox(
                    "Pilih Produk",
                    options=produk_tersedia,
                    format_func=lambda p: f"{p['nama']} — Rp {p['harga']:,.0f} (stok: {p['stok']})"
                )
            with col2:
                qty = st.number_input("Jumlah", min_value=1, max_value=pilihan["stok"], step=1)

            total = pilihan["harga"] * qty
            st.info(f"💵 Total: **Rp {total:,.0f}**")

            jual = st.form_submit_button("💰 Catat Penjualan")
            if jual:
                for p in st.session_state.produk:
                    if p["id"] == pilihan["id"]:
                        p["stok"] -= qty
                        break
                st.session_state.transaksi.append({
                    "nama": pilihan["nama"],
                    "qty": qty,
                    "harga_satuan": pilihan["harga"],
                    "total": total,
                    "waktu": datetime.now().strftime("%d/%m/%Y %H:%M"),
                })
                st.success(f"✅ Terjual {qty}x {pilihan['nama']} — Rp {total:,.0f}")
                st.rerun()

# ── TAB 3: Riwayat ─────────────────────────────────────────────────────────────
with tab3:
    st.subheader("📋 Riwayat Transaksi")

    if not st.session_state.transaksi:
        st.info("Belum ada transaksi.")
    else:
        for t in reversed(st.session_state.transaksi):
            col1, col2, col3 = st.columns([4, 2, 2])
            with col1:
                st.markdown(f"**{t['nama']}**")
                st.caption(f"{t['waktu']} · {t['qty']} pcs @ Rp {t['harga_satuan']:,.0f}")
            with col2:
                st.markdown(f"<span style='color:#00f2fe;font-weight:700'>Rp {t['total']:,.0f}</span>", unsafe_allow_html=True)
            with col3:
                st.markdown("<span style='color:#00e676'>✅ Selesai</span>", unsafe_allow_html=True)

        st.divider()
        st.markdown(f"<h4 style='color:#a18cd1'>💰 Total Pendapatan: Rp {total_pendapatan:,.0f}</h4>", unsafe_allow_html=True)

        if st.button("🗑️ Hapus Semua Riwayat"):
            st.session_state.transaksi = []
            st.rerun()
