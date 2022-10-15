import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

def find_labels(points, centers):
    """Assign points to a cluster."""
    distances, labels = cKDTree(centers).query(points, 1)
    return labels


def compute_centers(points, labels):
    """Calculate the cluster centres."""
    df = pd.DataFrame(points)
    return df.groupby(labels).mean().values


def kmeans(points, n_clusters):
    """Calculates the cluster centres repeatedly until nothing changes."""
    centers = points[-n_clusters:]
    while True:
        old_centers = centers
        labels = find_labels(points, centers)
        centers = compute_centers(points, labels)
        if np.all(centers == old_centers):
            break
    return labels
