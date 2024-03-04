import streamlit as st
import matplotlib.pyplot as plt
import mpld3
import plotly.express as px

# Using mpld3
def mpld3_plot():
    # Create a sample Matplotlib plot
    fig, ax = plt.subplots()
    ax.plot(range(10))

    # Convert using mpld3
    mpld3_fig = mpld3.fig_to_html(fig)
    st.write(mpld3_fig, unsafe_allow_html=True)

# Using Plotly
def plotly_plot():
    # Sample data
    df = px.data.iris()

    # Create a Plotly figure 
    fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species")

    # Display in Streamlit
    st.plotly_chart(fig)

# Sidebar selection
option = st.sidebar.selectbox(
    'Select Plot Type:',
    ('Matplotlib (mpld3)', 'Plotly')
)

# Main app
st.title('Interactive Plots')

if option == 'Matplotlib (mpld3)':
    mpld3_plot()
elif option == 'Plotly':
    plotly_plot()
