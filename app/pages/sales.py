import streamlit as st
import sys
import os
from datetime import datetime

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from database.connection import get_connection
from database.insert_data import record_sale

st.title("Record Sale")

sale_id = st.text_input("Sale ID")
product_id = st.text_input("Product ID")
quantity_sold = st.number_input(
    "Quantity Sold",
    min_value=1,
    step=1
)

if st.button("Record Sale"):

    connection = get_connection()

    try:

        record_sale(
            connection,
            sale_id,
            product_id,
            datetime.now(),
            quantity_sold
        )

        st.success("Sale recorded successfully!")

    except ValueError as error:

        st.error(str(error))

    except Exception as error:

        st.error("An unexpected error occurred.")

    finally:

        connection.close()
if st.button("Refresh Inventory Alerts"):
    st.rerun()