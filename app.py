import json
import os
import streamlit as st

FILE = "counts.json"
PEOPLE = ["Sara", "Albert", "Robert"]


def load_counts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {name: 0 for name in PEOPLE}


def save_counts(counts):
    with open(FILE, "w") as f:
        json.dump(counts, f, indent=4)


st.title("🍺 Beer Trip Counter")

counts = load_counts()

for name in PEOPLE:
    counts.setdefault(name, 0)

cols = st.columns(len(PEOPLE))

for col, name in zip(cols, PEOPLE):
    with col:
        st.subheader(name)
        st.metric("Beers", counts[name])

        if st.button(f"+1 🍺", key=f"plus_{name}"):
            counts[name] += 1
            save_counts(counts)
            st.rerun()

        if st.button(f"-1 🤮", key=f"minus_{name}"):
            counts[name] = max(0, counts[name] - 1)
            save_counts(counts)
            st.rerun()

st.divider()

if st.button("Reset all"):
    counts = {name: 0 for name in PEOPLE}
    save_counts(counts)
    st.rerun()

st.subheader("Current JSON")
st.json(counts)