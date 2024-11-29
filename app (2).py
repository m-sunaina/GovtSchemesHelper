import streamlit as st
import pandas as pd

# Load the dataset (replace 'government_schemes.csv' with your dataset file)
df = pd.read_csv('govt_schemes.csv')

# Streamlit Chatbot Interface
st.title("Government Schemes Chatbot")

# Create an input box to enter user query
user_input = st.text_input("Ask me about government schemes:")

# Function to search for matching schemes in the dataset
def find_schemes(query):
    query = query.lower()
    results = []
    for _, row in df.iterrows():
        eligibility = row['eligibility criteria'].lower()
        target_group = row['target group'].lower()

        if query in eligibility or query in target_group:
            scheme_info = {
                "Scheme": row['scheme name'],
                "Eligibility": row['eligibility criteria'],
                "Target Group": row['target group'],
                "Link": row.get('Link', 'N/A')
            }
            results.append(scheme_info)
    
    return results

# Display the result based on user input
if user_input:
    results = find_schemes(user_input)
    
    if results:
        st.write(f"Here are the schemes related to '{user_input}':")
        for scheme in results:
            st.subheader(scheme["Scheme"])
            st.write(f"Eligibility: {scheme['Eligibility']}")
            st.write(f"Target Group: {scheme['Target Group']}")
            st.write(f"Link: {scheme['Link']}")
    else:
        st.write(f"Sorry, no schemes found for '{user_input}'. Try asking something else.")



