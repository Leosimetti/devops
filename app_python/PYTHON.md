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
This framework was chosen because it is very light-weight and simple. I am also a little familiar with it.
So, it turned out to be the best choice for such a simple one-page web app.

## Best practices
- Using venv and requirements.txt
> It allows anyone to easily install the project's dependencies
> without cluttering the global python package environment.
> The venv folder was used during development and got added to `.gitignore` afterwards
- Using a TOML file for configurations
> Toml is a file format for configurations.
> In this project it was used to store pytest arguments.
- Using ENV variables for additional configurability.
> Environmental variables are a good way to pass arguments. 
> In this project application IP and PORT are passed this way.  
- Making Tests folder a part of the application code
> Directory with tests was inlined into the application package 
> as it is directly related to it. (tests use the `create_app()` method) 
- Following naming conventions
> snake_case for methods; PascalCase for classes; ALL_CAPS for constants
- Using fixtures in tests
> Fixtures allow the code to be reused
- Installing a proper server for Flask 
> instead of a default development one.
