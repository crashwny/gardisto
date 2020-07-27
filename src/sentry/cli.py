from argparse import ArgumentParser as aparse
from sentry import hostentry, hostcheck, removehost, hostInfo
import sys
def create_parser():
    parser = aparse(description="""
    Sentry: Monitor local and remote hosts and get notified if they are unreachable.
    """)

    parser.add_argument("toDo", help="Choose to run the check or add a host")
    parser.add_argument('-host', action="store", dest='host', help="Enter a hostname for the desired action")
    parser.add_argument('-all', dest="allhost", action="store_true", help="Use all hosts for desired action")
    parser.add_argument('-stat', action="store", dest="stat", help="Enter a specific statistic to check")
    parser.add_argument('-stats', action="store_true", help="Run check with all statistics")
    return parser

def main():
    from sentry import hostentry, hostping, hostcheck 
    args = create_parser().parse_args()
    print(args.toDo)
    print(args.host)
    print(args.allhost)
    print(args.stat)
    print(args.stats)
    if args.toDo == 'addhost':
        hostentry.processdata()
        sys.exit()
    if args.toDo == 'run':
        hostcheck.start()
        sys.exit()
    if args.toDo == 'removehost':
        removehost(host)
        sys.exit()
    if args.toDo == 'edithost':
        edithost(host)
        sys.exit()
    if args.toDo == 'show':
        if args.allhost == False:
            hostInfo.showone(args.host)
        elif args.allhost ==True:
            hostInfo.showall()
        else:
            hostInfo.showall()
        sys.exit()
    if args.toDo == 'showstats':
        if args.stats == True:
            showstats.allStats()
            sys.exit()
        else:
            showstats.oneStat(stat)
            sys.exit()

