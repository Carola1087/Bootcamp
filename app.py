import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 20), #Crear valores aleatorios
    columns=("col %d" % i for i in range(20)) #Llenar columnas con los valores aleatorios, %d es el digito de la columna
    )
#Aplicar estilo "hightlight" al DataFrame
st.dataframe(df.style.highlight_max(axis=0)) #Resalta el valor máximo de cada columna

import streamlit as st
import pandas as pd
from datetime import date

df = pd.DataFrame(
    {
        "Date": [date(2024, 1, 1), date(2024, 2, 1), date(2024, 3, 1)],
        "Total": [13429, 23564, 23452],
    }
)
df.set_index("Date", inplace=True)

config = {
    "_index": st.column_config.DateColumn("Month", format="MMM YYYY"),
    "Total": st.column_config.NumberColumn("Total ($)"),
}

st.dataframe(df, column_config=config)

#
