
def main():
    email = (input("Enter your email : "))
    if len(email) >= 6:
        if email[0].isalpha():
            if ('@' in email) and (email.count("@") == 1):
                if(email[-4] == '.' or (email[-3] == '.')):
                    for char in email:
                        if(char == " "):
                            print("Wrong Email space included.")
                            break
                        elif (char.isupper()):
                            print("Uppercase founded.")
                            break
                else:
                    print("Wrong Email . not found")
            else:
                print("Wrong Email due to @ .")
        else:
            print("Wrong Email alphabet not found at first.")
    else:
        print("Wrong Email error.")

if __name__ == '__main__':
    main()