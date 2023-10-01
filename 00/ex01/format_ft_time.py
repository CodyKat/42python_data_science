from datetime import datetime

def main():
    old = datetime(1970, 1, 1, 0, 0, 0)
    new = datetime.now()

    seconds_past = (new - old).total_seconds()

    print(f"Seconds since January 1, 1970: {seconds_past:,.4f} or {seconds_past:2.2e} in scientific notation")
    print("{0:s} {1:s} {2:4d}".format(new.strftime("%b"), new.strftime("%d"), new.year))

if __name__ == "__main__":
    main()