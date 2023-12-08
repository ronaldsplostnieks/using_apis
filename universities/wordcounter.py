counting_dict = {}
test_data = []

with open("teksts.txt", "r", encoding="utf8") as file:
    for line in file:
        for word in line.split():
            word = word.strip("[$@&().,!?:%-+;\n\"")
            test_data.append(word.lower())

for name in test_data:
    if name in counting_dict.keys():
        counting_dict[name] += 1
    else: 
        counting_dict[name] = 1

biggest = ""
biggest_value = 0

for key, value in counting_dict.items():
    if value > biggest_value:
        biggest_value = value
        biggest = key


print(biggest, biggest_value)