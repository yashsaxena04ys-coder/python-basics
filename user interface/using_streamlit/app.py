import streamlit as st 

st.title('My Streamlit App')
st.subheader('My First WebApp using Python')
st.text('this some simple text')

st.text_input('enter your name', placeholder='James Bond')
#st.text_area('enter your address')
#st.number_input('enter the number')

c1,c2 = st.columns(2)

v1 = c1.number_input('enter first number')
v2 = c2.number_input('enter second number')

operations = ['add','substract','product','divide']
choice = st.radio('Select Operation',options=operations)

submit_btn = st.button('calculate')
result = 0
if submit_btn:
    if choice == 'add':
        result=v1+v2
    elif choice == 'substract':
        result=v1-v2
    elif choice == 'product':
        result=v1*v2
    else:
        result=v1/v2

st.success(f'result calculated:{result}')
