cimport numpy as np
import numpy as np


cdef double dist(double[:] x, double[:] y):
    """Calculate the distance"""
    cdef double dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i]) ** 2
    return dist

def find_labels(double[:, :] points, double[:, :] centers):
    """Assign points to a cluster."""
    cdef int n_points = points.shape[0]
    cdef int n_centers = centers.shape[0]
    cdef double[:] labels = np.zeros(n_points)
    cdef double distance, nearest_distance
    cdef int nearest_index

    for i in range(n_points):
        nearest_distance = np.inf
        for j in range(n_centers):
            distance = dist(points[i], centers[j])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_index = j
        labels[i] = nearest_index
    return np.asarray(labels)


def compute_centers(points, labels):
    """Calculate the cluster centres."""
    n_centers = len(set(labels))
    n_dims = len(points[0])
    
    centers = [[0 for i in range(n_dims)] for j in range(n_centers)]
    counts = [0 for j in range(n_centers)]
    
    for label, point in zip(labels, points):
        counts[label] += 1
        centers[label] = [a + b for a, b in zip(centers[label], point)]
        
    return [[x / count for x in center] for center, count in zip(centers, counts)]


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
