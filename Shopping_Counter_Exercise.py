class Cashier:
    till = {}
    
    #method to initialise the till which accepts initial values of different coins in the till.
    #till must be a dictionary. It creates a map of how many of each coin currency are in the till.  
    def __init__(self, till):
        self.till = dict(till)
        
    #method that can be called repeated that performs all the transaction at the till
    #it accepts the sale amount= cost and customers payment, return change available at till.
    def transaction(self, customer_payment, cost):
        if customer_payment == cost:
            print("No change")
            return 0
        elif customer_payment < cost:
            print ("More money")
            return 0
        
        else: #when customer_payment >cost.
            change_required = customer_payment - cost
            print("Wait for change")
            currency_list = sorted(list(self.till)) #sort the keys in the dictionary from smallest to biggest value            
            
            
            #performing Greedy Search Algorithm, picks currency as its best option.
            #currency is the highest key(coin) in the "till" dictionary.
            #if the currency is higher than the change_required, then remove that currency coin and continue.
            change_available = 0
            while (change_required > 0 and len(currency_list)> 0):
                currency = currency_list[len(currency_list)-1]
                if currency > change_required:
                    currency_list.pop()
                    continue
                change_available += currency
                change_required -= currency
                
                #check function to update the amount of currency remaining at till.
                #dictionary value.
                self.till[currency] = self.till[currency] - 1
                if self.till[currency] == 0:
                    currency_list.pop()
                    self.till.pop(currency,None)

            if (change_required <= 0):
                return change_available
            else:
                return print ("Sorry, Not enough change!!")
                                
    
def main():
    #using British currency
    x = Cashier({0.10:3, 0.05:2, 10:1, 5:3, 15:1})
    print ("Initial amount in till: ",sorted(x.till))
    print(x.transaction(41,20))
    print("****** Next Customer!! ***********")
    print("Remaining amount in till is: ", x.till)
    print(x.transaction(18, 8))


if __name__ =="__main__":
    main()