import streamlit as st

    # --- ASCII art strings (keep exactly as-is so spacing is preserved) ---
heart_ascii = """⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣾⣿⣦⣀⣴⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠛⣻⣿⠛⣿⣟⠛
⠀⠀⠀⠀⠀⠀⠀⠀ ⢠⣾⣿⡏ ⠀⢹⣿⣷⡄
⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⡟ ⠀⠀⠀⢻⡀"""

bottom_ascii = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣤⠞⠿⣿⣿⣿⣿⣿⣿⣿⡿⣤⡀⠀⠀⠀⠀⠀
⠀⠀⣠⠶⠋⠉⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠙⠳⣤⡀⠀⠀
⢀⡞⠁⠀⢀⡶⠃⠀⠦⠀⠀⢀⣀⠀⠀⢠⡄⠀⣄⠀⠀⠙⢷⡄
⠘⣇⠀⠀⣼⠁⠀⠀⠀⠀⢖⡬⢧⣰⠀⠀⠀⠀⢻⡀⠀⠀⠀⣿
⠀⠈⠛⢛⡿⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄⡀⠀⠀⠀⢻⡦⠤⠾⠃
⠀⠀⣴⣿⠃⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠙⠲⠀⠀⠈⣧⠀⡀⠀
⠀⣸⣃⡏⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⣤⡀⠀⠀⠀⠀⢹⡾⠙⣆
⢰⠏⢹⡇⠀⡴⠖⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣠⠇
⠸⣇⠈⠃⢸⡇⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠀
⠀⠙⠲⠶⠾⢧⣀⠀⢀⣀⡀⠀⠀⣀⣀⣀⣀⣠⡤⠶⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

    # --- Top row: hearts on left and right, empty center ---
top_cols = st.columns([1, 6, 1])
top_cols[0].markdown(
        f"<div style='white-space:pre; font-family:monospace; font-size:14px'>{heart_ascii}</div>",
        unsafe_allow_html=True,
    )
    # center intentionally left empty to keep GIF centered in next block
top_cols[2].markdown(
        f"<div style='white-space:pre; font-family:monospace; font-size:14px; text-align:right'>{heart_ascii}</div>",
        unsafe_allow_html=True,
    )

    # small vertical spacing
st.markdown("<br>", unsafe_allow_html=True)

    # --- Middle row: centered GIF ---
mid_cols = st.columns([1, 1, 1])
with mid_cols[1]:
        # adjust path if your GIF is inside a subfolder (e.g. "kath/love.gif")
        st.image("love.gif", use_container_width=True)

    # a bit more spacing before the bottom ASCII
st.markdown("<br><br>", unsafe_allow_html=True)

    # --- Bottom row: big ASCII aligned to the right column ---
bottom_cols = st.columns([1, 1, 1])
bottom_cols[2].markdown(
        f"<div style='white-space:pre; font-family:monospace; font-size:12px; text-align:right'>{bottom_ascii}</div>",
        unsafe_allow_html=True,
    )
