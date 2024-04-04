from . import counts
import argparse

parser = argparse.ArgumentParser(
                    prog='Example Package',
                    description='Package dfescription... can be loadded from README.md')
 
parser.add_argument('--add_one', action='store_true', default=False, help='Add one to a number')

def main(args=None):
    args, leftovers = parser.parse_known_args()
    
    if args.add_one:    
        if len(leftovers) != 1:
            print("Please provide one number")
            exit(1)
        
        number_str = leftovers[0]
        if not leftovers[0].isnumeric():
            print("Please provide a integer number")
            exit(1)
        number = int(number_str)
        print(counts.add_one(number))
    
    else:
        parser.print_help()
