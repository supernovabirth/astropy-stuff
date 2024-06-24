def calculate_mean(fluxes):
    return sum(fluxes) / len(fluxes)


if __name__ == '__main__':
    mean = calculate_mean([1, 2.2, 0.3, 3.4, 7.9])
    print(mean)
