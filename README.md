# 📝 Blog Website

A fully functional **Django-based Blog Website** where users can **read, create, edit, and manage blog posts**.  
The project includes **user authentication, categories, an admin dashboard, and media uploads**, making it a solid foundation for a modern blogging platform.  

--------------------------------------------------------------------------------
🚀 Features
--------------------------------------------------------------------------------
- User registration and login system  
- Create, edit, and delete blog posts  
- Categorize posts for better organization  
- Admin dashboard for managing posts, users, and categories  
- Media uploads for posts and user profiles  
- Responsive templates for a clean, modern look  
- Search functionality (by keywords or categories)  
- Modular Django apps for scalability and expansion  

--------------------------------------------------------------------------------
🛠️ Tech Stack
--------------------------------------------------------------------------------
- **Backend**: Django 4.x  
- **Database**: SQLite (default, for local dev)  
- **Frontend**: HTML, CSS, Django Templates  
- **Static & Media Handling**: Django static and media configuration  

--------------------------------------------------------------------------------
⚙️ Installation
--------------------------------------------------------------------------------
# 1. Clone the repository
git clone https://github.com/nagarkotiArun420/Blog_website.git
cd Blog_website

# 2. Create a virtual environment and activate it
python -m venv env
env\Scripts\activate     # Windows
source env/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirement.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser for admin access
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver

--------------------------------------------------------------------------------
📂 File Structure
--------------------------------------------------------------------------------
Blog-Website/
│── manage.py
│── db.sqlite3
│── requirement.txt
├── authentication/       # Handles user registration & login
├── blog_app/             # Core blog functionality
├── blog_category/        # Category management
├── blog_main/            # Main app settings and config
├── dashboard/            # Admin dashboard
├── media/                # Uploaded media files
└── templates/            # HTML templates

--------------------------------------------------------------------------------
📖 Usage
--------------------------------------------------------------------------------
- Register or log in to create and manage blog posts.  
- Admin dashboard allows management of **users, posts, and categories**.  
- Use the search bar to filter posts by **keywords or categories**.  

--------------------------------------------------------------------------------
🚧 Future Improvements
--------------------------------------------------------------------------------
- Add comment functionality for posts  
- Implement pagination for blog lists  
- Switch to PostgreSQL for production-ready deployment  
- Add social login & enhanced user profiles  
- Upgrade frontend using **Bootstrap** or **TailwindCSS**  

--------------------------------------------------------------------------------
📜 License
--------------------------------------------------------------------------------
This project is **open-source** and free to use.  

--------------------------------------------------------------------------------
📬 Contact
--------------------------------------------------------------------------------
- GitHub: https://github.com/nagarkotiArun420
- Email: nagarkotiarun420@gmail.com
- LinkedIn: https://www.linkedin.com/in/arun-nagarkoti-b53276263/
