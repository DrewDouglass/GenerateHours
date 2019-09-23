#!python3
import sys


def main():
    # Example 2019-09-22
    date_arg = sys.argv[1]
    print(f'Generating hours for: {date_arg}')
    for i in range(24):
        #2019-09-22 01
        #2019-09-22 02 etc
        print(f'{date_arg} {str(i).zfill(2)}')


if __name__ == "__main__":
    main()
