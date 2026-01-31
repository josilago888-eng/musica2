import streamlit as st
import pandas as pd
import urllib.parse

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Billboard Top 10 Search", page_icon="🎵", layout="centered")

# --- 1. GERAÇÃO DA BASE DE DADOS (CSV FICTÍCIO) ---
@st.cache_data
def generate_billboard_data():
    # Músicas e Artistas reais para popular o CSV fictício
    musicas_base = [
        "Blinding Lights", "The Box", "Levitating", "Save Your Tears", 
        "As It Was", "Heat Waves", "Anti-Hero", "Flowers", 
        "Cruel Summer", "Vampire", "Paint The Town Red", "Espresso"
    ]
    artistas_base = [
        "The Weeknd", "Roddy Ricch", "Dua Lipa", "The Weeknd", 
        "Harry Styles", "Glass Animals", "Taylor Swift", "Miley Cyrus", 
        "Taylor Swift", "Olivia Rodrigo", "Doja Cat", "Sabrina Carpenter"
    ]

    rows = []
    for ano in range(2020, 2026):
        for mes in range(1, 13):
            for pos in range(1, 11):
                # Seleção para preencher o CSV
                idx = (ano + mes + pos) % len(musicas_base)
                titulo = musicas_base[idx]
                cantor = artistas_base[idx]
                
                # Gerando o link de busca oficial do Spotify
                query = urllib.parse.quote(f"{titulo} {cantor}")
                link_spotify = f"https://open.spotify.com/search/{query}"
                
                rows.append({
                    "Ano": ano,
                    "Mes": mes,
                    "Colocacao": pos,
                    "Titulo": titulo,
                    "Cantor": cantor,
                    "Spotify_Link": link_spotify
                })
    return pd.DataFrame(rows)

# Criar o DataFrame (representando o CSV)
df = generate_billboard_data()

# --- 2. INTERFACE PRINCIPAL ---
st.title("🎵 Billboard Top 10 Explorer")
st.markdown("Consulte os sucessos dos EUA entre 2020 e 2025.")

# --- 3. FILTROS NA ÁREA PRINCIPAL ---
st.write("### Selecione o Período")
c1, c2 = st.columns(2)

with c1:
    ano_selecionado = st.selectbox("📅 Ano", sorted(df['Ano'].unique(), reverse=True))

with c2:
    meses_pt = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
        7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    mes_nome = st.selectbox("📆 Mês", list(meses_pt.values()))
    mes_selecionado = [k for k, v in meses_pt.items() if v == mes_nome][0]

st.divider()

# --- 4. FILTRAGEM E EXIBIÇÃO ---
# O sistema busca no DataFrame baseado na sua escolha de filtros
resultado = df[(df['Ano'] == ano_selecionado) & (df['Mes'] == mes_selecionado)]
resultado = resultado.sort_values(by="Colocacao")

if not resultado.empty:
    st.subheader(f"🏆 Top 10 em {mes_nome} de {ano_selecionado}")
    
    for _, row in resultado.iterrows():
        with st.container():
            col_rank, col_info, col_link = st.columns([0.6, 3, 1.4])
            
            with col_rank:
                st.markdown(f"## {row['Colocacao']}º")
            
            with col_info:
                # Puxando Nome e Artista diretamente do CSV
                st.markdown(f"**{row['Titulo']}**")
                st.caption(f"Cantor: {row['Cantor']}")
            
            with col_link:
                # Link de busca gerado no CSV
                st.link_button("🔍 Spotify", row['Spotify_Link'])
            
            st.divider()
else:
    st.warning("Dados não encontrados para esta seleção.")

# --- DOWNLOAD DO CSV ---
st.markdown("---")
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Baixar Base de Dados CSV (2020-2025)",
    data=csv_data,
    file_name='billboard_data.csv',
    mime='text/csv',
)

