# ==========================================================
# 🚀 Math_Laplace Module
# ==========================================================
#
# This module provides a simple numerical implementation
# of the Laplace transform for 1D signals.
#
# Function:
#  - Laplace_function(func, s_points, t_max, dt)
#      Computes the Laplace transform F(s) of a time-domain
#      function `func(t)` using numerical integration (trapezoid rule).
#
# Arguments:
#  - func : callable function of time (t) returning ndarray
#  - s_points : ndarray of s values (Laplace domain)
#  - t_max : maximum time for integration (default 6.0)
#  - dt : time step for integration (default 0.001)
#
# Returns:
#  - ndarray of F(s) values corresponding to s_points
#
# ==========================================================

from module import imports

# get only np and Callable
np = imports().np
Callable = imports().Callable

def Laplace_function(func: Callable[[np.ndarray], np.ndarray],
                     s_points: np.ndarray,
                     t_max: float = 6.0,
                     dt: float = 0.001) -> np.ndarray:
    """
    Compute the numerical Laplace transform of a 1D time function.

    Parameters:
        func: callable function of time returning ndarray
        s_points: ndarray of Laplace variable values
        t_max: maximum integration time
        dt: time step

    Returns:
        ndarray of Laplace transform values at s_points
    """
    t = np.arange(0.0, t_max, dt)           # time vector
    value = func(t)                         # evaluate function at all t
    results = []
    for s in s_points:
        results.append(np.trapezoid(value * np.exp(-s * t), t))  # numerical integral
    return np.array(results)
