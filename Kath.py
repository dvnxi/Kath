import streamlit as st

st.set_page_config(layout="wide")

# Sidebar sections
st.sidebar.title("Menu")
section = st.sidebar.radio("Go to:", ["To Kath", "🌸", "Sorry, my baby"])

# Letter for Kath
if section == "To Kath":

    st.markdown("""
<p style='color:#FFC0CB; font-style: italic; text-align: left; font-family: "Times New Roman", serif; font-size: 22px;'>
My dearest Kath,
</p>

<div style='color:#FFFFFF; text-align: left; font-family: "Times New Roman", serif; font-size: 18px; line-height: 1.5;'>
I just want to take this moment to tell you how much I love you.<br>
I hope you know how much you mean to me.<br>
You're not just my love, you're my safe place, my joy, my inspiration,<br>
and the most beautiful blessing God has given me.<br><br>

I want you to know that my patience for you will never run out (although you always worry that it might ehe).<br>
No matter what comes our way, I will always stand by your side,<br>
through your light and through your darkness. Kakampi mo ako palagi.<br>
I love all that you were, all that you are, and all that you will become (you always hear me say this).<br>
There is nothing in this world that could change the way I see you.<br>
You will always be my prettiest and cutest baby girl, mwehehe.<br><br>

I'm so glad that you came into my life so unexpectedly.<br>
You've filled my days with warmth, laughter, and meaning.<br>
You've shown me a kind of love that feels both comforting and exciting,<br>
like feeling at home and dreaming big at the same time.<br><br>

Please remember, my baby girl, that my love for you is endless.<br>
I will hold your hand through every storm, celebrate every victory with you,<br>
and remind you every day just how precious you are to me.<br>
You don't have to be perfect, because for me, you already are.<br><br>

Thank you for being with me, for loving me back, and for simply being you.<br>
I'll spend the rest of my days cherishing you, protecting you,<br>
and loving you with everything I have.<br><br>

With all my heart,<br>
Devon
</div>
""", unsafe_allow_html=True)



elif section == "🌸":
    col1, col2 = st.columns([6, 8])  # 2:1 ratio for ASCII vs GIF

    with col1:
        st.text("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠻⠟⢉⠙⢿⠉⡌⢻⡿⢿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⠻⢿⣿⣿⣿⣿⣿⣿⡏⢀⣷⣄⠀⢿⣧⡀⠀⠇⠀⡠⠀⣿⣿⣿
⣿⣿⣿⣿⠇⢀⣦⡀⠙⢿⣿⣿⣿⠿⠀⠈⣉⡉⠂⠈⢿⣧⠴⢀⡜⠁⣈⣡⠈⢹
⣿⣿⣿⣿⡂⢸⣿⣿⣦⡀⣉⣠⣤⣴⣾⣧⣈⠙⠓⠢⡜⢠⣦⡄⠰⠞⠋⠡⣴⣿
⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⠏⢁⣤⣤⣴⠖⢁⡀⠙⢁⠼⣶⣶⣦⠀⣿
⣿⣿⣿⣿⡇⠘⣿⡿⠛⠛⠛⢿⡿⠋⠁⠀⠉⠉⡁⢀⣾⠋⠹⣷⠀⢠⣈⣤⣶⣿
⣿⣿⣿⣿⣧⠀⠃⡄⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠁⠾⠋⠀⠀⢿⡇⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡀⠸⣇⠀⠀⠀⠀⠀⠐⣄⣀⢀⣴⠗⢀⣠⣴⣦⣤⡄⠈⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠙⣷⣦⣴⡞⠀⣄⠈⠛⠿⠁⢰⣿⡿⠿⣿⣿⣿⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣦⣀⠉⠛⠁⠚⠛⠛⠂⣠⡦⠀⣠⣤⣴⣿⣿⣿⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣰⣶⣶⣶⣿⣿⣿⡁⠸⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⢀⣼⣿⣿⣿⣿⣿⣿⣿⣧⠀⢹⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠁⣠⠿⠋⣁⠈⣿⣿⣿⣿⣿⣿⡇⠰⠿⠿⠛⠉⢠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠁⠔⠁⣴⣿⠏⠀⣿⣿⣿⠿⢻⣿⣷⡄⢰⣶⣾⣧⡀⠹⣿⣿⣿⣿
⡿⠟⠉⠛⠿⠦⠴⠞⠛⢁⠀⢸⣿⣿⠋⢠⠀⢻⣿⡇⢸⣿⣿⣿⣿⣾⣿⣿⣿⣿
⠀⠰⣿⣶⣶⣶⣶⠶⠛⡁⠀⣾⣿⡟⠀⣾⡆⠘⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⣄⡈⢉⣉⣁⣤⣴⣾⡇⠠⣿⣿⠁⣸⣿⣿⡀⠘⠋⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠻⠇⢀⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)

    with col2:
        st.image("love.gif", use_container_width= True)  # file should be inside your kath folder
        
elif section == "Sorry, my baby":
    heart_ascii = """⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣦⣀⣴⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠛⣻⣿⠛⣿⣟⠛
⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⡏ ⠀⢹⣿⣷⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟ ⠀⠀⠀⢻⡀"""

    bottom_ascii = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣷⣦⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⠞⠿⣿⣿⣿⣿⣿⣿⣿⡿⣤⡀⠀⠀⠀
⠀⠀⣠⠶⠋⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠙⠳⣤⡀
⢀⡞⠀⢀⡶⠃⠀⠦⠀⠀⢀⣀⠀⠀⢠⡄⠀⣄⠀⠀⠙
⠘⣇⠀⣼⠁⠀⠀⠀⠀⢖⡬⢧⣰⠀⠀⠀⠀⢻⡀⠀⠀
⠀⠈⠛⡿⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄⡀⠀⠀⢻⡦⠤⠾
⠀⠀⣴⣿⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠙⠲⠀⠈⣧⠀⡀
⠀⣸⣃⡏⠀⠀⠀⠀⠀⠀⠀⠙⠶⣤⡀⠀⠀⠀⢹⡾⠙
⢰⠏⢹⡇⠀⡴⠖⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣠
⠸⣇⠈⠃⢸⡇⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀
⠀⠙⠶⠾⢧⣀⠀⢀⣀⡀⠀⠀⣀⣀⣀⣠⡤⠶⠋⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀"""

    # Top row: hearts closer
    top_cols = st.columns([1, 4, 1])
    top_cols[0].markdown(f"<pre style='font-size:12px; line-height:1'>{heart_ascii}</pre>", unsafe_allow_html=True)
    top_cols[2].markdown(f"<pre style='font-size:12px; line-height:1; text-align:right'>{heart_ascii}</pre>", unsafe_allow_html=True)

    # Middle row: smaller GIF
    mid_cols = st.columns([1, 4, 1])
    with mid_cols[1]:
        st.image("love.gif", width=200)  # smaller width for mobile

    # Bottom row: compact ASCII bottom-right
    bottom_cols = st.columns([1, 4, 1])
    bottom_cols[2].markdown(f"<pre style='font-size:11px; line-height:1; text-align:right'>{bottom_ascii}</pre>", unsafe_allow_html=True)
