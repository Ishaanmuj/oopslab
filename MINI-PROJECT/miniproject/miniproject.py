import streamlit as st

def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


def calculate_compound_interest(principal, rate, time, frequency):

    amount = principal * (1 + rate / (frequency * 100)) ** (frequency * time)
    compound_interest = amount - principal
    return compound_interest, amount

st.title("Interest Calculator")


interest_type = st.selectbox("Choose the type of Interest:", ("Simple Interest", "Compound Interest"))

principal = st.number_input("Enter the Principal Amount (₹):", min_value=1, value=1000)
rate = st.number_input("Enter the Rate of Interest (%):", min_value=0.1, value=5.0)
time = st.number_input("Enter the Time Period (in years):", min_value=1, value=2)

if interest_type == "Compound Interest":
    frequency = st.selectbox("Compounding Frequency:", ("Annually", "Semi-Annually", "Quarterly", "Monthly"))

    frequency_map = {
        "Annually": 1,
        "Semi-Annually": 2,
        "Quarterly": 4,
        "Monthly": 12
    }
    frequency = frequency_map[frequency]

if st.button("Calculate Interest"):
    if interest_type == "Simple Interest":
        interest = calculate_simple_interest(principal, rate, time)
        total_amount = principal + interest
        st.write(f"Simple Interest: ₹{interest:.2f}")
        st.write(f"Total Amount (Principal + Interest): ₹{total_amount:.2f}")
    elif interest_type == "Compound Interest":
        compound_interest, total_amount = calculate_compound_interest(principal, rate, time, frequency)
        st.write(f"Compound Interest: ₹{compound_interest:.2f}")
        st.write(f"Total Amount (Principal + Interest): ₹{total_amount:.2f}")
