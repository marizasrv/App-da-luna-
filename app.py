import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import random, io

st.set_page_config(page_title="Mundo da Luna", page_icon="🌙", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(180deg,#160b2f,#2d1457,#4b2478); color:white;}
h1,h2,h3 {color:#ffd86b !important;}
</style>
""", unsafe_allow_html=True)

st.title("🌙 Mundo da Luna")
st.subheader("Jogos, atividades e desenhos para colorir")

tabs = st.tabs(["🎨 Colorir", "🧠 Memória", "❓ Quiz", "🔎 Caça-palavras", "📚 História"])

with tabs[0]:
    st.header("🎨 Colorir")
    up = st.file_uploader("Envie um desenho da Luna em preto e branco", type=["png","jpg","jpeg"])
    if up:
        img = Image.open(up).convert("RGB")
        img.thumbnail((700,700))
        cor = st.color_picker("Cor do lápis", "#FF69B4")
        esp = st.slider("Espessura", 1, 30, 8)
        res = st_canvas(
            stroke_width=esp,
            stroke_color=cor,
            background_image=img,
            drawing_mode="freedraw",
            height=img.height,
            width=img.width,
            key="canvas"
        )
        if res.image_data is not None:
            painted = Image.fromarray(res.image_data.astype("uint8"))
            b = io.BytesIO()
            painted.save(b, format="PNG")
            st.download_button("💾 Baixar desenho", b.getvalue(), "desenho_luna.png", "image/png")
    else:
        st.info("Use desenhos da Luna, do coelhinho, do castelo e do livro mágico.")

with tabs[1]:
    st.header("🧠 Jogo da memória")
    pares = ["🌙","🐰","📖","🏰","⭐","🪄"]
    if "cards" not in st.session_state:
        cards = pares*2
        random.shuffle(cards)
        st.session_state.cards = cards
        st.session_state.matched = set()
        st.session_state.opened = []
    if st.button("🔄 Reiniciar"):
        cards = pares*2
        random.shuffle(cards)
        st.session_state.cards = cards
        st.session_state.matched = set()
        st.session_state.opened = []
        st.rerun()

    cols = st.columns(4)
    for i, card in enumerate(st.session_state.cards):
        with cols[i%4]:
            vis = i in st.session_state.matched or i in st.session_state.opened
            if st.button(card if vis else "❓", key=f"c{i}", use_container_width=True):
                if i not in st.session_state.matched and i not in st.session_state.opened:
                    st.session_state.opened.append(i)
                if len(st.session_state.opened) == 2:
                    a,b = st.session_state.opened
                    if st.session_state.cards[a] == st.session_state.cards[b]:
                        st.session_state.matched.update([a,b])
                    st.session_state.opened = []
                st.rerun()
    if len(st.session_state.matched) == 12:
        st.success("✨ Parabéns! Você encontrou todos os pares!")

with tabs[2]:
    st.header("❓ Quiz da Luna")
    qs = [
        ("Quem acompanha Luna?", ["Coelhinho","Gato","Dragão"], 0),
        ("Qual objeto é mágico?", ["Livro","Sapato","Chapéu"], 0),
        ("Onde fica o castelo?", ["Floresta encantada","Cidade","Praia"], 0),
    ]
    ans = []
    for i,(q,ops,c) in enumerate(qs):
        r = st.radio(q, ops, key=f"q{i}")
        ans.append((ops.index(r),c))
    if st.button("Ver resultado"):
        score = sum(1 for a,c in ans if a==c)
        st.success(f"Você acertou {score} de {len(qs)}! ⭐")

with tabs[3]:
    st.header("🔎 Caça-palavras")
    st.markdown("**LUNA • COELHO • LIVRO • LUA • CASTELO • ESTRELA**")
    grade = [
        "L U N A X E S T",
        "C O E L H O R E",
        "L I V R O A L A",
        "L U A M A G I C",
        "C A S T E L O X",
        "E S T R E L A S",
    ]
    st.code("\n".join(grade), language=None)

with tabs[4]:
    st.header("📚 História")
    st.write("Luna abriu seu livro mágico e uma luz dourada tomou conta do quarto. Em poucos segundos, ela e seu coelhinho chegaram a uma floresta encantada. Ao longe, um castelo brilhava sob a lua. E assim começou mais uma aventura no Mundo da Luna. 🌙✨")

st.divider()
st.caption("Mundo da Luna • App de jogos e atividades")
