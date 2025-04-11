import time
import random
from src import algorithms
from src import constants
from src import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size, pattern_probability):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size, pattern_probability)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size, pattern_probability):
    samples = [
        data_generator.generate_random_text_and_pattern(size, pattern_probability) for _ in range(samples_by_size)
    ]
    # print("samples: " + str(samples))

    return [
        take_time_for_algorithm(samples, algorithms.naive_search),
        take_time_for_algorithm(samples, algorithms.kmp_search),
        take_time_for_algorithm(samples, algorithms.boyer_moore_search),
        take_time_for_algorithm(samples, algorithms.rabin_karp),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, algorithm):
    times = []

    for sample in samples_array:
        start_time = time.time()
        # print("sample: " + str(sample))
        res = algorithm(sample[0], sample[1])
        print(str(algorithm) + " res: " + str(res))
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
