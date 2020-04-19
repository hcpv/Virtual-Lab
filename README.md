# Virtual Lab for Control System
Virtual lab is an online platform for performing various experiments related to control systems.
## Usage
Clone the project
```
git clone https://github.com/himanshuamd1/Virtual-Lab.git
```
Change the directory to the project folder
```
cd Virtual-Lab
```
Install the project dependencies<br/>
[Optional] To setup virtual env
```
pipenv install
pipenv shell
```
```
py -m pip install -r requirements.txt
```
Make migrations
```
py manage.py makemigrations
py manage.py migrate
```
Run Server
```
py manage.py runserver
```
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
## Built With
* Django web framework
* python
* html
* css
