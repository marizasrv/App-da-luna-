
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from PIL import Image
import io, random

st.set_page_config(page_title="Mundo da Luna", page_icon="🌙", layout="wide")

ASSETS = Path(__file__).parent / "assets"
st.markdown("""
<style>
.stApp {
    background:
      radial-gradient(circle at 15% 20%, rgba(255,255,255,.12) 0 2px, transparent 3px),
      radial-gradient(circle at 78% 14%, rgba(255,255,255,.10) 0 1.5px, transparent 2.5px),
      radial-gradient(circle at 42% 70%, rgba(255,255,255,.08) 0 1.5px, transparent 2.5px),
      linear-gradient(180deg, #2a1046 0%, #5e3097 48%, #8d63cf 100%);
    background-size: 180px 180px, 220px 220px, 260px 260px, auto;
    color: #ffffff;
}

.block-container {
    padding-top: 5.8rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

h1 {
    color: #ffe79c !important;
    font-weight: 900 !important;
    font-size: 2.15rem !important;
    line-height: 1.15 !important;
}
h2, h3 {
    color: #ffe79c !important;
    font-weight: 850 !important;
}

p, li, label, div, span {
    color: #ffffff !important;
}

.stCaption, small {
    color: #ffffff !important;
    opacity: 1 !important;
    font-size: 0.98rem !important;
    font-weight: 600 !important;
}

.luna-card {
    padding: 18px 18px;
    border-radius: 20px;
    background: rgba(234, 215, 255, .20);
    margin: 12px 0 18px 0;
    border: 1.5px solid rgba(255,255,255,.30);
    box-shadow: 0 8px 22px rgba(27, 9, 50, .18);
}

.luna-card b {
    font-size: 1.2rem !important;
}

button, .stButton > button, .stDownloadButton > button {
    background: #d8b4ff !important;
    color: #2a1046 !important;
    border-radius: 14px !important;
    border: none !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    min-height: 44px !important;
}

div[data-testid="stTabs"] button {
    color: #ffffff !important;
    font-size: 0.95rem !important;
    font-weight: 750 !important;
    padding-left: 0.45rem !important;
    padding-right: 0.45rem !important;
    white-space: nowrap !important;
}

div[data-testid="stTabs"] {
    overflow-x: auto !important;
}

div[data-testid="stRadio"] label,
div[data-testid="stCheckbox"] label {
    font-size: 1rem !important;
    font-weight: 650 !important;
    color: #ffffff !important;
}

input, textarea {
    font-size: 1rem !important;
    color: #2a1046 !important;
    background-color: #ffffff !important;
}

div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    font-size: 1rem !important;
    font-weight: 700 !important;
}

pre, code {
    color: #2a1046 !important;
    background: #f5ecff !important;
    font-size: 1rem !important;
    border-radius: 10px !important;
}

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,.12);
    border-radius: 16px;
    padding: 10px;
    border: 1px solid rgba(255,255,255,.22);
}

@media (max-width: 700px) {
    .block-container {
        padding-top: 6.4rem !important;
    }

    div[data-testid="stMarkdownContainer"] p {
        line-height: 1.45 !important;
    }

    h1 { font-size: 1.55rem !important; margin-top: 0 !important; padding-top: 0 !important; }
    h2 { font-size: 1.32rem !important; }
    h3 { font-size: 1.2rem !important; }

    .block-container {
        padding-left: .75rem !important;
        padding-right: .75rem !important;
    }

    div[data-testid="stTabs"] button {
        font-size: 0.78rem !important;
        padding-left: .24rem !important;
        padding-right: .24rem !important;
        min-width: max-content !important;
    }

    .luna-card {
        padding: 15px 15px !important;
    }
}

/* Ajustes da aba Jogos no celular */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,.96) !important;
    color: #2a1046 !important;
    border-radius: 14px !important;
    min-height: 48px !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
}

div[data-baseweb="popover"] {
    max-height: 52vh !important;
}

ul[role="listbox"] {
    max-height: 48vh !important;
    overflow-y: auto !important;
}

li[role="option"] {
    font-size: 1rem !important;
    padding-top: 12px !important;
    padding-bottom: 12px !important;
    color: #2a1046 !important;
    background: #ffffff !important;
}

.game-card {
    background: rgba(255,255,255,.14);
    border: 1.5px solid rgba(255,255,255,.28);
    border-radius: 18px;
    padding: 16px;
    margin-top: 10px;
    margin-bottom: 16px;
}


/* Letras mais escuras nos campos claros */
div[data-baseweb="select"] > div,
div[data-baseweb="select"] span,
div[data-baseweb="select"] input,
ul[role="listbox"],
li[role="option"] {
    color: #2a1046 !important;
    font-weight: 800 !important;
}

input, textarea,
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    color: #2a1046 !important;
    font-weight: 800 !important;
    background: #ffffff !important;
}

.stButton > button,
.stDownloadButton > button {
    color: #2a1046 !important;
    font-weight: 800 !important;
}

[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p {
    color: #2a1046 !important;
    font-weight: 700 !important;
}

/* Mantém textos sobre o fundo roxo claros */
.stApp h1, .stApp h2, .stApp h3,
.stApp p, .stApp label {
    text-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🌙 Mundo da Luna")
st.subheader("Atividades escolares, jogos, histórias e mídia da Luna")
st.caption("✨ Tema lilás e roxo, com leitura fácil no celular.")

tabs = st.tabs([
    "🏠 Início",
    "✏️ Alfabetização",
    "🔢 Matemática",
    "🌍 Conhecimentos",
    "🧩 Jogos",
    "📚 Histórias para dormir",
    "📸 Fotos e vídeos"
])

with tabs[0]:
    img = ASSETS/"livro.png"
    if img.exists():
        st.image(str(img), use_container_width=True)
    st.markdown(
        '<div class="luna-card"><b>Aprender brincando com Luna e seu coelhinho.</b><br>'
        'Atividades simples para crianças em fase de alfabetização e primeiros anos escolares.</div>',
        unsafe_allow_html=True
    )

with tabs[1]:
    st.header("✏️ Alfabetização")
    st.write("Complete as palavras:")
    a1 = st.text_input("L_NA", key="alf1")
    a2 = st.text_input("C_ELHO", key="alf2")
    a3 = st.text_input("L_VRO", key="alf3")
    if st.button("Corrigir palavras"):
        score = 0
        score += 1 if a1.strip().upper() == "U" else 0
        score += 1 if a2.strip().upper() == "O" else 0
        score += 1 if a3.strip().upper() == "I" else 0
        st.success(f"Você acertou {score} de 3! ⭐")

    st.divider()
    st.write("Qual palavra começa com a letra **L**?")
    r = st.radio("Escolha uma opção:", ["Lua", "Coelho", "Castelo"], key="letra_l")
    if st.button("Ver resposta", key="resp_l"):
        st.success("Correto! 🌙" if r == "Lua" else "Tente novamente.")

    st.divider()
    st.subheader("📝 Sílabas")
    silaba = st.radio("Qual sílaba completa COE__O?", ["LHI", "LHO", "LHA"], key="silaba_coelho")
    if st.button("Corrigir sílaba", key="corrigir_silaba"):
        st.success("Muito bem! COELHO 🐰" if silaba == "LHO" else "Tente novamente.")

    st.divider()
    st.subheader("🔠 Vogais")
    vogal = st.radio("Qual destas letras é uma vogal?", ["B", "A", "T"], key="vogal")
    if st.button("Corrigir vogal", key="corrigir_vogal"):
        st.success("Correto! A é uma vogal. ⭐" if vogal == "A" else "Tente novamente.")

with tabs[2]:
    st.header("🔢 Matemática")
    st.write("Resolva as continhas:")
    n1 = st.number_input("2 + 3 =", min_value=0, max_value=20, step=1, key="m1")
    n2 = st.number_input("5 - 2 =", min_value=0, max_value=20, step=1, key="m2")
    n3 = st.number_input("4 + 4 =", min_value=0, max_value=20, step=1, key="m3")
    if st.button("Corrigir matemática"):
        score = int(n1 == 5) + int(n2 == 3) + int(n3 == 8)
        st.success(f"Você acertou {score} de 3! ⭐")

    st.divider()
    st.write("Conte os símbolos:")
    st.write("⭐ ⭐ ⭐ ⭐ ⭐")
    qtd = st.number_input("Quantas estrelas aparecem?", min_value=0, max_value=10, step=1)
    if st.button("Conferir estrelas"):
        st.success("Muito bem! ⭐" if qtd == 5 else "Conte mais uma vez.")

    st.divider()
    st.subheader("🍎 Probleminha")
    st.write("Luna tinha 3 estrelas e encontrou mais 2. Quantas estrelas ela tem agora?")
    resposta = st.number_input("Resposta:", min_value=0, max_value=20, step=1, key="problema_estrelas")
    if st.button("Corrigir probleminha", key="corrigir_problema"):
        st.success("Isso! 3 + 2 = 5 ⭐" if resposta == 5 else "Tente novamente.")

with tabs[3]:
    st.header("🌍 Conhecimentos")
    q1 = st.radio("Qual aparece no céu à noite?", ["Lua", "Árvore", "Livro"], key="c1")
    q2 = st.radio("Qual animal acompanha Luna?", ["Coelho", "Peixe", "Leão"], key="c2")
    q3 = st.radio("Onde encontramos livros?", ["Biblioteca", "Piscina", "Garagem"], key="c3")
    if st.button("Corrigir conhecimentos"):
        score = int(q1=="Lua") + int(q2=="Coelho") + int(q3=="Biblioteca")
        st.success(f"Você acertou {score} de 3! 🌟")



with tabs[4]:
    st.header("🧩 Jogos da Luna")
    st.caption("Escolha um jogo no menu abaixo. Apenas o jogo selecionado aparece na tela.")

    st.markdown('<div class="game-card"><b>Escolha um jogo e brinque com a Luna ✨</b></div>', unsafe_allow_html=True)

    jogo = st.selectbox(
        "Jogo:",
        [
            "🔤 Complete a palavra",
            "🔢 Qual número vem depois?",
            "🧠 Memória rápida",
            "👀 Qual é diferente?",
            "🔗 Ligue a palavra ao símbolo",
            "⭐ Conte as estrelas",
            "✅ Verdadeiro ou falso",
            "🎯 Acerte a sequência",
        ],
        key="seletor_jogos"
    )

    if jogo == "🔤 Complete a palavra":
        st.subheader("🔤 Complete a palavra")
        palavra = st.text_input("Complete: E _ T R E L A", key="jogo_palavra")
        if st.button("Conferir palavra", key="btn_palavra"):
            if palavra.strip().upper() == "S":
                st.success("Muito bem! ⭐ A palavra é ESTRELA.")
            else:
                st.info("Tente outra vez. A letra que falta é S.")

    elif jogo == "🔢 Qual número vem depois?":
        st.subheader("🔢 Próximo número")
        numero = st.radio("2, 3, 4, ___", ["5", "6", "7"], key="seq_num")
        if st.button("Conferir sequência", key="btn_seq"):
            st.success("Correto! 🎉" if numero == "5" else "Observe a sequência e tente novamente.")

    elif jogo == "🧠 Memória rápida":
        st.subheader("🧠 Memória")
        st.write("Memorize: 🌙 🐰 ⭐ 📖")
        memoria = st.multiselect(
            "Escolha os quatro símbolos que apareceram:",
            ["🌙", "🐰", "⭐", "📖", "🍎", "🚗"],
            key="memoria_rapida"
        )
        if st.button("Ver resultado", key="btn_mem"):
            certos = {"🌙", "🐰", "⭐", "📖"}
            if set(memoria) == certos:
                st.success("Parabéns! Você lembrou de todos. 🧠✨")
            else:
                st.info("Quase! Tente novamente.")

    elif jogo == "👀 Qual é diferente?":
        st.subheader("👀 Encontre o diferente")
        escolha = st.radio("Encontre o símbolo diferente:", ["⭐", "⭐", "🌙", "⭐"], key="diferente")
        if st.button("Conferir", key="btn_diferente"):
            st.success("Isso! A lua é diferente. 🌙" if escolha == "🌙" else "Tente novamente.")

    elif jogo == "🔗 Ligue a palavra ao símbolo":
        st.subheader("🔗 Palavra e símbolo")
        opcao = st.selectbox("Qual símbolo combina com a palavra COELHO?", ["🌙", "🐰", "📖"], key="liga")
        if st.button("Conferir ligação", key="btn_liga"):
            st.success("Muito bem! 🐰" if opcao == "🐰" else "Tente de novo.")

    elif jogo == "⭐ Conte as estrelas":
        st.subheader("⭐ Conte as estrelas")
        st.write("⭐ ⭐ ⭐ ⭐ ⭐ ⭐")
        qtd = st.number_input("Quantas estrelas aparecem?", min_value=0, max_value=10, step=1, key="conta_jogo")
        if st.button("Conferir contagem", key="btn_conta_jogo"):
            st.success("Perfeito! São 6 estrelas. ⭐" if qtd == 6 else "Conte mais uma vez.")

    elif jogo == "✅ Verdadeiro ou falso":
        st.subheader("✅ Verdadeiro ou falso")
        vf = st.radio("A lua aparece no céu à noite.", ["Verdadeiro", "Falso"], key="vf1")
        if st.button("Conferir resposta", key="btn_vf"):
            st.success("Correto! 🌙" if vf == "Verdadeiro" else "Tente novamente.")

    elif jogo == "🎯 Acerte a sequência":
        st.subheader("🎯 Complete a sequência")
        st.write("🌙 ⭐ 🌙 ⭐ ___")
        seq = st.radio("Qual vem depois?", ["🌙", "⭐", "🐰"], key="seq_simbolo")
        if st.button("Conferir sequência", key="btn_seq_simbolo"):
            st.success("Muito bem! A sequência continua com 🌙" if seq == "🌙" else "Observe o padrão e tente de novo.")


with tabs[5]:
    st.header("📚 Histórias para dormir")

    stories = {
        "🌙 Luna e a Lua que Sussurrava":
        """Numa noite muito calma, Luna percebeu que a lua brilhava mais perto da janela.
        Quando abriu seu livro mágico, uma voz suave chamou seu nome.
        Luna e o coelhinho seguiram um caminho de estrelas até um jardim silencioso.
        Lá, a lua contou que algumas estrelas estavam com medo do escuro.
        Luna segurou o livro junto ao coração e uma luz dourada iluminou o céu.
        As estrelas voltaram a brilhar e, pouco a pouco, todo o jardim adormeceu.
        Luna voltou para casa, abraçou o coelhinho e fechou os olhos enquanto a lua vigiava a janela.""",

        "🐰 Luna e o Sonho do Coelhinho":
        """O coelhinho de Luna não conseguia dormir. Ele dizia ter perdido um sonho bonito.
        Luna abriu o livro mágico e os dois chegaram a uma floresta coberta por nuvens macias.
        Cada nuvem guardava um sonho diferente.
        Depois de procurar com cuidado, encontraram uma pequena nuvem em forma de cenoura.
        O coelhinho sorriu e reconheceu seu sonho.
        De volta ao quarto, ele se aconchegou perto de Luna e logo adormeceu.""",

        "🏰 Luna e o Castelo Silencioso":
        """Luna chegou ao castelo numa noite em que todos os sinos estavam quietos.
        A princesa explicou que o castelo só voltaria a cantar quando alguém encontrasse a melodia escondida.
        Luna e o coelhinho seguiram pequenas notas douradas pelos corredores.
        No alto da torre, encontraram uma caixinha de música.
        Quando Luna a abriu, uma melodia suave percorreu todo o castelo.
        As luzes se acenderam, os sinos tocaram baixinho e todos foram dormir em paz.""",

        "✨ Luna e o Jardim das Estrelas":
        """Luna e o coelhinho encontraram um jardim onde pequenas estrelas cresciam como flores.
        Algumas estavam apagando devagar.
        Uma borboleta de luz mostrou o caminho até uma fonte antiga.
        Luna abriu seu livro mágico e uma luz dourada tocou a água.
        A fonte voltou a brilhar e todas as estrelas-flor se acenderam.
        Antes de partir, uma estrela pousou por um instante sobre o livro de Luna e iluminou seu caminho de volta para casa."""
,

        "🌌 Luna e a Ponte de Nuvens":
        """Numa noite tranquila, Luna viu uma pequena ponte de nuvens aparecer diante da janela.
        Ela e o coelhinho atravessaram devagar e chegaram a um céu cheio de estrelas sonolentas.
        Cada estrela precisava encontrar seu lugar antes de dormir.
        Luna ajudou uma a uma, até que todo o céu ficou organizado e brilhante.
        Quando voltou para casa, o coelhinho já bocejava.
        Luna fechou o livro mágico e os dois adormeceram sob a luz suave da lua.""",

        "🕯️ Luna e a Luz do Castelo":
        """O castelo estava escuro e silencioso quando Luna chegou.
        A princesa contou que a pequena luz da torre havia desaparecido.
        Luna e o coelhinho subiram as escadas em silêncio.
        No alto, encontraram uma chama minúscula escondida dentro de uma lanterna.
        Luna aproximou o livro mágico e a luz cresceu devagar, iluminando todo o castelo.
        A princesa sorriu, o coelhinho se aconchegou e a noite ficou calma outra vez."""

    }

    choice = st.selectbox("Escolha uma história:", list(stories.keys()))
    st.markdown(f"### {choice}")
    st.write(stories[choice])

    st.markdown("#### 🔊 Narração")
    st.caption("Você pode ouvir com voz de narradora ou com uma voz mais infantil para a Luna.")

    modo_voz = st.radio(
        "Escolha a voz:",
        ["📖 Narradora suave", "🌙 Luna infantil"],
        horizontal=True,
        key="modo_voz_historia"
    )

    if modo_voz == "🌙 Luna infantil":
        narrar_texto(stories[choice], choice, perfil="luna")
    else:
        narrar_texto(stories[choice], choice, perfil="narradora")

    st.info(
        "A voz exata depende das vozes disponíveis no celular ou computador. "
        "O modo Luna usa tom mais agudo e um ritmo um pouco mais leve."
    )

with tabs[6]:
    st.header("📸 Fotos e vídeos da Luna")
    st.write("Aqui você pode enviar fotos e vídeos da Luna para ver dentro do app.")

    photos = st.file_uploader(
        "Enviar fotos",
        type=["png","jpg","jpeg","webp"],
        accept_multiple_files=True,
        key="photos"
    )
    if photos:
        st.subheader("🖼️ Fotos enviadas")
        cols = st.columns(2)
        for i, f in enumerate(photos):
            with cols[i % 2]:
                st.image(f, caption=f.name, use_container_width=True)

    videos = st.file_uploader(
        "Enviar vídeos",
        type=["mp4","mov","m4v","webm"],
        accept_multiple_files=True,
        key="videos"
    )
    if videos:
        st.subheader("🎬 Vídeos enviados")
        for v in videos:
            st.video(v)

    st.info(
        "Importante: no Streamlit gratuito, os arquivos enviados ficam disponíveis durante a sessão. "
        "Para guardar fotos e vídeos permanentemente, depois podemos conectar o app a um armazenamento como Google Drive ou outro serviço."
    )

st.divider()
st.caption("Mundo da Luna • App educativo e de atividades")
