import streamlit as st
import streamlit as st
import pandas as pd
from datetime import date
import numpy as np

def step_1():
    st.title("Step 1: Snowflake Credentials")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    account = st.text_input("Account")
    warehouse = st.text_input("Warehouse")
    
    return username, password, account, warehouse

def step_2():
    st.title("Step 2: Table Details")
    schema = st.text_input("Schema")
    table = st.text_input("Table Name")
    
    return schema, table

def step_3():
    st.title("Step 3: Upload CSV")
    csv_file = st.file_uploader("Choose a CSV file")

def step_4():
    import streamlit as st
    
    left, middle, right = st.columns(3)
    if left.button("Plain button", use_container_width=True):
        username = st.text_input("Username")
    if middle.button("Emoji button", icon="😃", use_container_width=True):
        middle.markdown("You clicked the emoji button.")
    if right.button("Material button", icon=":material/mood:", use_container_width=True):
        right.markdown("You clicked the Material button.")

def step_5():
    adv_name = st.text_input("Adv Name")
    client_name = st.text_input("Client Name")
    client_name2 = st.text_input("Client Name2")
    df = pd.DataFrame(
            {
                "Adv Name": [adv_name],
                "Client Name": [client_name],
            }
        )
    st.dataframe(df)
    
    # col1, col2 = st.columns(2)
    # with col1:
    #     adv_name = st.text_input("Adv Name")
    # with col2:
    #     client_name = st.text_input("Client Name")
    save_data = st.button("Save", type="primary")
    if save_data:
        df = pd.DataFrame(
            {
                "Adv Name": ["adv_name2"],
                "Client Name": ["client_name2"],
            }
        )
        st.dataframe(df)
        
        return df


    # df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
    
    # st.dataframe(df.style.highlight_max(axis=0))

def reset():
    username, password, account, warehouse = "", "", "", ""
    schema, table = "", ""
    csv_file = None

def main():
    st.sidebar.title("Form Wizard")
    current_step = st.sidebar.selectbox("Step", ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5"])
    
    
    if current_step == "Step 1":
        username, password, account, warehouse = step_1()        
    
    elif current_step == "Step 2":
        schema, table = step_2()
        
    
    elif current_step == "Step 3":
        csv_file = step_3()
        next_step_button = st.sidebar.button("Submit")
        
    elif current_step == "Step 4":
        input_list = step_4()
        
    elif current_step == "Step 5":
        cust_df = step_5()
         

    
    
    if st.sidebar.button("Reset", key="reset"):
        username, password, account, warehouse = "", "", "", ""
        schema, table = "", ""
        csv_file = None

if __name__ == "__main__":
    main()
