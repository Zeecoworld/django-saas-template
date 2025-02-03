# Django SaaS Template

A modern, production-ready Django SaaS (Software as a Service) template with Appwrite integration for database and authentication, and Stripe for subscription management.

## 🚀 Features

### Current Features
- **Appwrite Integration**
  - Database management
  - User authentication
  

- **Authentication & Authorization**
  - User registration and login
  

- **Subscription Management (Stripe)**
  - Payment processing
  - Usage-based billing
  - Webhook integration

- **Core Features**
  - Responsive dashboard
  - User profile management
  - Activity logging
  - API endpoints

### 🔜 Coming Soon
- Multi-tenancy support
- Team collaboration features
- Advanced analytics
- Custom reporting
- Webhook management
- API documentation
- Integration with popular services
- Enhanced security features

## 📋 Prerequisites

- Python 3.8+
- Appwrite instance (database for both users/subscriptions)
- Stripe account
  

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/django-saas-template.git
cd django-saas-template
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```
# Django
DEBUG=True
SECRET_KEY=your-secret-key

# Appwrite
APPWRITE_ENDPOINT=your-appwrite-endpoint
APPWRITE_PROJECT_ID=your-project-id
APPWRITE_API_KEY=your-api-key

# Stripe
STRIPE_PUBLIC_KEY=your-stripe-public-key
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_WEBHOOK_SECRET=your-webhook-secret
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

## 🔧 Configuration

### Appwrite Setup

1. Create an Appwrite project
2. Set up collections for:
   - Users
   - Profiles
   - Subscriptions
   - Settings
3. Configure authentication methods
4. Set up security rules

### Stripe Setup

1. Create a Stripe account
2. Set up products and pricing
3. Configure webhooks
4. Add payment methods
5. Set up billing portal

## 📁 Project Structure

```
django-saas-template/
├── apps/
│   ├── users/          # User management
│   ├── subscription/   # Subscription handling
│   
├── project-name/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
├── static/
├── docs/
└── manage.py
```

## 🚀 Deployment

1. Set up your production environment
2. Configure your web server
3. Set up SSL certificates
4. Configure email service
5. Set up monitoring

Detailed deployment guide available in `docs/deployment.md`

## 🔒 Security

- CSRF protection enabled
- XSS prevention
- SQL injection protection
- Secure password hashing
- Session security
- CORS configuration

## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Support
- Create an issue
- Email: zeecomedia2@gmail.com

## 🙏 Acknowledgments
- Django community
- Appwrite team
- Stripe developers
- All contributors

## 📚 Documentation

Full documentation is available at [docs/](docs/):
- Installation guide
- Configuration options
- API documentation
- Customization guide
- Deployment instructions
- Security best practices

---
Made with ❤️ by @zeecomedia
