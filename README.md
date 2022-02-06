# Book Management System 
_Developed by:_
__Dipendra Tamang__
***
######This Management system explains in following ways
Completed Project as per Internship Task given by[Treeleaf](https://treeleaf.ai/) Company<br/>
if user.is_superuser :<br/>
 superuser can easily add the details of book from the admin page.<br/>
 superuser can also buy and delete the book from the database.<br/>
if user.is not superuser:<br/>
user can buy book <br/>
<br/>
once  buy button is clicked it will update on in_stock attribute of book<br/>
Simply clone the project from [Github](https://github.com/DipendraBravo/sales-mgmt) and follow the procedure <br/>
Install all the packages 
used command from console
```cython
pip install requirements.txt
```
```cython
py manage.py migrate
```
create super admin
```cython
py manage.py createsuperuser
```
Run the server and enjoy it
```cython
py manage.py runserver
```