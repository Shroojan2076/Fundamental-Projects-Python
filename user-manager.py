from sqlalchemy import create_engine, select, or_, String, Integer, func
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped
from datetime import datetime


engine = create_engine('sqlite:///users.db')

class Base(DeclarativeBase):
    pass

now = lambda: f'{datetime.now().strftime(f"%d/%m/%Y %H:%M:%S")}'

class User(Base):
    __tablename__  = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    created_at: Mapped[str] = mapped_column(String(100), default=now)

Base.metadata.create_all(engine)

session = Session(engine)

def add_user():
    while True:
        name = input('Enter your name: ')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        
        if name and email and password:
            user = session.scalar(select(User).where(or_(func.lower(User.name) == name.lower(), User.email == email, User.password == password)))
            if user:
                if user.name.lower() == name.lower():
                    print("the name is already taken, please try again.")
                elif user.email == email:
                    print("the email is already registered.")
                else:
                    print("The password is already taken, try again.")
            else:
                new_user = User(name=name, email=email, password=password)

                session.add(new_user)
                session.commit()
                print(f'User {name} successfully added.')
                break
        else:
            print('Please fill all the fields.')

def edit_user():
    while True:
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        if email and password:
            stmt = select(User).where(User.email == email, User.password == password)
            user = session.scalar(stmt)
            if user:
                edit = input('what do you want to change? (name, email, password): ')
                if edit == 'name':
                    new_name = input('Enter new name: ')
                    edit_user = session.scalar(select(User).where(func.lower(User.name) == new_name.lower()))
                    if edit_user and edit_user.id != user.id:
                        print("the name is already taken, please try again.")
                    else:
                        user.name = new_name
                        session.commit()
                        print('Name updated succesfully')
                        break
                elif edit == 'email':
                    new_email = input('Enter new email: ')
                    edit_user = session.scalar(select(User).where(User.email == new_email))
                    if edit_user and edit_user.id != user.id:
                        print("the email is already registered.")
                    else:
                        user.email = new_email
                        session.commit()
                        print('Email updated succesfully')
                        break
                elif edit == 'password':
                    new_password = input('Enter new password: ')
                    edit_user = session.scalar(select(User).where(User.password == new_password))
                    if edit_user and edit_user.id != user.id:
                        print("The password is already taken, try again.")
                    else:
                        user.password = new_password
                        session.commit()
                        print('Password updated succesfully')
                        break
                else:
                    print("Invalid entry.")
            else:       
                print('User not found')
        else:
            print('Please fill all the fields.')
    

def delete_user():
    while True:
        email = input('Enter the email of the user to delete: ')
        password = input('Enter the password: ')
        
        if email and password:
            stmt = select(User).where(User.email == email, User.password == password)
            user = session.scalar(stmt)
            if user:
                session.delete(user)
                session.commit()
                print("User succesfully deleted.")
                break
            else:
                print('User not found')
        else:
            print('Please fill all the fields.')
            
actions = {
    1: add_user,
    2: edit_user,
    3: delete_user,
}

while True:
    print("\n")
    print("Welcome!")
    print("What would you like to do?")
    print("1. Add a user.\n2. Edit a user.\n3. Delete a user.\n4. Exit")
    try:
        action = int(input('--> '))
        if action in actions:
            actions[action]()
        elif action == 4:
            break
        else:
            print('Please select a valid operation.')
    except ValueError:
        print('Please select a valid operation.')