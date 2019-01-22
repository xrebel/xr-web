# XR-Web

This project will hopefully soon be used to generate
https://extinctionrebellion.de

Issues and pull requests are very welcome. If something is hart to understand or
should be explained in this readme, please also create an Issue.

The same goes for content: If don't feel comfortable making the relevant changes
yourself, create an Issue.

## Getting Started
[Getting Started]: #getting-started

1. Install [Git] and
2. Clone the repository. You may want to [fork] it before.  
   `git clone https://github.com/xrebel/xr-web.git`
3. Enter the repository.  
   `cd xr-web`
4. Checkout the plugins repository.  
   `git submodule update --init`
5. Install [pipenv].  
   `pip3 install --user pipenv`
6. Install [pyenv] as described on their website.
   This allows us to specify the Python version we want to use.
7. Install the development environment.  
   `pipenv install --dev`

## Add Your Changes (Make a Pull Request)

For changes which can be done through the GitHub website:

1. Navigate to the file you would like to change.
2. Log In.
3. Use the Pencil-Icon to edit the file.
4. Commit the changes using a commit message in present tense describing what
   you change and why.
5. Create a Pull Request.

For changes of copies on your computer using [Git]:

1. If you have not done so, follow [Getting Started].
2. Please, [fork] this repository.
3. On your local repository, you set the `upstream` remote
   to pull changes from the original repository.  
   `git remote add upstream https://github.com/xrebel/xr-web.git`
4. Set your remote `origin`
   - ssh: `git remote set-url origin git@github.com:USERNAME/xr-web.git`
     (replate `USERNAME`)
   - https: `git remote set-url origin https://github.com/xrebel/xr-web.git`
5. Check out a new branch, e.g. for a certain issue.  
   `git checkout -b issue-1`
6. Commit the changes using a commit message in present tense describing what
   you change and why.  
   `git add ...`  
   `git commit -m"..."`
7. Update your changes to the latest version on the `master` branch.  
   `git pull --rebase upstream master`
8. Push the changes.  
   `git push -u origin issue-1`  
   Git will show you a message with a link where you can create a pull request.

## Running the project
1. `pipenv run make devserver` (You need to have GNU make installed)
2. Open your browser at localhost:8000
3. Start changing things :) If you notice anything weird, don't hesitate to
   create an issue

[Git]: https://git-scm.com/
[fork]: https://github.com/xrebel/xr-web/fork
[pipenv]: https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv
[pyenv]: https://github.com/pyenv/pyenv#installation

