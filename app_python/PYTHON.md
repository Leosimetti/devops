## Some available prod-ready frameworks:

1. FastAPI

> A framework suitable for creating fast async APIs quickly.

2. Django

> Very powerful framework that can be used to create fullstack apps.

4. Pyramid

> A universal, flexible and minimalistic framework used as an alternative to other popular frameworks.

4. Flask

> A microframework with support for Jinja 2. Used by many companies for simple microservices.

## Framework choice justification (Flask)

This framework was chosen because it is very lightweight and simple. I am also a little familiar with it. So, it turned
out to be the best choice for such a simple one-page web app.

## Python Best practices

- Using venv and requirements.txt

> It allows anyone to easily install the project's dependencies
> without cluttering the global python package environment.
> The venv folder was used during development and got added to `.gitignore` afterwards

- Using a TOML file for configurations

> Toml is a file format for configurations.
> In this project it was used to store pytest arguments.

- Following naming conventions

> snake_case for methods; PascalCase for classes; ALL_CAPS for constants

## Flask Best practices

- Installing a proper server for Flask

> The provided development server is not designed to used for
> production. As a result, it is not very efficient, stable, and secure,

- Using ENV variables for additional configurability.

> Environmental variables are a good way to pass arguments.
> In this project application IP and PORT are passed this way.

## Unit Testing Best practices

- Using fixtures in tests

> Fixtures allow for the code to be reused. In this case the `client`
> fixture is used to make requests to the application.

- Mocking values and functions

> Mocks aee able to "fake" functionality to make tests independent.
> In this case `freezegun` is used to mock time in order to avoid waiting.

- Parametrizing the tests

> Parametrization enables a small piece of code to test many behaviours.

- Scoping fixtures

> It is possible to set a scope to a fixture, making it reset upon exiting this scope.
> This is especially applicable to `yield` fixtures that are dependent on some resource's state.

- Avoiding fixture modification at runtime

> Fixture data modification is a bad idea, as doing so can cause unexpected behaviour
> in case multiple functions are using the same fixture.

- Running tests before actually committing the code

> This action can be automated using a pre-commit hook that automatically runs tests before the code is committed.
> (as it is done in this project)

- Making test case names as descriptive and long as needed

> Although it is a convention to keep function names short, doing so is not very applicable to tests,
> as test functions names are not called explicitly and are only shown in the report.

- Reasonably optimizing tests to make them run fast
> Slow running tests are a hindrance to the development speed, as slow-running tests are less likely to be run.
> Thus, it is important to get all tests to run fast. However, tested functionality should not be compromised in favor of speed.
