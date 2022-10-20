import streamlit as st
st.title("Mi App")
st.header("Esto es solo un ejemplo")
st.sidebar("http://fcq.uach.mx/images/institucionales/")
boton = st.button()
if boton:
  st.balloon()
  
