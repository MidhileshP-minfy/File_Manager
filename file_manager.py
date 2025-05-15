import os

def create_file(file_path, content="Hi, This is Midhilesh"):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{file_path}': {e}")



while True:
    try:
        ccc=input("Give the input\n").split(" \"")
        print(os.getcwd())
        if len(ccc)>1:
            ccc[1]=ccc[1][:-1]
        if len(ccc)>2:
            ccc[2]=ccc[2][:-1]

        if ccc[0]=="touch":
            if len(ccc)>2:
                create_file(ccc[1],ccc[2])
            else:
                create_file(ccc[1])
        elif ccc[0]=="ls":
            dir=os.listdir(".")
            for i in dir:
                if os.path.isdir(i):
                    print(f"{i}/",end=" ")
                elif os.path.isfile(i):
                    print(f"{i}",end=" ")
            print("\n")
        
        elif ccc[0]=="cd":
            os.chdir(ccc[1])

    except KeyboardInterrupt:
        print("Exiting from loop...")
        break  
