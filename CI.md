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

- Avoid running Docker inside Docker (dind)

> Use sockets to communicate with the host docker via the `docker.sock` file.

## References

1. [Building minimal docker containers](
   https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/)
