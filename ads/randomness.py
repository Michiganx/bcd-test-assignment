import random
import sys

HELP_TEXT = 'Usage: python randomness.py <file> <K>'


if __name__ == '__main__':
    if '-h' in sys.argv or len(sys.argv) != 3:
        print(HELP_TEXT)
        exit()
    else:
        path, k = sys.argv[1], int(sys.argv[2])
        result = []
        try:
            with open(path) as f:
                ads = f.read().splitlines()
            result = random.sample(ads, k)  # Will throw ValueError if k>len(ads)
        except IOError:
            print('file', path, 'not found or corrupt')
        except ValueError:
            print('K is bigger than the list')
            print('shuffling the list')
            random.shuffle(ads)  # Shuffling in place, no additional memory required.
            result = ads

        for item in result:
            print(item)
