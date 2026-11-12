import numpy as np

def calculate_portfolio_variance(cov_matrix: list[list[float]], weights: list[float]) -> float:
    """
    Calculate the variance of a portfolio.

    Args:
        cov_matrix (list[list[float]]): Covariance matrix of asset returns.
        weights (list[float]): Portfolio weights.

    Returns:
        float: Portfolio variance.
    """
    # Your code here
    weights = np.array(weights, dtype = float)
    cov_matrix = np.array(cov_matrix, dtype = float)
    variance = weights.T @ cov_matrix@weights
    return float(variance)