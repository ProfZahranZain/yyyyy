import streamlit as st

st.header(':green[Informasi-informasi yang dibutuhkan]', divider='rainbow')
st.sidebar.markdown("# Informasi mengenai Identifikasi Golongan Ion I-V")
with st.sidebar.container():
    st.image("https://acalpk.files.wordpress.com/2024/05/pemisahan-ion-kation.png?resize=219%2C219")

tab1, tab2, tab3 = st.tabs(['Kation secara umum', 'Pereaksi Selektif', 'Pereaksi Spesifik'])

with tab1:
    st.header('Pengertian Umum Kation')
    st.write('Kation adalah jenis ion yang terbentuk ketika suatu atom kehilangan satu atau beberapa elektron. Proses ini menyebabkan atom tersebut menjadi bermuatan positif. Kation biasanya terbentuk dari logam, karena atom-atom logam cenderung memiliki kecenderungan untuk melepaskan elektron. Contoh yang paling umum adalah kation natrium (Na+), yang terbentuk ketika atom natrium kehilangan satu elektron. Kation juga dapat terbentuk dari atom-atom non-logam yang memiliki kecenderungan untuk kehilangan elektron, seperti hidrogen (H+) atau amonium (NH4+).')
    st.image("https://acalpk.wordpress.com/wp-content/uploads/2024/05/images.jpeg?resize=219%2C219")

with tab2:
    st.header('Pereaksi Selektif')
    st.write('Pereaksi selektif adalah pereaksi yang memberikan reaksi tertentu untuk satu jenis kation tertentu.')
    st.write('Pereaksi Selektif untuk pemisahan kation golongan I-V adalah',':blue[HCl, H2S, (NH4)2S, (NH4)2CO3]')
    st.image("https://acalpk.wordpress.com/wp-content/uploads/2024/05/tabung_reaksi_87566068.png?resize=219%2C219")


with tab3:
    st.header('Pereaksi Spesifik')
    st.write('Reaksi spesifik adalah reaksi khas yang merupakan reaksi antara bahan tertentu dengan pereaksi spesifik untuk bahan tersebut.')
    st.write('Pereaksi Spesifik untuk pemisahan kation golongan I-V adalah',':blue[NH4OH, HNO3, K2CrO4, NaOH, NH4SCN/KSCN, Na2CO3, CH3COOH, H2C2O4]')
    st.image("https://acalpk.wordpress.com/wp-content/uploads/2024/05/oip-1-1.jpeg?resize=219%2C219")
