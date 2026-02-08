import streamlit as st

from datetime import datetime

def Sidebar():
    with st.sidebar:
        st.header("Gradient Descent Settings")
        
        alpha = st.slider(
            r"Learning Rate ($\alpha$)",
            min_value=0.01,
            max_value=1.0,
            value=0.3,
            step=0.01,
        )
        
        steps = st.slider(
            r"Number of steps",
            min_value=3,
            max_value=25,
            value=8,
            step=1,
        )
        
        st.write("Inicial Point")
        
        xcolummns, ycolumns = st.columns(2)
        
        with xcolummns:
            x0 = st.number_input("$x_0$", value=3.0)
            pass
        
        with ycolumns:
            y0 = st.number_input("$y_0$", value=3.0)
            pass
        
        st.header("Configurations")
        
        show_table = st.checkbox("Show Table")
        last_update = datetime.now().strftime("%Y-%m-%d")
        
        st.markdown(
            f"""
            <hr>
            <div style="text-align: center; font-size: 0.9em; color: gray;">
                <p style="margin-bottom: 8px;"><strong>Developed by:</strong></p>
                <p style="margin: 2px 0;">Humberto J. Llinas M. (lhumberto@uninorte.edu.co)</p>
                <p style="margin: 2px 0;">Dr. rer. nat. Humberto J. Llinas S. (hllinas@uninorte.edu.co)</p>
                <p style="margin-top: 20px;"><em>Last updated: {last_update}</em></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    return alpha, steps, x0, y0, show_table

    
    