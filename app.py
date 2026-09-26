
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from PIL import Image
import io, random, json

st.set_page_config(page_title="Mundo da Luna", page_icon="🌙", layout="wide")

ASSETS = Path(__file__).parent / "assets"


def narrar_texto(texto, titulo, perfil="narradora"):
    """Mostra botões para ouvir/parar a história usando a voz do navegador."""
    texto_js = json.dumps(str(texto), ensure_ascii=False)
    titulo_js = json.dumps(str(titulo), ensure_ascii=False)
    perfil_js = json.dumps(str(perfil), ensure_ascii=False)

    html = f"""
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 10px 0;">
      <button id="playVoice" style="
          flex:1;min-width:150px;padding:12px 16px;border:0;border-radius:14px;
          background:#d8b4ff;color:#2a1046;font-weight:800;font-size:16px;">
          ▶️ Ouvir história
      </button>
      <button id="stopVoice" style="
          flex:1;min-width:120px;padding:12px 16px;border:0;border-radius:14px;
          background:#f3e8ff;color:#2a1046;font-weight:800;font-size:16px;">
          ⏹️ Parar
      </button>
    </div>
    <script>
    const storyText = {texto_js};
    const storyTitle = {titulo_js};
    const profile = {perfil_js};

    function escolherVoz() {{
      const voices = window.speechSynthesis.getVoices() || [];
      const ptbr = voices.filter(v => (v.lang || "").toLowerCase().startsWith("pt-br"));
      const pt = voices.filter(v => (v.lang || "").toLowerCase().startsWith("pt"));
      const pool = ptbr.length ? ptbr : (pt.length ? pt : voices);

      if (!pool.length) return null;

      if (profile === "luna") {{
        const preferred = pool.find(v =>
          /female|femin|luciana|leticia|maria|vitoria|brasil/i.test((v.name || "") + " " + (v.voiceURI || ""))
        );
        return preferred || pool[0];
      }}
      return pool[0];
    }}

    document.getElementById("playVoice").onclick = function() {{
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(storyText);
      u.lang = "pt-BR";
      u.rate = profile === "luna" ? 0.95 : 0.88;
      u.pitch = profile === "luna" ? 1.35 : 1.0;
      const voice = escolherVoz();
      if (voice) u.voice = voice;
      window.speechSynthesis.speak(u);
    }};

    document.getElementById("stopVoice").onclick = function() {{
      window.speechSynthesis.cancel();
    }};
    </script>
    """
    components.html(html, height=95)

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

<style>
.top-space{height:75px;}
@media(max-width:700px){.top-space{height:90px;}}
.hero-wrap img{border-radius:26px;border:3px solid rgba(255,216,107,.9);box-shadow:0 12px 30px rgba(0,0,0,.28);}
</style>


<style>
.v20-banner{
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.22);
    padding: 12px 14px;
    border-radius: 16px;
    margin: 6px 0 14px 0;
    font-size: 0.98rem;
}
div.stButton > button, div.stDownloadButton > button {
    min-height: 44px;
    border-radius: 12px;
}
@media (max-width: 700px) {
    .block-container {
        padding-left: 0.85rem !important;
        padding-right: 0.85rem !important;
    }
    h1 { font-size: 2rem !important; }
    h2 { font-size: 1.45rem !important; }
    h3 { font-size: 1.15rem !important; }
    div[data-baseweb="select"] > div {
        min-height: 44px;
    }
}
</style>

""", unsafe_allow_html=True)


st.subheader("Atividades escolares, jogos, histórias e mídia da Luna")
st.caption("✨ Tema lilás e roxo, com leitura fácil no celular.")


st.markdown("""
<style>
:root{
  --luna-purple:#6f2dbd;
  --luna-deep:#35105d;
  --luna-pink:#f6b7ff;
  --luna-lilac:#efe4ff;
  --luna-gold:#ffd86b;
}
.stApp{
  background:
    radial-gradient(circle at 10% 10%, rgba(255,255,255,.14), transparent 22%),
    radial-gradient(circle at 85% 8%, rgba(255,225,120,.12), transparent 18%),
    linear-gradient(180deg,#3f1470 0%,#6d2aa6 44%,#8a4fd0 100%);
}
.block-container{
  max-width: 980px;
  padding-top: 1.2rem !important;
  padding-bottom: 6rem !important;
}
[data-testid="stHeader"]{
  background: rgba(45,8,77,.75);
  backdrop-filter: blur(8px);
}
h1,h2,h3,p,label,.stMarkdown,.stCaption{
  color:#fff !important;
}
.luna-hero{
  border-radius:28px;
  overflow:hidden;
  border:3px solid rgba(255,216,107,.9);
  box-shadow:0 14px 40px rgba(0,0,0,.35);
  margin-bottom:18px;
  background:rgba(255,255,255,.06);
}
.luna-hero img{
  width:100%;
  display:block;
}
.luna-tag{
  text-align:center;
  font-weight:800;
  font-size:1.05rem;
  background:linear-gradient(90deg,#f5c7ff,#fff1a6);
  color:#4a1a6d !important;
  padding:10px 14px;
  border-radius:18px;
  margin:10px 0 18px 0;
}
div.stButton > button{
  width:100%;
  min-height:72px;
  border-radius:22px !important;
  border:2px solid rgba(255,255,255,.55) !important;
  background:linear-gradient(145deg,#ffffff,#f2e3ff) !important;
  color:#4b1972 !important;
  font-weight:800 !important;
  font-size:1.02rem !important;
  box-shadow:0 7px 18px rgba(24,0,44,.2);
}
div.stButton > button:hover{
  transform:translateY(-1px);
  border-color:#ffd86b !important;
}
[data-testid="stTabs"] button{
  background:rgba(255,255,255,.14) !important;
  border-radius:16px !important;
  margin-right:6px !important;
  padding:8px 12px !important;
  color:white !important;
  font-weight:700 !important;
}
[data-testid="stTabs"] button[aria-selected="true"]{
  background:#f1dbff !important;
  color:#4b1972 !important;
}
[data-testid="stSelectbox"] > div > div,
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-baseweb="input"] input{
  background:#fff !important;
  color:#2d1244 !important;
  border-radius:14px !important;
}
[data-testid="stFileUploader"]{
  background:rgba(255,255,255,.10);
  border-radius:18px;
  padding:10px;
}
.luna-section{
  background:rgba(255,255,255,.10);
  border:1px solid rgba(255,255,255,.18);
  border-radius:22px;
  padding:14px 16px;
  margin:8px 0 16px;
}
@media(max-width:700px){
  .block-container{
    padding-left:.7rem !important;
    padding-right:.7rem !important;
    padding-top:.7rem !important;
  }
  .luna-hero{border-radius:22px}
  div.stButton > button{
    min-height:64px;
    font-size:.98rem !important;
  }
  [data-testid="stTabs"]{
    overflow-x:auto;
  }
  [data-testid="stTabs"] button{
    white-space:nowrap;
  }
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="top-space"></div>', unsafe_allow_html=True)
st.image(str(Path(__file__).parent / "assets" / "luna_capa.png"), use_container_width=True)
st.markdown(
    '<div class="luna-tag">✨ Jogos, atividades e histórias mágicas para aprender brincando ✨</div>',
    unsafe_allow_html=True
)

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

    st.markdown('<div class="luna-section"><h3>🌟 Explore o Mundo da Luna</h3><p>Escolha uma área nas abas acima para brincar, aprender ou ouvir uma história.</p></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.info("🎮 **Jogos**\n\nDesafios divertidos de letras, números, memória e lógica.")
        st.info("📚 **Histórias**\n\nContos mágicos da Luna e do coelhinho para ouvir e relaxar.")
    with col2:
        st.info("✏️ **Atividades**\n\nAlfabetização, matemática e conhecimentos.")
        st.info("📸 **Fotos e vídeos**\n\nUm espaço para a família visualizar mídias durante a sessão.")
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



    elif game == "🔠 Qual é a primeira letra?":
        palavra = st.radio("Qual letra começa a palavra **LUA**?", ["A", "L", "U"], key="g9")
        if st.button("Conferir", key="g9b"):
            if palavra == "L":
                st.success("Muito bem! LUA começa com L. 🌙")
            else:
                st.info("Tente outra vez. A palavra LUA começa com L.")

    elif game == "➕ Soma relâmpago":
        resposta = st.radio("Quanto é **3 + 2**?", ["4", "5", "6"], key="g10")
        if st.button("Conferir", key="g10b"):
            if resposta == "5":
                st.success("Acertou! 3 + 2 = 5. ⭐")
            else:
                st.info("Quase! Conte 3 estrelinhas e depois mais 2.")

    elif game == "🌈 Escolha a cor":
        resposta = st.radio("Qual destas é uma cor?", ["Azul", "Coelho", "Livro"], key="g11")
        if st.button("Conferir", key="g11b"):
            if resposta == "Azul":
                st.success("Isso! Azul é uma cor. 💙")
            else:
                st.info("Tente novamente. Azul é uma cor.")

    elif game == "🐾 Quem deixou a pegada?":
        resposta = st.radio("Quem pode deixar pegadinhas pequenas no jardim?", ["Coelhinho", "Castelo", "Lua"], key="g12")
        if st.button("Conferir", key="g12b"):
            if resposta == "Coelhinho":
                st.success("Muito bem! O coelhinho pode deixar pegadinhas. 🐰")
            else:
                st.info("Pense em quem anda pelo jardim com patinhas.")

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
st.markdown("""
<div class="luna-section" style="margin-top:24px;text-align:center;">
  <b>👨‍👩‍👧 Área para pais e responsáveis</b><br>
  <span style="font-size:.92rem;">Acompanhe a criança durante o uso e escolha as atividades adequadas à idade.</span>
</div>
""", unsafe_allow_html=True)
