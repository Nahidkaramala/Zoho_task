import streamlit as st
import hmac
import pandas as pd
import regex as re
import mysql.connector
import pymysql
import os

connection_parameters= {'host' : "localhost",
  'user' : "root",
  'password' : "Nahid123"
#   'database' : 'Zoho'
  }

connection = pymysql.connect(**connection_parameters)
cursor= connection.commit
db= f"CREATE DATABASE{'Zoho'}"
cursor.execute(db)
# connection.close()

# Create table
table= """CREATE TABLE IF NOT EXISTS 'user_info'(id INT,
username VARCHAR(50),
password VARCHAR(50),
age INT,
date_of_birth VARCHAR(50),
email VARCHAR(50),
contact_number VARCHAR(50))"""
cursor.execute(table)

st.title("Zoho form")
options=["Login", "Register"]
st.caption("Login credentials")


select = st.selectbox("New User/ Existing User", options)
# @ st.authentication
# def authentication():
#     return

if select == "Register":    
    if st.button("Create Account"): 
        username = st.write("Enter Username", input())
        password = ("Enter Password", input(), st.secrets["password"])   
        age = st.write("Enter Age", int(input()))
        date_of_birth = st.write("Enter Date Of Birth in MM/DD/YYYY format", input())
        email = st.write("Enter email ID", input())
        contact_number = st.write("Enter Contact Number", input())
    
        st.write("Confirm Password", input(), st.secrets["password"])

# Create dataframe of the information provided by user
    dataframe=pd.DataFrame ({username,
                                password,
                                age,
                                date_of_birth,
                                email,
                                contact_number})

 # INSERT THE USER INFO TO SQL TABLE 
user_info = ("""INSERT INTO 'user_info' (username,
                                 password,
                                 age,
                                 date_of_birth,
                                 email,
                                 contact_number), 
             VALUES= %s %s %s %s %s %s""")
cursor.execute(user_info, dataframe)

         



if select == "Login":            
    with st.button():
        st.write("Enter Username", input())
        st.write("Enter Password", input(), st.secrets["password"])
        

        def check_password():
            # check whether the password entered by the user is correct or not
            def password_entered():
                if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
                    st.session_state["password"] = True
                    st.write("Wrong password Entered")
                else:
                    st.session_state["password_correct"] = False
                    st.write("Correct Password")


        if st.button("Login"):
            query= """SELECT * FROM user_info;"""
            cursor.execute(query)
