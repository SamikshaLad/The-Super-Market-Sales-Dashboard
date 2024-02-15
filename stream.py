import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt 
import plotly.express as px 
#page Name
st.set_page_config(page_title="Super Market Sales Dashboard",page_icon="📊",layout="wide")

tab1, tab2 = st.tabs([ "🗃 Data","📈 Visualization"])

#read CSV file
df=pd.read_csv("shipping_dataset.csv")
with tab1:
    st.subheader("Description:")
    st.markdown('''The provided dataset, named the Super Market Sales Shipping Dataset, 
    offers detailed insights into the shipping activities associated with sales transactions within a supermarket context.
    It encompasses various attributes that illuminate different factors of the shipping process and sales performance.
    The dataset comprises key attributes, including Order Date, Ship Mode, Segment, Category,
    Sub-Category, Sales, Profit, Region, State,etc.The dataset can be leveraged for various analytical purposes,
    including sales performance analysis, profitability assessment, evaluation of shipping efficiency,
    identification of high-performing product categories or regions, 
    and trend analysis to understand sales patterns.''')
    st.header("The Super Market Sales Shipping Dataset")
    st.write(df)
   
with tab2:

    #give Title to Dashboard (for centre ,use htlm command)
    
    st.markdown("<h1 style='text-align: center;'>🚚📦Super Market Sales Dashboard📦🚚</h1>", unsafe_allow_html=True)
    #add slicer of region and year
    st.sidebar.title("Filter Options")
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
    df['Year'] = df['Order Date'].dt.year
    selected_year = st.sidebar.selectbox('Select a Year',df['Year'].unique())
    filtered_df = df[df['Year'] == selected_year]
    selected_region = st.sidebar.selectbox('Select a Region', ['All'] + list(filtered_df['Region'].unique()))
    # Filter DataFrame by the selected region, or keep all regions if 'All' is selected
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    st.divider()
    col1,col2=st.columns(2)
    with col1:
        total_sales=filtered_df["Sales"].sum()/1000
        st.subheader("📈 Total Sales:")
        st.subheader(f"${total_sales:,.2f}")
    with col2:
        total_profit=filtered_df["Profit"].sum()/1000
        st.subheader("💰 Total Profit:")
        st.subheader(f"${total_profit:,.2f}")

    st.divider()
    col1,col2 =st.columns(2)
    #Bar Chart of Sales by Ship mode
    with col1:
        st.subheader("Sales by Ship Mode")
        mode_sales = filtered_df.groupby('Ship Mode')['Sales'].sum().reset_index()
        fig = px.bar(mode_sales, x='Ship Mode', y='Sales')
        st.plotly_chart(fig, use_container_width=True)
    
    # pie chart of Sales by segment
    with col2:
        st.subheader("Sales by Segment")
        category_sales = filtered_df.groupby('Segment')['Sales'].sum().reset_index()
        fig = px.pie(category_sales, values='Sales', names='Segment')
        st.plotly_chart(fig, use_container_width=True)
    st.divider()

    col1,col2 =st.columns(2)
    #Donut Chart of Sales by Category
    with col1:
        st.subheader("Sales by Category")
        category_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
        fig = px.pie(category_sales, values='Sales', names='Category', hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    #Bar Chart of Sales by Sub-Category
    with col2:
        st.subheader("Sales by Sub-Category")
        subcat_sales = filtered_df.groupby('Sub-Category')['Sales'].sum().reset_index()
        subcat_sales_sorted = subcat_sales.sort_values(by='Sales', ascending=False)
        fig = px.bar(subcat_sales_sorted, x='Sales', y='Sub-Category', orientation='h')
        fig.update_yaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    #Line Chart of Profit by States
    st.subheader("Profit by State")
    state_profit =filtered_df.groupby('State')['Profit'].sum().reset_index()
    fig = px.bar(state_profit, x='State', y='Profit')
    st.plotly_chart(fig, use_container_width=True) 
    st.divider()
    st.title("Overall Conclusion:")
    st.markdown('''    The bar chart above represents the sales figures categorized by different shipping modes.
    This analysis provides valuable insights into the distribution of sales across various shipping modes,
    enabling better decision-making and optimization of shipping strategies.''')
    st.markdown('''The pie chart above illustrates the distribution of sales across different market segments.
     This analysis aids in understanding the sales performance across different market segments,
    allowing for targeted marketing strategies and customer engagement efforts.''')
    st.markdown('''The donut chart above visualizes the distribution of sales across different product categories.
     This analysis helps in understanding the contribution of each category to total sales,
    enabling better inventory management and product assortment decisions.''')
    st.markdown(''' The horizontal bar chart above displays the total sales for each sub-category of products.
    Understanding the sales performance of different sub-categories is crucial for optimizing
    product offerings, marketing strategies, and inventory management.''')
    st.markdown('''The bar chart above illustrates the total profit generated in each state.
    Understanding the profitability of different states can help in identifying regions of strength 
    and areas that may require further attention or improvement in business operations. ''')

    
    
    


    
