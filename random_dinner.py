import random
import streamlit as st
import pandas as pd

st.title("Chicago Dinner Picker")

df = pd.read_csv("dataset.csv")
cuisines = sorted(df['cuisine'].unique())

if 'step' not in st.session_state:
    st.session_state.step = 0
if 'options' not in st.session_state:
    st.session_state.options = []
if 'suggestion' not in st.session_state:
    st.session_state.suggestion = None
if 'food_choice' not in st.session_state:
    st.session_state.food_choice = ''

choices = ["Yes", "No", "Dealer's Choice"]
answer = st.selectbox("Do you know what you want to eat?", choices, key="main_choice")

if answer == "Yes":
    cuisine = st.selectbox("What do you want to eat?", cuisines, key="cuisine_yes")
    if st.session_state.food_choice != cuisine:
        st.session_state.food_choice = cuisine
        st.session_state.options = []
        st.session_state.suggestion = None
    if not st.session_state.options:
        st.session_state.options = df[df['cuisine'] == cuisine].index.tolist()
    if st.button("Suggest a place!", key=f"suggest_{cuisine}"):
        if st.session_state.options:
            idx = random.choice(st.session_state.options)
            st.session_state.suggestion = idx
        else:
            st.session_state.suggestion = None
    if st.session_state.suggestion is not None:
        row = df.loc[st.session_state.suggestion]
        st.write(f"How about {row['name']}?")
        st.write(f"Location: {row['location']}")
        st.write(f"Hours: {row['hours']}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("I'm satisfied!", key=f"satisfied_{cuisine}"):
                st.success(f"Great! Enjoy your {cuisine} at {row['name']}!")
                st.session_state.suggestion = None
                st.session_state.options = []
        with col2:
            if st.button("Suggest another", key=f"suggest_another_{cuisine}"):
                if st.session_state.suggestion is not None:
                    st.session_state.options.remove(st.session_state.suggestion)
                if st.session_state.options:
                    idx = random.choice(st.session_state.options)
                    st.session_state.suggestion = idx
                else:
                    st.warning("No more options left for this cuisine.")
                    st.session_state.suggestion = None
elif answer == "No":
    cuisine = st.selectbox("What type of food do you want?", cuisines, key="cuisine_no")
    if st.session_state.food_choice != cuisine:
        st.session_state.food_choice = cuisine
        st.session_state.options = []
        st.session_state.suggestion = None
    if not st.session_state.options:
        st.session_state.options = df[df['cuisine'] == cuisine].index.tolist()
    if st.button("Suggest a place!", key=f"suggest_{cuisine}"):
        if st.session_state.options:
            idx = random.choice(st.session_state.options)
            st.session_state.suggestion = idx
        else:
            st.session_state.suggestion = None
    if st.session_state.suggestion is not None:
        row = df.loc[st.session_state.suggestion]
        st.write(f"How about {row['name']}?")
        st.write(f"Location: {row['location']}")
        st.write(f"Hours: {row['hours']}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("I'm satisfied!", key=f"satisfied_{cuisine}"):
                st.success(f"Great! Enjoy your {cuisine} at {row['name']}!")
                st.session_state.suggestion = None
                st.session_state.options = []
        with col2:
            if st.button("Suggest another", key=f"suggest_another_{cuisine}"):
                if st.session_state.suggestion is not None:
                    st.session_state.options.remove(st.session_state.suggestion)
                if st.session_state.options:
                    idx = random.choice(st.session_state.options)
                    st.session_state.suggestion = idx
                else:
                    st.warning("No more options left for this cuisine.")
                    st.session_state.suggestion = None
elif answer == "Dealer's Choice":
    if st.session_state.food_choice != "Dealer's Choice":
        st.session_state.options = df.index.tolist()
        st.session_state.suggestion = None
        st.session_state.food_choice = "Dealer's Choice"
    st.write(f"Options left: {len(st.session_state.options)}")
    if st.button("Suggest a place!"):
        if st.session_state.options:
            idx = random.choice(st.session_state.options)
            st.session_state.suggestion = idx
    if st.session_state.suggestion is not None:
        row = df.loc[st.session_state.suggestion]
        st.write(f"How about {row['name']} for dinner?")
        st.write(f"Location: {row['location']}")
        st.write(f"Hours: {row['hours']}")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("I'm satisfied!", key="satisfied_dealer"):
                st.success(f"Great! Enjoy your dinner at {row['name']}!")
                st.session_state.suggestion = None
                st.session_state.options = []
        with col2:
            if st.button("Suggest another", key="suggest_another_dealer"):
                if st.session_state.suggestion is not None:
                    st.session_state.options.remove(st.session_state.suggestion)
                if st.session_state.options:
                    idx = random.choice(st.session_state.options)
                    st.session_state.suggestion = idx
                else:
                    st.warning("No more options left for dealer's choice.")
                    st.session_state.suggestion = None
        with col3:
            if st.button("Start Over", key="reset_dealer"):
                st.session_state.options = df.index.tolist()
                st.session_state.suggestion = None

