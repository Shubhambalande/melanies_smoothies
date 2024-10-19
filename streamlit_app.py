# Import python packages
import streamlit as st
from snowflake.support.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    """Choose the fruit you want in your custom Smoothie
    """
)


NAME_ON_ORDER=st.text_input('Name on Smoothie')
st.write('The name on your Smoothie will be ', NAME_ON_ORDER)
from snowflake.snowpark.functions import col


session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
st.dataframe(data=my_dataframe, use_container_width=True)

intgredients_list =st.multiselect(
'choose up to 5 intgredients;',
my_dataframe,
)

if intgredients_list :
    ingredients_string =''

    for fruit_chosen in intgredients_list:
        ingredients_string += fruit_chosen +''

#st.write(ingredients_string)

my_insert_stmt =""" insert into SMOOTHIES.PUBLIC.ORDERS(ingredients,NAME_ON_ORDER)
        values('""" + ingredients_string +"""','"""+ NAME_ON_ORDER +"""')"""

#st.write(my_insert_stmt)
#st.stop()

time_to_insert = st.button('Submit Order')


cnx =st.connection("snowflake")
session=cnx.session()


