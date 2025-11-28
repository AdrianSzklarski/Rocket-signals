# ==========================================================
# 🚀 Rocket Laplace Test
# ==========================================================
#
# Minimal test for Laplace_function module.
# Demonstrates computing Laplace transform of a target signal.
#
# Features:
#  - Define a target function Y(t)
#  - Compute Laplace transform F(s) for a range of s values
#  - Save |F(s)| plot to PNG (no GUI required)
#
# Author:
# Date: 2025-11-28
# ==========================================================

from module import imports
from module.Math_Laplace import Laplace_function
import matplotlib
matplotlib.use('TkAgg')   # <- interaktywny backend
import matplotlib.pyplot as plt

np = imports().np

if __name__ == "__main__":
    try:
        # --- Example target function ---
        target_y = lambda t: np.sin(t) + 0.1 * np.random.randn(len(t))  # small noise

        # --- s points in Laplace domain ---
        s_values = np.linspace(0.1, 5, 50)

        # --- Call Laplace_function ---
        F_s = Laplace_function(
            func=target_y,
            s_points=s_values,
            t_max=6.0,
            dt=0.001
        )

        # --- Print results ---
        print("F(s) =", F_s)

        # --- Plot and save to file ---
        plt.plot(s_values, np.abs(F_s))
        plt.xlabel('s')
        plt.ylabel('|F(s)|')
        plt.title('Laplace Transform of Target Position')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("laplace_test.png")
        print("Plot saved as laplace_test.png")
        plt.show()

    except Exception as e:
        print("Error during Laplace test:", e)
