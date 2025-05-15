import numpy as np

def train_linear_regression(file_path):
    charging_times = []
    battery_lives = []

    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                charge, life = map(float, line.strip().split(','))
                # Remove artificially clipped battery life entries
                if life < 8.0:
                    charging_times.append(charge)
                    battery_lives.append(life)

    X = np.array(charging_times).reshape(-1, 1)
    y = np.array(battery_lives)

    # Add bias column (intercept)
    X_b = np.hstack((np.ones((X.shape[0], 1)), X))

    # Normal equation: theta = (X^T X)^-1 X^T y
    XTX = X_b.T @ X_b
    if np.linalg.det(XTX) == 0:
        theta = np.linalg.pinv(XTX) @ X_b.T @ y
    else:
        theta = np.linalg.inv(XTX) @ X_b.T @ y

    return theta  # [intercept, slope]

def predict(charge_time, theta):
    intercept, slope = theta
    prediction = intercept + slope * charge_time
    return round(prediction, 2)

if __name__ == "__main__":
    theta = train_linear_regression("trainingdata.txt")
    try:
        charge_input = float(input().strip())
        result = predict(charge_input, theta)
        # Cap prediction at 8.0 if needed
        result = min(result, 8.0)
        print("{0:.2f}".format(result))
    except:
        print("Invalid input.")
