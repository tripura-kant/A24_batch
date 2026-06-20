# Print 1 to N using recursion

N = 5
i = 1
def func(i,N):
    if i > N:
        return
    print(i)
    func(i+1,N)

func(i,N)

