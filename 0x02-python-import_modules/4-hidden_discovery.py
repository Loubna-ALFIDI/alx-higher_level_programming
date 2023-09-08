#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for str in range(dir(hidden_4)):
        if dir(hidden_4)[str][:2] == "__":
            continue
        else:
            print("{}".format(str))
