f = open("marathi_training_data.txt", "r", encoding="utf-8")
w = open("marathi_testing_ann.txt", "w", encoding="utf-8")

lines = f.readlines()

for i in range(0, len(lines)):
    if i > 200000:
        w.write(lines[i])

