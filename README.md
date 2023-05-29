# Google Calendar Integration using Django REST API

This Django project demonstrates the integration of Google Calendar using the Django REST API. It allows users to authenticate with their Google accounts and retrieve a list of events from their calendars.

## Features

- OAuth2 authentication with Google
- Fetching events from the user's calendar
- JSON response with event details

## Requirements

- Python 3.x
- Django 3.x
- Requests library

## Installation

1. Clone the repository or download the source code:

```
   git clone https://github.com/your-username/google-calendar-integration.git
```

2. Navigate to the project's root directory:

```
   cd google-calendar-integration
```
3. Create a virtual environment (optional but recommended):

```
  python3 -m venv venv
  source venv/bin/activate
```

4. Install the required packages:

```
  pip install -r requirements.txt
```

5. Configure the Google API credentials:
Obtain the client ID and client secret from the Google Cloud Console.
Update the settings.py file in the project's Django settings with your Google API credentials:

```
  GOOGLE_CLIENT_ID = 'your-client-id'
  GOOGLE_CLIENT_SECRET = 'your-client-secret'
```

6. Run the Django development server:

```
  python manage.py runserver
```
