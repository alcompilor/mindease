<br />
<img width="300" alt="Mindease Logo" src="https://i.imgur.com/shPchlq.png">
<br />

| ![license badge](https://img.shields.io/badge/license%20-MIT-green) | ![coverage badge](https://img.shields.io/badge/coverage%20-90%25-success) | ![pylint badge](https://img.shields.io/badge/pylint-passed-blue) | ![pylint badge](https://img.shields.io/badge/flake8-passed-blue) |
|:---:|:---:|:---:|:---:|

## 🤔 What is Mindease?

Mindease is an open-source web application built with [Flask](https://flask.palletsprojects.com/). It allows users to track and work to elevate their mood swings on a daily basis using a scale. Additionally, users can journal to reflect on their day, share their progress with a psychologist, and unwind while listening to instrumental music that encourages meditation.

## 🤔 Who is this documentation for?

This documentation is intended for hobbyists or businesses who want to host this web application on their own servers and link it to their own database. 

Please [refer here](#) if you would like to see a demo for the web application.
## ⚠️ Requirements

**python** - >= v3.10

**make** - You might want to use Chocolatey in order to install make on Windows

**pip** - Usually comes with Python but you might need to manually install it

**mysql** - Must be up and running with a ready to use database

**phpmyadmin** (Optional) - In case you need a decent Web GUI to administer the database

*Since the application will require port 5000 when operating, it must be open and available.*

## 🚀 Get Started
*Follow the steps below in order to properly host and run the application*

Clone the project

```bash
  git clone https://github.com/bigcbull/mindease.git
```

Go to the project directory

```bash
  cd mindease
```

Create and activate a virtual environment - (Linux/macOS) 

```bash
  python -m venv venv && source ./venv/bin/activate
```

Create and activate a virtual environment - (Windows)

```bash
  python -m venv venv && . .venv/Scripts/activate
```

Install required dependencies

```bash
  make init
```

Create a **.env** file inside the project's root directory, and set the following parameters inside it:

```bash
DATABASE_NAME = <Your Database Name>
DATABASE_HOSTNAME = <Your Database Hostname>
DATABASE_USER = <Your Database User>
DATABASE_PASSWORD = <Your Database Password>
APP_SECRET_KEY = <Random Solid Key>

# Example:

DATABASE_NAME=mindease
DATABASE_HOSTNAME=db.mindease.com
DATABASE_USER=mindease_user
DATABASE_PASSWORD=XPxv39ebR5P4B4a
APP_SECRET_KEY=SyRe462xk9uScqB
```

Run the application:

```bash
  make run
```

***Important:*** *Always reactivate the virtual environment before running the application.*

***Note:*** *The application will run on port 5000*
## ⚙️ Running Tests - for development purposes

To execute tests and linters, run the following command

```bash
  make test dir=./src/utils/<package>
```

Example - To run tests and linters on the user package one can do the following:

```bash
  make test dir=./src/utils/user
```


***Note:*** *Windows users must use a bash terminal such as [git bash](https://gitforwindows.org/) in order for this to work correctly.*

## 📃 Documentation - for development purposes

To view documentation for specific module, run the following command

```bash
  make doc module=./src/utils/<package>/<module>.py
```

Example - To view documentation for the user module in the user package one can do the following:

```bash
  make doc module=./src/utils/user/user.py
```

***Note:*** *Windows users might need to use a bash terminal such as [git bash](https://gitforwindows.org/) in order for this to work correctly.*
## 👨‍🎓 Authors
- [@Shuayb Warsame](https://www.github.com/shuaybw)
- [@Mohammed Alkateb](https://www.github.com/mohammed-alkateb)
- [@Ahmed Abbasi](https://www.github.com/bigcbull)
- [@Mohamed Nour Humeidi](https://www.github.com/MoNourH)
- [@Joseph Hammami](https://www.github.com/josephhammami)