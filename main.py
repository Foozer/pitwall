import argparse

def next():
    print("next race is China")

def standings():
    print("standings")

def driver():
    print("driver details...")

def main():
    global_parser = argparse.ArgumentParser(prog="Pitwall",description="F1 info on the CLI")
    subparsers = global_parser.add_subparsers(
        title="subcommands", help="Pitwall Options"
    )

    next_parser = subparsers.add_parser("next", help="give information about the next race weekend")
    next_parser.set_defaults(func=next)

    standings_parser = subparsers.add_parser("standings", help="Gives the current driver standings")
    standings_parser.set_defaults(func=standings)

    driver_parser = subparsers.add_parser("driver", help="gives information about the selected driver")
    driver_parser.set_defaults(func=driver)

    args = global_parser.parse_args()

    args.func()

if __name__ == "__main__":
    main()
