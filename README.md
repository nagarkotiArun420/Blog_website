
# Blog Website

A fully functional **Django-based Blog Website** where users can read, create, edit, and manage blog posts. The project includes user authentication, categories, a dashboard for admin management, and media uploads.

---

## Features

- User registration and login system
- Create, edit, and delete blog posts
- Categorize posts
- Admin dashboard for managing posts, users, and categories
- Media uploads for posts and user profiles
- Responsive templates for a modern blog look
- Search posts by keywords or categories
- Modular Django apps for easy expansion

---

## Tech Stack

- Backend: Django 4.x
- Database: SQLite (default)
- Frontend: HTML, CSS, Django Templates
- Static & Media Files: Handled with Django static and media configuration

---

## Installation

1. Clone the repository:
\`\`\`bash
git clone <your-repo-url>
cd Blog-Website
\`\`\`
2. Create a virtual environment and activate it:
\`\`\`bash
python -m venv env
env\Scripts\activate
\`\`\`
3. Install dependencies:
\`\`\`bash
pip install -r requirement.txt
\`\`\`
4. Apply migrations:
\`\`\`bash
python manage.py migrate
\`\`\`
5. Create a superuser:
\`\`\`bash
python manage.py createsuperuser
\`\`\`
6. Run the development server:
\`\`\`bash
python manage.py runserver
\`\`\`

---

## File Structure

\`\`\`text
Blog-Website/
│   manage.py
│   db.sqlite3
│   requirement.txt
├── authentication/
├── blog_app/
├── blog_category/
├── blog_main/
├── dashboard/
├── media/
└── templates/
\`\`\`

---

## Usage

- Register or log in to create and manage posts.  
- Admin dashboard allows user and category management.  
- Use search to filter posts by keywords or categories.  

---

## Future Improvements

- Add comment functionality for posts  
- Implement pagination  
- Use PostgreSQL for production  
- Add social login and user profiles  
- Enhance frontend with Bootstrap or TailwindCSS  

---

## License

This project is open-source and free to use.
"@ | Set-Content README.md
