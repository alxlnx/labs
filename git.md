## Setting up git & github: 
- Add info about you to git: ``git config --global user.name "Saul Goodman"; git config --global user.email "dead@dead.zombie"``
- Create ssh keys: ``shh-keygen [-t ed25519] file_name``
- Add generated public key (.pub extension) to your github account (see your profile settings)
- Add private key (you need that for deciphering messages sent to you) to your machine: ``ssh-add file_name``
- Clone desired repo: ``git clone "SSH_link_from_github"``
## How to merge branches
- Sync everything in your local repo with the server: ``git fetch``
- Switch to the merging branch to make sure you have a local copy of it: ``git checkout merge_from``
- Switch to the merged branch (main in the example command): ``git checkout main``
- Merge the branches: ``git merge merge_from``
- Push changes: ``git push``
## How to make a branch and use it:
- Create a branch: ``git branch bRaNcH``
- Switch to a branch: ``git checkout bRaNcH``
- Add the branch to your repo: ``git push --set-upstream origin i_have_no_friends_to_do_this``
