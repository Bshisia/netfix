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
- Django 3.1.14 (or compatible version)

### Installation

1. **Clone/Download the project**
   ```bash
   cd netfix
   ```

2. **Install Django** (if not already installed)
   ```bash
   pip install django==3.1.14
   ```

3. **Run Database Migrations**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

4. **Create Superuser** (for admin access)
   ```bash
   python3 manage.py createsuperuser
   ```

5. **Load Sample Data** (optional)
   ```bash
   python3 setup_sample_data.py
   ```

6. **Run the Development Server**
   ```bash
   python3 manage.py runserver
   ```

7. **Access the Application**
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

1. **Migration Errors**: Make sure to run migrations in order:
   ```bash
   python3 manage.py makemigrations users
   python3 manage.py makemigrations services
   python3 manage.py migrate
   ```

2. **Static Files Not Loading**: Ensure DEBUG=True in settings.py for development

3. **Import Errors**: Check Django version compatibility

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