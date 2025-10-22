import streamlit as st
import matplotlib.pyplot as plt

def mostrar(df):
    st.header("🌍 8️⃣ Proporción de usuarios por continente")

    # --- Diccionario de mapeo país → continente ---
    continent_map = {
        'Armenia': 'Asia', 'China': 'Asia', 'Portugal': 'Europe', 'Poland': 'Europe',
        'Panama': 'North America', 'Iran': 'Asia', 'Slovenia': 'Europe',
        'Ethiopia': 'Africa', 'Finland': 'Europe', 'Serbia': 'Europe',
        'Brazil': 'South America', 'Indonesia': 'Asia', 'Tanzania': 'Africa',
        'Syria': 'Asia', 'Tajikistan': 'Asia', 'Philippines': 'Asia', 'Honduras': 'North America',
        'Ireland': 'Europe', 'Kazakhstan': 'Asia', 'Greece': 'Europe', 'Spain': 'Europe',
        'Chile': 'South America', 'Canada': 'North America', 'South Africa': 'Africa',
        'Ukraine': 'Europe', 'Cuba': 'North America', 'South Korea': 'Asia',
        'Sweden': 'Europe', 'Japan': 'Asia', 'Argentina': 'South America',
        'Russia': 'Europe', 'Latvia': 'Europe', 'Burkina Faso': 'Africa',
        'Thailand': 'Asia', 'Colombia': 'South America', 'Egypt': 'Africa',
        'Madagascar': 'Africa', 'Morocco': 'Africa', 'Croatia': 'Europe',
        'Guatemala': 'North America', 'Vietnam': 'Asia', 'Mexico': 'North America',
        'Nigeria': 'Africa', 'Albania': 'Europe', 'Netherlands': 'Europe',
        'Swaziland': 'Africa', 'Micronesia': 'Oceania', 'Peru': 'South America',
        'Hungary': 'Europe', 'Costa Rica': 'North America', 'Jamaica': 'North America',
        'Cambodia': 'Asia', 'Nicaragua': 'North America', 'Venezuela': 'South America',
        'Zambia': 'Africa', 'Czech Republic': 'Europe', 'Papua New Guinea': 'Oceania',
        'France': 'Europe', 'Belarus': 'Europe', 'Jordan': 'Asia', 'Botswana': 'Africa',
        'North Korea': 'Asia', 'Luxembourg': 'Europe', 'Israel': 'Asia',
        'Azerbaijan': 'Asia', 'Niger': 'Africa', 'United States': 'North America',
        'United Kingdom': 'Europe', 'Moldova': 'Europe', 'Sierra Leone': 'Africa',
        'Palau': 'Oceania', 'Mongolia': 'Asia', 'Pakistan': 'Asia', 'Zimbabwe': 'Africa',
        'Georgia': 'Asia', 'Macedonia': 'Europe', 'Paraguay': 'South America',
        'Sri Lanka': 'Asia', 'Lithuania': 'Europe', 'Denmark': 'Europe', 'Norway': 'Europe',
        'Mali': 'Africa', 'Malta': 'Europe', 'Palestinian Territory': 'Asia',
        'Bosnia and Herzegovina': 'Europe', 'Nepal': 'Asia', 'Malaysia': 'Asia',
        'Germany': 'Europe', 'Ghana': 'Africa', 'Libya': 'Africa', 'Bulgaria': 'Europe',
        'New Zealand': 'Oceania', 'Myanmar': 'Asia', 'Cyprus': 'Europe',
        'Afghanistan': 'Asia', 'Somalia': 'Africa', 'Australia': 'Oceania',
        'French Polynesia': 'Oceania', 'Puerto Rico': 'North America',
        'Suriname': 'South America', 'Taiwan': 'Asia', 'Lesotho': 'Africa',
        'Estonia': 'Europe', 'Yemen': 'Asia', 'Ecuador': 'South America',
        'Tunisia': 'Africa', 'Bahrain': 'Asia', 'Iraq': 'Asia', 'Belize': 'North America',
        'Turks and Caicos Islands': 'North America', 'Haiti': 'North America',
        'Uganda': 'Africa', 'Uruguay': 'South America', 'Greenland': 'North America',
        'Montenegro': 'Europe', 'Cape Verde': 'Africa', 'Trinidad and Tobago': 'North America',
        'Chad': 'Africa', 'Bhutan': 'Asia', 'Guinea': 'Africa'
    }

    # --- Asignar continente ---
    df['continent'] = df['country'].map(continent_map)

    # --- Contar usuarios por continente ---
    continent_counts = df['continent'].value_counts()

    # --- Mostrar tabla ---
    st.dataframe(
        continent_counts
            .rename(columns={'count': 'Usuarios', 'continent': 'Continente'})
            .reset_index(drop=True)
    )

    # --- Gráfico circular ---
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(continent_counts, labels=continent_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Distribución de usuarios por continente 🌎")
    st.pyplot(fig)
