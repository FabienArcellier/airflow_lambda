## Motivation

I need to invoke AWS lambda worker managed by airflow.

## Synopsis

* the operator LambdaOperator comes from https://github.com/yashap/airflow

## The latest version

You can find the latest version to ...

```bash
git clone ...
```

## Usage

You can run the application with the following command

```python

```

## Contributing

### Install development environment

Use make to instanciate a python virtual environment in ./venv3 and install the
python dependencies.

```bash
make venv3
make install_requirements_dev
```

### Initiate or update the library requirements

If you want to initiate or update all the package and freeze a new requirements.txt, use
this procedure

```bash
make update_requirements
```

### Activate the python environment

When you setup the requirements, a `venv3` directory on python 3 is created.
To activate the venv, you have to execute /

```bash
source venv3/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute pylint to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

A short snippet describing the license (MIT, Apache, etc.)
