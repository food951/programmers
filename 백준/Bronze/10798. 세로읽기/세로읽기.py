
str1 = input()
str2 = input()
str3 = input()
str4 = input()
str5 = input()
str6 = ""
max_length = max(len(str1), len(str2), len(str3), len(str4), len(str5))

str1 = str1.ljust(max_length)
str2 = str2.ljust(max_length)
str3 = str3.ljust(max_length)
str4 = str4.ljust(max_length)
str5 = str5.ljust(max_length)


for i in range(max_length):
    if str1[i]!=" ":
        str6 +=str1[i]
    if str2[i]!=" ":
        str6 +=str2[i]
    if str3[i]!=" ":
        str6 +=str3[i]
    if str4[i]!=" ":
        str6 +=str4[i]
    if str5[i]!=" ":
        str6 +=str5[i]
print(str6)

    