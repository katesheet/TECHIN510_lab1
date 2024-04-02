import streamlit as st

st.title("Hi, my name is Kate")


col1, col2 = st.columns(2)

with col1:
   st.header("My cat")
   st.image("image/catcat.jpg")

with col2:
   st.header("My car")
   st.image("image/carcar.jpg")


multi = '''
## About
- My name is Kate, an aspiring product manager.
## Education
- Psychology and Computer Science
## Work Experience
- Big techs
- Venture capital
- Consulting

## Hobbies
- Photography
- Bodybuilding
- Being angry about code

## Interesting facts
- Here's my cute cate &mdash;\
            :cat::cat::cat:

'''
st.markdown(multi)