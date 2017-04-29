# Ares
[![Build Status](https://travis-ci.org/tehpug/Ares.svg?branch=master)](https://travis-ci.org/tehpug/Ares)

# Battlefield - http://battlefield.tehpug.ir
Battlefield is a place for developers to have fun and learn more about coding. Developers can create robots (write codes) to play in different games at battlefield and run them against other developers robots and get score!

## Supervisor
Battlefield needs a supervisor to handle jobs like running the games, keeping scores, managing leagues and tournaments and etc. **Ares**(this project) is the supervisor of Battlefield.

### Usage
The project is deployed and working at [http://battlefield.tehpug.ir](http://battlefield.tehpug.ir). but if you wanted to run the project for yourself clone the project
```
$ git clone git@github.com:tehpug/Ares.git
```
and install the dependencies (we recommend using [virtual environment](https://docs.python.org/3/library/venv.html))
```
$ pip install -U requirements.txt
```
create a `.env` file at root of the project and write the configurations you need like `DATABASE_URL`
execute this command to create or update the schema in your database
```
$ python manage.py migrate
```
and finally run the project by this command
```
$ python manage.py runserver
```
you also need to create a superuser to access the admin panel.

### Why?
Basically for fun :) but there are some other reasons. TehPUG is a great community with so much potential. One of the reasons to creating this project was to do something practical at TehPUG that it will last more than 2 or 3 sessions. with this project. we could write codes and create new robots, come up with new ideas both for robots and games and the creativity, learning and fun will last for more than years :)

### Contribute
We're so happy that you're looking at the project and we know that you're may be thinking about contributing to the project and we also think it's a great idea. but **please before doing anything read this [document](CONTRIBUTING.md) carefully**.

### Maintainer
[@mehdy](https://github.com/mehdy) is currently the maintainer of the project.

### Top Contributors
1. [@geraneum](https://github.com/geraneum)

### why is it called "Ares"?
[Ares](https://en.wikipedia.org/wiki/Ares) is the greek god of war. this project is managing everything in the battlefield so it's kinda the god of war :))

### Contact
if you want to follow the project or talk to the project's developers you can join `#battlefield` at [tehpug's slack](https://irpython.slack.com/). if you're not registered yet you cain join using this [link](https://irpython.slack.com/shared_invite/MTcxOTYwNjkwNjI1LTE0OTI3NjQwMjItYzk4OGQ1NjU3Zg)

## License
GPLv3 License. See the [LICENSE](LICENSE) file for more information.
