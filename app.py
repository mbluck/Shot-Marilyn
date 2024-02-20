import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
#import base64

st.title("A Data-Based Interpretation of Andy Warhol's" + '"Shot Marilyn"')

st.image(image='c:/Users/Melanie/OneDrive/Projects/Marilyn/assets/marilyns.png', 
         caption='The Shot Marilyns from left to right, top to bottom: "Orange", "Blue", "Red", "Turquoise", "Sage"')

hsv_data = pd.read_csv('c:/Users/Melanie/OneDrive/Projects/Marilyn/data/hsv_data.csv')

# Saturation -------------

og = hsv_data[hsv_data['Color']=='original']['Saturation']
orange = hsv_data[hsv_data['Color']=='orange']['Saturation']
blue = hsv_data[hsv_data['Color']=='blue']['Saturation']
red = hsv_data[hsv_data['Color']=='red']['Saturation']
turq = hsv_data[hsv_data['Color']=='turquoise']['Saturation']
sage = hsv_data[hsv_data['Color']=='sage']['Saturation']

'''
sat_fig = ff.create_distplot(
    [og, orange, blue, red, turq, sage],
    group_labels=['original', 'orange', 'blue', 'red', 'turquoise', 'sage'], 
    colors=['#8FA0A9','#EB7C44', '#445DEB', '#EB4444', '#58ECEC', '#58EC89'], 
    show_hist=False
)

st.plotly_chart(sat_fig, use_container_width=True)
'''
fig = px.histogram(hsv_data, x="Saturation", color='Color', marginal='rug')
st.plotly_chart(fig, use_container_width=True)
#st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmp6cnNuNzhya3M3ZTlzYnpsOWEwdGUzNWdxY2w3ejF6ZDdtcHVibyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xtPipzBmlA5N9Em7Ix/giphy.gif")