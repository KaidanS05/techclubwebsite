import streamlit as st

st.title("Page 4")
st.write("This is the content of page 4.")
display_Private_View = st.write("Hopefully only authorized users are seeing this.")

AUTHORIZED_USERS = {
    'test@email.com',
    'kstiles2005@gmail.com',
}

if st.experimental_user.email in AUTHORIZED_USERS:
    display_Private_View()