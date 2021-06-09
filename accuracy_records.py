# Japanese and Hindi (full Hindi dataset, 1000 spectrograms for Japanese)
error_rates = [0.029586, 0.059172, 0.065476, 0.017857, 0.011905, 0.029762, 0.059524, 0.029762, 0.053892, 0.017964]
accuracy = 1 - sum(error_rates) / 10
print(f"Overall accuracy is {accuracy * 100}%")
# Overall accuracy is 96.251%

# Japanese and Arabic (3000 spectrograms each)


# Japanese, Arabic, and Chinese (3000 spectrograms each)
error_rates = [0.052083, 0.044838, 0.052192, 0.056367, 0.068894, 0.060543, 0.056367, 0.062630, 0.043887, 0.055381]
accuracy = 1 - sum(error_rates) / 10
print(f"Overall accuracy is {accuracy * 100}%")
# Overall accuracy is 94.46818%

# Japanese, Arabic, Chinese, and Russian (3000 spectrograms each)
error_rates = [0.039588, 0.049921, 0.045995, 0.048374, 0.057891, 0.054718, 0.046788, 0.038858, 0.043685, 0.042891]
accuracy = 1 - sum(error_rates) / 10
print(f"Overall accuracy is {accuracy * 100}%")
# Overall accuracy is 95.31290999999999%

# Japanese, Arabic, Chinese, Russian, and Spanish (3000 spectrograms each)
error_rates = [0.058824, 0.049264, 0.052497, 0.055058, 0.061460, 0.063380, 0.058899, 0.056978, 0.047466, 0.051956]
accuracy = 1 - sum(error_rates) / 10
print(f"Overall accuracy is {accuracy * 100}%")
# Overall accuracy is 94.44218% 

# Japanese, Arabic, Chinese, Russian, Spanish, and Hindi (618 spectrograms for Hindi, 3000 spectrograms for every other language)
error_rates = [0.063961, 0.052308, 0.060961, 0.062192, 0.065887, 0.070813, 0.054803, 0.057882, 0.050617, 0.064815]
accuracy = 1 - sum(error_rates) / 10
print(f"Overall accuracy is {accuracy * 100}%")
# Overall accuracy is 93.95761%


# Spanish and Portuguese
pt_vs_es_error_rates = [0.034711, 0.028099, 0.031405, 0.039669, 0.033058, 0.034711, 0.039735, 0.024834, 0.033167, 0.033167]

# Russian and Ukrainian
uk_vs_ru_error_rates = [0.014803, 0.019737, 0.018092, 0.023026, 0.021382, 0.019737, 0.023026, 0.016447, 0.009885, 0.019769]
