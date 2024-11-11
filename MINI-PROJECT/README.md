### Project: Interest Calculator Using Streamlit

#### **Introduction:**
This project is an interactive **Interest Calculator** web application developed using **Streamlit**. The application allows users to calculate **Simple Interest** and **Compound Interest** based on the principal amount, rate of interest, and time period. Users can also choose different compounding frequencies for calculating compound interest.

#### **Libraries Used:**
- **Streamlit:** Streamlit is an open-source Python library used to create web applications with minimal effort. It enables us to create interactive apps for data science and machine learning projects.
- **Python (built-in):** The app uses Python's built-in capabilities for mathematical calculations such as interest calculations.

#### **Features:**
1. **Simple Interest Calculation:**
   - Users can input the principal amount, rate of interest, and time period (in years) to calculate the simple interest.
   - The app will display both the simple interest and the total amount (principal + interest).

2. **Compound Interest Calculation:**
   - Users can calculate compound interest by selecting the principal amount, rate of interest, and time period (in years).
   - The app allows users to select the compounding frequency: annually, semi-annually, quarterly, or monthly. Based on this, it calculates the compound interest using the formula:
     \[
     \text{Compound Interest} = P \left(1 + \frac{r}{n}\right)^{nt} - P
     \]
     where:
     - \( P \) is the principal amount
     - \( r \) is the annual interest rate (in percentage)
     - \( n \) is the number of times the interest is compounded per year
     - \( t \) is the time period in years

#### **Output:**

![Alt Text](https://i.postimg.cc/ZY8hn24D/miniproject.png)


