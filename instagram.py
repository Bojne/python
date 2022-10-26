
from random import random
import requests
import streamlit as st 

t1, t2 = st.columns([1,3])

with t1: 
    st.button('Refresh')
with t2:
    total_image =  st.slider("選一個數字", 9,99, step=3)

col1, col2 = st.columns([1,3])
# st.slider("Generate photos", 3,100, step=3)


with col1: 
    
    st.image('https://github.com/bojne.png')

with col2: 
    "### @robot_123" 

    st.write(f"##### `{total_image}` posts `318` followers `430` following")
    "🔗 [vsco.co/yuehan18](https://vsco.co/yuehan18)"

"# "

def get_random_image(): 
    for _ in range(3):
        id = str(int(random() * 1000+1))
        image_str = 'https://picsum.photos/id/' + id + '/200'
        if requests.get(image_str).status_code != 404:
            return st.image(image_str, 'id: ' + id)
    else: 
        return 


p1, p2, p3 = st.columns(3)
with st.spinner("Loading..."):

    for i in range(int(total_image//3)):
        with p1: 
            get_random_image()
        with p2: 
            get_random_image()
        with p3:
            get_random_image()


# i = str(int(random()*12))
# photo_list = list(requests.get('https://picsum.photos/v2/list?page='+i+'&limit=100').json())
# photo_list = [elem['download_url'][:-9] + '200'for elem in photo_list]

# p1, p2, p3 = st.columns(3)
# for i in range(0,int(total_image), 3):
#     with p1: 
#             st.image(photo_list[i])
#     with p2: 
#             st.image(photo_list[i+1])
#     with p3: 
#             st.image(photo_list[i+2])
    