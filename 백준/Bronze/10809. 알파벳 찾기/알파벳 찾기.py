S = input()
list1= list(S)
alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet_list=list(alphabet)
for i in range(len(alphabet_list)):
    if alphabet_list[i] in list1:
         print(list1.index(alphabet_list[i]), end = " ")
    else :
        print(-1, end = " ")