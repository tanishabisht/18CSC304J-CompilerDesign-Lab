# left recursion

def func(n):
    s = input("Enter the grammar:")
    if s[0] != s[3]:
        print("No left recursion")
    if s[0] == s[3]:
        l = len(s)
        alpha = ''
        beta = ''
        b = s[0]+"'"
        for i in range(l):
            if s[i] == "|":
                alpha = alpha+s[i+1:]
        for i in range(l):
            if s[i] == "|":
                beta = beta+s[4:i]
        alpha = alpha+b
        beta = beta+b
        print("___")
        print(s[0], "->", alpha)
        print(b, "->", beta, "| epsilon\n")


n = int(input("Enter number of transitions: \n"))
for i in range(n):
    func(i)
