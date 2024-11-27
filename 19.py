moves = input("enter movments seprated with * : ").split("*")
moves.pop()
print(moves)
cont = 0
for move in moves:
    if move[0] == move[-1] :
        cont+=1
print(cont)  