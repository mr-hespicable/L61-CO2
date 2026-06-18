def validate(board: list):
    # board is n by n

    g = sum(board, [])
    n2n = len(board) * (len(board)-1)

    kv = {}
    for val in g:
        if val in kv.keys():
            kv[val] += 1
        else:
            kv[val] = 1

    if max(kv.values()) > n2n:
        return False
    else:
        return True
    

tests = int(input())

tf = []

for t in range(tests):
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]
    
    if validate(board):
        tf.append("YES")
    else:
        tf.append("NO")

print('\n'.join(tf))
