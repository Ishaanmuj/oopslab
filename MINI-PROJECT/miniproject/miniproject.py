import streamlit as st
import matplotlib.pyplot as plt

def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def calculate_compound_interest(principal, rate, time, frequency):
    amount = principal * (1 + rate / (frequency * 100)) ** (frequency * time)
    compound_interest = amount - principal
    return compound_interest, amount

def calculate_emi(principal, rate, tenure_years):
    monthly_rate = rate / (12 * 100)
    months = tenure_years * 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return emi

def plot_growth(principal, rate, time, interest_type, frequency=None):
    years = list(range(1, time + 1))
    amounts = []

    if interest_type == "Simple Interest":
        for t in years:
            interest = calculate_simple_interest(principal, rate, t)
            amounts.append(principal + interest)
    elif interest_type == "Compound Interest":
        for t in years:
            compound_interest, amount = calculate_compound_interest(principal, rate, t, frequency)
            amounts.append(amount)

    plt.figure(figsize=(10, 6))
    plt.plot(years, amounts, marker='o', label=f'{interest_type} Growth')
    plt.title(f'{interest_type} Growth Over Time', fontsize=16)
    plt.xlabel('Time (Years)', fontsize=12)
    plt.ylabel('Total Amount (₹)', fontsize=12)
    plt.grid(True)
    plt.legend()
    return plt

st.title("Interest Calculator")

interest_type = st.selectbox("Choose the type of Calculation:", ("Simple Interest", "Compound Interest", "Loan EMI"))

principal = st.number_input("Enter the Principal Amount (₹):", min_value=1, value=1000)
rate = st.number_input("Enter the Rate of Interest (%):", min_value=0.1, value=5.0)

if interest_type == "Loan EMI":
    tenure_years = st.number_input("Enter Loan Tenure (in years):", min_value=1, value=1)
    if st.button("Calculate EMI"):
        emi = calculate_emi(principal, rate, tenure_years)
        total_payment = emi * tenure_years * 12
        st.write(f"EMI: ₹{emi:.2f}")
        st.write(f"Total Payment (Principal + Interest): ₹{total_payment:.2f}")

else:
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

            plt = plot_growth(principal, rate, time, interest_type)
            st.pyplot(plt)

        elif interest_type == "Compound Interest":
            compound_interest, total_amount = calculate_compound_interest(principal, rate, time, frequency)
            st.write(f"Compound Interest: ₹{compound_interest:.2f}")
            st.write(f"Total Amount (Principal + Interest): ₹{total_amount:.2f}")

            plt = plot_growth(principal, rate, time, interest_type, frequency)
            st.pyplot(plt)
