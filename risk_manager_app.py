import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Risk Manager", layout="centered")

# --- STILE PERSONALIZZATO ---
st.markdown("""
<style>
body {
    background-color: #f5f7fa;  /* sfondo chiaro */
    color: #003366;             /* testo principale blu scuro */
    font-family: 'Arial', sans-serif;
}
h1, h2, h3 {
    color: #003366;
}
.result-box {
    background-color: #005b96; /* blu scuro */
    color: white;
    padding: 20px;
    border-radius: 12px;
    margin: 10px 0;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.title("💰 Risk Manager - Calcolo Lotti")

# --- INPUT UTENTE ---
strumento = st.selectbox("Seleziona lo strumento:", ["EURUSD", "XAUUSD"])
capitale = st.number_input("Capitale account (€):", min_value=0.0, value=1000.0, step=1.0)
rischio_euro = st.number_input("Quanto vuoi rischiare (€):", min_value=0.0, value=20.0, step=1.0)
prezzo_entry = st.number_input("Prezzo di entrata:", min_value=0.0, value=1.0, step=0.01)
prezzo_sl = st.number_input("Prezzo Stop Loss:", min_value=0.0, value=0.99, step=0.01)

# --- CALCOLI ---
if strumento == "EURUSD":
    pips = abs(prezzo_entry - prezzo_sl) * 10000
    valore_pip = 10
elif strumento == "XAUUSD":
    pips = abs(prezzo_entry - prezzo_sl) * 10
    valore_pip = 10

if pips != 0:
    lotti = rischio_euro / (pips * valore_pip)
    rischio_reale = lotti * pips * valore_pip
else:
    lotti = 0
    rischio_reale = 0

# --- RISULTATI ---
st.markdown(f"""
<div class="result-box">
<h3>📊 Risultato:</h3>
<p>Stop Loss in pips: <b>{pips:.1f} pips</b></p>
<p>Lotti consigliati: <b>{lotti:.2f}</b></p>
<p>Rischio reale se lo stop viene colpito: <b>{rischio_reale:.2f} €</b></p>
</div>
""", unsafe_allow_html=True)
