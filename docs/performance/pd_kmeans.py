import numpy as np
import pandas as pd

def find_labels(points, centers):
    """Assign points to a cluster."""
    diff = (points[:, None, :] - centers)
    distances = (diff ** 2).sum(-1)
    return distances.argmin(1)


def compute_centers(points, labels):
    """Calculate the cluster centres."""
    df = pd.DataFrame(points)
    return df.groupby(labels).mean().values


def kmeans(points, n_clusters):
    """Calculates the cluster centres repeatedly until nothing changes."""
    centers = points[-n_clusters:].tolist()
    while True:
        old_centers = centers
        labels = find_labels(points, centers)
        centers = compute_centers(points, labels)
        if centers == old_centers:
            break
    return labels
