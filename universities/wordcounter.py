counting_dict = {}
test_data = []

with open("teksts.txt", "r", encoding="utf8") as file:
    for line in file:
        for word in line.split():
            word = word.strip("[$@&().,!?:%-+;\n\"")
            if len(word) > 3:
                test_data.append(word.lower())


# for name in test_data: 
#     name_key = name[:4]
#     if name_key in counting_dict.keys(): 
#         counting_dict[name_key] += 1 
#     else: 
#         counting_dict[name_key] = 1

for name in test_data: 
    if name in counting_dict.keys(): 
        counting_dict[name] += 1 
    else: 
        counting_dict[name] = 1

for key, value in counting_dict.items():
    print(key, value)

scounting_dict = sorted(counting_dict.items(), key=lambda x: x[1], reverse=True)[:5]
print(scounting_dict)