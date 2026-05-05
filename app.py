import streamlit as st
from dotenv import load_dotenv
from ui.streamlit_ui import main

if __name__ == "__main__":
    load_dotenv()
    main()