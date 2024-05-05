import streamlit as st
import pandas as pd
import plotly.express as px
import os
st.title("my Dashboard")

file = st.file_uploader("upload file",type=({"csv","xlsx"}))

dir = os .chdir(r"C:\Users\91638\Documents\Data Set")
if file is not None:
    st.write("selectfile.name:" + file.name)
    df= pd.read_csv(file.name,encoding="ISO-8859-1")
    st.write(df)
else:
    df= pd.read_csv(r"C:\Users\91638\Documents\Data Set\superstore.csv",encoding= "ISO-8859-1")  
    st.write(df)  

# col1,col2 = st.column((2))

# df["Order Date"] = pd.to_datetime(df["Order Date"]),format="mixed"

# date1 =pd.to_datetime(df["Order Date"]).min()
# date2 = pd.to_datetime(df["Order Date"]).max()
# st.write(date1)
# st.write(date2)

# with col1:
#     startTime = pd.to_datetime(st.date_input("Start Date"),date1)

                                             

#     with col2:
#         endTime = pd.to_datetime(st.date_input("end date"),date2)   

   

### sort values
df.sort_values(["Profit","Sales"],axis=0,ascending=[False,False],inplace=True)   


# Graph b/w region and category
fig= px.bar(df.head(20),x='Region',color='Category',width=700 , title='Graph b/w region and category')
st.plotly_chart(fig)



#graph b/w region and profit
fig= px.bar(df.head(20),x='Region',y="Sales",color='Profit',width=700,title='Sales in Region with heighest value')
st.plotly_chart(fig)


##grapg b/w order count vs sub category
fig=px.bar(df.head(100),x='Sub-Category',color='Category',width=700,title='order count of category sub-category')
st.plotly_chart(fig)


fig=px.bar(df.head(20),x='Customer Name',y='Quantity',color ='Profit',hover_data=['Discount','Category'],width=700, title='order count of category sub-category')
st.plotly_chart(fig)



fig=px.pie(df,names='Sub-Category',values='Profit',width=700,title='order count of category sub-category')
st.plotly_chart(fig)

                                  
                