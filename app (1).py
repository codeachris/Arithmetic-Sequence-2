import streamlit as st

def arithmetic_sequence(first_term, common_difference, num_terms):
    return [first_term + common_difference * n for n in range(num_terms)]

st.title('Arithmetic Sequence Generator')

first_term = st.number_input('First term', value=1)
common_difference = st.number_input('Common difference', value=1)
num_terms = st.number_input('Number of terms', min_value=1, value=5)

if st.button('Generate sequence'):
    sequence = arithmetic_sequence(first_term, common_difference, num_terms)
    st.write('Arithmetic Sequence:')
    st.write(sequence)