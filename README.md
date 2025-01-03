# Django Quiz Project

This is a simple Django-based quiz application that allows users to start a quiz by visiting a specific URL.

## Prerequisites

Ensure you have the following installed:

- Python (3.8+ recommended)
- Django (4.x or higher)
- Database (SQLite is used by default)

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone <repository_url>
cd <project_directory>

### 2. Create a Virtual Environment

It's recommended to create a virtual environment to manage your dependencies. Run the following commands:

# Create virtual environment (if you're using Python 3)
python3 -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

### 3. Install Dependencies
Once the virtual environment is activated, install the required dependencies using pip:

pip install -r requirements.txt

### 4. Run Migrations
Before running the project, you need to apply the database migrations. Run the following command:

python manage.py migrate
This will set up the necessary database tables for your project.

### 5. Start the Development Server
Now, you're ready to run the Django development server. Use the following command:

python manage.py runserver
The server will start, and you should see output indicating that the server is running on http://127.0.0.1:8000/.

### 6. Access the Quiz
To start the quiz, open your web browser and navigate to the following URL:

http://127.0.0.1:8000/quiz/start

This will direct you to the quiz start page.#   Q u i z  
 #   Q u i z  
 