## How to merge branches
- Sync everything in your local repo with the server: ``git fetch``
- Switch to the merging branch to make sure you have a local copy of it: ``git checkout merge_from``
- Switch to the merged branch (main in the example command): ``git checkout main``
- Merge the branches: ``git merge merge_from``
- Push changes: ``git push``
