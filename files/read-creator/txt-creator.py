def create():
    try:
        arq = open("README.md", "rt")
        arq.close()
    except FileNotFoundError:
        arq = open("README.md", "wt+")
        print("the file was created")
    else:
        print("File Exists")
