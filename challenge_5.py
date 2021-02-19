import pickle

with open("banner.p", "rb") as f:
    something = pickle.load(f)
    for row in something:
        for something2 in row:
            print(something2[0] * something2[1], end="")
        print("")