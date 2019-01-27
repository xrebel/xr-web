# XR-Web

This project will hopefully soon be used to generate
https://extinctionrebellion.de

Issues and pull requests are very welcome. If something is hard to understand or
should be explained in this readme, please also create an Issue.

The same goes for content: If don't feel comfortable making the relevant changes
yourself, create an Issue.

## Getting started
1. Checkout the plugins repository: `git submodule update --init`
2. Install pipenv
   https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv
   For Mac OSX Users, it is recommended to use a package manager (Homebrew seems to be most convenient): `brew install pipenv`
   More info about Homebrew: https://brew.sh
3. `pipenv install --dev`

## Running the project
1. `pipenv run make devserver` (You need to have GNU make installed)
2. Open your browser at localhost:8000
3. Start changing things :) If you notice anything weird, don't hesitate to
   create an issue
