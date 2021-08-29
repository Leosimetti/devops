# CI Best Practices

## GitHub actions

- Tagging commits

> Tags allow for actions to be invoked only when they are specifically requested for invocation.

- Using GitHub Secrets

> Hiding sensitive information in secrets is a better approach than leaving it hardcoded.

- Using build cache

> Doing so allows for speed-ups in the CI process.

- Using matrices in `strategy` section

> This allows for the app to be tested in several environments with a minimal amount of code.

- Using pre-commit hooks

> Pre-commit are able to perform a number of useful actions on the code before it gets actually committed.

## Jenkins

- Avoid running Docker inside Docker (if Jenkins is running in a container)

> When a need to run pipelines arises - use sockets to communicate with the host docker via the `docker.sock` file.

- Using Jenkins credentials to store sensitive information

> Hiding sensitive information in credentials is a better approach than leaving it hardcoded.

- Properly handling string interpolation of sensitive information

> "${SECRET}" is visible in the logs, while '$SECRET' is hidden

- Specifying a branch for stages

> Using `when{ branch 'x'}` allows for stages to trigger only on specific branches

- Using `dir()` in steps

> This command allows for better indication of the current working folder than `cd`

## References

1. [Building minimal docker containers](
   https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/)
