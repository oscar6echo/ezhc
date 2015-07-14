__author__ = 'oborderi'

from aconda.mod_push import push_folder
from cdotools.gitutils import before_push

# Don't forget to commit all your local modifications
# Update the _package.json with the new version
# Commit this modification
# `git tag vX.Y.Z` where X.Y.Z is the same version as your _package.json version
# You can call this script `python push_to_repo.py` to push the new version to the conda mirror
# Don't forget to type `git push --tags origin master` if you want to push the tags

folder = "ezhc"
if before_push(folder):
    print("Pushing {}...".format(folder))
    push_folder(folder)
