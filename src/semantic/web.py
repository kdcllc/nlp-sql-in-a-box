import asyncio
import pandas as pd
import streamlit as st

from util import setup_kernel, get_result_from_database

st.title("SQL Query Generator with GPT")
st.write("Enter your message to generate SQL and view results.")

# Input field for the user to type a message
user_message = st.text_input("Enter your message:")


if user_message:

    kernel, plugin = setup_kernel()
    
    sql_query = asyncio.run(kernel.run(plugin["nlpToSQLPlugin"], input_str=user_message)).result

    # Display the generated SQL query
    st.write("Generated SQL Query:")
    st.code(sql_query, language="sql")

    try:
        # Run the SQL query and display the results
        sql_results = get_result_from_database(sql_query)

        df = pd.DataFrame.from_records(sql_results)

        st.write("Query Results:")
        st.dataframe(df)

    except Exception as e:
        st.write(f"An error occurred: {e}")

