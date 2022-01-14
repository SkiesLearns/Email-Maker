import re

class email_maker():

    def __init__(self, domain, stored_emails: dict = {}):
        self.domain = domain
        self.stored_emails = stored_emails

    #Gets users full name, email and adds it to stored_emails.
    def make_email(self):
        #Gets the users information ready to be added.
        while True:
            user_name = input('Enter your name: ').lower()
            if not re.match("^[A-Za-z]*$", user_name):
                print('Invalid character entered.')
            else:
                user_surname = input('Enter your surname: ').lower()
                if not re.match("^[A-Za-z]*$", user_surname):
                    print('Invalid character entered.')
                    break
                print('Email added successfully.')
                break

        #This will be stored in dict
        user_email = f"{user_name}.{user_surname}@{self.domain}"
        user_fullname = f"{user_name}_{user_surname}"

        self.stored_emails[user_email] = user_fullname

    #Deletes any existing email stored if user requests.
    def delete_email(self):
        try:
            remove_email = input('Enter email to remove: ').lower()
            del self.stored_emails[remove_email]
            print('E-Mail remove from stored data.')

        except KeyError:
            print('E-Mail not in stored data.')

    #Displays stored data.
    def display_email(self):
        #Lets user know no emails are stored if so
        if self.stored_emails:
            output = ""
            for email, full_name in self.stored_emails.items():
                output += f'Full Name: {full_name.title().replace("_", " ")} | E-Mail: {email}\n'
            print(output)
        else:
            print('No emails are currently saved.')


def main():
    user_domain = input(f"Enter domain in format 'mycompany.com': ").lower()

    email = email_maker(user_domain)

    while True:
        user_decide = input("""=====================================================
To create a users email, type 'MAKE'
To delete a E-Mail, type 'DELETE'
To show all names and emails saved, type 'DISPLAY'
To exit application, type 'EXIT'
=====================================================
: """).lower()
        if user_decide in ['make', 'display', 'delete']:
            action = getattr(email, f'{user_decide}_email')()
        elif user_decide == 'exit':
            print('Closing...')
            exit()
        else:
            print('Invalid input')


if __name__ == '__main__':
    main()
