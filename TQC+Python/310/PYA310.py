def compute(n: int) -> int:
    nums = [i for i in range(1, n) if sum(int(j) ** len(str(i)) for j in str(i)) == i]
    print("\n".join((*map(str,nums),)),sum(nums),sep="\n")

a = eval(input())

compute(a)