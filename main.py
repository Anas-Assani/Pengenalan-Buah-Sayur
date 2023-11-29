import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","Anggota Kelompok","Tentang Project"])

#Main Page
if(app_mode=="Home"):
    st.header("SISTEM PENGENALAN BUAH & SAYUR")
    image_path = "header.jpg"
    st.image(image_path)

# elif(app_mode=="Prediction"):
    st.subheader("Coba Sekarang !")
    test_image = st.file_uploader("Pilih Gambar:")
    if(st.button("Tampilkan Gambar")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Kenali Gambar")):
        st.write("Hasil")
        result_index = model_prediction(test_image)
        #Reading Labels
        with open("labels.txt") as f:
            content = f.readlines()
        label = []
        for i in content:
            label.append(i[:-1])
        st.success("Ini adalah {}".format(label[result_index]))
        
elif(app_mode=="Anggota Kelompok"):
    st.subheader("Anggota Kelompok:")
    image_path = "Anggota\Putri Wahyuni Sanjaya.jpg"
    st.image(image_path, width=100)
    st.text("1. Putri Wahyuni Sanjaya \n(Universitas Nahdlatul Wathan Mataram)\n")
    image_path = "Anggota\Elis Shofiyatul Wasilah.jpg"
    st.image(image_path, width=100)
    st.text("2. Elis Shofiyatul Wasilah \n(Universitas Lambung Mangkurat)\n")
    image_path = "Anggota\Tri Noviyansyah.jpg"
    st.image(image_path, width=100)
    st.text("3. Tri Noviyansyah \n(Universitas Borneo Tarakan)\n")
    image_path = "Anggota\Anis Fadhil Faisal.jpg"
    st.image(image_path, width=100)
    st.text("4. Anis Fadhil Faisal Rahmatillah \n(Universitas Lambung Mangkurat)\n")
    image_path = "Anggota\Nur Zaini Khafid.jpg"
    st.image(image_path, width=100)
    st.text("5. Nur Zaini Khafid \n(Universitas Lambung Mangkurat)\n")
#About Project
elif(app_mode=="Tentang Project"):
    st.header("Tentang Project")
   
    st.subheader("Tentang Dataset")
    st.text("Dataset Meliputi:")
    st.code("Buah - pisang, apel, pear, anggur, jeruk, kiwi, semangka, delima, nanas, mangga.")
    st.code("Sayur - timun, wortel, capsicum, bawang, kentang, lemon, tomat, lobak, beetroot, kol, selada, bayam, kedelai, kembang kol, bell pepper, cabai, turnip, jagung, jagung manis, ubi jalar, paprika, jalepeño, jahe, bawang putih, kacang polong, terong.")
    st.subheader("Content")
    st.text("Dataset Ini Berisi Tiga Folder:")
    st.text("1. train => (terdiri dari 36 folder dengan masing-masing 100 gambar di dalamnya)")
    st.text("2. test => (terdiri dari 36 folder dengan masing-masing 10 gambar di dalamnya)")
    st.text("3. validation => (terdiri dari 36 folder dengan masing-masing 10 gambar di dalamnya)")


