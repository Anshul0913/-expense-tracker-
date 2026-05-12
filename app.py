from database import create_table , view_all, add_expense , delete_expense ,total_spend, filter_by_category
from datetime import date

def show_expenses(Rows):
    if not Rows:
        print("Koi expense nahi mili!")
        return
    
    print(f"\n{'ID':<5} {'Item':<15} {'Amount':<10} {'Category':<12} {'Date'}")
    print("-" * 55)
    
    for row in Rows :
        print(f"{row[0]:<5} {row[1]:<15} Rs.{row[2]:<9} {row[3]:<12} {row[4]}")  


def main():
    create_table()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Expense add karo")
        print("2. Sab expenses dekho")
        print("3. Total kitna kharch hua")
        print("4. Expense delete karo")
        print("5. Category se filter karo")
        print("6. Exit")

        choice = input("\nApna choice enter karo: ")

        if choice == "1":
            item     = input("Item ka naam: ")
            amount   = float(input("Amount (Rs.): "))
            category = input("Category (food/travel/bills/other): ")
            today     = str(date.today())
            add_expense(item, amount, category, today )

        elif choice == "2":
            rows = view_all()
            show_expenses(rows)

        elif choice == "3":
            total = total_spend()
            print(f"\nTotal kharch: Rs.{total}")

        elif choice == "4":
            rows = view_all()
            show_expenses(rows)
            expense_id = int(input("\nKaunsa ID delete karna hai: "))
            delete_expense(expense_id)

        elif choice == "5":
            category = input("Kaunsi category: ")
            rows = filter_by_category(category)
            show_expenses(rows)

        elif choice == "6":
            print("\nBye bro! 👋")
            break

        else:
            print("Galat choice — dobara try karo!")

if __name__ == "__main__":
    main()