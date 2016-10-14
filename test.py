#!/usr/bin/env python3

import git

repo = git.Repo()

tree = repo.commit().tree

tuple(tree)
