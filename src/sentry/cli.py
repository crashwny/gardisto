from argparse import ArgumentParser as aparse
from sentry import hostentry, hostcheck
import sys
def create_parser():
    parser = aparse(description="""
    Sentry: watch over remote hosts and get notified if they are unreachable.
    """)

    parser.add_argument("toDo", help="Choose to run the check or add a host")

    return parser

def main():
    from sentry import hostentry, hostping, hostcheck 
    args = create_parser().parse_args()
    if args.toDo == 'addhost':
        hostentry.processdata()
        sys.exit()
    if args.toDo == 'run':
        hostcheck.start()
        sys.exit()

