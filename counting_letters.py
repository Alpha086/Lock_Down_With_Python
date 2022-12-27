text = input()
print("--------------------------------------------------")
print("printing counted letters")
x = " "

for i in range(len(text)):
    count = 1
    for j in range(i+1, len(text)):
        if text[i] == text[j]:
            count += 1
    if text[i] == x:
        continue
    print(text[i], "=", count)
    x = text[i]



