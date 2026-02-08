import streamlit as st
import pandas as pd
import sympy as sp

from plots.plot import plot2d
from core.functions import build_function
from core.optimizer import learning

x_sym = sp.symbols('x')

def two_dimension(alpha, steps, x0, show_table):
    st.title("Interactive Gradient Descent in Two Dimension (2D)")

    st.markdown(
        r"""            
            ### Instructions

            - Enter the **function of interest** in the **$f(x)$** input field (e.g. `x**2`, `x**2 + 3*x + 1`).
            - The derivative **$f'(x)$** is computed automatically and represents the gradient.
            - Use the sidebar to adjust the **learning rate $\alpha$**, the **number of steps**, and the **initial point $x_0$**.
            - The plot shows the function together with the path followed by the gradient descent algorithm.
            - The table displays the numerical values obtained at each iteration.
        """
    )

    # --- Function input (single logical block) ---
    st.subheader("Function")

    fx_col, input_col = st.columns([1, 5])
    with fx_col:
        st.latex("f(x)")
    with input_col:
        function = st.text_input(
            label="",
            placeholder="x**2 + 3*x + 1",
            label_visibility="collapsed",
            key="function_2d"
        )
        function = function.replace("^", "**")

    if not function:
        st.info("Enter a function to start the simulation.")
        return

    try:
        # --- Symbolic math ---
        expr = sp.sympify(function)
        derivative = sp.diff(expr, x_sym)

        f_num, grad_num = build_function(expr, [x_sym])

        vec = learning(
            initial_point=[x0],
            alpha=alpha,
            steps=steps,
            grad_f=grad_num,
        )

        st.divider()
        
        if show_table:
            space = [3,2]
        else:
            space = [3,1]
        
        plot_col, table_col = st.columns(space, gap="large")

        with plot_col:
            st.subheader("Gradient Descent Visualization")
            st.latex(rf"f(x) = {sp.latex(expr)}")
            st.latex(rf"f'(x) = {sp.latex(derivative)}")

            fig = plot2d(vec, f_num)
            
            st.plotly_chart(fig, width='content')

        if show_table:
            with table_col:
                st.subheader("Iteration data")
                
                xs = vec[:, 0]

                data = pd.DataFrame(
                    {
                        r"$x$": xs,
                        r"$f(x)$": [f_num(x) for x in xs],
                        r"$f'(x)$": [grad_num(x) for x in xs],
                    },
                )
                
                st.table(data.style.format("{:.3f}"))
                
                if st.button("Export to excel", key='2d'):
                    data.to_excel('data.xlsx')
                
    except Exception as e:
        st.error(f"Error parsing function: {e}")