import streamlit as st
import streamlit_card as sc


st.set_page_config("Displaying project", "📖", initial_sidebar_state="collapsed")
a = st.session_state["PROJECT_NAME"]
def styled_card():
    st.write(
        f"""
        <div class = "card">
        <div>
            <h3 style = ' display: flex;
                           justify-content: center;
                           align-items: center;
                           text-align: center;'><u>Project</u>
            </h3>
        </div>
            <p class = "p_card">{a}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Usage
styled_card()

st.columns(3)[1].write("\n\n\nThank you.")

st.warning("Please take screenshot of your project.")


with open('style.css') as f:
    st.markdown( f"<style>{f.read()}</style>", unsafe_allow_html = True)

