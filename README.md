# QuickFindMovies

**QuickFindMovies** is a simple Django web application that allows users to **browse and filter movies** by **genre, year, and country** from an Excel file.

---

##  Features

-  Import movie data from an Excel file.
-  Display movie list dynamically with Django templates.
-  Filter movies by:
  - Genre (e.g. Action, Comedy)
  - Year (e.g. 2020, 2021)
  - Country (e.g. Bangla, Hindi, English)

---

##  Tech Stack

- Python 3.x
- Django
- Pandas
- Openpyxl
- HTML, CSS, Bootstrap (Django Template Engine)


## Installation Guide

Follow these steps to run the project locally:

**Clone the Repository**

    ```bash
    git clone https://github.com/hasdajustin/quick_find_movies.git
    cd quick_find_movies

**Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv env
    venv\Scripts\activate       # For Windows
    # source venv/bin/activate  # For macOS/Linux
    
**Install dependencies:**

    ```bash
    pip install -r requirements.txt

**Run database migrations:**

    ```bash
    python manage.py migrate

**Start the development server:**

    ```bash
    python manage.py runserver

**Access the site:**

    Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Excel File Format

    Your `movies.xlsx` file should be placed at the project root, and must follow this structure:

    | title           | genre     | year | director       | country   |

---

**Place the File in the Project Root**
    Save your Excel file in the main project directory (same level as manage.py).
    Recommended filename: `movies.xlsx`

**(Optional) Use a Different File Name**
    If you want to use a different file name (like - my_movies.xlsx), 
    open the file:
    core/management/commands/import_movies.py.
    Replace this line:
    df = pd.read_excel('movies.xlsx').
    With:
    df = pd.read_excel('my_movies.xlsx').

**Clear Previous Data**

    ```bash
    python manage.py flush

**Import the Movies**

    ```bash
    python manage.py import_movies
