def ArcTg(X):
    Sum= X
    Term= X
    Y= - X * X

    for I in range(3, 17, 2):
        Term*= Y
        Sum+= Term / I

    return Sum

print(16 * ArcTg(1. / 5) - 4 * ArcTg(1. / 239))
