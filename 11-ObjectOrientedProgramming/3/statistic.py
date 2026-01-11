from statisticcode import Statistics
data = [12, 37, 6, 9, 17]
def main():
    stats = Statistics(data)
    stats.show() 
    print("Greatest:", stats.greatest())
    print("Smallest:", stats.smallest())
    print("Mean:", stats.mean())
    print("Median:", stats.median())

if __name__ == "__main__":
    main()