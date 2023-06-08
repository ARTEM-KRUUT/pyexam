def main(s):
    z = int(s, 16)
    return z & 15, (z >> 4) & 31, (z >> 16) & 7
