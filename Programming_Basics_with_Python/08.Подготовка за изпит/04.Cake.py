l = int(input())
w = int(input())
size = l*w
pieces_taken = int(input())
pieces_remaining = size

while size/pieces_taken >= 1:
    pieces_taken = int(input())
    pieces_taken += pieces_taken
    if size/pieces_remaining <1:
        print("stop")






