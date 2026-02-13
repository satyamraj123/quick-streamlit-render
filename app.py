import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Lisa ❤️", page_icon="💖", layout="centered")

# Hide Streamlit menu/footer
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    overflow: hidden;
    text-align: center;
    font-family: 'Courier New', monospace;
    color: white;
}

h1 {
    font-size: 60px;
    margin-top: 80px;
    animation: fadeIn 3s ease-in-out;
}

.typing {
    font-size: 28px;
    margin-top: 20px;
    border-right: .15em solid white;
    white-space: nowrap;
    overflow: hidden;
    width: 0;
    animation: typing 5s steps(40, end) forwards, blink .75s step-end infinite;
}

@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

@keyframes blink {
    from, to { border-color: transparent }
    50% { border-color: white }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.heart {
    position: absolute;
    color: red;
    font-size: 24px;
    animation: float 6s linear infinite;
}

@keyframes float {
    0% { transform: translateY(100vh) scale(1); opacity: 1; }
    100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
}

.signature {
    position: fixed;
    bottom: 10px;
    right: 15px;
    font-size: 12px;
    opacity: 0.6;
}
</style>
</head>
<body>

<h1>To Lisa 💖</h1>
<div class="typing">You make my world brighter every single day ✨</div>

<div class="signature">— satyam</div>

<script>
function createHeart() {
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (Math.random() * 20 + 15) + "px";
    heart.style.animationDuration = (Math.random() * 3 + 3) + "s";
    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 6000);
}

setInterval(createHeart, 300);
</script>

</body>
</html>
"""

components.html(html_code, height=700)
