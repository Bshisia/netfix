# Netfix - Service Marketplace

A Django-based service marketplace where customers can request services and companies can provide them.

## Features

- **User Registration**: Separate registration for customers and companies
- **Service Management**: Companies can create and manage their services
- **Service Requests**: Customers can request services with automatic cost calculation
- **User Profiles**: View user information and service history
- **Service Discovery**: Browse, search, and filter services
- **Admin Interface**: Manage all data through Django admin

## Setup Instructions

### Prerequisites
- Python 3.x
- Virtual environment (recommended)

### Installation

1. **Clone/Download the project**
   ```bash
   cd netfix
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv netfix_env
   source netfix_env/bin/activate  # On Linux/Mac
   # OR
   netfix_env\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   # OR manually install Django
   pip install "Django>=4.2,<5.0"
   ```

4. **Run Database Migrations**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Create Superuser** (for admin access)
   ```bash
   python3 manage.py createsuperuser
   ```

6. **Load Sample Data** (optional)
   ```bash
   python3 setup_sample_data.py
   ```

7. **Run the Development Server**
   ```bash
   python3 manage.py runserver
   ```

8. **Access the Application**
   - Main site: http://localhost:8000/
   - Admin interface: http://localhost:8000/admin/

## Sample Accounts

After running the sample data script:

### Admin Account
- Username: `admin`
- Password: `admin123`

### Sample Customer
- Username: `john_customer`
- Email: `john@example.com`
- Password: `password123`

### Sample Companies
- **Plumbing Pro**
  - Username: `plumbing_pro`
  - Email: `contact@plumbingpro.com`
  - Password: `password123`
  - Field: Plumbing

- **All Services**
  - Username: `all_services`
  - Email: `info@allservices.com`
  - Password: `password123`
  - Field: All in One

## User Types

### Customers
- Register with: email, password, username, date of birth
- Can request services
- View service request history in profile

### Companies
- Register with: email, password, username, field of work
- Can create and manage services
- Field restrictions apply (except "All in One" companies)

## Available Service Categories

- Air Conditioner
- Carpentry
- Electricity
- Gardening
- Home Machines
- House Keeping
- Interior Design
- Locks
- Painting
- Plumbing
- Water Heaters

## Project Structure

```
netfix/
├── main/           # Home page and common functionality
├── users/          # User management (customers, companies)
├── services/       # Service management and requests
├── static/         # CSS, images, and static files
├── templates/      # HTML templates
└── manage.py       # Django management script
```

## Troubleshooting

### Common Issues

1. **Externally Managed Environment Error**: If you get this error when installing Django:
   ```bash
   # Create virtual environment first
   python3 -m venv netfix_env
   source netfix_env/bin/activate
   pip install "Django>=4.2,<5.0"
   ```

2. **Distutils Module Error**: If you get "No module named 'distutils'" error:
   ```bash
   # Use newer Django version compatible with Python 3.13
   pip uninstall django
   pip install "Django>=4.2,<5.0"
   ```

3. **Migration Errors**: Make sure to run migrations in order:
   ```bash
   python3 manage.py makemigrations users
   python3 manage.py makemigrations services
   python3 manage.py migrate
   ```

4. **Static Files Not Loading**: Ensure DEBUG=True in settings.py for development

5. **Import Errors**: Check Django version compatibility and virtual environment activation

### Database Reset
If you need to reset the database:
```bash
rm db.sqlite3
python3 manage.py migrate
python3 manage.py createsuperuser
python3 setup_sample_data.py
```

## Development Notes

- The project uses SQLite database by default
- Static files are served automatically in development mode
- Email-based authentication is implemented
- All forms include CSRF protection
- Responsive design with custom CSS