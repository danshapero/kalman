
import numpy as np

def update(x0, C0, y, M, Q):
    """
    Parameters:
    ==========
    x0: prior estimate
    C0: covariance of the prior estimate
    y:  vector of measurements
    M:  measurement matrix
    Q:  covariance of the measurement process
    """

    # Precompute measurement matrix * a priori covariance
    MC = np.dot(M, C0)
    L = np.dot(MC, M.T) + Q

    # Compute the residual vector
    r = y - np.dot(M, x0)

    # Compute the a posteriori estimate and covariance
    x = x0 + np.dot(MC.T, np.linalg.solve(L, r))
    C = C0 - np.dot(MC.T, np.linalg.solve(L, MC))

    return x, C


if __name__ == "__main__":
    nn = 16
    z = np.array(map(lambda k: np.sin(2 * np.pi * k / nn), range(nn)))

    L = np.zeros((nn, nn), dtype = np.float64)

    for i in range(nn):
        j = (i + 1) % nn
        L[i, i] = 1.0
        L[i, j] = 0.5

    x0 = z + np.dot(L, np.random.randn(nn)) / 16
    C0 = np.dot(L, L.T) / 256

    y = np.zeros(nn/2)

    # The measurement matrix is a blurring kernel
    M = np.zeros((nn/2, nn), dtype = np.float64)
    for k in range(nn/2):
        i = 2*k
        j = 2*k + 1
        M[k, i] = 0.5
        M[k, j] = 0.5

    y = np.dot(M, x0) + np.random.randn(nn) / 16.0
