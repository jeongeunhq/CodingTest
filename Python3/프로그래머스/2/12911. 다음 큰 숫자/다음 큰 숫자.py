def solution(n):
    count=bin(n)[2:].count("1")

    while True:
        n+=1
        if count==bin(n)[2:].count("1"):
            break
        
    return n