# Software needed to run the project
- Anaconda Prompt
- Python
- MongoDB

# Steps to run the project
1. Download or clone this repository.
2. Launch the anaconda prompt
3. Change the directory to the project's directory
4. Perform the following commands:
  - conda create --name JournalEnv django ///// Creates a new virtual environment called LMS /////
  - conda activate JournalEnv ///// Activates the newly created virtual environment /////
  - pip install -r requirements.txt ///// Installs additional files to help run this project universally with different versions of django /////
  - python manage.py makemigrations ///// Makes migrations in case of any changes in models /////
  - python manage.py migrate ///// Migrates everything to the database /////
  - python manage.py runserver ///// Start the server /////
5. Paste this host http://127.0.0.1:8000/

