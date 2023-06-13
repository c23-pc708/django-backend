# Django Backend

A REST API backend for the mobile application

## SETUP GUIDE
1. Have Python installed
2. Create a virtual env `python -m venv env` and activate it `env\Scripts\activate.bat`
3. Install requirements `pip install -r requirements.txt`
4. Set .env (see .env.example). Be sure to have a postgres database running.
5. Run database migration, `python manage.py makemigrations`, then `python manage.py migrate`
6. Run the server `python manage.py runserver`

## DEPLOYMENT GUIDE
You can deploy this application in any platform you like. In our case, we used Cloud Run as our deployment platform since it supports autoscaling, and our dockerization method ensures that our application can be run anywhere. A Dockerfile is provided alongside this repository. Please refer to Google Cloud Run's documentation to deploy on your own: https://cloud.google.com/run/docs/quickstarts/deploy-continuously.

Because env variables are used, database migration is not done as a container build step. As a result, you will have to do your migration from your local machine (connected to the deployment database) using the right database credentials.