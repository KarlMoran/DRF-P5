<img width="316" alt="lookbook" src="https://user-images.githubusercontent.com/92300013/196944892-09a81215-9f5c-4c44-9bd0-45a641831976.png">

This section of the project is the backend API database built to support the ReactJS frontend, and it is powered by the Django Rest Framework.

<hr />

* DEPLOYED API HEROKU <a href="https://drf-lookbook.herokuapp.com/" target="_blank">LINK HERE</a>
* DEPLOYED FRONTEND HEROKU LINK - <a href="https://lookbook-p5.herokuapp.com/" target="_blank">LIVE SITE</a>
* DEPLOYED FRONTEND REPOSITORY <a href="https://github.com/KarlMoran/lookbook" target="_blank">ClICK HERE</a>

<hr />

# User Stories:

* I have included links to the GitHub Issues for this project - <a href="https://github.com/KarlMoran/lookbook/issues" target="_blank">ClICK HERE</a>

* KANBAN BOARD - <a href="https://github.com/users/KarlMoran/projects/1/views/1" target="_blank">ClICK HERE </a>

# Database 

To view Database design for the DRF-p5 project <a href="https://lucid.app/documents/embedded/41f6af3b-8516-4c31-82bd-654871dbbe80?invitationId=inv_5276e9a1-0add-4676-b1bb-74ce3264a8aa#" target="_blank">ClICK HERE </a>

# Testing 

<h1>Manual Testing: </h1>

1. Manually verified each url path created works & opens without error.
2. Verified that the CRUD functionality is available in each app via the development version: Comments, Followers, Likes, Posts, Profiles
* Checked this by going to each link.
* Creating a new item.
* Checking new item URL path.
* Editing the item (not available for Likes, Followers or Users)
* Deleting the item (Not available for Users or Profiles)
3. Ensured search feature for Posts & liked apps returns results.
* had issues with my filtering, pages where not coming up correclty. Had to make sure that i had the most recent backend deployed. 
4. Repeated the steps for the deployed API, and all pages.
5. Frontend App throws a 500 operational error
* Had to reset database and migrations 
* created a new super user to test functionality

# Technologies Used:
## Main Languages Used:
* Python
* Frameworks, Libraries & Programs Used:
* Django
* Django RestFramework
* Cloudinary
* Heroku
* Pillow
* Django Rest Auth
* PostgreSQL
* Cors Headers
* DrawSQL:

# Deployment:
## Project creation:
1. Create the GitHub repository.
2. Create the project app on Heroku.
3. Add the Postgres package to the Heroku app via the Resources tab.
4. Once the GitHub repository was launched on GitPod, installed the following packages using the pip install command:
- 'django<4'
- dj3-cloudinary-storage
- Pillow
- djangorestframework
- django-filter
- dj-rest-auth
- 'dj-rest-auth[with_social]'
- djangorestframework-simplejwt
- dj_database_url psycopg2
- gunicorn
- django-cors-headers
5. Created the Django project with the following command:
django-admin startproject project_name .
6. Navigated back to Heroku, and under the Settings tab, added the following configvars:
* Key: SECRET_KEY | Value: hidden
* Key: CLOUDINARY_URL | Value: cloudinary://hidden
* Key: DISABLE_COLLECTSTATIC | Value: 1
* Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com
7. Add two additional configvars once the ReactApp has been created:
* Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
* Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
* Check that the trailing slash \ at the end of both links has been removed.
* Gitpod occasionally updates the browser preview link. Should this occur, the CLIENT_ORIGIN_DEV value shall need to be updated.
8. Created the env.py file, and added the following variables. The value for DATABASE_URL was obtained from the Heroku configvars in the previous step:
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'hidden'
os.environ['DATABASE_URL'] = 'postgres://hidden'

## In settings.py:

9. Add the following to INSTALLED_APPS to support the newly installed packages:

- 'cloudinary_storage',
- 'django.contrib.staticfiles',
- 'cloudinary',
- 'rest_framework',
- 'django_filters',
- 'rest_framework.authtoken',
- 'dj_rest_auth',
- 'django.contrib.sites',
- 'allauth',
- 'allauth.account',
- 'allauth.socialaccount',
- 'dj_rest_auth.registration',
- 'corsheaders',

10. Import the database, the regular expression module & the env.py
- import dj_database_url
- import re
- import os

if os.path.exists('env.py')
    import env

11. Below the import statements, add the following variable for Cloudinary:

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
- Below INSTALLED_APPS, set site ID:
SITE_ID = 1

12. Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:

- REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
13. Set the default renderer to JSON:

if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
    
14. Beneath that, added the following:
- REST_USE_JWT = True
- JWT_AUTH_SECURE = True
- JWT_AUTH_COOKIE = 'my-app-auth'
- JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
- JWT_AUTH_SAMESITE = 'None'

15. Then added:
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}

16. Updated DEBUG variable to:
DEBUG = 'DEV' in os.environ

17. Updated the DATABASES variable to:
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}

18. Added the Heroku app to the ALLOWED_HOSTS variable:
os.environ.get('ALLOWED_HOST'),
'localhost',

19. Below ALLOWED_HOST, added the CORS_ALLOWED variable as shown in DRF-API walkthrough:
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
    
20. Also added to the top of MIDDLEWARE:
'corsheaders.middleware.CorsMiddleware',
- During a deployment issue, it was suggested by a fellow student, Johan, to add the following lines of code below CORS_ALLOW_CREDENTIALS:
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CSRF_TRUSTED_ORIGINS = [os.environ.get(
    'CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN',
)]

## Final requirements:

21. Created a Procfile, & added the following two lines:
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi

22. Migrated the database:
python3 manage.py makemigrations
python3 manage.py migrate

23. Froze requirements:
pip3 freeze --local > requirements.txt

24. Added, committed & pushed the changes to GitHub
25. Navigated back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
Deployed the branch.


# CREDITS:
## Content:
- The creation of this API database was provided through the step by step guide of the C.I. DRF-API walkthrough project.
- All classes & functions have been credited.
- Modifications have been made.
- Thanks to  Tutor support who went above & beyond to assist me in resolving some issue with my database.