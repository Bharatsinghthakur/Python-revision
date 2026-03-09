# PIP

"""
commands for pip

pip help install

pip help

pip search packagename
pip search pympler

pip list
-- for all the list of the packages

pip uninstall pympler

pip list -o
this command will compare your package version with
current package version

to install a package

pip install -u setuptools

#####
Now you want to provide the list of package
to your friend

pip freeze
pip freeze > requirement.txt

once you provide this they can install it like

pip install -r r_test.txt

-r is requirement


"""

import requests

r = requests.get("http://coreyms.com")
print(r.status_code)
