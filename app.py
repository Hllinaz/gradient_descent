import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp

from sidebar import Sidebar
from plot2d import two_dimension
from plot3d import three_dimension

def main():   
    st.set_page_config(layout="wide")
    
    alpha, steps, x0, y0, show_table = Sidebar()
    
    st.markdown(
        r"""
            ### Introduction
            
            This interactive app lets you experiment with the Gradient Descent algorithm on
            two-dimensional (single-variable) and three-dimensional (two-variable) functions.

            You can visualize how the algorithm iteratively moves toward a local minimum by
            following the direction of steepest descent at each step.

            The update rule used in the algorithm is:
            
            $$ \mathbf{v}_{n+1} = \mathbf{v}_n - \alpha \nabla f(\mathbf{v}_n), \ \forall n \in \mathbb{N}_0. $$
            
            where:
            
             * $\mathbb{N}_0 = \{ 0, 1, 2, ... \}.$
             * $\mathbf{v}_n$ is the current point.
             * $\alpha$ is the learning rate.
             * $\nabla f(\mathbf{v}_n)$ is the gradient of the function.
            
            #### Download
            
            The **plot can be downloaded as a PNG image** .
            
            The **table can be exported to Excel** for further analysis.
        """
    )

    tab1, tab2 = st.tabs(['2D Dimension', '3D Dimension'])
    
    with tab1:
        two_dimension(alpha, steps, x0, show_table)
    
    with tab2:
        three_dimension(alpha, steps, x0, y0, show_table)
    
if __name__ == "__main__":
    main()