def main(team_a, team_b):
    print(sum(team_a) - sum(team_b) + 1)


if __name__ == "__main__":
    team_a = [int(i) for i in (input().split())]
    team_b = [int(i) for i in (input().split())]

    main(team_a, team_b)
