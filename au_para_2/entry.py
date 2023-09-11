from . import find_args


def help():
    args = find_args()
    print(f'You typed {", ".join(str(s) for s in args.ELEMENT)} Sum is {sum(args.ELEMENT)}')
