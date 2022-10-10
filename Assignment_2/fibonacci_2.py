Number = int(input("\nPlease Enter the Range of no:- : "))
i = 0
F_Value = 0
S_Value = 1
while(i < Number):
    if(i <= 1):
        Next = i
    else:
        Next = F_Value + S_Value
        F_Value = S_Value
        S_Value = Next
    print(Next)
    i = i + 1