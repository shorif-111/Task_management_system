# Task Management System

Welcome to the **Task Management System**! This application helps you organize your tasks efficiently by allowing you to add, edit, categorize, complete, and remove tasks. Whether you’re managing personal goals or collaborating with a team, this system provides an intuitive interface and essential features to streamline your workflow.

---

## Features

- **Add Tasks**: Create new tasks and assign them to categories for better organization.
- **Edit Tasks**: Easily update or modify task details at any time.
- **Complete Tasks**: Mark tasks as complete once you’re done.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Categories**: Group your tasks by custom categories to keep things organized.

---



---

## Usage

- **Add a Task**: Use the input field to type your task and select a category.
- **Edit a Task**: Click the edit icon next to a task to update its details.
- **Complete a Task**: Click the "Complete" button to mark a task as done.
- **Delete a Task**: Click the "Delete" button to remove a task.
- **Manage Categories**: Add new categories for better organization.

---

## Demo

Here’s how the Task Management System looks in action:

<img width="1351" height="686" alt="Demo Screenshot" src="https://github.com/user-attachments/assets/b1a93aaa-92dd-497a-b963-f05f58643c00" />

---


### Prerequisites

&

### Installation


## Django & Crispy Bootstrap Installation
If you want to use Django and django-crispy-forms with Bootstrap 5, follow these steps:

- Clone this repository:
  ```bash
  git clone https://github.com/shorif-111/Task_management_system.git
  ```

### 1. Install Python

Make sure you have Python installed (preferably version 3.7+).  
Check your Python version:
```bash
python --version
```
or  
```bash
python3 --version
```

### 2. Create a Virtual Environment

Create a new directory for your project and set up a virtual environment:
```bash
mkdir myproject
cd myproject
python -m venv venv
```
or  
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` in your terminal prompt.

### 4. Install Django

Install Django using pip:
```bash
pip install django
```

### 5. Start a New Django Project

Navigate to the project directory:
   ```bash
   cd Task_management_system
   ```


### 6. Install django-crispy-forms and crispy-bootstrap5

Install crispy forms and Bootstrap 5 crispy template pack:
```bash
pip install django-crispy-forms crispy-bootstrap5
```

### 7. Configure Installed Apps

Add `'crispy_forms'` and `'crispy_bootstrap5'` to your `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'crispy_forms',
    'crispy_bootstrap5',
]
```

Set the crispy template pack in `settings.py`:
```python
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

### 8. Run Migrations

Apply initial migrations:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### 9. Start the Development Server

Run your server:
```bash
python manage.py runserver
```
Open your browser and visit [http://localhost:8000](http://localhost:8000).

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or new features.

---

## Author

Developed by [Sharif Sheikh](https://github.com/shorif-111).

---

## References

- [Django Documentation](https://docs.djangoproject.com/)
- [Crispy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Crispy Bootstrap5 Pack](https://github.com/django-crispy-forms/crispy-bootstrap5)
