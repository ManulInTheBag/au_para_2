import argparse


def find_args():
    parser = argparse.ArgumentParser(
        prog='au_para_2',
        description='Trying to sum arguments'
    )
    parser.add_argument('ELEMENT', type=int, nargs='+')
    return parser.parse_args()