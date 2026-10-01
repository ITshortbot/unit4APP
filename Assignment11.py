# Apply pandas to create a series containing ten random numbers and perform indexing,
# filtering, and statistical operations such as mean, median, minimum, and maximum.
import pandas as pd
import numpy as np


def analyze_series(series):
    print("Original Series:")
    print(series)

    # Indexing using positional access for pandas Series
    print("\nFirst element:")
    print(series.iloc[0])

    print("\nLast element:")
    print(series.iloc[-1])

    # Filtering
    print("\nElements greater than 50:")
    print(series[series > 50])

    # Statistical operations
    print("\nMean:", series.mean())
    print("Median:", series.median())
    print("Minimum:", series.min())
    print("Maximum:", series.max())


def main():
    numbers = pd.Series(np.random.randint(1, 100, size=10), name="Random Numbers")
    analyze_series(numbers)


if __name__ == "__main__":
    main()
