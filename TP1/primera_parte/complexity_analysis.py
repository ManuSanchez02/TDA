from timeit import timeit
from matplotlib import pyplot as plt
from kmerge_dyc import kmerge as kmerge_dyc
from kmerge_heap import kmerge as kmerge_heap
from utils import random_sorted_array

CASES = 100

def plot_k_constant(k, kmerge):
    case_multiplier = 1
    cases = [[random_sorted_array(i*case_multiplier) for _ in range(k)] for i in range(CASES)]

    dyc_times = [timeit(lambda: kmerge(*case), number=10) for case in cases]

    plt.xlabel("Cantidad de elementos por arreglo (h)")
    plt.ylabel("Tiempo de ejecucion (ms)")
    plt.title("Complejidad temporal")
    plt.plot([i*case_multiplier for i in range(CASES)], dyc_times, label='O(n)')

    plt.show()

def plot_h_constant(h, kmerge):
    case_multiplier = 10

    cases = [[random_sorted_array(h) for _ in range(i*case_multiplier)] for i in range(CASES)]

    dyc_times = [timeit(lambda: kmerge(*case), number=10) for case in cases]

    plt.xlabel("Cantidad de elementos por arreglo (h)")
    plt.ylabel("Tiempo de ejecucion (ms)")
    plt.title("Complejidad temporal")
    plt.plot([i*case_multiplier for i in range(CASES)], dyc_times, label='O(n)')

    plt.show()


plot_k_constant(5, kmerge_dyc)