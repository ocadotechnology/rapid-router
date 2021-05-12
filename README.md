# Rapid Router (codename: ocargo)

[![Workflow Status](https://github.com/ocadotechnology/rapid-router/actions/workflows/ci.yml/badge.svg)](https://github.com/ocadotechnology/rapid-router/actions/workflows/ci.yml)
[![Coverage Status](https://codecov.io/gh/ocadotechnology/rapid-router/branch/master/graph/badge.svg)](https://codecov.io/gh/ocadotechnology/rapid-router)
[![Code Climate](https://codeclimate.com/github/ocadotechnology/rapid-router/badges/gpa.svg)](https://codeclimate.com/github/ocadotechnology/rapid-router)
[![Crowdin](https://d322cqt584bo4o.cloudfront.net/code-for-life/localized.svg)](https://crowdin.com/project/code-for-life)

## Code for Life and Rapid Router Overview

Rapid Router is a [Code for Life][c4l] project, aimed at teaching primary school children programming concepts through a vehicle routing game.
Ocado Technology's [Code for Life][c4l] initiative has been developed to inspire the next generation of computer scientists and to help teachers deliver the computing curriculum.

This repository hosts the source code of the **Rapid Router game**.

The other repos for Code For Life:

- the main portal or the website: [Code For Life Portal](https://github.com/ocadotechnology/codeforlife-portal)
- our second game for older children: [Kurono (code name: aimmo)](https://github.com/ocadotechnology/aimmo)
- the [deployment code for Google App Engine](https://github.com/ocadotechnology/codeforlife-deploy-appengine)

## How to play

Go to [Code For Life website][c4l]. You can [play Rapid Router](https://www.codeforlife.education/rapidrouter/) right away. You can register and log in as teacher or independent student to save your progress.

## How to set up and run locally

Clone the repo: `https://github.com/ocadotechnology/rapid-router.git`.

> If you want to contribute, [fork it first](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo), work on a branch, make a fix, and submit a pull request.

### Ubuntu / Linux Mint

- Run `sudo apt-get install python-dev`.

- Run `sudo apt-get update` to save having to do it later in the process.

- Follow the instructions for [installing pyenv](https://github.com/pyenv/pyenv#installation).

- Run `sudo apt-get install python-pip`.

- Run `pip install pipenv` to get the [pipenv](https://pipenv.readthedocs.io/en/latest/) virtual environment.

### Mac

- Get the [brew](https://brew.sh/) package manager.

- It's recommended to update sqlite3 as Mac default version may be incompatible. Check [common issues here](https://github.com/ocadotechnology/aimmo/blob/development/docs/common-issues.md).  
  To update sqlite3 with brew: `brew install sqlite3`. Then follow the instructions in `brew info sqlite3` before installing a python version with `pyenv`.

```
If you need to have sqlite first in your PATH, run:
  echo 'export PATH="/usr/local/opt/sqlite/bin:$PATH"' >> ~/.zshrc

For compilers to find sqlite you may need to set:
  export LDFLAGS="-L/usr/local/opt/sqlite/lib"
  export CPPFLAGS="-I/usr/local/opt/sqlite/include"
```

- Then install pyenv with the right sqlite3 version (make sure `LDFLAGS` and `CPPFLAGS` are set as above): `brew install pyenv`.

- Run `brew install pipenv`.

### Development and tests

- Run `pipenv install --dev` to get the requirements for the project.

- Followed by `pipenv shell` to activate the virtual env.

- `./run` - This will:
  - sync the database
  - collect the static files
  - run the server
- Once you see `Quit the server with CONTROL-C`, you can open the portal in your browser at `localhost:8000`.

- Run `pytest` to run unit tests. All tests will be run on github when PR is submitted, but it's good to check locally too to make sure the tests run successfully after your changes.

### Localisation

If you have problems seeing the portal on machines with different locale (e.g. Polish), check the terminal for errors mentioning `ValueError: unknown locale: UTF-8`. If you see them, you need to have environment variables `LANG` and `LC_ALL` both set to `en_US.UTF-8`.

- Either export them in your `.bashrc` or `.bash_profile`
- or restart the portal with command `LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 ./run`.

For localisation admins:

- `./run --with-translation-tools` in your rapid-router dir to include the translation/localisation libraries
- You will need your crowdin api key locally in the `CROWDIN_API_KEY` environment variable, e.g. `export CROWDIN_API_KEY=<key>`. This can be obtained from [the settings page](https://crowdin.com/project/code-for-life/settings#integration)
- Set your `django_language` cookie to `lol-us` to enable in-context localisation

## To contribute

Check our [contributing section](https://github.com/ocadotechnology/rapid-router/contribute). It contains the guidelines and issues labelled as "good first issue," selected for their relative approachability for first-time contributors.

**Found a problem? Please check whether it has already been reported in our [issue tracker][issues] first!** If not, [add it][add-issue] as a bug report. Please make sure that you give us a suitable level of detail about the symptoms and how to reproduce it.

You can also [submit a feature request][add-issue]. Make sure that you give us a suitable level of detail about the feature. Please note that we may not act upon all suggestions, if they are not in line with the direction we want to take the project, or if we don't have the development resources to get it done.

> One word of caution: **please do not add any issues related to security**. Evil hackers are everywhere nowadays... If you do find a security issue, let us know using our contact form on [the website][c4l]. (Scroll down, click on `Contact us`)

[c4l]: https://www.codeforlife.education/
[issues]: https://github.com/ocadotechnology/rapid-router/issues
[add-issue]: https://github.com/ocadotechnology/rapid-router/issues/new/choose
