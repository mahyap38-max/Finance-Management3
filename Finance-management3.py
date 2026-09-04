#Creating a database table if not exists.
#by using context manager for sqlite
#dataclass for transaction 
#basic logging
#Enum (in ADD function)


import sqlite3
with sqlite3.connect('management.db')as connection:
        cursor=connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS
        management(
        id INTEGER PRIMARY KEY,
        title TEXT,
        amount TEXT,
        type TEXT,
        date TEXT,
        description TEXT)""")

#The transaction structure created by dataclass
#Included [title,amount,type,date,description]
from enum import Enum
class TypeStatus(Enum):
       Income=1
       Expense=2
from dataclasses import dataclass
@dataclass
class transaction:

    title : str
    amount : str
    type: TypeStatus
    date: str
    description: str | None=None

    def totuple(self)->str:
        return(
             self.title,
             self.amount,
             self.type.name,
             self.date,
             self.description 
        )

import logging
logging.basicConfig(filename='finance.log',level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
#functions to connect to the database
#Included functions as [add,delete,update,search]
class database:

    def add_trans() -> str:
        while True:
    
            title=(input("Enter the title: ").strip()).lower()
            if (len(title)==0):
                                    
                                    logging.error("Please enter a title.")
                                    continue
            elif (title.isdigit()):
                    logging.exception("Please enter a text.")
                    continue
    
            break

        while True:
            try:
                     amount=(input("Enter the amount:").strip())
                     if(len(amount)==0 or not amount.isdigit() or int (amount)<=0):
                           logging.error("Invalid input \nPlease try again.")
                           continue
                     else:
                         break
            except Exception as e:
                 logging.exception(f"Error: {e}")
                 continue
              
        print("Choose transaction type. \n1.Income \n2.Expense")

            

        while True:
            try:
                 choice=(int(input("Enter: ")))
            except ValueError :
                 logging.exception("Please choose a number among the list above.")
                 continue
            
            if (choice==TypeStatus.Income.value):
                   type=TypeStatus.Income
                   break

            elif(choice==TypeStatus.Expense.value):
                   type=TypeStatus.Expense
                   break
            else:
                   logging.error("Invalid input \nPlease try again.")
                   continue
                   
                

                
        print("Enter date.")
        while True:
                try:
                        day=(input("Day: ").strip()).lower()
                
                        if(not day.isdigit() or int(day)>31 or int(day)<=0):
                            print("invalid input \n Please try again")
                            continue
                        else:
                            break
                except Exception as e:
                     print(f"Error: {e}")
                     continue
        if (len(day)==1):
               day='0'+day

        while True:
                try:
                        month=(input("Month: ").strip()).lower()

                        if(not month.isdigit() or int(month)>12 or int(month)<=0):
                            logging.error("Invalid input \nPlease try again")
                            continue
                        else:
                            break
                except Exception as e:
                     logging.exception(f"Error: {e}")
                     continue
        if len(month)==1:
               month='0'+month

        while True:
            try:
                    year=(input("Year: ").strip()).lower()

                    if(not year.isdigit() or len(year)!=4 or int(year)<=0):
                        logging.error("Invalid input \nPlease try again")
                        continue
                    else:
                        break
            except Exception as e:
                 logging.exception(f"Error: {e}")
                 continue

        newdate=year+'-'+month+'-'+day

        while True:
                try:
                
                        description=(input("*optional* \nEnter description: "))

                        break 
                except Exception as e:
                    logging.exception(f"Error: {e}")
        
        try:
                    newtrans=transaction(title,amount,type,newdate,description)

                    with sqlite3.connect('management.db') as connection: 
                           cursor=connection.cursor()
                           cursor.execute("""
                                            INSERT INTO management( title,amount,type,date,description)
                                            VALUES(?,?,?,?,?)""",(newtrans.totuple()))
                  
        except Exception as e:
              logging.exception(f"Error: {e}")
                

        logging.info("transaction added.")
        return "Done"


    def delete_trans() -> str:

            
            while True:

                    title=(input("Enter title: ").strip()).lower()
                    if (len(title)==0):
                           logging.error("Please enter a title.")
                           continue

                  
                    try:
                        connection=sqlite3.connect("management.db")
                        cursor=connection.cursor()
                        
                        cursor.execute("SELECT * FROM management WHERE title LIKE ? ",(f"%{title}%",))
                        rows=cursor.fetchall()

                        if not rows :
                              logging.error("No data found for this title.\nPlease try again")
                              continue
                        
                    except Exception as e:
                        logging.exception(f"Error: {e}")
                        continue

                
                    try:
                        validids=[]
                        for row in rows:
                                validids.append(row[0])
                                print(row)

                            
                    except Exception as e:
                        logging.exception(f"Error: {e}")
                        continue

                    break
                
                    
                  

            print("Enter the ID to delete:")
            while True:
                    try:
                        id=int(input("ID: "))
                    except ValueError:
                        logging.error("Please enter an integer number.")
                        continue

                    if id not in validids:
                          logging.error("Please choose one of the displayed IDs.")
                          continue

                    try:
                        connection=sqlite3.connect("management.db")
                        cursor=connection.cursor()
                        cursor.execute("""
                        DELETE FROM management 
                        WHERE id=? """,(id,))
                        connection.commit()
                    except Exception as e:
                        logging.exception(f"Error: {e}")
                        continue
                    if connection:
                        connection.close()
                    break

            logging.info("transaction deleted." \
            "")
            return "Done"                       


    def update_trans() -> str:

            while True:
    
                        title=(input("Enter title: ").strip()).lower()
                        if(len(title)==0):
                                               logging.error("Please enter a title.")
                                               continue
                    
                        try:
                            connection=sqlite3.connect("management.db")
                            cursor=connection.cursor()
                            cursor.execute("SELECT * FROM management WHERE title LIKE ? ",(f"%{title}%",))
                            rows=cursor.fetchall()

                            
                            if not rows :
                                logging.error("No data found for this title.\nPlease try again")
                                continue
                            
                        except Exception as e:
                            logging.exception(f"Error: {e}")
                            continue
    
                    
                        try:
                            validids=[]
                            for row in rows:
                                    validids.append(row[0])
                                    print(row)
    
                        except Exception as e:
                            logging.exception(f"Error: {e}")
                            continue
                        break

            print("Enter the ID to update:")
            while True:
                                try:
                                   id=int(input("ID: "))
                                except ValueError:
                                   logging.error("Please enter an integer number.")
                                   continue
           
                                if id not in validids:
                                     logging.error("Please choose one of the displayed IDs.")
                                     continue
                                break

            while True:
                                try:
                                        amount=(input("Enter the amount:").strip())
                                        if(len(amount)==0 or not amount.isdigit() or int (amount)<=0):
                                            logging.error("Invalid input \nPlease try again.")
                                            continue
                                        else:
                                            break
                                except Exception as e:
                                    logging.exception(f"Error: {e}")
                                    continue
                                
                                
            print("Choose transaction type. \n1.Expense \n2.Income")
                
            while True:
                    try:
                        choice=(int(input("Enter: ")))
                    except ValueError :
                        logging.error("Please choose a number among the list above.")
                        continue
                    try:
                            if choice==1:
                                type="Expense"
                                break
                            elif choice==2:
                                type="Income"
                                break
                            else:
                                logging.error("Invalid input \nPlease try again.")
                                continue
                    except Exception as e:
                        logging.exception(f"Error: {e}")
                        continue

                        
            print("Enter date.")
            while True:
                        try:
                                day=(input("Day: ").strip()).lower()
                        
                                if(not day.isdigit() or int(day)>31 or int(day)<=0):
                                    logging.error("invalid input \n Please try again")
                                    continue
                                else:
                                    break
                        except Exception as e:
                            logging.exception(f"Error: {e}")
                            continue
            if(len(day))==1:
                   day="0"+day

            while True:
                        try:
                                month=(input("Month: ").strip()).lower()

                                if(not month.isdigit() or int(month)>12 or int(month)<=0):
                                    logging.error("Invalid input \nPlease try again")
                                    continue
                                else:
                                    break
                        except Exception as e:
                            logging.exception(f"Error: {e}")
                            continue
            if(len(month))==1:
                   month="0"+month

            while True:
                    try:
                            year=(input("Year: ").strip()).lower()
                            if(not year.isdigit() or len(year)!=4 or int(year)<=0):
                                logging.error("Invalid input \nPlease try again")
                                continue
                            else:
                                break
                    except Exception as e:
                        logging.exception(f"Error: {e}")
                        continue
            while True:
                try:
                            date=year+'-'+month+'-'+day

                            description=(input("*optional* \nEnter description: "))
                except Exception as e:
                                logging.exception(f"Error: {e}")
                                continue
                break


            try:
                  connection=sqlite3.connect("management.db")
                  cursor=connection.cursor()
                  cursor.execute("""
                  UPDATE management
                  SET amount=? , type=? , date=? , description=?
                  WHERE id=?  """,
                  (amount,type,date,description,id))
                  connection.commit()

                  if connection:
                        connection.close()
            except Exception as e:
                  logging.exception(f"Error: {e}")


            logging.info("transaction updated.")
            return "Done"


    def search_by_title() -> str:

        while True:
            try:
                title=(input("Enter title:").strip()).lower()
                if(len(title)==0):
                       logging.error("Please enter a title.")
                       continue
                connection=sqlite3.connect("management.db")
                cursor=connection.cursor()
                cursor.execute("SELECT * FROM management WHERE title LIKE ?",(f"%{title}%",))
                rows=cursor.fetchall()

                if not rows :
                                    logging.error("No data found for this title.\nPlease try again")
                                    continue
                
                                        
            except Exception as e:
                                        logging.exception(f"Error: {e}")
                                        continue
                
                                
           
                                       
            for row in rows:  
                                    print(row)
                
                                            
            
            if connection:
                   connection.close()
            break

        logging.info("transaction searched by title: %s " , title)
        return "Done"


    def search_by_date() -> str:

        print("Enter date.")

        while True:
                           try:
                                   day=(input("Day: ").strip()).lower()
                           
                                   if(not day.isdigit() or int(day)>31 or int(day)<=0):
                                       logging.error("invalid input \n Please try again")
                                       continue
                                   else:
                                       break
                           except Exception as e:
                                logging.exception(f"Error: {e}")
                                continue
        if(len(day))==1:
               day='0'+day
           
        while True:
                           try:
                                   month=(input("Month: ").strip()).lower()
           
                                   if(not month.isdigit() or int(month)>12 or int(month)<=0):
                                       logging.error("Invalid input \nPlease try again")
                                       continue
                                   else:
                                       break
                           except Exception as e:
                                logging.exception(f"Error: {e}")
                                continue
        if(len(month))==1:
               month='0'+month
        while True:
                        try:
                               year=(input("Year: ").strip()).lower()
           
                               if(not year.isdigit() or len(year)!=4 or int(year)<=0):
                                   logging.error("Invalid input \nPlease try again")
                                   continue
                               else:
                                   break
                        except Exception as e:
                            logging.exception(f"Error: {e}")
                            continue
       
        date=year+'-'+month+'-'+day
                   
                                
        while True:
                try:
                    connection=sqlite3.connect("management.db")
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM management WHERE date=?",(date,))
                    rows=cursor.fetchall()
                    connection.commit()

                    if not rows:
                            logging.error("No data found for this date.")
                            break
                except Exception as e:
                       logging.exception(f"Error: {e}")

                for row in rows:
                       print(row)
                if connection:
                       connection.close()

                break


        logging.info("transaction searched by date: %s", date)
        return "Done"


#functions for reports as[total income / total expense / current balance]
class statistics:

    def total_income() -> str:

        try:
            
                    connection=sqlite3.connect("management.db")
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM management WHERE type=? ", ("Income",))
                    rows=cursor.fetchall()
                    connection.commit()
                    amount=0
                    for row in rows:
                            amount+=float(row[2])
                    print(f"Total income is :{amount}")
                
        except Exception as e:
               logging.exception(f"Error: {e}")
        if connection:
               connection.close()
        
       

        amount_data=[{"Income":"Total income","Amount":amount}]
        try: 
                                   import pandas as pd
                                   data=pd.DataFrame(amount_data)
                                   import matplotlib.pyplot as plt
                                   data.plot(kind='bar',x='Income',y="Amount",title='Total Income',color='pink',width=0.1)
                                   plt.show()
        except Exception as e:
               logging.exception(f"Error: {e}")

        logging.info('Total income calculated and barchart created.')
        return "Done"

    def total_expense() -> str:

            try:
                    connection=sqlite3.connect("management.db")
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM management WHERE type=? ", ("Expense",))
                    rows=cursor.fetchall()
                    amount=0
                    connection.commit()
                    for row in rows:
                            amount+=float(row[2])
                    print(f"Total expense is :{amount}")
            except Exception as e:
                          logging.exception(f"Error: {e}")
            if connection:
                   connection.close()


            amount_data=[{"Expense":"Total expense","Amount":amount}]
            try:
                   import pandas as pd
                   data=pd.DataFrame(amount_data)
                   import matplotlib.pyplot as plt
                   data.plot(kind='bar',x='Expense',y='Amount',title='Total expense',color='red',width=0.1)
                   plt.show()
            except Exception as e:
                   logging.exception(f"Error: {e}")

            logging.info('Total expense calculated and barchart created.')
            return "Done"
                       
    def current_balance() -> str :
            try:
                    connection=sqlite3.connect("management.db")
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM management WHERE type=? ", ("Income",))
                    rows=cursor.fetchall()
                    income=0
                    for row in rows:
                            income+=float(row[2])
                   
            except Exception as e:
                          logging.exception(f"Error: {e}")
            try:
                    cursor.execute("SELECT * FROM management WHERE type=? ", ("Expense",))
                    rows=cursor.fetchall()
                    expense=0
                    connection.commit()
                    for row in rows:
                            expense+=float(row[2])
                   
            except Exception as e:
                                      logging.exception(f"Error: {e}")

            if connection:
                   connection.close()

            balance=income-expense

            print(f"current balance is: {balance}")


            balance_data=[{'Balance':'current balance','Amount':balance}]
            try:
                   import pandas as pd
                   data=pd.DataFrame(balance_data)
                   import matplotlib.pyplot as plt
                   data.plot(kind='bar',x='Balance',y='Amount',title='Current Balance',color='blue',width=0.1)
                   plt.show()
            except Exception as e:
                   logging.exception(f"Error: {e}")
            logging.info('Current balance calculated and barchart created.')
            return "Done"

    def min_max_avg () -> str:

        try:
           with sqlite3.connect('management.db')as connection:
                  cursor=connection.cursor()
                  cursor.execute("SELECT amount FROM management WHERE type=?",("Income",))
                  income_rows=cursor.fetchall()
                  cursor.execute("SELECT amount FROM management WHERE type=?",("Expense",))
                  expense_rows=cursor.fetchall()
        except Exception as e:
                  logging.exception(f"Error: {e}")
                  return "Error"

        try:
                  import pandas as pd
                  income_data=pd.DataFrame(income_rows, columns=['amount'])
                  income_data['amount']= income_data['amount'].astype(float)
                  income_max=income_data['amount'].max()
                  income_min=income_data['amount'].min()
                  income_avg=income_data['amount'].mean()
        except Exception as e:
                  logging.exception(f"Error: {e}")
                  return "Error"
        print(f"The average of total income is {income_avg}. \n Minnimum amount:{income_min} Maximum amount:{income_max} ")


        try: 
                  expense_data=pd.DataFrame(expense_rows, columns=['amount'])
                  expense_data['amount']= expense_data['amount'].astype(float)
                  expense_max=expense_data['amount'].max()
                  expense_min=expense_data['amount'].min()
                  expense_avg=expense_data['amount'].mean()
        except Exception as e:
               logging.exception(f"Error: {e}")
               return "Error"
        print(f"The average of total expense is {expense_avg}.\n Minimum amount:{expense_min} Maximum amount:{expense_max}")

        logging.info("Maximum , Minimum and Average of total expense and income calculated.")
        return "Done"

    def monthly_report():

            while True:

                try:  

                        month=int(input("Enter month: "))

                        if(not 1<=month<=12):
                               logging.error("Please enter a number between 1 and 12")
                               continue
                        break 
                except ValueError :
                       logging.error('Please enter an integer number between 1 and 12.')
                       continue
            
            month=str(month)
            if len(month)==1:
                   month='0'+month

            try:
                    with sqlite3.connect('management.db')as connection:
                            cursor=connection.cursor()
                            cursor.execute("SELECT amount ,type , date FROM management")
                            rows=cursor.fetchall()
            except Exception as e :
                        logging.exception(f"Error: {e}")

            expense=0
            income=0

            try:
                    for amount, type , date in rows:
                            if date[5:7]==month:
                                    if type=="Income":
                                            income+=float(amount)
                                    elif type=="Expense":
                                            expense+=float(amount)
                   
            except Exception as e:
                    logging.exception(f"Error: {e}")

            balance = income - expense

            data=[income,expense, balance]
            xaxis=["Income","Expense","Balance"]

            import matplotlib.pyplot as plt

            try:
                   plt.bar(xaxis, data,color='purple')
                   plt.title("Monthly report")
                   plt.ylabel("Amount")
                   plt.xlabel("Categories")
                   plt.show()
            except Exception as e:
                   logging.exception(f"Error: {e}")

            print(balance)
            return "Done"

                    

#menu
#Main menu with two submenus (Transaction Management and Statistics)
while True:
        print("---------Finance Manager---------")
        print("Choose 1 to access transaction.")
        print("Choose 2 to access statistics.")
        print("Choose 0 to exit.")

        while True:
            try:
                choice=int(input("Enter your choice: "))
                if (not 0<=choice<=2):  
                    logging.error("Please choose from the list above.")
                    continue
                        
            
            except ValueError:
                logging.error("Please choose a number from the list above.")    
                continue
            break     
             
            

        match choice :
               case 1:

                    while True:
                            print("---Transaction Management---")
                            print("[1] Add transaction")
                            print('[2] Delete transaction')
                            print('[3] Update transaction')
                            print('[4] Search by title')
                            print('[5] Search by date')
                            print('[0] Return to main menu')

                            while True:
                                    try:
                                        choice2=int(input("Enter your choice: "))
                                        if (not 0<=choice2<=5):
                                               
                                          logging.error("Please choose a number from the list above.")
                                          continue
                                                
                                    except ValueError :
                                           logging.error("Please choose from the list above.")
                                           continue
                                    break

                                           
                            match choice2:

                                   case 0:
                                          print("Returning to main menu")
                                          logging.info("Returned to main menu.")
                                          break
                               
                                   case 1:
                                            try:
                                                    print(database.add_trans())
                                            except Exception as e:
                                                   print(e)
                                
                                                
                                   case 2:
                                          print(database.delete_trans())
                                         
                                   case 3:
                                          print(database.update_trans())
                                         
                                   case 4:
                                          print(database.search_by_title())
                                          
                                   case 5:
                                          print(database.search_by_date())
                                          


               case 2:
                      while True:
                             print("---Statistics---")
                             print("[1] Total income")
                             print("[2] Total expense")
                             print("[3] Current balance")
                             print("[4] Minimum & Maximum & Average of total Income and Expense")
                             print('[5] Monthly report')
                             print("[0] Return to main menu")
                             while True:
                                        try:
                                            choice3=int(input("Enter your choice: "))
                                            if (not 0<=choice3<=5):
                                                   
                                                logging.error("Please choose a number from the list above.")
                                                continue
                                        except ValueError :
                                            logging.error("Please choose from the list above.")
                                            continue
                                        break
                                       
                             match choice3:

                                    case 0:
                                           print("Returning to main menu")
                                           logging.info("Returned to main menu.")
                                           break
                                           
                                    case 1:
                                           print(statistics.total_income())
                                          
                                    case 2:
                                           print(statistics.total_expense())
                                         

                                    case 3:
                                           print(statistics.current_balance())

                                    case 4:
                                           print(statistics.min_max_avg())

                                    case 5:
                                           print(statistics.monthly_report())

                               
                                         

               case 0:
                      print("Exiting program...")
                      logging.info("Program exited.")
                      break
                                          
                                                    
                        



                                

                                
                                    
                






        
        