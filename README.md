# Stress Test Programs for CPU and Memory

This repository contains Python programs designed to stress test both the CPU and memory. These tests are useful for evaluating performance and stability in monitored environments, such as during infrastructure benchmarking or system diagnostics.

This repository contains two distinct programs:

**benchmark_cpu.py:**

This program stresses the CPU by checking for prime numbers, iterating sequentially from 1 to a given upper limit. It is highly CPU-intensive as it performs no I/O operations, involving substantial calculations. Users can specify the number of processes to run concurrently, enabling full utilization of all CPU cores and providing a robust CPU stress test.

**benchmark_ram.py:**

This program stresses the RAM by creating multiple strings, each of size 512 MB. The user can specify the number of strings to generate, controlling the total memory consumed during the test. Additionally, the user can set how long these strings will remain in memory, allowing control over both memory usage and the duration of the test. This provides a flexible tool for simulating high memory load scenarios.


## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Prerequisites](#prerequisites)

## Installation

To clone the repository and install any dependencies, run the following commands:

```bash
git clone https://github.com/DiegoBaleironPais/stress-test.git
cd stress-tests
```

## Usage
**CPU Stress**
usage: python StressTestCPU.py [-h] [-c CORES]

**RAM Stress**
usage: python benchmark_ram.py [-h] string_number seconds_alive

## Prerequisites
CPU test doesn´t use any non default library.

RAM test needs numpy.

pip install numpy