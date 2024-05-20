# Django To-Do Application

This is a simple To-Do application built with Django. It allows users to create, update, and delete tasks, and mark them as completed. Users need to sign up and log in to access their personalized to-do lists.

## Features

- User authentication (sign up, log in, log out)
- Create new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as complete or incomplete
- Separate lists for completed and incomplete tasks

## Prerequisites

- Python 3.x
- Django 3.x or later

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser (optional, for admin access):
    ```sh
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Sign Up

1. Go to the sign-up page at `http://127.0.0.1:8000/`.
2. Fill in the required details (username, email, password) and sign up.

### Log In

1. Go to the login page at `http://127.0.0.1:8000/login/`.
2. Enter your username and password to log in.

### To-Do List

1. Once logged in, you will be redirected to your to-do list.
2. Add a new task using the input field at the bottom.
3. Update or delete tasks using the edit and delete buttons.
4. Mark tasks as complete by checking the checkbox next to them.

## Project Structure

- `views.py`: Contains the views for handling user authentication and task operations.
- `models.py`: Defines the `Task` model.
- `urls.py`: Defines the URL patterns for the application.
- `templates/`: Contains the HTML templates for the application.
- `static/`: Contains static files like CSS and JavaScript.

## File Details

### `views.py`

- `signup`: Handles user sign-up.
- `user_login`: Handles user login.
- `todolist`: Displays the to-do list and handles adding new tasks.
- `task_delete`: Deletes a specified task.
- `update_task_completion`: Updates the completion status of a task via AJAX.
- `user_logout`: Logs out the user.
- `update_todo`: Handles updating an existing task.

### `urls.py`

Defines the following URL patterns:

- `/`: Sign-up page
- `/login/`: Login page
- `/todo/`: To-do list page
- `/delete/<int:id>/`: Delete task
- `/complete/<int:task_id>/`: Update task completion status
- `/logout/`: Log out user
- `/update/<int:id>`: Update task

### Templates

- `signup.html`: User sign-up page.
- `login.html`: User login page.
- `todo.html`: To-do list page.
- `update.html`: Task update page.

### Static Files

- `todo.css`: Contains the styles for the application.
- `jquery.min.js`: jQuery library for handling AJAX requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Django for providing a robust web framework.
- Icons from [Font Awesome](https://fontawesome.com/).

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Contact

If you have any questions or feedback, feel free to contact me.

