import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views import View
from django.http import JsonResponse
from django.urls import reverse
from urllib.parse import urlencode


class GoogleCalendarInitView(View):
    def get(self, request):
        params = {
            'client_id': settings.GOOGLE_CLIENT_ID,
            'redirect_uri': request.build_absolute_uri(reverse('calendar-redirect')),
            'scope': 'https://www.googleapis.com/auth/calendar.readonly',
            'response_type': 'code',
        }
        oauth_url = 'https://accounts.google.com/o/oauth2/auth?' + urlencode(params)
        return HttpResponseRedirect(oauth_url)


class GoogleCalendarRedirectView(View):
    def get(self, request):
        code = request.GET.get('code')

        token_url = 'https://accounts.google.com/o/oauth2/token'
        token_params = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': request.build_absolute_uri(reverse('calendar-redirect')),
            'grant_type': 'authorization_code',
        }

        response = requests.post(token_url, data=token_params)
        if response.status_code == 200:
            access_token = response.json().get('access_token')

            events_url = 'https://www.googleapis.com/calendar/v3/calendars/primary/events'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Accept': 'application/json',
            }

            response = requests.get(events_url, headers=headers)
            if response.status_code == 200:
                events = response.json().get('items', [])

                return JsonResponse(events, safe=False)

        error_message = response.json().get('error', 'An error occurred during the OAuth process.')
        return JsonResponse({'error': error_message}, status=400)
