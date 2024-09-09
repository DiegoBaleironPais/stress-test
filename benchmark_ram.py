import argparse
import time
import numpy as np

def stress_memory(size_in_gb):
    # Convert GB to bytes
    size_in_bytes = size_in_gb * (1024 ** 3)
    # Create a large array to consume the specified amount of memory
    try:
        large_array = np.zeros(size_in_bytes, dtype=np.uint8)
        print(f"Allocated {size_in_gb} GB of memory.")
        time.sleep(90)  # Keep the array in memory for 60 seconds to simulate stress
    except MemoryError:
        print(f"Failed to allocate {size_in_gb} GB of memory. Not enough RAM.")

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        prog="python StressTestMemory.py",
        description=(
            "This program stresses the memory by allocating a large array of a specified size in GB."
        )
    )
    
    arg_parser.add_argument('size', type=int, help="The amount of memory to allocate in GB.")
    
    args = arg_parser.parse_args()
    
    start_time = time.time()
    stress_memory(args.size)
    end_time = time.time()
    
    print(f"Memory stress test completed in {end_time - start_time} seconds")
