import streamlit as st

def tools():
    st.title("Tools")

    st.header("Free Resources for Your Success")
    
    st.markdown("""
    At Computer Café, we care about your productivity! That's why we’ve gathered these free tools to help you stay organized and efficient. Whether you're working on documents, managing tasks, or collaborating with a team, these resources are here to help you succeed.
    """)
    
    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.image("./img/google/google docs.png", width=150)
    col1.markdown("""
        **Google Docs**<br>
        Create, edit, and collaborate on documents online for free.<br>
        [Open Google Docs](https://docs.google.com/)
    """, unsafe_allow_html=True)

    col2.image("./img/google/google sheets.png", width=150)
    col2.markdown("""
        **Google Sheets**<br>
        Manage and analyze data with free online spreadsheets.<br>
        [Open Google Sheets](https://sheets.google.com/)
    """, unsafe_allow_html=True)

    col3.image("./img/google/google slides.png", width=150)
    col3.markdown("""
        **Google Slides**<br>
        Design presentations and collaborate in real-time.<br>
        [Open Google Slides](https://slides.google.com/)
    """, unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    col4.image("./img/google/google calendar.png", width=150)
    col4.markdown("""
        **Google Calendar**<br>
        Keep track of events, appointments, and deadlines easily.<br>
        [Open Google Calendar](https://calendar.google.com/)
    """, unsafe_allow_html=True)

    col5.image("./img/google/google forms.png", width=150)
    col5.markdown("""
        **Google Forms**<br>
        Create surveys and collect data with free online forms.<br>
        [Open Google Forms](https://forms.google.com/)
    """, unsafe_allow_html=True)

    col6.image("./img/google/google keep.png", width=150)
    col6.markdown("""
        **Google Keep**<br>
        Take notes, create to-do lists, and organize your ideas.<br>
        [Open Google Keep](https://keep.google.com/)
    """, unsafe_allow_html=True)

    col7, col8, col9 = st.columns(3)

    col7.image("./img/google/google sites.png", width=150)
    col7.markdown("""
        **Google Sites**<br>
        Build and publish simple websites quickly for free.<br>
        [Open Google Sites](https://sites.google.com/)
    """, unsafe_allow_html=True)

    col8.image("./img/canva.png", width=150)
    col8.markdown("""
        **Canva**<br>
        Design anything from graphics to presentations using free templates.<br>
        [Open Canva](https://www.canva.com/)
    """, unsafe_allow_html=True)