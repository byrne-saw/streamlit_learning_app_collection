import streamlit as st

st.title("My First Streamlit App")

user_input = st.text_input("Enter some text:")

uppercase_text = user_input.upper()

st.write(f"Uppercase text: {uppercase_text}")

st.write("Here's our first attempt at using data to create a table:")

st.write('what the hell is this?')

# make a plot
st.line_chart([1,2,3,4,5,6,7,8,9,10])

# make a form with 10 fields
st.form(key='my_form')
st.text_input(label='Enter some text')
st.slider(label='Select a range of values')
st.selectbox(label='Choose an option from a list', options=['a', 'b', 'c'])
st.multiselect(label='Choose one or more options from a list', options=['a', 'b', 'c'])
st.text_area(label='Enter a long string')
st.date_input(label='Select a date')
st.time_input(label='Select a time')
st.number_input(label='Enter a number')
st.checkbox(label='Check me out')
st.radio(label='Choose an option from a list', options=['a', 'b', 'c'])

