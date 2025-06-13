import streamlit as st
import pandas as pd
import openpyxl
import io

pd.set_option('display.float_format', '{:.0f}'.format)

def add_data(df):
    details = {}
    with st.form(key="account form"):
        details["NAME"] = st.text_input("name of the person")
        details["ACCOUNT NUMBER"] = st.text_input("Account number")
        details["IFSC CODE"] = st.text_input("IFSC code")

        submit_button = st.form_submit_button()

        if submit_button:
            df.loc[-1] = [details["NAME"], details["ACCOUNT NUMBER"], details["IFSC CODE"]]

def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    output.seek(0)
    return output

def open_df_and_write(file_uploaded):
    df = pd.DataFrame(pd.read_excel(file_uploaded))
    st.write(df)
    # if st.button("add new data"):
    #     add_data(uploaded_file)
    selected_cols = st.multiselect("select the names", options=df["NAME"])
    new_df = df[df["NAME"].isin(selected_cols)]
    st.write(new_df)
    excel_data = to_excel(new_df)
    return excel_data



st.title("Bank account info")
st.write("This app lets you upload a excel file and then choose the required columns(from NAME)")

def uploadfile():
    uploaded_file = st.file_uploader("Upload the excel file")
    return uploaded_file

uploaded_file = uploadfile()

if uploaded_file:
    excel_data = open_df_and_write(uploaded_file)
    st.download_button(label="Download Data as excel",
                    data = excel_data,
                    file_name="Filtered_Data.xlsx",
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
