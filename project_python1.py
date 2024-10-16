# دليل الهاتف
phone_book = {
    '1111111111':'Kholoud',
    '2222222222':'Sarah',
    '3333333333':'Maram',
    '4444444444':'Abdullah',
    '5555555555':'Rawan',
    '6666666666':'Saad',
    '7777777777':'Reem'
}

def valid_number(number):
    """تحقق مما إذا كان الرقم صالحا (10 ارقام)"""
    return number.isdigit() and len(number) == 10

def search_by_number():
    """البحث عن اسم باستخدام رقم الهاتف"""
    number = input('Enter The number:')

    if not valid_number(number):
         print('This number is invalid')
         return

    if number in phone_book:
        print(f'The name of the owner of the number is: {phone_book[number]}')
    else:
        print('Sorry, the number is not found!')

def search_by_name():
    """البحث عن رقم الهاتف باستخدام الاسم"""
    name = input('Enter name:')

    if name in phone_book.values():
        number = [num for num, n in phone_book.items() if n == name][0]
        print(f'The number for {name} is: {number}')
    else:
        print('Sorry, the name is not found!')

def add_contact():
    """إضافة مستخدم جديد إلى الدليل"""
    name = input('Enter user name:')
    number = input('Enter phone number:')

    if not valid_number(number):
        print('This is an invalid number')
        return  # تأكد من الخروج من الدالة إذا كان الرقم غير صالح

    phone_book[number] = name  # تأكد من استخدام الرقم كمفتاح
    print(f'Added {name} with number {number} to the phone book')

def main():
    while True:
        print("\nChoose an option:")
        print("1. Search by phone number")
        print("2. Search by name")
        print("3. Add a new user")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            search_by_number()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_contact()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

# Example usage
if __name__ == "__main__":
    main()