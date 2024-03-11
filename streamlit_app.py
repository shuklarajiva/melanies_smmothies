# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruit you want in cutom Smoothie !
    """
)



name_on_order = st.text_input('Name On Smoothie')
st.write('The name on your Smoothie will be : ', name_on_order)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('Fruit_Name'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list = st.multiselect('Choose upto 5 ingredients',my_dataframe,max_selections =5)

if ingredients_list:
 #st.write(ingredients_list)
 #st.text(ingredients_list)
 ingredients_String = ''
 for fruit_chosen in ingredients_list:
    ingredients_String += fruit_chosen + ' '
 #st.write(ingredients_String)
 my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_String + "',""" +"'"+ name_on_order + """')"""
 
    
 time_to_insert = st.button(' Submit Order')
 #st.write(my_insert_stmt)
 #st.stop
 if time_to_insert:
     if ingredients_String:
        session.sql(my_insert_stmt).collect()
     st.success('Your Smoothie is ordered,' + name_on_order +  "!", icon="✅")
     
