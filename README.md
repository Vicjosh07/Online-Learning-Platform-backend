# 🎓 Online Learning Platform

A comprehensive Django-based e-learning platform that enables educational institutions to manage courses, students, and lecturers with role-based access control and interactive dashboards.

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [User Roles](#-user-roles)
- [API Endpoints](#-api-endpoints)
- [Database Models](#-database-models)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 🔐 Authentication & User Management
- **Multi-role Authentication**: Students, Lecturers, and Visitors
- **Custom User Profiles**: Extended user profiles with personal information
- **Role-based Access Control**: Different permissions for different user types
- **Profile Picture Upload**: Image processing with automatic resizing
- **Social Media Integration**: LinkedIn and Facebook profile links

### 📚 Course Management
- **Course Creation**: Lecturers can create and manage courses
- **Level-based Organization**: Courses organized by academic levels (100-600)
- **Department Categorization**: Courses grouped by departments
- **Course Thumbnails**: Visual representation of courses
- **Document Links**: External resource integration
- **Course Topics**: Structured course content with ordering

### 🎯 Student Features
- **Personal Dashboard**: Customized learning dashboard
- **Course Enrollment**: Add/remove courses from personal collection
- **Progress Tracking**: Track learning progress
- **Profile Customization**: Manage personal information and preferences

### 👨‍🏫 Lecturer Features
- **Course Upload Interface**: Easy course creation and management
- **Student Management**: Track enrolled students
- **Content Organization**: Structure course materials effectively
- **Profile Management**: Professional profile setup

### 🌐 Public Features
- **Homepage**: Showcases recent courses and platform information
- **Course Catalog**: Browse all available courses
- **About Section**: Platform information
- **FAQ Section**: Common questions and answers
- **Contact Page**: Get in touch with administrators
- **Blog Section**: Educational content and updates

## 🛠 Technology Stack

- **Backend Framework**: Django 5.1.7
- **Database**: SQLite3 (Development) / PostgreSQL (Production Ready)
- **Authentication**: Django Built-in Authentication System
- **Image Processing**: Pillow (PIL)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Static Files**: Django Static Files Management
- **Media Handling**: Django Media Files System

## 🏗 Project Structure

```
elearning/
├── accounts/                    # User authentication and profiles
│   ├── models.py               # UserProfile model
│   ├── views.py               # Auth views (login, register, logout)
│   ├── urls.py                # Auth URLs
│   ├── decorators.py          # Role-based access decorators
│   ├── middleware.py          # Custom middleware
│   ├── context_processors.py # Template context processors
│   └── templates/             # Auth templates
├── dashboard/                  # Student/User dashboard
│   ├── models.py              # Course and UserCourse models
│   ├── views.py               # Dashboard views
│   ├── urls.py                # Dashboard URLs
│   └── templates/             # Dashboard templates
├── sections/                   # Public pages and lecturer tools
│   ├── views.py               # Public views and course creation
│   ├── urls.py                # Public URLs
│   └── templates/             # Public page templates
├── elearning/                  # Main project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
├── templates/                  # Global templates
├── media/                      # User uploaded files
│   ├── course_thumbnails/     # Course images
│   └── profile_pics/          # User profile pictures
├── staticfiles/               # Collected static files
└── manage.py                  # Django management script
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)

### Step-by-step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vicjosh07/Online-Learning-Platform-backend.git
   cd Online-Learning-Platform-backend
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv myenv
   myenv\Scripts\activate

   # Linux/Mac
   python -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==5.1.7
   pip install pillow
   pip install numpy  # Required for image processing
   ```

4. **Navigate to project directory**
   ```bash
   cd elearning
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📖 Usage

### For Students/Visitors
1. **Register** for a new account or **login** with existing credentials
2. Browse available courses from the **Courses** page
3. Add courses to your personal dashboard
4. Access your **Dashboard** to view enrolled courses
5. Update your **Profile** with personal information

### For Lecturers
1. **Register** with "Lecturer" role or **login** with lecturer credentials
2. Access the **Course Upload** interface
3. Create new courses with thumbnails and descriptions
4. Add course topics and organize content
5. Manage your course offerings

### For Administrators
1. Access the **Django Admin Panel**
2. Manage users, courses, and platform content
3. Monitor platform activity and user engagement

## 👥 User Roles

### 🎓 Student
- Browse and enroll in courses
- Access personal dashboard
- Manage profile information
- Track learning progress

### 🎯 Visitor
- Browse public course catalog
- View course information
- Limited access to platform features
- Can upgrade to student account

### 👨‍🏫 Lecturer
- Create and manage courses
- Upload course materials
- Organize course content
- Access specialized lecturer dashboard

## 🔗 API Endpoints

### Authentication
- `POST /accounts/register/` - User registration
- `POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout

### Dashboard
- `GET /dashboard/` - User dashboard
- `POST /dashboard/add-course/<int:course_id>/` - Add course to dashboard
- `POST /dashboard/remove-course/<int:user_course_id>/` - Remove course
- `GET /dashboard/profile/` - User profile
- `POST /dashboard/update-profile/` - Update profile

### Public Pages
- `GET /` - Homepage
- `GET /about/` - About page
- `GET /courses/` - All courses
- `GET /faq/` - FAQ page
- `GET /contact/` - Contact page
- `GET /blog/` - Blog section

### Lecturer Tools
- `GET /profile/` - Lecturer profile/course upload
- `POST /create-course/` - Create new course
- `POST /add-topic/` - Add course topic
- `DELETE /delete-course/<int:course_id>/` - Delete course

## 🗃 Database Models

### UserProfile
```python
- user: OneToOneField(User)
- profile_pic: ImageField
- role: CharField (STUDENT, VISITOR, LECTURER)
- matric: CharField
- phonenumber: CharField
- description: TextField
- first_name, last_name: CharField
- linkedin, facebook: CharField
- occupation: CharField
```

### Course
```python
- thumbnail: ImageField
- title: CharField
- lecturer: ForeignKey(User)
- level: CharField (100-600 Level)
- department: CharField
- description: TextField
- document_link: URLField
```

### CourseTopic
```python
- course: ForeignKey(Course)
- title: CharField
- content: TextField
- order: PositiveIntegerField
```

### UserCourse
```python
- user_profile: ForeignKey(UserProfile)
- course: ForeignKey(Course)
- added_at: DateTimeField
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file for production:
```env
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
ALLOWED_HOSTS=your-domain.com
```

### Media Settings
- **Profile Pictures**: Automatically resized to 200x200px
- **Course Thumbnails**: Stored in `media/course_thumbnails/`
- **Default Images**: Fallback images for profiles

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure production database
3. Set up static file serving
4. Configure media file serving
5. Set proper `ALLOWED_HOSTS`
6. Use environment variables for sensitive data
7. Set up SSL/HTTPS
8. Configure backup strategy

### Recommended Hosting
- **Heroku**: Easy deployment with PostgreSQL addon
- **PythonAnywhere**: Simple Python hosting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write clear commit messages
- Add tests for new features
- Update documentation as needed


## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact me


## 🙏 Acknowledgments

- Django framework community
- Bootstrap for responsive design
- FontAwesome for icons
- Frontend Contributor - Ola Timothy (unibuja developer) 

---

**Made with ❤️ by [Vicjosh07](https://github.com/Vicjosh07)**
