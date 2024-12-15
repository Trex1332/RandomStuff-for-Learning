def main():
    amount = float(input("how much is the bill? "))
    people = float(input("how many people are there? "))
    
    per_person = billsplit(amount,people)

    print(f"the price per person is £{per_person} per person")

def billsplit(amount,people):
    return amount / people 

main()