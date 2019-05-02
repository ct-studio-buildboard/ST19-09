# How to run?

If you want to run the machine learning model, you can access the CLeaned_ML_Model_Copy1.ipynb and run everything from beginning to end. The first cell contains all of the requirements needed to run and will need to be installed. The training model will require approximately 8 hours to train locally because there are 14,000 tweets being used.

To run the flask app, go into the Contentor_dashboard/app folder, and install all of the requirements from requirements.txt. You must also set the FLASK_APP environment variable to application.py. Afterwards, you can call "flask run" and the application will run. On Mac, the command is "export FLASK_APP=application.py" and for Windows, it is "set FLASK_APP=application.py"


# How will this information be used?
This information will be used to generate a website featuring all Studio projects.
* For Startup Studio: http://buildboard-10044.cornelltech.io/startup-studio-2019
* For BigCo Studio: http://buildboard-10044.cornelltech.io/bigco-studio-2019
