print("This program will print any word with letters removed as per user input")

s = input("Enter a word: ")
r = int(input("Enter how many letters you want to remove from the word: "))
s_l = len(s)
r_s = ""
for num in range(r, s_l):
    r_s += s[num]
print(f"This is the new word after removed {r} letters from the original word: {r_s}")