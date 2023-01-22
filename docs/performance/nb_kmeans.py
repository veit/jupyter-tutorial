import numba


@numba.jit(nopython=True)
def dist(x, y):
    """Calculate the distance"""
    dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i]) ** 2
    return dist


@numba.jit(nopython=True)
def find_labels(points, centers):
    """Assign points to a cluster."""
    labels = []
    min_dist = np.inf
    min_label = 0
    for i in range(len(points)):
        for j in range(len(centers)):
            distance = dist(points[i], centers[j])
            if distance < min_dist:
                min_dist, min_label = distance, j
        labels.append(min_label)
    return labels


def compute_centers(points, labels):
    """Calculate the cluster centres."""
    n_centers = len(set(labels))
    n_dims = len(points[0])

    centers = [[0 for i in range(n_dims)] for j in range(n_centers)]
    counts = [0 for j in range(n_centers)]

    for label, point in zip(labels, points):
        counts[label] += 1
        centers[label] = [a + b for a, b in zip(centers[label], point)]

    return [
        [x / count for x in center] for center, count in zip(centers, counts)
    ]


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
