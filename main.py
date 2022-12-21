if __name__ == "__main__":
    print("hello world!!")
    print("Fancy say hello to everyone!!!!!!")
    with open("export.csv","r") as f:
        for x in f:
            print(x)