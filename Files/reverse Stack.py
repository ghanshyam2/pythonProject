def reverseStack(St):
    def swap(indx, n, St):
        if indx > n:
            return
        St[indx], St[n] = St[n], St[indx]

        swap(indx + 1, n - 1, St)

    swap(0, len(St) - 1, St)


print(reverseStack([4, 5, 7]))
