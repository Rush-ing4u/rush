q = 'is'
start = 0
while True:
    pos = long_msg.find(q, start)
    start = pos + 1
    if pos == -1:
        break
    print(pos)