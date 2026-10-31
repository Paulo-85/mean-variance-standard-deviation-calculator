import numpy as np


def calculate(list):
    """Return column, row, and overall statistics for nine numbers."""
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)
    operations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    calculations = {}
    for name, operation in operations.items():
        calculations[name] = [
            operation(matrix, axis=0).tolist(),
            operation(matrix, axis=1).tolist(),
            operation(matrix).item(),
        ]

    return calculations
