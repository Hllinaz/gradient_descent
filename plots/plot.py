import numpy as np
import plotly.graph_objects as go

def plot_margin(path, min_spread=5, scale=1.1):
    path = np.asarray(path)

    # ---- Caso 1D: (n,) o (n,1) ----
    if path.ndim == 1 or (path.ndim == 2 and path.shape[1] == 1):
        x = path.flatten()

        center = np.mean(x)
        max_range = abs(x.max() - x.min())
        spread = max(max_range * scale, min_spread)

        return center - spread, center + spread, None, None

    # ---- Caso 2D: (n,2) ----
    elif path.ndim == 2 and path.shape[1] == 2:
        x_center = np.mean(path[:, 0])
        y_center = np.mean(path[:, 1])

        max_range = max(
            abs(path[:, 0].max() - path[:, 0].min()),
            abs(path[:, 1].max() - path[:, 1].min()),
        )

        spread = max(max_range * scale, min_spread)

        return (
            x_center - spread,
            x_center + spread,
            y_center - spread,
            y_center + spread,
        )

    else:
        raise ValueError("path must be 1D or shape (n, 2)")

def  plot2d(path, f):
    x_min, x_max, y_min, y_max = plot_margin(path)
    
    x = np.linspace(x_min, x_max, 100)
    
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=x,
            y=f(x),
            mode='lines',
            opacity=0.7,
            line=dict(color='cyan', width=2),
            name='Function'
        )
    )
    
    xs = path[:, 0]
    ys = f(xs)
    
    fig.add_trace(
        go.Scatter(
            x=xs,
            y=ys,
            mode="lines",
            line=dict(color='red', width=2),
            name='Descense'
        )   
    )
    
    fig.add_trace(
        go.Scatter(
            x=[xs[0]],
            y=[ys[0]],
            mode="markers",
            marker=dict(color='blue', size=10),
            name='Start'
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=[xs[-1]],
            y=[ys[-1]],
            mode="markers",
            marker=dict(color='green', size=10),
            name='Final'
        )
    )
    
    fig.update_layout(
        xaxis_title='x',
        yaxis_title='y',
        showlegend=True,
        width=800,
        height=600
    )
    
    return fig

def plot3d(path, f):
    x_min, x_max, y_min, y_max = plot_margin(path)
    
    # ---- Superficie ----
    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    fig = go.Figure()
    
    fig.add_trace(
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            colorscale="Viridis",
            opacity=0.8,
            name="f(x,y)"
        )
    )
    
    xs = path[:, 0]
    ys = path[:, 1]
    zs = f(xs, ys)

    fig.add_trace(
        go.Scatter3d(
            x=xs,
            y=ys,
            z=zs,
            mode="lines+markers",
            line=dict(color="red", width=5),
            marker=dict(size=4),
            name="Gradient Descent"
        )
    )
    
    # ---- Punto inicial ----
    fig.add_trace(
        go.Scatter3d(
            x=[xs[0]],
            y=[ys[0]],
            z=[zs[0]],
            mode="markers",
            marker=dict(size=8, color="blue"),
            name="Start"
        )
    )

    # ---- Punto final ----
    fig.add_trace(
        go.Scatter3d(
            x=[xs[-1]],
            y=[ys[-1]],
            z=[zs[-1]],
            mode="markers",
            marker=dict(size=8, color="green"),
            name="Final"
        )
    )
    
    fig.update_layout(
        scene=dict(
            xaxis_title="x",
            yaxis_title="y",
            zaxis_title="f(x,y)"
        ),
        width=800,
        height=800,
        showlegend=False
    )
    
    return fig
    