import numpy as np


def power_iteration(A, num_simulations):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    z = np.random.rand(A.shape[1])

    for m in range(num_simulations):
        print(f'm: {m}')
        print(f'z: {z}')
        if m > 0:
            print(f'l: {l}')

        if m > 1:
            if m > 2:
                old_error = error

            error = l-old_l
            print(f'error: {error}')
            if m > 2:
                print(f'ratio: {error/old_error}')

        w = np.dot(A,z)
        z = w/max(w)
        if m > 0:
            old_l = l

        l = w[2]/z[2]

A = np.array([[1,5,-8],[5,-2,5],[-8,5,1]])
power_iteration(A, 15)
