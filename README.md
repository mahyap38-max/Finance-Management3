#  Finance Management — Edition 3

A console-based personal finance management application built with Python and SQLite.

This is the **third edition** of the project. Compared with the previous version, this edition introduces stronger data organization, statistical analysis, logging, and graphical reporting.

---

##  Features

### Transaction Management
- Add new transactions
- Update existing transactions
- Delete transactions
- Search transactions by title
- Search transactions by date
- Store transactions in an SQLite database

### Transaction Types
Transaction types are managed using Python's `Enum` instead of relying only on plain strings.

- Income
- Expense

### Statistics
The application provides financial statistics such as:

- Total income
- Total expenses
- Current balance
- Maximum transaction amount
- Minimum transaction amount
- Average transaction amount
- Monthly financial reports

### Data Analysis
`Pandas` is used to process transaction data and calculate statistical values such as:

- Maximum value
- Minimum value
- Average value

### Data Visualization
`Matplotlib` is used to generate graphical financial reports.

The application can visualize:

- Income
- Expenses
- Balance

using a bar chart for the selected month.

### Logging
The application uses Python's `logging` module to record:

- Errors
- Exceptions
- Important application events

This makes debugging and tracking application behavior easier.

---

## Technologies Used

- **Python**
- **SQLite3**
- **Enum**
- **Logging**
- **Pandas**
- **Matplotlib**

---


## Author
Mahya Hosseini Parsa
