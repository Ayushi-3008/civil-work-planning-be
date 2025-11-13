🧩 User Management & Permission Control System
A scalable Django-based user management system designed to handle complex organizational structures such as departments, sub-departments, roles, and fine-grained dashboard permissions at multiple levels — from department-wide to individual users.

🚀 Features
1. 👥 User Management:
    1. Manage users with department, sub-department, and role assignments
    2. Track user activity and activation status

2. 🏢 Department Hierarchy:
    1. Departments and nested sub-departments with linked relationships

3. 🔑 Role-Based Access:
    1. Create roles with distinct access levels across dashboards

4. 🧭 Dynamic Dashboard Permissions:
    1. Manage what each user, role, or department can view, edit, or download on specific dashboards
    2. Flexible permission control via reusable Permission Templates

5. ⚙️ Granular Permission Levels:
    1. Assign permissions at:
        i. Department level
        ii. Sub-department level
        iii. Role level
        iv. User level

6. 🧱 Extensible Design:
    1. Designed for future scalability (e.g., configurable dashboards, API access control, audit logs)

🧠 System Architecture
Entity Overview
| Table                  | Purpose                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| **Department**         | Stores top-level organizational units.                                                   |
| **SubDepartment**      | Subsections of a department, linked via FK.                                              |
| **Role**               | Defines user roles such as “Manager”, “Engineer”, etc.                                   |
| **User**               | Represents users within the organization, linked to Department, SubDepartment, and Role. |
| **Dashboard**          | Registry of available dashboards and configuration metadata (JSON-based).                |
| **PermissionTemplate** | Defines available actions (e.g., “Edit Analytics”, “Download Report”) for dashboards.    |
| **Permission**         | Actual permission mapping — linking departments/roles/users with templates.              |

🗃️ Database Schema
The project contains 7 tables interconnected through foreign keys and unique constraints.

📘 SQL schema file:
👉 user_management_schema.sql

You can visualize this schema using:
1. DrawSQL
2. dbdiagram.io
3. QuickDBD

⚡ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2️⃣ Create & activate a virtual environment
python -m venv venv
source venv/bin/activate  # for macOS/Linux
venv\Scripts\activate     # for Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create the Django project database
python manage.py makemigrations
python manage.py migrate

5️⃣ Create an admin user
python manage.py createsuperuser

6️⃣ Run the development server
python manage.py runserver


Now visit:
👉 http://127.0.0.1:8000/admin

🔐 Permission Flow Overview

1. Create Departments, SubDepartments, and Roles
    These define the structure of your organization.

2. Create Dashboards
    Each dashboard defines a feature module (e.g., Analytics, Reports, etc.).

3. Define Permission Templates
    Templates define what actions (e.g., Edit, Download, View) are available for each dashboard.

4. Assign Permissions
    Assign templates to departments, roles, or individual users using the Permission model.

5. Access Control
    The frontend (e.g., React app) can consume these permission APIs to dynamically show/hide dashboard features based on user permissions.

🧩 Future Enhancements:
1. API endpoints for CRUD operations on permissions and templates
2. Integration with React dashboard UI for dynamic rendering
3. Permission-based API rate limiting
4. Audit trails for permission changes
5. Export/import functionality for permission templates

🧑‍💻 Tech Stack
Backend: Django (Python)
Database: PostgreSQL / MySQL (compatible)
Auth: Django’s built-in authentication system
ORM: Django ORM
Frontend (future-ready): ReactJs
Visualization: DrawSQL / dbdiagram.io

📂 Project Structure
civilworkplanning/
│
├── civilapp/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   ├── migrations/
│
├── manage.py
└── requirements.txt

🧾 License
This project is released under the MIT License — feel free to modify and extend as needed.