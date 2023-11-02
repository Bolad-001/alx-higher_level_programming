#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined in hidden_4 module."""
    import hidden_4

    name = dir(hidden_4)
    for i in name:
        if i[:2] != "__":
            print(i)
