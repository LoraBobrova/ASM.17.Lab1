from .computers import Computers

def main():
        Comp = Computers()

        list = [
        ["Add computer", Comp.read],
        ["Change computer", Comp.change],
        ["Delete computer", Comp.delete],
        ["Display list", Comp.write],
        ["Write to the file list", Comp.write_file],
	["Read from the file list", Comp.read_file],
        ["Clear list", Comp.clear]
	]
        
        try:
                while True:
                        i=1
                        print("Select")
                        for o in list:
                                print(i, o[0])
                                i+=1
                        print("Press any key to exit\n")        
                        k = int(input())
                        print("------------------------------")
                        list[k-1][1]()
                        print("------------------------------")
        except:
                print("bye")
                        
                
                        
