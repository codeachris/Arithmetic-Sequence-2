import streamlit as st

st.title("Sequence Generator: Arithmetic & Geometric")

seq_type = st.selectbox("Select sequence type:", ["Arithmetic", "Geometric"])
first_term = st.number_input("First term (a₁)", value=1.0)
if seq_type == "Arithmetic":
    common_diff = st.number_input("Common difference (d)", value=1.0)
    sequence_param_label = "Common difference (d)"
else:
    common_diff = st.number_input("Common ratio (r)", value=2.0)
    sequence_param_label = "Common ratio (r)"
n_terms = st.number_input("Number of terms (n)", min_value=1, step=1, value=5)

if st.button(f"Show {seq_type} sequence"):
    if seq_type == "Arithmetic":
        sequence = [first_term + i * common_diff for i in range(int(n_terms))]
        nth_term = first_term + (n_terms-1) * common_diff
        sum_seq = n_terms/2 * (2*first_term + (n_terms-1)*common_diff)
    else:
        sequence = [first_term * common_diff ** i for i in range(int(n_terms))]
        nth_term = first_term * common_diff ** (n_terms-1)
        sum_seq = first_term * (1 - common_diff ** n_terms)/(1 - common_diff) if common_diff != 1 else first_term * n_terms

    st.markdown(f"### Sequence:")
    st.write(sequence)
    st.markdown(f"#### Sequence details:")
    st.write({
        "Type": seq_type,
        "First term (a₁)": first_term,
        sequence_param_label: common_diff,
        "Number of terms (n)": n_terms,
        f"n-th term (aₙ)": nth_term,
        "Sum of sequence (Sₙ)": sum_seq
    })