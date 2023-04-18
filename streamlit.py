import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import cv2
st.set_page_config(page_title='UC-merced klassifikatsiya',layout='wide')

model = tf.keras.models.load_model('models\VGG-19\model_with_transfer.h5')

title = "UC-merced dataseti yordamida o'qitilgan modelni sinovdan o'tkazish"
st.markdown("<h1 style='text-align: center;font-size: 30px;'>"+title+"</h1>", unsafe_allow_html=True)

image = st.file_uploader("Faylni yuklang")

if image is not None:

    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    c1,c2,c3 = st.columns(3)
    c2.image(img, channels="BGR",use_column_width=True)
    
    if c2.button("Predict",use_container_width=True):
        # normalizatsiya
        image = np.array(img)
        image = np.array(cv2.resize(image,(224,224),interpolation = cv2.INTER_AREA))
        image = np.array(image).astype('float16')/255.0
        image = image.reshape(1,224,224,3)
        
        classlar = ["agricultural","airplane","baseballdiamond","beach","buildings","chaparral","denseresidential","forest","freeway","golfcourse","harbor","intersection","mediumresidential","mobilehomepark","overpass","parkinglot","river","runway","sparseresidential","storagetanks","tenniscourt"]
        one_hot = model.predict(image)
        index = np.argmax(one_hot)
        predict = classlar[index]
        probability=one_hot[0][index]
        
        result = {"Atributlar":["Class nomi","Ehtimollik"],"Qiymatlar":[predict,probability]}
        
        st.dataframe(result,use_container_width=True)
