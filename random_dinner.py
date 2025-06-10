import random
import streamlit as st

st.title("Chicago Dinner Picker")

italian_place = ["Alla Vita", "Quartino Ristorante", "OLIO E PIU", "Gibson Italia", "Ciccio Mio", "The Village", "Sapori Trattoria", "Coda di Volpe"]
american_place = ["The Dearborn", "The Gage", "Girl & The Goat", "RPM Steak", "Maple & Ash", "The Smith", "Beatrix", "Bub City", "Butcher and the Bear"]
mexican_place = ["Frontera Grill", "Xoco", "Cemitas Puebla", "La Vaca Margarita Bar", "Mercadito", "El Cid", "Salpicon", "Carnitas Uruapan"]
thai_place = ["Siam Noodle & Rice", "Tac Quick", "Herb", "Yes Thai", "Sticky Rice", "Opart Thai House", "Noodles in the Pot", "Thai Pastry"]
chinese_place = ["MingHin Cuisine", "Duck Duck Goat", "Golden Bull Restaurant", "Little Wok", "Qung Xiang Yuan Dumplings", "Chi Cafe"]
indian_place = ["Indian House", "Indian Graden", "ROOP", "Dhanteraz Indian Fusion", "Kama"]
dealers_choice = italian_place + american_place + mexican_place + thai_place + chinese_place + indian_place

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
    cuisine = st.selectbox("What do you want to eat?", ["Italian", "American", "Mexican", "Thai", "Chinese", "Indian"], key="cuisine_yes")
    if st.session_state.food_choice != cuisine:
        st.session_state.food_choice = cuisine
        st.session_state.options = []
        st.session_state.suggestion = None
    if not st.session_state.options:
        if cuisine == "Italian":
            st.session_state.options = italian_place.copy()
        elif cuisine == "American":
            st.session_state.options = american_place.copy()
        elif cuisine == "Mexican":
            st.session_state.options = mexican_place.copy()
        elif cuisine == "Thai":
            st.session_state.options = thai_place.copy()
        elif cuisine == "Chinese":
            st.session_state.options = chinese_place.copy()
        elif cuisine == "Indian":
            st.session_state.options = indian_place.copy()
    if st.button("Suggest a place!", key=f"suggest_{cuisine}"):
        if st.session_state.options:
            st.session_state.suggestion = random.choice(st.session_state.options)
        else:
            st.session_state.suggestion = None
    if st.session_state.suggestion:
        st.write(f"How about {st.session_state.suggestion}?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("I'm satisfied!", key=f"satisfied_{cuisine}"):
                st.success(f"Great! Enjoy your {cuisine} at {st.session_state.suggestion}!")
                st.session_state.suggestion = None
                st.session_state.options = []
        with col2:
            if st.button("Suggest another", key=f"suggest_another_{cuisine}"):
                if st.session_state.suggestion is not None:
                    st.session_state.options.remove(st.session_state.suggestion)
                if st.session_state.options:
                    st.session_state.suggestion = random.choice(st.session_state.options)
                else:
                    st.warning("No more options left for this cuisine.")
                    st.session_state.suggestion = None
elif answer == "No":
    cuisine = st.selectbox("What type of food do you want?", ["Italian", "American", "Mexican", "Thai", "Chinese", "Indian"], key="cuisine_no")
    if st.session_state.food_choice != cuisine:
        st.session_state.food_choice = cuisine
        st.session_state.options = []
        st.session_state.suggestion = None
    if not st.session_state.options:
        if cuisine == "Italian":
            st.session_state.options = italian_place.copy()
        elif cuisine == "American":
            st.session_state.options = american_place.copy()
        elif cuisine == "Mexican":
            st.session_state.options = mexican_place.copy()
        elif cuisine == "Thai":
            st.session_state.options = thai_place.copy()
        elif cuisine == "Chinese":
            st.session_state.options = chinese_place.copy()
        elif cuisine == "Indian":
            st.session_state.options = indian_place.copy()
    if st.button("Suggest a place!", key=f"suggest_{cuisine}"):
        if st.session_state.options:
            st.session_state.suggestion = random.choice(st.session_state.options)
        else:
            st.session_state.suggestion = None
    if st.session_state.suggestion:
        st.write(f"How about {st.session_state.suggestion}?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("I'm satisfied!", key=f"satisfied_{cuisine}"):
                st.success(f"Great! Enjoy your {cuisine} at {st.session_state.suggestion}!")
                st.session_state.suggestion = None
                st.session_state.options = []
        with col2:
            if st.button("Suggest another", key=f"suggest_another_{cuisine}"):
                if st.session_state.suggestion is not None:
                    st.session_state.options.remove(st.session_state.suggestion)
                if st.session_state.options:
                    st.session_state.suggestion = random.choice(st.session_state.options)
                else:
                    st.warning("No more options left for this cuisine.")
                    st.session_state.suggestion = None
elif answer == "Dealer's Choice":
    if st.session_state.food_choice != "Dealer's Choice":
        st.session_state.options = dealers_choice.copy()
        st.session_state.suggestion = None
        st.session_state.food_choice = "Dealer's Choice"
    st.write(f"Options left: {len(st.session_state.options)}")
    if st.button("Suggest a place!"):
        if st.session_state.options:
            st.session_state.suggestion = random.choice(st.session_state.options)
    if st.session_state.suggestion:
        st.write(f"How about {st.session_state.suggestion} for dinner?")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("I'm satisfied!", key="satisfied_dealer"):
                st.success(f"Great! Enjoy your dinner at {st.session_state.suggestion}!")
                st.session_state.suggestion = None
                st.session_state.options = []
        with col2:
            if st.button("Suggest another", key="suggest_another_dealer"):
                if st.session_state.suggestion is not None:
                    st.session_state.options.remove(st.session_state.suggestion)
                if st.session_state.options:
                    st.session_state.suggestion = random.choice(st.session_state.options)
                else:
                    st.warning("No more options left for dealer's choice.")
                    st.session_state.suggestion = None
        with col3:
            if st.button("Start Over", key="reset_dealer"):
                st.session_state.options = dealers_choice.copy()
                st.session_state.suggestion = None

