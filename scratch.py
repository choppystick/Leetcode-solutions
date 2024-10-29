import os
import re


def sanitize_folder_name(name):
    """
    Sanitize folder name by removing/replacing invalid Windows characters
    """
    # Replace colons, question marks, and other invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '', name)
    # Replace multiple spaces with single space
    sanitized = re.sub(r'\s+', ' ', sanitized)
    # Remove leading/trailing spaces and periods
    sanitized = sanitized.strip('. ')
    return sanitized


def create_folder_structure():
    # Main directory
    root_dir = "D:\\SQL_Top_50_Q"

    # Create main directory
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # Categories and their problems from the images
    structure = {
        "Select": [
            "Recyclable and Low Fat Products",
            "Find Customer Referee",
            "Big Countries",
            "Article Views I",
            "Invalid Tweets"
        ],
        "Basic Joins": [
            "Replace Employee ID With The Unique Identifier",
            "Product Sales Analysis I",
            "Customer Who Visited but Did Not Make Any Transactions",
            "Rising Temperature",
            "Average Time of Process per Machine",
            "Employee Bonus",
            "Students and Examinations",
            "Managers with at Least 5 Direct Reports",
            "Confirmation Rate"
        ],
        "Basic Aggregate Functions": [
            "Not Boring Movies",
            "Average Selling Price",
            "Project Employees I",
            "Percentage of Users Attended a Contest",
            "Queries Quality and Percentage",
            "Monthly Transactions I",
            "Immediate Food Delivery II",
            "Game Play Analysis IV"
        ],
        "Sorting and Grouping": [
            "Number of Unique Subjects Taught by Each Teacher",
            "User Activity for the Past 30 Days I",
            "Product Sales Analysis III",
            "Classes More Than 5 Students",
            "Find Followers Count",
            "Biggest Single Number",
            "Customers Who Bought All Products"
        ],
        "Advanced Select and Joins": [
            "The Number of Employees Which Report to Each Employee",
            "Primary Department for Each Employee",
            "Triangle Judgement",
            "Consecutive Numbers",
            "Product Price at a Given Date",
            "Last Person to Fit in the Bus",
            "Count Salary Categories"
        ],
        "Subqueries": [
            "Employees Whose Manager Left the Company",
            "Exchange Seats",
            "Movie Rating",
            "Restaurant Growth",
            "Friend Requests II Who Has the Most Friends",  # Removed colon
            "Investments in 2016",
            "Department Top Three Salaries"
        ],
        "Advanced String Functions Regex Clause": [  # Removed slashes
            "Fix Names in a Table",
            "Patients With a Condition",
            "Delete Duplicate Emails",
            "Second Highest Salary",
            "Group Sold Products By The Date",
            "List the Products Ordered in a Period",
            "Find Users With Valid E Mails"  # Removed hyphen
        ]
    }

    # Create the folder structure
    for category, problems in structure.items():
        # Create category folder
        category_path = os.path.join(root_dir, sanitize_folder_name(category))
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # Create problem folders and solution files
        for problem in problems:
            sanitized_problem = sanitize_folder_name(problem)
            problem_path = os.path.join(category_path, sanitized_problem)
            if not os.path.exists(problem_path):
                os.makedirs(problem_path)

            # Create solution files
            mysql_solution = os.path.join(problem_path, "MySQL_solution.sql")
            pandas_solution = os.path.join(problem_path, "Pandas_solution.py")
            mssql_solution = os.path.join(problem_path, "MsSQL_solution.sql")

            # Create empty solution files if they don't exist
            if not os.path.exists(mysql_solution):
                with open(mysql_solution, 'w') as f:
                    f.write("-- MySQL solution for " + problem + "\n")

            if not os.path.exists(pandas_solution):
                with open(pandas_solution, 'w') as f:
                    f.write("# Pandas solution for " + problem + "\n")

            if not os.path.exists(mssql_solution):
                with open(mssql_solution, 'w') as f:
                    f.write("-- MsSQL solution for " + problem + "\n")


if __name__ == "__main__":
    try:
        create_folder_structure()
        print("Folder structure created successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")