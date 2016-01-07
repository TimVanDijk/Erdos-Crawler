import ErdosCrawler as EC

def main():
    start_url = input("Target URL: ")
    crawler = EC.ErdosCrawler(start_url)
    res = crawler.crawl()
    print("Erdös number found: " + str(res[0]))
    print("Path: " + str(res[1]))

if __name__ == "__main__":
    main()