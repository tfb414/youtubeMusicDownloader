if __name__ == "__main__":
    main()

import os
import glob


def main():
    files = glob.glob('tmp/*')
    for f in files:
        print(f)
        os.remove(f)

    hidden_files = glob.glob('tmp/.*')
    for f in hidden_files:
        print(f)
        os.remove(f)


main()
