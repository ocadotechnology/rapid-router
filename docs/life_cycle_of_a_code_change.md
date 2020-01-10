# Life cycle of a code change
Once you're confident with the changes implemented in your local branch, you should push them and open a GitHub pull request that can be reviewed and approved. **Note that** this should be a `semantic` pull request (see [semantic release notes](https://github.com/semantic-release/semantic-release)).

More details about pull request submissions can be found [here](../CONTRIBUTING.md).

## Development to Staging
The branch is ready to be merged into the `master` branch when all changes are reviewed and there are no conflicts or blocking errors. Semaphore CI is notified and deploys it to our staging server, where the code changes will be tested further. See more details in our deploy app engine [documentation](https://github.com/ocadotechnology/codeforlife-deploy-appengine/blob/master/docs/life-cycle-of-a-code-change.md).

## Staging to Production
Deployment to production is manually triggered on Semaphore CI.
