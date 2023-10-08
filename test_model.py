import random

# Number of test sets to generate
n_samples = 5

for i in range(n_samples):
    print(f"Sample {i+1}:")

    # Generate sample data
    timestamp_sample = random.uniform(1.5, 2.5)  # Assuming Timestamps were scaled and float64
    status_sample = random.choice([200, 404, 500])  # Assuming Status is one of these HTTP status codes
    method_delete_sample = random.uniform(0, 1)  # Assuming Method_DELETE was scaled and float64
    method_get_sample = random.uniform(0, 1)  # Assuming Method_GET was scaled and float64
    method_post_sample = random.uniform(0, 1)  # Assuming Method_POST was scaled and float64
    method_put_sample = random.uniform(0, 1)  # Assuming Method_PUT was scaled and float64

    # Output sample data
    print(f"  Timestamp: {timestamp_sample}")
    print(f"  Status: {status_sample}")
    print(f"  Method_DELETE: {method_delete_sample}")
    print(f"  Method_GET: {method_get_sample}")
    print(f"  Method_POST: {method_post_sample}")
    print(f"  Method_PUT: {method_put_sample}")
    print("---")
