from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Nothing to do!')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

MENU = """1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit"""

def main():

    while True:
        print(MENU)
        choice = int(input())
        print()
        today = datetime.today()
        if choice == 1:
            print(f"Today {today.strftime('%d %b')}: ")
            todays_list = session.query(Table).filter(Table.deadline == today.date()).order_by(Table.deadline).all()
            rows = session.query(Table).order_by(Table.deadline).all()

            if rows == []:
                print("Nothing to do!")
            else:
              for i in todays_list:
                  print(i)

              print()

        elif choice == 2:
            print("Week's tasks!")
            for n in range(0,7):
                weeks_tasks(n)

        elif choice == 3:
            rows = session.query(Table).order_by(Table.deadline).all()
            if rows == []:
                print("Nothing to do!")
            else:
                num = 1
                for item in rows:
                    print(f"{num}. {item}. {item.deadline.strftime('%-d %b')}")
                    num+=1
            print()

        elif choice == 4:
            missed_tasks()

        elif choice == 5:
            task = input("Enter task ")
            deadline = datetime.strptime(input("Enter deadline"), '%Y-%m-%d')
            new_row = Table(task=task, deadline=deadline)
            session.add(new_row)
            session.commit()
            print("The task has been added!\n")

        elif choice == 6:
            delete_tasks()

        elif choice == 0:
            print("Bye!")
            quit()

def weeks_tasks(n):

    today = datetime.today() + timedelta(days=n)
    print(f"{today.strftime('%A %d %b')}: ")
    days_list = session.query(Table).filter(Table.deadline == today.date()).order_by(Table.deadline).all()
    num = 1
    if days_list == []:
        print("Nothing to do!")
    else:
        for i in days_list:
            print(f"{num}. {i}")
            num+=1

    print()

def missed_tasks():

    today = datetime.today()
    print("Missed tasks:")

    days_list = session.query(Table).filter(Table.deadline < today.date()).order_by(Table.deadline).all()

    num = 1
    for i in days_list:
      if days_list == []:
          print("Nothing is missed!")
      else:
          print(f"{num}. {i} {i.deadline.strftime('%-d %b')}")
          num+=1

    print()

def delete_tasks():
    task_to_delete = int(input("Choose the number of the task you want to delete:"))
    days_list = session.query(Table).order_by(Table.deadline).all()
    session.delete(days_list[task_to_delete-1])
    session.commit()
    print("The task has been deleted!")


if __name__ == "__main__":
    main()
