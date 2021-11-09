#!/bin/bash

echo "File to add: "
read ADD
git add $ADD

echo "Commit message: "
read MESSAGE
git commit -m "$MESSAGE"

echo "Branch: "
read BRANCH
git push -u origin $BRANCH
