from argparse import ArgumentParser as aparse

def create_parser():
    parser = aparse(description="""
    Sentry: watch over remote hosts and get notified if they are unreachable.
    """)

    parser.add_argument("toDo", help="Choose to run the check or add a host", required=True)

    return parser
