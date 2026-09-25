import streamlit as st
from pathlib import Path
from PIL import Image
import io, random

st.set_page_config(page_title="Mundo da Luna", page_icon="🌙", layout="wide")
ASSETS = Path(__file__).parent / "assets"

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg,#150a2f 0%,#2d1457 55%,#4a2675 100%);
    color: white;
}
h1,h2,h3 { color:#ffd86b !important; }
.luna-card {
    padding: 14px 16px;
    border-radius: 18px;
    background: rgba(255,255,255,.08);
    margin: 10px 0 16px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("🌙 Mundo da Luna")
st.subheader("Atividades escolares, desenhos para colorir, histórias e mídia da Luna")

tabs = st.tabs([
    "🏠 Início",
    "✏️ Alfabetização",
    "🔢 Matemática",
    "🌍 Conhecimentos",
    "🎨 Colorir",
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

with tabs[3]:
    st.header("🌍 Conhecimentos")
    q1 = st.radio("Qual aparece no céu à noite?", ["Lua", "Árvore", "Livro"], key="c1")
    q2 = st.radio("Qual animal acompanha Luna?", ["Coelho", "Peixe", "Leão"], key="c2")
    q3 = st.radio("Onde encontramos livros?", ["Biblioteca", "Piscina", "Garagem"], key="c3")
    if st.button("Corrigir conhecimentos"):
        score = int(q1=="Lua") + int(q2=="Coelho") + int(q3=="Biblioteca")
        st.success(f"Você acertou {score} de 3! 🌟")

with tabs[4]:
    st.header("🎨 Desenhos para colorir")
    st.write("Escolha um desenho, abra e salve para imprimir ou colorir.")
    coloring = [
        ("Luna e o Livro Mágico","colorir_livro.png"),
        ("Luna e o Portal Mágico","colorir_portal.png"),
        ("Luna e o Mapa Estelar","colorir_mapa.png"),
        ("Luna no Jardim Lunar","colorir_jardim.png"),
        ("Luna na Varanda Encantada","colorir_varanda.png"),
    ]
    for title, fn in coloring:
        p = ASSETS/fn
        if p.exists():
            st.subheader(title)
            st.image(str(p), use_container_width=True)
            data = p.read_bytes()
            st.download_button(
                f"⬇️ Baixar {title}",
                data=data,
                file_name=fn,
                mime="image/png",
                key=f"down_{fn}"
            )

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
    }

    choice = st.selectbox("Escolha uma história:", list(stories.keys()))
    st.markdown(f"### {choice}")
    st.write(stories[choice])

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
