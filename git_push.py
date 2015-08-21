"""
script to test push capability of GitPython and using my personal token to gitautmatetest repo
"""

import string
import random
from git import Repo
import os

chars = "".join( [random.choice(string.letters[:26]) for i in xrange(64)] )

with open('foo.txt', 'w') as txt:
    txt.write(chars)

repo = Repo(os.path.abspath(os.path.dirname(__file__)))

assert not repo.bare
print repo.untracked_files

print repo.heads[0].commit.message

for x in repo.iter_commits():
    print x
#    print x.id

repo.git.add('foo.txt')
repo.index.commit('Random string generated in foo.txt')
repo.remotes.origin.push(repo.head)

#g.commit('Added random string')
#g.push()
