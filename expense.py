def main():
    amount = input("how much is the bill? ")
    people = input("how many people are there? ")
    
    per_person = billsplit(amount,people)

    print(f"the price per person is {per_person}")

def billsplit(amount,people):
    return amount / people 

main()