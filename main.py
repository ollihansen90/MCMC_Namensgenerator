import streamlit as st
import random

from utils import MCMC, load_data

st.title("Namensgenerator")

st.subheader("MCMC")
st.write("Dieser Namensgenerator basiert auf einem Markov-Chain-Monte-Carlo-Algorithmus. Dieser Algorithmus generiert neue Namen, indem er die Wahrscheinlichkeiten von Buchstabenkombinationen in einem vorgegebenen Datensatz analysiert und daraus neue Namen generiert. In diesem Fall wurde der Algorithmus auf unterschiedlicher Universen (z.B. Harry Potter oder Herr der Ringe) trainiert.")
st.html("""Unseren Code finden wir bei Colab: (Musterlösung) <a href="https://colab.research.google.com/github/ollihansen90/Mathe-SH/blob/main/MCMC_Namensgenerator_MatheSH.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" rel="noopener noreferrer"/></a>""")

st.markdown("### Wähle Hyperparameter:")
dataset = st.selectbox("Datensatz", ["Harry Potter", "Herr der Ringe", "Star Wars", "Marvel", "Deutsche Städte"], 0)
mapping = {"Harry Potter": "harrypotternames", "Herr der Ringe": "lotrnames", "Star Wars": "starwarsnames", "Marvel": "marvelnames", "Deutsche Städte": "staedtenamen"}
tlen = st.slider("Tokenlänge", 1, 10, 4)
seed = st.text_input("Seed", "0")
random.seed(seed)
#data = load_data("harrypotternames")
#data = load_data("lotrnames")
data = load_data(mapping[dataset])
#data = load_data("starwarsnames")
mcmc = MCMC(data, tlen)
namelist = []
for i in range(10):
    namelist.append(mcmc.generate())

st.markdown(f"""### Generierte Namen:
{"".join(["- "+name+"\n" for name in namelist])}""")
st.button("MEHR")