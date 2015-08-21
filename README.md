# gitautomatetest
Automate git and test things like personal tokens and updating the files in the repo from a script.

Test-1
======

* Create a personal token [help](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)

* Update the foo.txt file, commit on command line and push to origin.

* when asked for password, give the token instead and see if git can consume it and push the code to github.

[Solution](https://github.com/neotheicebird/gitautomatetest/wiki)

Test-2
======

* if test-1 is successful, try the same using a python script using GitPython

* write a dummy text to foo.txt

* commit and push origin using token

Test-3
======

* if test-2 is successful, write a python function to rollback to previous commit.

* upgrade: rollback(num=3) should rollback 3 commits.


