from argparse import ArgumentParser as aparse
from sentry import hostentry, hostcheck, removehost, printdata
import sys
def create_parser():
    parser = aparse(description="""
    Sentry: Monitor local and remote hosts and get notified if they are unreachable.
    """)

    parser.add_argument("toDo", default="run", help="Choose to run the check or add a host")
    parser.add_argument('-host', action="store", dest='host', help="Enter a hostname for the desired action")
    parser.add_argument('-all', dest="allhost", action="store_true", help="Use all hosts for desired action")
    parser.add_argument('-stat', action="store", dest="stat", help="Enter a specific statistic to check")
    parser.add_argument('-stats', action="store_true", help="Run check with all statistics")
    parser.add_argument('-script', action="store", dest="scriptJson")
    return parser

def main():
    from sentry import hostentry, hostping, hostcheck, removehost, edithost
    args = create_parser().parse_args()

    #print(args.toDo)
    #print(args.host)
    #print(args.allhost)
    #print(args.stat)
    #print(args.stats)
    if args.toDo == 'addhost':
        hostentry.processdata()
        sys.exit()
    if args.toDo == 'run':
        hostcheck.start()
        sys.exit()
    if args.toDo == 'removehost':
        removehost.removehost(args.host)
        sys.exit()
    if args.toDo == 'edithost':
        edithost.oneHost(args.host)
        sys.exit()
    if args.toDo == 'show':
        if args.allhost == False:
            printdata.prettyPrint(args.host)
        elif args.allhost ==True:
            printdata.printmany()
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
    if args.toDo == 'scriptEntry':
        scriptrun()
        sys.exit()


    else:
        print("Please use an argument")
        sys.exit()
