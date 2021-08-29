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

- Optimizing actions and making them as minimal as possible

> Doing so lessens the possibility to hit the 2000 minutes/month limit.

- Using pre-commit hooks

> Pre-commit are able to perform a number of useful actions on the code before it gets actually committed.

## Jenkins

- Securing Jenkins with access control

> This makes third parties unable to freely execute arbitrary code.

- Trying to create clean builds

> The most reliable builds are ones created directly from source code.

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
2. [Are You Following These Jenkins Best Practices?](
   https://www.lambdatest.com/blog/jenkins-best-practices/
   )
3. [Jenkins Best Practices](
   https://wiki.jenkins.io/display/jenkins/jenkins+best+practices
   )
