import streamlit as st
import pandas as pd
import mysql.connector
import pymysql

# Connection parameters
connection_parameters = {
    'host': "localhost",
    'user': "root",
    'password': "Nahid123"
    # 'database': 'Zoho'
}

# Establishing the connection
connection = pymysql.connect(**connection_parameters)
cursor = connection.cursor()

# Creating the database
db = "CREATE DATABASE IF NOT EXISTS Zoho"
cursor.execute(db)
cursor.execute("USE Zoho")

# Creating the table
table = """
CREATE TABLE IF NOT EXISTS user_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    age INT,
    date_of_birth VARCHAR(50),
    email VARCHAR(50),
    contact_number VARCHAR(50)
)
"""
cursor.execute(table)
connection.commit()

# Streamlit UI
st.title("Zoho Form")
options = ["Login", "Register"]
select = st.selectbox("New User/ Existing User", options)

if select == "Register":
    st.caption("Register")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    age = st.number_input("Enter Age", min_value=0, max_value=120, step=1)
    date_of_birth = st.text_input("Enter Date Of Birth in MM/DD/YYYY format")
    email = st.text_input("Enter email ID")
    contact_number = st.text_input("Enter Contact Number")

    if st.button("Create Account"):
        if password == confirm_password:
            user_info = (username, password, age, date_of_birth, email, contact_number)
            insert_query = """
            INSERT INTO user_info (username, password, age, date_of_birth, email, contact_number)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, user_info)
            connection.commit()
            st.success("Account created successfully!")
        else:
            st.error("Passwords do not match")

if select == "Login":
    st.caption("Login")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        query = "SELECT * FROM user_info WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            st.success("Login successful!")
            st.write("User Info:")
            user_info_df = pd.DataFrame([result], columns=["ID", "Username", "Password", "Age", "Date of Birth", "Email", "Contact Number"])
            st.dataframe(user_info_df)
        else:
            st.error("Invalid username or password")

# Closing the connection
cursor.close()
connection.close()
