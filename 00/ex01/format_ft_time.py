from datetime import datetime

def main():
    old = datetime(1970, 1, 1, 0, 0, 0)
    new = datetime.now()

    seconds_past = (new - old).total_seconds()

    print("Seconds since January 1, 1970: {0:,.4f} or {1:2.2e} in scientific notation".format(seconds_past, seconds_past))
    print("{0:s} {1:s} {2:4d}".format(new.strftime("%b"), new.strftime("%m"), new.year))

if __name__ == "__main__":
    main()