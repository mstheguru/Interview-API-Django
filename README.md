# Interview-API-Django
API for candidates/interviewers to register their available time slots &amp; API which will return 
interview schedulable time slots as a list which will take candidate id and interviewer id as input.

##### Installation
- Clone this repository: `git clone https://github.com/mstheguru/Interview-API-Django.git`
- Create a virtual environment outside the cloned project using python 3.7 `virtualenv -p python3.7 <environment_name>`
- Activate the virtual environment: `source <path_to_virtual_env>/bin/activate`
- `cd` to the folder `Interview-API-Django`
- Install the dependencies using `pip intsall -r requirements.txt`
- Database used: `sqlite3`

##### Setting up the application
- Migrate using command `python manage.py migrate` before running the application
- Create super user for django admin access: `python manage.py createsuperuser`

##### Run the application
- Run the application using command: `python manage.py runserver <host>:<port>`
