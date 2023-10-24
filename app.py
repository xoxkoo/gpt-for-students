import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Sidebar contents
with st.sidebar:
    st.title("🔥 LLM Chat App")
    st.markdown(
        """
                    ##About
                    This app is an LLM-powered chatbot
                    """
    )
    add_vertical_space(5)
    st.write("Made by Frajer 🦍")


def main():
    st.header("Chat with PDF 🗯")

    #upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')


if __name__ == "__main__":
    main()
