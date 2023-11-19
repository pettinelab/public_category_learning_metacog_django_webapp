This is the code base for the Django implementation of Drone recon. The webapp has been designed to run on Azure, but can be reconfigured to run on other cloud services. Azure's boilerplate is located at the end of this document.

By Warren Woodrich Pettine, M.D.
Last modified 2023-11-18

For questions, email warren.pettine@hsc.utah.edu.

## jsPsych task implementation
The Django code is a frame around the jsPsych task. If desired, that jsPsych code can be taken out and run separately. Core jsPsych code is contained in the files:

- drone_recon/templates/drone_recon/game.html
- static/js/function.js

To extract the game and run it in a different location, simply use those files along with the stimuli and passed parameters.

## Getting stimuli
There are two options for obtaining the stimuli used in this task: download pre-made or build them yourselves. It is highly recommended that you download them, at least the first time. The download will include the feedback stimuli, schematics and such.

To download, go to the box link: https://uofu.box.com/s/jo4p7jk4r0liboj0kynw0lp21g60wonx

If the blob storage is active (no guarantee), you can also get them from: https://dronereconstorage.blob.core.windows.net

To create, use the script make_drone_stims.ipynb in the other repo and build the stimuli.

## Checklist for setting up to run locally
The objective is to building the local postress database with all the relevant tables and stimuli. 
- Either create the drone stimuli, or download them. Note the location.
- Create virtual environment for the webapp. Install packages from `requirements.txt`.
- Install postgress and run the server. This is going to be system dependent.
- Run `python manage.py migrate`.
- Open a shell with `python manage.py shell`.
- Import the function with `from drone_recon.functions import createFullStimulusDB`.
- set the `file_dir` variable to wherever you stored the stimuli.
- run `createFullStimulusDB(file_dir=file_dir)`.
- Now follow the steps to run a Django webapp on your system/IDE. That will depend on your setup. 

You can then use the following URL to test a local Prolific implementation where the key variables are passed through the url. You may need to change the local port. 
http://127.0.0.1:8000/?WEBAPP_USE=task&PROLIFIC_PID=wtest&SESSION_ID=foo&STUDY_ID=bar


## Checklist for building the db on the Azure
- Set up the blob storage for the image files.
- Set up a postgress DB.
- Put the relevant DB login info in the `AZURE_POSTGRESQL_CONNECTIONSTRING` variable stored server-side.
- To get the static files working, I recommend the link: https://medium.com/@DawlysD/django-using-azure-blob-storage-to-handle-static-media-assets-from-scratch-90cbbc7d56be

## Additional azure details
Follow the instructions below. Also, the webapp is set up to use a google recapchu. That information is stored server side in the variables `GOOGLE_RECAPTCHA_SITE_KEY` and `GOOGLE_RECAPTCHA_SECRET_KEY`. 


#### THE FOLLOWING IS THE AZURE BOILERPLATE ####

# Deploy a Python (Django) web app with PostgreSQL in Azure
This is a Python web app using the Django framework and the Azure Database for PostgreSQL relational database service. The Django app is hosted in a fully managed Azure App Service. This app is designed to be be run locally and then deployed to Azure. You can either deploy this project by following the tutorial [*Deploy a Python (Django or Flask) web app with PostgreSQL in Azure*](https://docs.microsoft.com/azure/app-service/tutorial-python-postgresql-app) or by using the [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview) according to the instructions below.

## Requirements

The [requirements.txt](./requirements.txt) has the following packages:

| Package | Description |
| ------- | ----------- |
| [Django](https://pypi.org/project/Django/) | Web application framework. |
| [pyscopg2-binary](https://pypi.org/project/psycopg-binary/) | PostgreSQL database adapter for Python. |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from .env file and set them as environment variables. In this sample app, those variables describe how to connect to the database locally. <br><br> This package is used in the [manage.py](./manage.py) file to load environment variables. |
| [whitenoise](https://pypi.org/project/whitenoise/) | Static file serving for WSGI applications, used in the deployed app. <br><br> This package is used in the [azureproject/production.py](./azureproject/production.py) file, which configures production settings. |

## Using this project with the Azure Developer CLI (azd)

This project is designed to work well with the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview),
which makes it easier to develop apps locally, deploy them to Azure, and monitor them.

### Local development

This project has devcontainer support, so you can open it in Github Codespaces or local VS Code with the Dev Containers extension. If you're unable to open the devcontainer,
then it's best to first [create a Python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate that.

1. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

2. Create an `.env` file using `.env.sample` as a guide. Set the value of `DBNAME` to the name of an existing database in your local PostgreSQL instance. Set the values of `DBHOST`, `DBUSER`, and `DBPASS` as appropriate for your local PostgreSQL instance. If you're in the devcontainer, copy the values from `.env.sample.devcontainer`.

3. Run the migrations: (or use VS Code "Run" button and select "Migrate")

    ```shell
    python manage.py migrate
    ```

4. Run the local server: (or use VS Code "Run" button and select "Run server")

    ```shell
    python manage.py runserver
    ```

### Deployment

This repo is set up for deployment on Azure App Service (w/PostGreSQL server) using the configuration files in the `infra` folder.

🎥 Watch me deploy the code in [this screencast](https://www.youtube.com/watch?v=JDlZ4TgPKYc).

Steps for deployment:

1. Sign up for a [free Azure account](https://azure.microsoft.com/free/)
2. Install the [Azure Dev CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd). (If you opened this repository in a devcontainer, that part will be done for you.)
3. Provision and deploy all the resources:

    ```shell
    azd up
    ```

    It will prompt you to login and to provide a name (like "django-app") and location (like "eastus"). Then it will provision the resources in your account and deploy the latest code. If you get an error with deployment, changing the location (like to "centralus") can help, as there are availability constraints for some of the resources.

4. When `azd` has finished deploying, you'll see an endpoint URI in the command output. Visit that URI, and you should see the front page of the restaurant review app! 🎉 If you see an error, open the Azure Portal from the URL in the command output, navigate to the App Service, select Logstream, and check the logs for any errors.

    ![Screenshot of Django restaurants website](screenshot_website.png)

5. If you'd like to access `/admin`, you'll need a Django superuser. Navigate to the Azure Portal for the App Service, select SSH, and run this command:

    ```shell
    python manage.py createsuperuser
    ```

6. When you've made any changes to the app code, you can just run:

    ```shell
    azd deploy
    ```

### CI/CD pipeline

This project includes a Github workflow for deploying the resources to Azure
on every push. That workflow requires several Azure-related authentication secrets to be stored as Github action secrets. To set that up, run:

```shell
azd pipeline config
```

### Monitoring

The deployed resources include a Log Analytics workspace with an Application Insights dashboard to measure metrics like server response time.

To open that dashboard, just run:

```shell
azd monitor --overview
```

## Getting help

If you're working with this project and running into issues, please post in [Issues](/issues).
