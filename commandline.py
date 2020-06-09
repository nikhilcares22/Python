import argparse
import sys
def calc(args):
    if args.o=="add":
        return args.x+args.y

    elif args.o=="sub":
        return args.x-args.y

    elif args.o=="div":
        return args.x/args.y 

    elif args.o=="mul":
        return args.x*args.y
    else:
        return "ERROR"
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help="Enter the first number please contact me for more")
    parser.add_argument('--y',type=float,default=1.0,help="Enter the second number please contact me for more")
    parser.add_argument('--o',type=str,default="add",help="Enter the third number please contact me for more")
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))
