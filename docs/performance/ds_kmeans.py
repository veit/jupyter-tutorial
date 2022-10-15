from dask import array as da
from dask import dataframe as dd
import numpy as np

def find_labels(points, centers):
    """Assign points to a cluster."""
    diff = (points[:, None, :] - centers)
    distances = (diff ** 2).sum(-1)
    return distances.argmin(1)

def compute_centers(points, labels):
    """Calculate the cluster centres."""
    points_df = dd.from_dask_array(points)
    labels_df = dd.from_dask_array(labels)
    return points_df.groupby(labels_df).mean()

def kmeans(points, n_clusters):
    """Calculates the cluster centres repeatedly until nothing changes."""
    centers = points[-n_clusters:]
    points = da.from_array(points, 1000)
    while True:
        old_centers = centers
        labels = find_labels(points, da.from_array(centers, 5))
        centers = compute_centers(points, labels)
        centers = centers.compute().values
        if np.all(centers == old_centers):
            break
    return labels.compute()
