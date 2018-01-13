class Computer_case:
        
    def read(self):
        print("Enter the computer name")
        self.name = input()
        print("Enter motherboard")
        self.motherboard = input()
        print("Enter CPU")
        self.CPU = input()
        print("Enter HDD")
        self.HDD = input()
        print("Enter RAM")
        self.RAM = input()
        print("Enter GPU")
        self.GPU = input() 
        
    def write(self):
        print("Computer name:", self.name)
        print("Motherboard:", self.motherboard)
        print("CPU:", self.CPU)
        print("HDD:", self.HDD)
        print("RAM:", self.RAM)
        print("GPU:", self.GPU)
