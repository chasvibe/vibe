#!/usr/bin/bash

git add .

echo 'Enter commit message: '
read commitMessage

git commit -m "$commitMessage"

echo 'Enter the name of the branch:'
read branch

git push -u origin $branch

read
