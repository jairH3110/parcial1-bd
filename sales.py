import streamlit as st
import pandas as pd
import numpy as np
import codecs
import matplotlib.pyplot as plt
import seaborn as sns
bd_link = "./vgsales.csv"

@st.cache
def all_bd(nrows):
    data = pd.read_csv(bd_link)
    
    return data

def filtro_publicadox(publicador):
    data= pd.read_csv(bd_link)
    fil_publicadox = data[data["Publisher"].str.upper().str.contains(publicador,na=False)]
    return fil_publicadox



def filtro_genero(genero):
    data= pd.read_csv(bd_link)
    fil_genero = data[data["Genre"].str.upper().str.contains(genero)]
    return fil_genero

def filtro_opciones(public):
    data= pd.read_csv(bd_link,index_col=0)
    fil_desarrollador = data[data["Publisher"].str.contains(desarrolladora,na=False)]
    return fil_desarrollador


data_carga =st.text('los 100 videojuegos mejor vendidos')
data = all_bd(100)

st.sidebar.image("credencial.jpeg")
st.sidebar.write("josejair")
st.sidebar.write("zS18003182")
st.sidebar.markdown("##")

if st.sidebar.checkbox('mostrar toda la informacion sin filtro?'):
    st.subheader('info')
    st.write(data)
    


texto_fil1 = st.sidebar.write("buscador por")
buscador_x_genero =st.sidebar.text_input("genero")
botonGenero = st.sidebar.button("buscar-por-Genero")


texto_fil2 = st.sidebar.write("buscar_por_publicador")
buscador_x_p =st.sidebar.text_input("publicador")
Botonpublicador = st.sidebar.button("buscar-por-pucliadora")   


texto_filt3= st.sidebar.write("si no sabes que desarrolladoras existen busca aqui")
desarrolladora = st.sidebar.selectbox("selecciona desarrolladora",
                                      options=data["Publisher"].unique())
Botonselect =st.sidebar.button("buscar por opciones de publicador")

if botonGenero:
    filtro_gen = filtro_genero(buscador_x_genero.upper())
    rows= filtro_gen.shape[0]
    st.dataframe(filtro_gen)


if Botonpublicador:
    filtoPub =  filtro_publicadox(buscador_x_p.upper())
    rows = filtoPub.shape[0]
    st.dataframe(filtoPub)
    
   
    
if Botonselect:
    filtro_select = filtro_opciones(desarrolladora)
    rows = filtro_select.shape[1]
    st.dataframe(filtro_select)    

 
min_valuel = float(data['Global_Sales'].min()),
max_valuel = float(data['Global_Sales'].max())

optionals = st.sidebar.expander("expander configurations",True)
Global_Sales_min = optionals.slider(
    "minimo Global_Sales ",
    min_value = float(data['Global_Sales'].min()),
    max_value = float(data['Global_Sales'].max())
)



subset_Global_Sales = data[(data['Global_Sales'] <= max_valuel) & (Global_Sales_min <= data['Global_Sales'] )]

st.write(f" number of records with Global_Sales betwen {Global_Sales_min} and {max_valuel}: {subset_Global_Sales.shape[0]}")    
st.dataframe(subset_Global_Sales)


with st.expander("See explanation"):
        st.write(" The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random. ")
          

chart_data = pd.DataFrame((data['JP_Sales'].max(),data['JP_Sales'].min()),columns=["venta en jp"])
st.bar_chart(chart_data,use_container_width=True)
with st.expander("explanation"):
        st.write(" mayor venta de japon en la historia mostrada a 1= 100000 ")
 

datos = pd.read_csv('./vgsales.csv' )


fig, ax =plt.subplots()
ax.hist(datos['Year'])

st.pyplot(fig)

fig2,ax2 = plt.subplots()
y_pos =  datos["Publisher"]
x_pos = datos['Year']


ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Publisher")
ax2.set_xlabel("JP_Sales")
ax2.set_title('cuanto pagaron las clases de el titanic ')

st.header("grafica desarrolladores-venta")
st.pyplot(fig2)
with st.expander("Quieres ver la explicacion?"):
        st.write(" Relacion de las ventas de estados unidos respecto a las ventas globales: como se observa llego hasta su punto más alto en 2010 para despues ")



