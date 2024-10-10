import streamlit as st

st.title("Contact Us!")
st.write("Contact Information.")

#contact bar
with st.container():
    st.write("---")
    st.header("Contact the Tech Club!")
    st.write("##")

    #From https://formsubmit.co/ ...
    contact_form = """
    <form action="https://formsubmit.co/techclub.testajiYh68@email.com" method="POST">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Type your comments here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty