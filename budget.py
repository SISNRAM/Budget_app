class Category:

    def __init__(self, ledger):
        self.ledger = [ledger]

    def deposit(self, amount, description=""):
        IN = {"amount": amount, "description": description}
        self.ledger.append(IN)

    def withdraw(self, amount, description=""):
        OUT = {"amount": -amount, "description": description}

        if self.check_funds(amount):
            self.ledger.append(OUT)
            return True
        else:
            return False

    def get_balance(self):
        Total = 0
        for i in self.ledger[1:]:
            Total = Total + i["amount"]
        return Total

    def transfer(self, amount, Categ):
        Trans_Sender = {"amount": -amount,
                        "description": "Transfer to " + Categ.ledger[0]}
        # Costumized Withdraw
        if self.check_funds(amount):
            self.ledger.append(Trans_Sender)
            # Costumized deposit
            Categ.deposit(
                amount, description="Transfer from " + self.ledger[0])
            return True
        else:
            return False

    def print(self):
        Category_len = len(self.ledger[0])
        stars = 30 - Category_len
        St = int(stars / 2)
        print("*"*St+self.ledger[0]+"*"*St)

        for i in self.ledger[1:]:
            if isinstance(i["amount"], int):
                length_amount = len((str(i["amount"]))) + 3
            else:
                length_amount = len((str(i["amount"])))
            length_desc = len(i["description"])
            space = abs(length_amount + length_desc - 30)
            if len(i["description"]) > 23:
                print('%.23s' % i["description"], format(
                    i["amount"], '.2f'))
            
            else:
                print(i["description"] + space*" " +
                      format(i["amount"], '.2f'))
                

        print("Total:", self.get_balance())

    def check_funds(self, amount):
        return False if amount > self.get_balance() else True


def create_spend_chart(categories):
    print("Percentage spent by category")

    average = []
    # get the average to divise by
    for am in categories:
        tmp = 0
        for z in am.ledger[1:]:
            if z["amount"] < 0:
                tmp = abs(z["amount"]) + tmp
        average.append(tmp)
    handred = int(sum(average))

    # defining the number of 'O's to print
    otab = []
    for p in average:
        otab.append(int((p / handred) * 10)+1)
    # print(otab)
    for o in range(0, len(otab)):
        otab[o] = abs((otab[o]-1) * 10)
    # print(otab)

    for i in range(100, -1, -10):
        if len(str(i)) == 2:
            sp = 1
        elif len(str(i)) == 1:
            sp = 2
        else:
            sp = 0
        tabo = []
        for ham in otab:
            if ham >= i:
                num = 1
                tabo.append(num)
            else:
                num = 0
                tabo.append(num)
        
        test_z = ""
        for zb in tabo:
            test_z += "o"*zb + "  "
        print(sp*" " + str(i)+'|'+" "+test_z)


    print(4*" "+"-"+3*"-"*len(categories))

    longest = 0
    extended_Categ = []
    for x in categories:
        if longest < len(x.ledger[0]):
            longest = len(x.ledger[0])

        extended_Categ.append(x.ledger[0].ljust(8))

    for k in range(0, longest):
        print(5*" ", end="")
        for j in extended_Categ:
            print(j[k], end="  ")
        print()
