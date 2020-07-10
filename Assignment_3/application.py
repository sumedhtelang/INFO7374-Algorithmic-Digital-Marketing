import streamlit as st
import numpy as np
import pandas as pd

add_selectbox = st.sidebar.radio(
    "Select the type of SEARCH METHOD",
    ("Similarity", "FAISS")
)
# st.title('My first app')

# x = 4
# st.write(x, 'squared is', x * x)

# x = st.slider('x') # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
# 'How would you like to be contacted?',
# ('Email', 'Home phone', 'Mobile phone')
# )
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
# 'Select a range of values',
# 0.0, 100.0, (25.0, 75.0)
# )

# pics = {
#     "1": "d2.jpg",
#     "2": "d3.jpg",
#     "3": "d4.jpg"
# }
# pic = st.selectbox("Picture choices", list(pics.keys()), 0)
# st.image(pics[pic], use_column_width=True, caption=pics[pic])
if add_selectbox == 'Similarity' :
 st.title("_Images using Similarity Search!_ ")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('method1.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 st.subheader("Select an image from the dropdown menu :point_down:")
 pic = st.selectbox('Choices:', images)
 st.write("**You selected:**")
 st.image(pic,width=None)


 z = st.slider('How many images do you want to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("Output:")
 st.write('**Images similar to the image selected by you:**')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1

elif add_selectbox == 'FAISS':
 st.title("_Images using Facebook AI Similarity Search (Faiss)_ ")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('faiss.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 st.subheader("Select an image from the dropdown menu :point_down:")
 pic = st.selectbox('Choices:', images)
 st.write("**You selected:**")
 st.image(pic,width=None)


 z = st.slider('How many images do you want to see?', 1, 4, 2)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("Output:")
 st.write('**Images similar to the image selected by you:**')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1

 




