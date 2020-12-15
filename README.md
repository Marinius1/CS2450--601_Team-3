# AnyEmployee:<br/>A product by Innovative EmpTrack

## CS2450--601_Team-3 

In order to access the git repository, make sure that `git` is installed on your machine. Installation can be done at [https://git-scm.com/downloads](https://git-scm.com/downloads).

Once you have installed git, enter the following command `git clone --recurse-submodules https://github.com/Marinius1/CS2450--601_Team-3.git`.

Before getting started, make sure that you `pip install` the following dependencies: `Ttk`, `pynput`, `pyparsing`, `matplotlib`, and `pandas`.

Driver code lives in **window.py**.

To run the program, type `python3 window.py` into the command line. Make sure you are in the same directory as the file before you run.



# User Manual

### Home

**Payroll** - Gives payroll information for each employee including Pay type, Pay amount, and PTO.<br/>
**People** - Provides identification for each employee including Name, Employee Number, Phone Number, Role, Position, and assigned Team (basically a company directory).<br/>
**Admin** - Allows the admin to adjust employee information.<br/>

### Payroll

**First name** - First name of the employee. Default sorting is by this name.<br/>
**Last name** - Last name of the employee.<br/>
**Employee number** - Identification number of employee. Unique for every employee.<br/>
**Pay type** - Type of compensation the employee receives (Hourly, Salary, Commission)<br/>
**Pay amount** - Base pay for the employee. This will be reflected in the pay stub depending on their pay type.<br/>
**PTO Total** - Total PTO accrued <br/>
**PTO Uses** - Total PTO used by the employee<br/>
**Hours worked** - Total hours worked in the pay period<br/>
**Search** - Search bar that allows you to search for specific employees. Search option allows you to modify your search by First name, Last name, or Employee number<br/>
**Period** - Allows you to change the viewed pay period. <br/>

##### What can you do?

**Adjust PTO** - To change PTO values, you can directly influence the values in the PTO total and PTO used columns.</br>

**Create a new time period** - Click the button labeled "New Pay Period", doing so will archive the current pay information and bring up a fresh page with new data. </br>

**Upload sales made by commissioned employees** - Click the button labeled "import receipts", select the file where your receipts are and they will be added to the employees' database. You can also manually adjust the values in the Hours/Sales column to reflect the changes you desire. </br>

**Upload timecards for salaried and hourly employees** - Click the button labeled "Import Timecards", select your timecard files and the changes will be uploaded. Like with the receipts option, you can also manually adjust the values in the Hours/Sales column.</br>

**Issue Payments** - The "Pay" button will issue payments to all employees, sending them the total payment reflected in the total column </br>

**Save your changes** - The "save" button on the top right will save your changes. WARNING: no changes made to the page will be kept if they aren't saved.</br>

### People

**First Name** - First name of the employee listed in alphabetical order. This can be adjusted in the Admin page.<br/>
**Last Name** - Last name of the employee. This can be adjusted in the Admin page.<br/>
**Employee Number** - Unique identification for each employee. Allows for quick lookup of employees within the company. <br/>
**Phone** - Contact number for the employee. This can be adjusted in the Admin page.<br/>
**Role** - Employee's role within the company. Manager, Team lead, and Worker are the respective order for the hierarchy of the roles.<br/>
**Position** - Where the employee is located. Corporate indicates company HQ.<br/>
**Team** - Which team the employee belongs to. Teams are designated by a unique number and are assigned work per their number. <br/>

### Admin

**People** - Contains a list of all employees, select an employee from this list to edit their information. Select 'Add' to add a new employee into the company database. You can also search the employees by their First name, Last name, and Employee number by simply filtering through the dropdown list beside the search box.<br/> 
**Employee Info** - Allows you to adjust everything you see on the People page. You can edit the First name, Last name, address, phone number, birthday, and Social Security information. <br/>
**Job Info** - Allows you to edit everything that can be seen on the Payroll page. You can edit The job title, Team, role, Employee ID, Start Date, pay type, and pay rate. <br/>
**Delete** - if you wish to delete an employee from the company database you can delete them by clicking the delete button. <br/>
**Save** - if you are pleased with the adjustments that you have made, you can save the information by clicking the save button.<br/>

##### What can you do? 
**Add an employee** - To add an employee you simply click the "Add" button. Enter all the information of the employee. If you wish to scrap changes, simply click "Delete". If you wish to save the employee data, click "Save". If you try to move away from the page, you will be met with an "are you sure" popup that will either save the data or take you back to the open editor to allow you to change information or scrap changes.</br>

**Edit an existing employee** - Simply double click an employee's name from the list on the left side. Change the information you wish to change. If you try to move away from the page, you will be met with an "are you sure" popup that will either save or scrap your changes. </br>

**Search an employee** - Simply type the parameter you want to search by, select it in the select box, and the list below will populate with results. </br>
