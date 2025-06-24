import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Visualizer", layout="wide")
st.title("📊 Excel & CSV Data Visualizer")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xls", "xlsx"])

if uploaded_file:
    # Load the data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if not numeric_cols:
        st.warning("No numeric columns found for graphing.")
    else:
        st.subheader("📈 Graphs")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Bar Chart")
            x_axis = st.selectbox("X-Axis", df.columns, key="bar_x")
            y_axis = st.selectbox("Y-Axis (numeric only)", numeric_cols, key="bar_y")

            if x_axis and y_axis:
                fig, ax = plt.subplots()
                df.groupby(x_axis)[y_axis].mean().plot(kind='bar', ax=ax)
                st.pyplot(fig)

        with col2:
            st.markdown("### Line Chart")
            x_axis = st.selectbox("X-Axis", df.columns, key="line_x")
            y_axis = st.selectbox("Y-Axis (numeric only)", numeric_cols, key="line_y")

            if x_axis and y_axis:
                fig, ax = plt.subplots()
                df.sort_values(by=x_axis).plot(x=x_axis, y=y_axis, kind='line', ax=ax)
                st.pyplot(fig)

        if len(numeric_cols) >= 2:
            st.markdown("### 📉 Correlation Heatmap")
            fig, ax = plt.subplots()
            corr = df[numeric_cols].corr()
            im = ax.imshow(corr, cmap='coolwarm')
            ax.set_xticks(range(len(numeric_cols)))
            ax.set_yticks(range(len(numeric_cols)))
            ax.set_xticklabels(numeric_cols, rotation=45, ha='right')
            ax.set_yticklabels(numeric_cols)
            fig.colorbar(im)
            st.pyplot(fig)
