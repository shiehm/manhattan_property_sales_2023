import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('manhattan_sales_cleaned_2023.csv')

st.header('Manhattan Residential Property Sales')
st.subheader('April 2022 - March 2023')
st.write(df)
st.divider()

st.header('Building Class Historgrams')
building_class = sorted(df['building_class_at_time_of_sale'].str[0].unique())
building_class_dict = {'A': 'One-Family Dwelling',
                       'B': 'Two-Family Dwelling',
                       'C': 'Walk-up Apartment',
                       'D': 'Elevator Apartment',
                       'R': 'Condo',
                       'S': 'Primarily Residential Mixed Use'
                      }

for i in building_class:
    fig = px.histogram(df.query("building_class_at_time_of_sale.str[0] == @i")['unit_price'], 
                       nbins=50, 
                       title = building_class_dict[i],
                       labels = {'value':'Sale Price per Unit'}
                      )
    fig.update_layout(showlegend=False)
    fig.update_yaxes(title='Frequency')
    st.plotly_chart(fig, use_container_width=True)
st.divider()



st.header('Average Sale Price Across Neighborhoods')
neighborhood_avg = df.groupby('neighborhood')[['unit_price','sqft_price']].mean().reset_index()
neighborhood_avg = neighborhood_avg.sort_values('sqft_price', ascending=False)
# Create bar chart
fig = px.bar(neighborhood_avg.dropna(), 
             x='neighborhood', 
             y='sqft_price', 
             title='Average Price/SqFt Across Neighborhoods',
             labels = {
                 'neighborhood':'Neighborhood',
                 'sqft_price':'Price / SqFt'
             }
            )
# fig.update_layout(yaxis=dict(tickmode='linear', nticks=4))
st.plotly_chart(fig, use_container_width=True)
st.divider()



st.header('Residential Unit Size vs. Total Sale Price')
fig = px.scatter(df, 
             x='gross_square_feet', 
             y='sale_price', 
             title='Residential Sizes (Gross SqFt) vs. Sale Prices',
             labels = {
                 'gross_square_feet':'Unit Size (SqFt)',
                 'sale_price':'Sale Price'
             }
            )
st.plotly_chart(fig, use_container_width=True)
st.divider()



st.header('Price PSF Ranges by Neighborhood')
fig = px.box(df, 
             x='neighborhood', 
             y='sqft_price', 
             notched=True
            )
st.plotly_chart(fig, use_container_width=True)
st.divider()



st.subheader('Just for testing')
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

# st.checkbox(label, 
#             value=False, 
#             key=None, 
#             help=None, 
#             on_change=None, 
#             args=None, 
#             kwargs=None, *, 
#             disabled=False, 
#             label_visibility="visible")