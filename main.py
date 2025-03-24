import streamlit as st
import random

st.title("Namensgenerator")

st.markdown(f"""Hier ist eine Liste:
- {random.choice(["Peter", "Paul", "Mary"])}
- {random.choice(["Peter", "Paul", "Mary"])}
- {random.choice(["Peter", "Paul", "Mary"])}""")