import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="For Lisa ❤️", page_icon="💖", layout="centered")

# Hide Streamlit UI
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# Convert image to base64
def get_base64(img_file):
    with open(img_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64("5300938775661843669_1.jpg")  # Change name if needed

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    overflow: hidden;
    font-family: 'Courier New', monospace;
    text-align: center;
    color: white;
}}

h1 {{
    margin-top: 40px;
    font-size: 50px;
}}

.center-img {{
    margin-top: 40px;
    width: 300px;
    height: auto;
    border-radius: 20px;
    box-shadow: 0 0 40px rgba(255,255,255,0.8);
    animation: fadeIn 3s ease-in-out;
}}

@keyframes fadeIn {{
    from {{ opacity: 0; }}
    to {{ opacity: 1; }}
}}

.heart {{
    position: fixed;
    bottom: -10px;
    color: red;
    font-size: 24px;
    animation: floatUp linear infinite;
}}

@keyframes floatUp {{
    0% {{
        transform: translateY(0) scale(1);
        opacity: 1;
    }}
    100% {{
        transform: translateY(-110vh) scale(1.5);
        opacity: 0;
    }}
}}

.signature {{
    position: fixed;
    bottom: 10px;
    right: 15px;
    font-size: 12px;
    opacity: 0.6;
}}
</style>
</head>
<body>

<h1>Happy Valentine's Day\nTo Lisa 💖</h1>

<img src="data:image/jpg;base64,{img_base64}" class="center-img"/>

<p style="font-size:22px; margin-top:20px;">
You make my world brighter every single day ✨
</p>

<div class="signature">— satyam</div>

<script>
function createHeart() {{
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (Math.random() * 20 + 15) + "px";
    heart.style.animationDuration = (Math.random() * 3 + 4) + "s";
    document.body.appendChild(heart);

    setTimeout(() => {{
        heart.remove();
    }}, 7000);
}}

setInterval(createHeart, 300);
</script>

</body>
</html>
"""

components.html(html_code, height=800)
