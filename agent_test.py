import random
import statistics

def main():
    # Generate 50 random data points
    data = [random.uniform(0, 100) for _ in range(50)]
    
    # Calculate mean and variance
    mean_val = statistics.mean(data)
    var_val = statistics.variance(data)
    
    print("--- Summary Statistics ---")
    print(f"Number of data points: {len(data)}")
    print(f"Mean: {mean_val:.4f}")
    print(f"Variance: {var_val:.4f}")

if __name__ == "__main__":
    main()
