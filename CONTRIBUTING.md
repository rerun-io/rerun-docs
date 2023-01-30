# Contributing to Rerun
This is written for anyone who wants to contribute to the Rerun Docs repository.

Rerun is an open core company, and this repository is dual-licensed under MIT and APACHE. However, this repository is NOT YET open source, but IT WILL BE. Therefore we ask you to avoid making public clones of this repository, but in other respects treat it as any other open source GitHub project.

## What to contribute
The repository stores the high-level documentation for the main [rerun repository](https://github.com/rerun-io/rerun)

These docs should cover:
 - Getting started instructions
 - General usage information
 - How-to guides
 - Concepts
 - References

Specific API-related documentation should continue to live in the main repository.

* **Bug reports and issues**: Open them at <https://github.com/rerun-io/rerun/issues>.

## Pull Requests
We use [Trunk Based Development](https://trunkbaseddevelopment.com/), which means we encourage small, short-lived branches. Open draft PR:s to get some early feedback on your work.

All PR:s are merged with [`Squash and Merge`](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#squash-and-merge-your-commits), meaning they all get squashed to just one commit on the `main` branch. This means you don't need to keep a clean commit history on your feature branches. In fact, it is preferable to add new commits to a branch rather than rebasing or squashing. For one, it makes it easier to track progress on a branch, but rebasing and force-pushing also discourages collaboration on a branch.
