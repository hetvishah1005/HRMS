# HR Management System

## Project Overview

The **HR Management System** is designed to reduce the workload of HR personnel by automating various tasks. This system streamlines processes such as employee leave management, payroll, holiday tracking, employee performance awards, and password recovery. With distinct dashboards for HR and employees, the system ensures proper access and privileges for different users. It reduces the need for manual data entry by automatically handling employee attendance and payroll calculations.

## Features

1. **Employee Leave Management**: Manage and track employee leaves efficiently.
2. **Employee Details during Hiring**: Store and access employee details during the hiring process.
3. **Holiday Availability**: View and manage holidays within the organization.
4. **Department Management**: Organize employees based on their departments.
5. **Employee Awards**: Track employee performance and manage award assignments.
6. **Forgot Password**: A feature for password recovery when employees forget their login credentials.
7. **Employee Payroll**: Automate payroll calculations based on employee attendance and other factors.
8. **Attendance Tracking**: Track employee in-and-out times to automate the payroll system.

## File Structure

- **Attendace.py**: Manages employee attendance.
- **award.py**: Handles the employee awards section.
- **Database.py / dbase.py**: Manages the connection to the database and executes queries.
- **department.py**: Handles department-related functionalities.
- **Employee.py**: Manages employee details.
- **empmain.py**: Main script for employee dashboard functionalities.
- **forgotpass.py**: Feature for password recovery.
- **holiday.py**: Manages holiday information.
- **Leave.py / leaveE.py**: Handles employee leave requests and management.
- **list_of_department.py**: Provides a list of departments in the organization.
- **login.py**: Handles login functionality for employees and HR personnel.
- **main.py**: Main script that serves as the entry point for the HR Management System.
- **payroll.py**: Manages payroll calculations.
- **profile.py**: Displays employee profile information.

## Technologies Used

- **Python**: Core programming language for developing the system.
- **XAMPP**: Used for the database server (MySQL) for handling backend operations.
- **PyCharm**: Integrated Development Environment (IDE) used for coding the project.

## Requirements

- **XAMPP**: Ensure that XAMPP is installed and running to handle the MySQL database.
- **Python 3.x**: Basic understanding of Python is required for customizing and running the project.
- **Database Queries**: Some basic knowledge of SQL queries is required for database management.

## Setup Instructions

1. Install **XAMPP** to set up the MySQL server.
2. Clone or download the project files.
3. Open the project in **PyCharm** or any Python IDE of your choice.
4. Create a MySQL database and configure the database connection in `Database.py`.
5. Run `main.py` to start the HR Management System.
6. Access the system through HR and employee dashboards as per assigned privileges.

## Cloning the Repository

To clone this repository, follow these steps:

1. Ensure **Git** is installed on your system.
2. Open a terminal and navigate to the directory where you want to clone the repository.
3. Run the following command:

    ```bash
    git clone https://github.com/hetvishah1005/HRMS.git
    ```

4. Navigate into the cloned repository:

    ```bash
    cd HRMS
    ```

5. Open the project in **PyCharm** or your preferred IDE to start working on it.

## Collaborators

- **Jeel Patel** – Collaborator on this project.
- **Rajendra Rathod** – Project supervisor.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

### MIT License

