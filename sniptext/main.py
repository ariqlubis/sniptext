from sniptext.summarizer import summarize

def main():
    url = input("Enter a website URL: ")
    print("Summarizing...\n")
    print(summarize(url))

if __name__ == "__main__":
    main()
