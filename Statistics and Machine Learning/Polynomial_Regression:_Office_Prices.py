import numpy as np
from itertools import combinations_with_replacement

def generate_polynomial_features(X, degree):
    n_samples, n_features = X.shape
    features = [np.ones(n_samples)]  # bias term

    for deg in range(1, degree + 1):
        for comb in combinations_with_replacement(range(n_features), deg):
            feature = np.prod(X[:, comb], axis=1)
            features.append(feature)
    return np.vstack(features).T

if __name__ == "__main__":
    # Read input
    F, N = map(int, input().split())
    train_data = [list(map(float, input().split())) for _ in range(N)]
    train_data = np.array(train_data)

    train_features = train_data[:, :-1]
    train_targets = train_data[:, -1]

    T = int(input())
    test_features = np.array([list(map(float, input().split())) for _ in range(T)])

    # Generate polynomial features (up to degree 3)
    degree = 3
    X_train_poly = generate_polynomial_features(train_features, degree)
    X_test_poly = generate_polynomial_features(test_features, degree)

    # Solve for coefficients using least squares
    coefficients = np.linalg.lstsq(X_train_poly, train_targets, rcond=None)[0]

    # Make predictions
    predictions = X_test_poly @ coefficients
    for pred in predictions:
        print(f"{pred:.2f}")


