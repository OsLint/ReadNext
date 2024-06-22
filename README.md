# Book recommendations system

Project made for my PPY (Programing in Python) Class in Polish Japanese Academy of Information Technology.

## Initialize data base before running the app

### Run the database
```bash
flask db init

flask db migrate -m "initial migration"

flask db upgrade
```

if you don't have data in database you can seed it by running the following command
```bash
flask seed_db
```

## Common errors

if you are using chrome or chromium and you get 403 error when trying to login or running the app,
you can try to clear the socket pool by going to the following address in your browser
```
chrome://net-internals/#sockets
```

