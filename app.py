import streamlit as st
from PIL import Image
import numpy as np

st.title("Recommendations for Optical Eyeglass Frames Based on Face Shape")

tab1, tab2 = st.tabs(["Check Your Face Shape", "Glasses Frame"])

with tab1:
    st.header("Check this out!")

    from image_classification import teachable_machine_classification

    option = st.selectbox(
        'Gender',
        ('Female', 'Male'))

    st.write('You selected:', option)

    item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
    uploaded_file = st.file_uploader("Upload your photo", type=['png','jpg','jfif','jpeg','img'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Upload Classification', use_column_width=True)
        st.write("Bentuk wajah...")
        label = teachable_machine_classification(image, 'Model2.h5')
        if label == 0:
            st.write("heart")
            if option == 'Female':
                st.write('Female') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Female/Heart/{i+1}.png")
                    st.image(frame, caption='Female')
            else:
                st.write('Male') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Male/Heart/{i+1}.png")
                    st.image(frame, caption='Male')
            
        elif label == 1:
            st.write("oblong")
            if option == 'Female':
                st.write('Female') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Female/Oblong/{i+1}.png")
                    st.image(frame, caption='Female')
            else:
                st.write('Male') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Male/Oblong/{i+1}.png")
                    st.image(frame, caption='Male')
            
        elif label == 2:
            st.write("oval")
            if option == 'Female':
                st.write('Female') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Female/Oval/{i+1}.png")
                    st.image(frame, caption='Female')
            else:
                st.write('Male') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Male/Oval/{i+1}.png")
                    st.image(frame, caption='Male')
        
        elif label == 3:
            st.write("round")
            if option == 'Female':
                st.write('Female') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Female/Round/{i+1}.png")
                    st.image(frame, caption='Female')
            else:
                st.write('Male') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Male/Round/{i+1}.png")
                    st.image(frame, caption='Male')
           
        elif label == 4:
            st.write("square")
            if option == 'Female':
                st.write('Female') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Female/Square/{i+1}.png")
                    st.image(frame, caption='Female')
            else:
                st.write('Male') 
                for i in range(14):
                    frame=Image.open(f"./frame kacamata/Male/Square/{i+1}.png")
                    st.image(frame, caption='Male')
        else:
            st.write("tidak diketahui")



with tab2:
        st.header("Female")
        st.subheader('Heart')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Female/Heart/{i+1}.png")
            st.image(frame)

        st.subheader('Oblong')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Female/Oblong/{i+1}.png")
            st.image(frame)

        st.subheader('Oval')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Female/Oval/{i+1}.png")
            st.image(frame)

        st.subheader('Round')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Female/Round/{i+1}.png")
            st.image(frame)

        st.subheader('Square')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Female/Square/{i+1}.png")
            st.image(frame)
    
            st.header("Male")
        st.subheader('Heart')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Male/Heart/{i+1}.png")
            st.image(frame)

        st.subheader('Oblong')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Male/Oblong/{i+1}.png")
            st.image(frame)

        st.subheader('Oval')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Male/Oval/{i+1}.png")
            st.image(frame)

        st.subheader('Round')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Male/Round/{i+1}.png")
            st.image(frame)

        st.subheader('Square')
        item=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
        for i in range(14):
            frame=Image.open(f"./frame kacamata/Male/Square/{i+1}.png")
            st.image(frame)
