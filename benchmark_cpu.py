import argparse
import time 

from multiprocessing import Pool

def calculate_primes(limit):
    primes = [1]
    for next_number in range(2, limit):
        next_prime = len(primes) - 1
        while next_prime != 0 and next_number % primes[next_prime] != 0:
            next_prime -= 1
        if next_prime == 0: primes.append(next_number)
          
    print(len(primes))

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        prog="python StressTestCPU.py",
        description=(
            "This program stresses the CPU by calculating all prime numbers up to a specified limit, "
            "the program can be configurated to repeat the function in different process to increase the stress."
        )
    )
    
    arg_parser.add_argument('upper_limit', type=int, help="The upper limit (inclusive) for the prime number search.")
    arg_parser.add_argument('-c', '--process', type=int, help="Number of process that will repeat the calculation", default=1)
    
    args = arg_parser.parse_args()
    
    start_time = time.time()

    process_args = [args.upper_limit] * args.process
    #print("Process args -> ",process_args)
    with Pool(processes=4) as pool:
        pool.map(calculate_primes, process_args)
    end_time = time.time()

    print(f"The calculation took {end_time - start_time} seconds")