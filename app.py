import streamlit as st
# Print colored text using Markdown syntax
st.markdown('<span style="color: blue;">Arabic Word Correction Using Artificial Intelligence and Natural Language Processing 2023</span>', unsafe_allow_html=True)
# st.markdown('<span style="color: blue;">Shahed Al-khateeb</span>', unsafe_allow_html=True)

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
text2 = text2.replace("احتماليه", "احْتِمَالِيَّة")
text2 = text2.replace("معاني", "معانٍ")
text2 = text2.replace("أسباب", "سببٌ")
text2 = text2.replace("انكليزي", "إنجليزي")
text2 = text2.replace("عائشه", "عائشة")
text2 = text2.replace("بدون", "دون")
text2 = text2.replace("مواضيع", "موضوعات")
text2 = text2.replace("مشاريع", "مشروعات")
text2 = text2.replace("سنعملُ سويًّا", "سنعملُ معًا")
text2 = text2.replace("تمَّ إقامة", "أُقيم")
text2 = text2.replace("دائمن", "دائمًا")
text2 = text2.replace("روايه", "رواية")
text2 = text2.replace("أحسنتي", "أحسنتِ")
text2 = text2.replace("إمتحان", "امتحان")
text2 = text2.replace("قرأتو", "قرأته")
text2 = text2.replace("هاذا", "هذا")
text2 = text2.replace("أدعوا", "أدعو")
text2 = text2.replace("الاستاذ", "الأستاذ")
text2 = text2.replace("نأخد", "نأخذ")
text2 = text2.replace("مسائا", "مساءً")

# Display original and corrected text
st.markdown('**النص قبل التصحيح:** ' + blue(text), unsafe_allow_html=True)
st.markdown('**النص بعد التصحيح:** ' + green(text2), unsafe_allow_html=True)
