import argparse
import time

def stress_memory(string_number, seconds_alive):
    string_garbage = []
    for i in range(string_number):
        string_garbage.append(' ' * 512000000) # Allocation of 512 MB size strings
    time.sleep(seconds_alive)  # Keep the array in memory for x seconds to simulate stress
 

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        prog="python benchmark_ram.py",
        description="This program stresses the RAM by creating multiple 512 MB strings. The user can specify how many strings to generate and how long the strings will be kept in memory, allowing them to control both the memory usage and the duration of the stress test."
    )

    arg_parser.add_argument('string_number', type=int, help="Number of 512 MB size strings that will be created")
    arg_parser.add_argument('seconds_alive', type=int, help="Number of seconds that the strings will be stored")


    args = arg_parser.parse_args()

    stress_memory(args.string_number, args.seconds_alive)

