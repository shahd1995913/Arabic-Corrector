import streamlit as st
# Print colored text using Markdown syntax
st.markdown('<span style="color: green;">Arabic Word Correction Using Artificial Intelligence and Natural Language Processing 2023</span>', unsafe_allow_html=True)

# Styling functions for colored and bold text
def blue(text):
    return f'<span style="color: blue;">{text}</span>'

def green(text):
    return f'<span style="color: green;">{text}</span>'

# Set a title for the app
st.title('Arabic Word Correction')

# Get user input
text = st.text_input("الرجاء إدخال النص المراد تدقيقه")

# Perform replacements
text2 = text.replace("زرتو", "زرت")
text2 = text2.replace("درستو", "درست")
text2 = text2.replace("دائمن", "دائما")
text2 = text2.replace("الاستاذ", "الأستاذ")
text2 = text2.replace("مسائا", "مساءً")
text2 = text2.replace("هبه", "هبة")
text2 = text2.replace("دعى", "دعا")

# Display original and corrected text
st.markdown('**النص قبل التصحيح:** ' + blue(text), unsafe_allow_html=True)
st.markdown('**النص بعد التصحيح:** ' + green(text2), unsafe_allow_html=True)
