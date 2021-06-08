# Japanese and Hindi (full Hindi dataset, 1000 spectrograms for Japanese)
error_rates = [0.029586, 0.059172, 0.065476, 0.017857, 0.011905, 0.029762, 0.059524, 0.029762, 0.053892, 0.017964]
accuracy = 1 - sum(error_rates) / 10
print(f"Overall accuracy is {accuracy * 100}%")
# Overall accuracy is 96.251%

# Japanese and Arabic (3000 spectrograms each)


# Japanese, Arabic, and Chinese (3000 spectrograms each)
error_rates = [0.052083, 0.044838, 0.052192, 0.056367, 0.068894, ]
accuracy = 1 - sum(error_rates) / 10
print(f"Overall accuracy is {accuracy * 100}%")

# Japanese, Arabic, Chinese, and Russian (3000 spectrograms each)
# Japanese, Arabic, Chinese, Russian, and Spanish (3000 spectrograms each)
# Japanese, Arabic, Chinese, Russian, Spanish, and Hindi (618 spectrograms for Hindi, 3000 spectrograms for every other language)
error_rates = [0.063961, 0.052308, 0.060961, 0.062192, 0.065887, 0.070813, 0.054803, 0.057882, 0.050617, 0.064815]
accuracy = 1 - sum(error_rates) / 10
print(f"Overall accuracy is {accuracy * 100}%")
# Overall accuracy is 93.95761%
