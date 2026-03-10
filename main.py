import argparse

def main():
    parser = argparse.ArgumentParser(description="F1 info on the CLI")
    parser.add_argument("next", help="give information about the next race weekend")
    parser.add_argument("standings", help="Gives the current driver standings")
    parser.add_argument("driver", help="gives information about the selected driver")

    parser.add_argument("-v", "--verbose", action="store_true", help="incrase output verbosity")
    args = parser.parse_args()
    if args.verbose:
        print("verbosity turned on")
        print(args.echo)
    else:
        print(args.echo)

if __name__ == "__main__":
    main()
