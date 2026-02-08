import numpy as np

def learning(initial_point, grad_f, alpha=0.1, steps=50, epsilon=1e-6):
    """
    Gradient Descent with convergence criterion
    """
    x = np.array(initial_point, dtype=float)
    path = [x.copy()]

    for _ in range(steps):
        grad = np.array(grad_f(*x), dtype=float)
        x_new = x - alpha * grad

        # criterio de convergencia
        if np.linalg.norm(x_new - x) < epsilon:
            x = x_new
            path.append(x.copy())
            break

        x = x_new
        path.append(x.copy())

    return np.array(path)



