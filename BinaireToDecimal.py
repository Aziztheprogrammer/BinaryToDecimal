print("Created By : Mohamed Aziz Berhouma \nProject : Smart Equation \nGitHub : https://github.com/Aziztheprogrammer")

def binaire(decimal_num):
    binaire_num_list = []
    while (decimal_num / 2) != 0 :
            reste = decimal_num % 2
            binaire_num_list.insert(0, str(reste))
            decimal_num = decimal_num // 2
            binaire_num = ""
    print(binaire_num.join(binaire_num_list))
    
a = int(input("Donner Le Nombre Decimal :\n"))
binaire(a)
        