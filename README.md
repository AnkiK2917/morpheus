# morpheus

Dynamic Form Builder
Overview
The Dynamic Form Builder is a web application developed using Django that allows users to easily create and manage dynamic forms. Users can define various field types such as text input, text area, checkboxes, and radio buttons to build forms according to their needs. The application also supports form submission, capturing user responses, and rendering the submitted form data.

Features
Create Forms: Users can create custom forms with various field types like text, textarea, checkboxes, and radio buttons.
Dynamic Field Rendering: Form fields are dynamically rendered based on the database entries.
Submit Forms: Users can fill out and submit the forms, and the responses are saved for later review.
Manage Forms: Users can edit and add new fields to existing forms.
Responsive Design: The application is responsive and works on both desktop and mobile devices.
Assumptions
Users can freely create and manage forms without authentication.
The application uses simple field types such as text, textarea, checkboxes, and radio buttons.
The forms are rendered dynamically based on database data.
Technologies Used
Django - Backend framework for web development.
HTML/CSS - Frontend technologies for rendering forms and designing the user interface.
Django ORM - Database management system to store form and user data.
Bootstrap - CSS framework for responsive design.
Installation Instructions
Follow these steps to set up and run the project locally:

1. Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/AnkiK2917/morpheus.git
cd morpheus
2. Create a Virtual Environment
Create a virtual environment to isolate the project dependencies:

bash
Copy code
python -m venv venv
3. Activate the Virtual Environment
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On Mac/Linux:
bash
Copy code
source venv/bin/activate
4. Install Dependencies
Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
5. Apply Migrations
Run the migrations to set up the database schema:

bash
Copy code
python manage.py migrate
6. Create a Superuser (Optional)
If you want to access the Django admin interface, create a superuser:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create the superuser account.

7. Run the Development Server
Start the development server:

bash
Copy code
python manage.py runserver
The application will be available at http://127.0.0.1:8000/.

Usage
Home Page: Displays a list of all the available forms. Users can create a new form using the provided button.
Create Form: Allows users to enter a name for the form and create new forms.
Add Form Fields: After creating a form, users can add fields to it (text, textarea, checkboxes, or radio buttons). They can also define options for fields like radio buttons and checkboxes.
Render Form: Users can view and fill out the forms. Upon submission, the form responses are captured and saved in the database.
Edit Form Fields: Users can go back and modify the fields in any form they have created.

Future Enhancements
User Authentication & Roles: Implement user authentication to restrict form creation and management to authorized users.
Advanced Form Field Types: Add support for additional field types such as file uploads, date pickers, and dropdown menus.
Analytics and Reporting: Add functionality to view form submission analytics and generate reports.
Drag-and-Drop Interface: Implement a drag-and-drop builder for more intuitive form creation.
Email Notifications: Add email notifications for form submissions.
Multi-Language Support: Provide multi-language support for a wider user base.
