# expense/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense.settings')

application = get_wsgi_application()  # Ensure this line is present
