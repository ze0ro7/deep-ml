import numpy as np
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    # Your code here
    points = np.array(points, dtype=float)
    centroids = np.array(initial_centroids, dtype=float)

    for _ in range(max_iterations):
        # Step 1: Calculate distance between points and centroids
        distances = np.linalg.norm(
            points[:, np.newaxis] - centroids,
            axis=2
        )
        # Step 2: Assign each point to its nearest centroid
        clusters = np.argmin(distances, axis=1)

        # Step 3: Update centroids using cluster means
        new_centroids = np.array([
            points[clusters == i].mean(axis=0)
            if np.any(clusters == i)
            else centroids[i]
            for i in range(k)
        ])

        # Step 4: Stop if centroids don't change
        if np.allclose(centroids, new_centroids):
            centroids = new_centroids
            break

        centroids = new_centroids

    final_centroids = [tuple(c) for c in centroids]

    return final_centroids