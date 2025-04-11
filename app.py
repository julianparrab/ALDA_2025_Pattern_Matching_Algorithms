import sys
from src import algorithms
from src import execution_time_gathering
import matplotlib.pyplot as plt

if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 50000
    step = 5000
    samples_by_size = 10
    pattern_probability = 0

    table = execution_time_gathering.take_execution_time(
        minimum_size, maximum_size, step, samples_by_size, pattern_probability
    )

    print("Size | naive_search | kmp_search | boyer_moore_search | rabin_karp")
    for row in table:
        print(row)

    # Get Data for Plot Size vs Execution Time
    sizes = [row[0] for row in table]
    naive_search = [row[1] for row in table]
    kmp_search = [row[2] for row in table]
    boyer_moore_search = [row[3] for row in table]
    rabin_karp = [row[4] for row in table]

    fig, (plt1, plt2, plt3) = plt.subplots(3, 1, figsize=(8, 8))

    plt1.plot(sizes, naive_search, label="naive_search O(n * m)", marker="o")
    plt1.plot(sizes, kmp_search, label="kmp_search O(n + m)", marker="s")
    plt1.plot(sizes, boyer_moore_search, label="boyer_moore_search O(n + m)", marker="^")
    plt1.plot(sizes, rabin_karp, label="rabin_karp O(n*m)", marker="x")
    plt1.set_xlabel("Input Size")
    plt1.set_ylabel("Execution Time")
    plt1.set_title("Size vs Execution Time of Pattern Matching Algorithms P(0)")
    plt1.legend()

    pattern_probability = 0.5
    table1 = execution_time_gathering.take_execution_time(
        minimum_size, maximum_size, step, samples_by_size, pattern_probability
    )

    print("Size | naive_search | kmp_search | boyer_moore_search | rabin_karp")
    for row in table1:
        print(row)

    # Get Data for Plot Size vs Execution Time
    sizes = [row[0] for row in table1]
    naive_search = [row[1] for row in table1]
    kmp_search = [row[2] for row in table1]
    boyer_moore_search = [row[3] for row in table1]
    rabin_karp = [row[4] for row in table1]

    plt2.plot(sizes, naive_search, label="naive_search O(n * m)", marker="o")
    plt2.plot(sizes, kmp_search, label="kmp_search O(n + m)", marker="s")
    plt2.plot(sizes, boyer_moore_search, label="boyer_moore_search O(n + m)", marker="^")
    plt2.plot(sizes, rabin_karp, label="rabin_karp O(n*m)", marker="x")
    plt2.set_xlabel("Input Size")
    plt2.set_ylabel("Execution Time")
    plt2.set_title("Size vs Execution Time of Pattern Matching Algorithms P(0.5)")
    plt2.legend()

    pattern_probability = 1
    table2 = execution_time_gathering.take_execution_time(
        minimum_size, maximum_size, step, samples_by_size, pattern_probability
    )

    print("Size | naive_search | kmp_search | boyer_moore_search | rabin_karp")
    for row in table2:
        print(row)

    # Get Data for Plot Size vs Execution Time
    sizes = [row[0] for row in table2]
    naive_search = [row[1] for row in table2]
    kmp_search = [row[2] for row in table2]
    boyer_moore_search = [row[3] for row in table2]
    rabin_karp = [row[4] for row in table2]

    plt3.plot(sizes, naive_search, label="naive_search O(n * m)", marker="o")
    plt3.plot(sizes, kmp_search, label="kmp_search O(n + m)", marker="s")
    plt3.plot(sizes, boyer_moore_search, label="boyer_moore_search O(n + m)", marker="^")
    plt3.plot(sizes, rabin_karp, label="rabin_karp O(n*m)", marker="x")
    plt3.set_xlabel("Input Size")
    plt3.set_ylabel("Execution Time")
    plt3.set_title("Size vs Execution Time of Pattern Matching Algorithms P(1)")
    plt3.legend()

    plt.tight_layout()

    plt.show()
