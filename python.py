if __name__ == '__main__':
    N = int(input())
    foo = []
    bar = []
    for i in range(0, N):
        foo.append(input())
    for x in foo:
        if x[0:6] == "insert":
            bar.insert(int(x[7:8]), int(x[9:11]))
        elif x[0:6] == "remove":
            bar.remove(int(x[7:8]))
        elif x[0:5] == "print":
            print(bar)
        elif x[0:4] == "sort":
            bar.sort()
        elif x[0:7] == "reverse":
            bar.reverse()
        elif x[0:3] == "pop":
            bar.pop()

Your code did not pass this test case.
Input (stdin)
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Your Output (stdout)
[6, 5, 10]
[5, 10]
[5]
Expected Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
Compiler Message
Wrong Answer
