N = int(input())

def soultion(N) :
    i = 2
    while(1) :
        if N % i == 0 :
            print(i)
            N = N // i
        else :
            i+=1

        if N == 1:
            break

soultion(N)
