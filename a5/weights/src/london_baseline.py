# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

with open('../birth_dev.tst', encoding='utf-8') as f:
    count = len(f.readlines())

(total, correct) = utils.evaluate_places("../birth_dev.tsv", ['London']*count)
print(f'Correct: {correct} out of {total}: {correct * 100 / total}%')