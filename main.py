import argparse

from glone import fetch_group_projects, fetch_user_projects

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gitlab cloner")
    parser.add_argument('-t', '--token', help="Gitlab token", type=str)
    parser.add_argument('-g', '--group', help="Gitlab group id", type=str)
    parser.add_argument('-u', '--user', help="Gitlab username", type=str)

    args = parser.parse_args()

    if args.group:
        fetch_group_projects(args.group, args.token)

    if args.user:
        fetch_user_projects(args.user, args.token)
