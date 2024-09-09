# Stress Test Programs for CPU and Memory

This repository contains Python programs designed to stress test both the CPU and memory. These tests are useful for evaluating performance and stability in monitored environments, such as during infrastructure benchmarking or system diagnostics.

This repository contains two distinct programs:

**benchmark_cpu.py:**

This program checks for prime numbers by iterating sequentially from 1 to a given upper limit. It is highly CPU-intensive, as it performs no I/O operations and involves substantial calculations. The program also allows users to specify the number of processes that will run concurrently, enabling full utilization of all CPU cores and providing a robust CPU stress test.

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