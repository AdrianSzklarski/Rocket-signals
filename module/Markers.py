import numpy as np
from matplotlib.patches import Polygon as pol


# --- HELPER FUNCTION ---------------------------------------------------------
def _compute_missile_triangle(x, y, angle_deg, L=0.40, W=0.18):
    """
    Computes the rotated and translated missile triangle coordinates.
    """
    # Base triangle (missile initially pointing downward)
    tri = np.array([
        [0, 0],          # Tip of the missile
        [-W / 2, -L],    # Bottom-left
        [W / 2, -L]      # Bottom-right
    ])

    # Rotation
    angle = np.radians(angle_deg)
    R = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])

    # Rotate and translate the triangle to (x, y)
    return tri.dot(R) + np.array([x, y])


# --- MISSILE CREATION --------------------------------------------------------
def make_missile(ax, x, y, angle_deg, color, label):
    """
    Creates a missile and adds it to the given axis.
    """
    # Compute rotated triangle
    tri_rot = _compute_missile_triangle(x, y, angle_deg)

    # Create polygon for missile outline
    poly = pol(
        tri_rot,
        closed=True,
        edgecolor=color,
        facecolor="none",
        linewidth=2
    )
    ax.add_patch(poly)

    # Add text label above the missile
    text = ax.text(x, y + 0.3, label, fontsize=10, color=color)

    return poly, text


# --- MISSILE UPDATE ----------------------------------------------------------
def update_missile(poly, text, x, y, angle_deg):
    """
    Updates the missile's position and orientation.
    """
    # Compute updated triangle coordinates
    tri_rot = _compute_missile_triangle(x, y, angle_deg)

    # Update polygon vertices
    poly.set_xy(tri_rot)

    # Update label position
    text.set_position((x, y + 0.3))

# --- RADAR FUNCTION ----------------------------------------------------------
def make_radar(ax, x, y, color="black", label="Radar"):
    """
    Creates a stationary radar at (x, y) as a cross.
    """
    size = 10  # length of the cross arms in km
    # Vertical line
    ax.plot([x, x], [y - size, y + size], color=color, linewidth=2)
    # Horizontal line
    ax.plot([x - size, x + size], [y, y], color=color, linewidth=2)
    # Label above the cross
    ax.text(x, y + size + 5, label, fontsize=10, color=color, ha='center')
