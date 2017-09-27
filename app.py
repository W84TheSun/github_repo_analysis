from argparse import ArgumentParser


def main(args):
    print(args.branch)



if __name__ == '__main__':
    parser = ArgumentParser(description="Github repository analysis tool")
    parser.add_argument('url', help='Repository URL')
    parser.add_argument('start_date', help='Analysis start date')
    parser.add_argument('end_date', help='Analysis end date')
    parser.add_argument('--b', dest='branch', default='master', help='Repository branch. "master" by default')
    args = parser.parse_args()
    main(args)
