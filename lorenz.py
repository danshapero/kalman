
import numpy as np
from scipy.integrate import ode
import random

# ------------------------------
def lorenz_rhs(sigma, rho, beta):
    def F(t, q):
        return [sigma * (q[1] - q[0]),
                q[0] * (rho - q[2]) - q[1],
                q[0] * q[1] - beta * q[2]]

    return F


# -----------------------------------------------------------------------
def lorenz(q0, t0, t1, sigma = 10.0, rho = 28.0, beta = 8.0/3, dt = 0.01):
    solver = ode(lorenz_rhs(sigma, rho, beta)).set_integrator('dopri5')
    solver.set_initial_value(q0, t0)

    solution = []
    while solver.successful() and solver.t < t1:
        solver.integrate(solver.t + dt)
        solution.append(solver.y)

    return np.asarray(solution)


observational_data = lorenz([5.1, 5.1, 5.1], 0.0, 10.0, dt = 0.05)
nt, _ = np.shape(observational_data)
for t in range(nt):
    for k in range(3):
        observational_data[t,k] += random.normalvariate(0.0, 0.35)
