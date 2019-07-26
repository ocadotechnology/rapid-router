# Rapid Router (codename: ocargo)

[![Build Status](https://travis-ci.org/ocadotechnology/rapid-router.svg?branch=master)](https://travis-ci.org/ocadotechnology/rapid-router)
[![Coverage Status](https://coveralls.io/repos/ocadotechnology/rapid-router/badge.svg?branch=master&service=github)](https://coveralls.io/github/ocadotechnology/rapid-router?branch=master)
[![Code Climate](https://codeclimate.com/github/ocadotechnology/rapid-router/badges/gpa.svg)](https://codeclimate.com/github/ocadotechnology/rapid-router)
[![Crowdin](https://d322cqt584bo4o.cloudfront.net/code-for-life/localized.svg)](https://crowdin.com/project/code-for-life)

## A  [Code for Life](https://www.codeforlife.education/) project
* Rapid Router is a [Code for Life](https://www.codeforlife.education/) project, aimed at teaching primary-school children programming concepts through a vehicle routing
  game. 
  Ocado Technology's [Code for Life initiative](https://www.codeforlife.education/) has been developed to inspire the next generation of computer scientists and to help teachers deliver the computing curriculum.
* This repository hosts the source code of the **Rapid Router game**.
* The other repos for Code For Life:
    * the main portal (as well as registration, dashboards, materials...), [Code For Life Portal](https://github.com/ocadotechnology/codeforlife-portal)
    * the new game for teenagers, [currently at a very early stage](https://github.com/ocadotechnology/aimmo)
    * the [deployment code for Google App Engine](https://github.com/ocadotechnology/codeforlife-deploy-appengine)

## To use the app
Go to the official [Code For Life website][c4l].

## To run localy with Docker

* Install Docker https://www.docker.com/

* Run `docker-compose up`

* Navigate to http://localhost:8000

## To run the app locally

* Clone the repo: `https://github.com/ocadotechnology/rapid-router.git`. Fork it first if you want to contribute, and work on a separate branch for your work.

### Ubuntu / Linux Mint
* Install prerequisites
    * `sudo apt-get install git`
    * `sudo apt-get install python-dev python-pip`
    * `sudo pip install virtualenvwrapper`
    * `sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev gettext`
    * `sudo apt-get install ruby2.0`
    * `sudo gem install sass -v 3.3.4` - tested to work with Ruby >1.9 and <2.3.6

* Make and activate a virtualenv
    * e.g. the first time, `mkvirtualenv -a path/to/rapid-router rapid-router`
    * and thereafter `workon rapid-router`
    * **NOTE:** If you have trouble running these commands (e.g. `Command not found: workon`), refer to [this article][virtualenv], the top answer should help you resolve them. You may need to run:

          export WORKON_HOME=~/Envs
          source /usr/local/bin/virtualenvwrapper.sh

### Mac OS
* Install prerequisites
    * `brew install rbenv`
    * `brew install pyenv`
    * `brew install pyenv-virtualenv`

* Update `.zshrc` with the following
    * `eval "$(rbenv init -)"`
    * `eval "$(pyenv init -)"`
    * `eval "$(pyenv virtualenv-init -)"`

* Close and open terminal

* Run the following commands
    * `rbenv install 2.2.9`
    * `brew install zlib`
    * `brew install readline xz`
    * `xcode-select --install`
    * `pyenv install 2.7.14`

* Finally, go to the project root and run the following commands
  * `pyenv local 2.7.14`
  * `rbenv local 2.2.9`   

#### Mac OS Mojave

##### Pillow
On MacOS Mojave there is an error when installing `Pillow`.
To fix this issue you need to run the following command:
```
sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
``` 
cf: https://github.com/python-pillow/Pillow/issues/3438#issuecomment-435169249

##### Pyexpat
If you have the following error: `ImportError: No module named pyexpat` when installing `pyenv 2.7.14`, then you can try using the following command:
```
SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk MACOSX_DEPLOYMENT_TARGET=10.14 pyenv install 2.7.14
```
cf: https://github.com/pyenv/pyenv/issues/1066#issuecomment-504710495

##### Missing sass
If you have the following error: `pipeline.exceptions.CompilerError: env: sass: No such file or directory`, then you need to install sass:
```
gem install sass
```

### Running the Portal
* `./run` in your rapid-router directory - This will:
    * install all of the dependencies using pip
    * sync the database
    * collect the static files
    * run the server
* Once you see `Quit the server with CONTROL-C`, you can open the portal in your browser at `localhost:8000`.

* If you have problems seeing the portal on machines with different locale (e.g. Polish), check the terminal for errors mentioning `ValueError: unknown locale: UTF-8`. If you see them, you need to have environment variables `LANG` and `LC_ALL` both set to `en_US.UTF-8`.
    * Either export them in your `.bashrc` or `.bash_profile`
    * or restart the portal with command `LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 ./run`.

## Localisation
* For localisation admins: 
    * `./run --with-translation-tools` in your rapid-router dir to include the translation/localisation libraries
    * You will need your crowdin api key locally in the `CROWDIN_API_KEY` environment variable, e.g. `export CROWDIN_API_KEY=<key>`. This can be obtained from [the settings page](https://crowdin.com/project/code-for-life/settings#integration)
* Set your `django_language` cookie to `lol-us` to enable in-context localisation

## To contribute
__Guidelines__ Please read the [contributing guidelines](CONTRIBUTING.md) first, thank you.
__Found a problem? Please check whether it has already been reported in our [issue tracker][issues] first!__ If not,
[add it][add-issue]. Please make sure that you give us a suitable level of detail about the symptoms and how to
reproduce it. Please label it as a "bug".<br>
One word of caution: please do not add any issues related to security. Evil hackers are everywhere nowadays... If you do find a security issue, let us know using our [contact form][c4l-contact-form].

__Want to suggest a feature? Please check whether it has already been added to our [issue tracker][issues] first!__ if
not, [add it][add-issue]. Please make sure that you give us a suitable level of detail about the feature. Please label
it as a "suggestion". Please note that we may not act upon all suggestions, if they are not in line with the direction
we want to take the project, or if we don't have the development resources to get it done.

__Want to help develop?__ You can contact us using this [contact form][c4l-contact-form] and we'll get in touch as soon as possible. To know what's going on, check out the [issue tracker][issues]. The
[issues with the 'ready for pickup' label][ready-for-pickup] are tasks we think are ready to be picked up. Once you have
chosen an issue, make sure you assign it to yourself so others don't also pick it up. Develop it on your fork of the
project. Please ensure all files have the license at the top (see another source file for an example). Once you are
happy that it works, and have written tests for it, submit a pull request. We'll then look to review the changes. If it
looks good, we'll merge it. If we find issues with it, we'll let you know and hopefully we can work with you to improve
it and get it re-submitted. If it is a change that we just don't want, we'll reject it.

[c4l]: https://www.codeforlife.education/
[virtualenv]: https://stackoverflow.com/a/13855464
[c4l-portal]: http://github.com/ocadotechnology/codeforlife-portal/
[c4l-contact-form]: https://www.codeforlife.education/contact/
[issues]: https://github.com/ocadotechnology/rapid-router/issues
[add-issue]: https://github.com/ocadotechnology/rapid-router/issues/new
[ready-for-pickup]: https://github.com/ocadotechnology/rapid-router/labels/ready%20for%20pickup
