
def function(mode,A):
    with open("need_to_train.txt",mode=mode) as file:
        if mode=="r":
            arr=[]
            file=file.readlines()
            for i in file:
                arr.append(int(i.split()))
            return arr
        else:
            for i in A:
                file.write(f"{i}\n")
            return

def save_value(arr):
    function("w",arr)

def get_value():
    return function("r",[])