
import streamlit as st
import sympy as sp
import pandas as pd

from plots.plot import plot3d
from core.functions import build_function
from core.optimizer import learning

x_sym, y_sym = sp.symbols('x y')

def three_dimension(alpha, steps, x0, y0, show_table):
    st.title("Interactive Gradient Descent in Three Dimension (3D)")

    st.markdown(
        r"""            
            ### Instructions

            - Enter the **function of interest** in the **$f(x,y)$** input field (e.g. `x**2 + y**2`, `cos(x)+sin(y)`).
            - The derivative **$\nabla f(x,y)$** is computed automatically and represents the gradient.
            - Use the sidebar to adjust the **learning rate $\alpha$**, the **number of steps**, and the **initial point $x_0$ and $y_0$**.
            - The plot shows the function together with the path followed by the gradient descent algorithm.
            - The table displays the numerical values obtained at each iteration.
        """
    )

    # --- Function input (single logical block) ---
    st.subheader("Function")
    
    fx_col, input_col = st.columns([1, 5])

    with fx_col:
        st.latex("f(x, y)")
    with input_col:
        function = st.text_input(
            label="",
            placeholder="x**2 + y**2",
            label_visibility="collapsed",
            key="function_3d"
        )
        function = function.replace("^", "**")
    
    if not function:
        st.info("Enter a function to start the simulation.")
        return

    try:
        # --- Symbolic math ---
        expr = sp.sympify(function)
        grad_expr = (
            sp.diff(expr, x_sym),
            sp.diff(expr, y_sym)
        )

        f_num, grad_num = build_function(expr, [x_sym,y_sym])
        
        vec = learning(
            initial_point=[x0,y0],
            grad_f=grad_num,
            alpha=alpha,
            steps=steps,
        )
        
        st.divider()
        
        if show_table:
            space = [3,2]
        else:
            space = [3,1]
        
        plot_col, table_col = st.columns(space, gap="large")

        with plot_col:
            st.subheader("Gradient Descent Visualization")
            st.latex(rf"f(x, y) = {sp.latex(expr)}")
            st.latex(
                rf"""
                    \nabla f(x, y) = 
                    \begin{{pmatrix}}
                    {sp.latex(grad_expr[0])} \\
                    {sp.latex(grad_expr[1])}
                    \end{{pmatrix}}
                """
            )
            
            fig = plot3d(vec, f_num)
            
            st.plotly_chart(fig, width='stretch')
        
        if show_table:
            with table_col:
                st.subheader("Iteration data")

                xs = vec[:, 0]
                ys = vec[:, 1]

                gx = []
                gy = []

                for x, y in vec:
                    gxi, gyi = grad_num(x, y)
                    gx.append(gxi)
                    gy.append(gyi)

                data = pd.DataFrame(
                    {
                        r"$x$": xs,
                        r"$y$": ys,
                        r"$f(x,y)$": [f_num(x, y) for x, y in vec],
                        r"$\partial f / \partial x$": gx,
                        r"$\partial f / \partial y$": gy,
                    },
                )

                st.table(data.style.format("{:.3f}"))
                
                if st.button("Export to excel", key='3d'):
                    data.to_excel('data.xlsx')
                
    except Exception as e:
        st.error(f"Error parsing function: {e}")