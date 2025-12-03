# TODOs

- Marketing:
  - [reddit.com/r/Python/](https://www.reddit.com/r/Python/)
- Analytics:
  - [ ] Google Analytics
  - [ ] Github Insights
  - [ ] PyPI Insights
  - [ ] [Susie](https://philippedeb.github.io/susie/#/)
- Integrate Github Release Drafter
- Github Social Preview:
  - Search: Github Social Preview Generator
- Github Templates:
  - [devspace/awesome-github-templates: :octocat: Curated list of GitHub Issues and Pull Requests templates](https://github.com/devspace/awesome-github-templates)
- README Templates:
  - Search for README Templates and Awesome READMEs
  - [othneildrew/Best-README-Template: An awesome README template to jumpstart your projects!](https://github.com/othneildrew/Best-README-Template)
- CI/CD Pipelines:
  - Tools:
    - [Codium-ai/pr-agent: 🚀CodiumAI PR-Agent: An AI-Powered 🤖 Tool for Automated Pull Request Analysis, Feedback, Suggestions and More! 💻🔍](https://github.com/Codium-ai/pr-agent)
  - [ ] Publish:
    - [ ] PyPI
    - [ ] Scoop
    - [ ] Windows Store
    - [ ] Homebrew
    - [ ] Docker Hub
    - [ ] GitHub Packages
  - [ ] `.github`
    - [ ] `workflows`
      - [ ] `ci.yml`
      - [ ] `cd.yml`
      - [ ] `check-pr-title.yml`
      - [ ] `gh-pages.yml`
      - [ ] `release-drafter.yml`
    - [ ] `ISSUE_TEMPLATE`
      - [ ] `bug_report.md`
      - [ ] `feature-request.md`
    - [ ] `PULL_REQUEST`
      - [ ] `pull_request_template.md`
    - [ ] `dependabot.yml`
    - [ ] `FUNDING.yml`
  - [ ] Documentation:
    - [ ] `mkdocs.yml`
  - [ ] Application:
    - [ ] As a package.
    - [ ] As a CLI Tool.
    - [ ] As a GUI Tool.
    - [ ] As a Web Server.
  - [ ] Project Configuration and Metadata:
    - [ ] Optional Dependencies.
    - [ ] Authors and Maintainers.
    - [ ] Proper Licensing.
    - [ ] Trove Classifiers.
    - [ ] Keywrods.
  - [ ] Tests:
    - [ ] Unit Tests.
    - [ ] Integration Tests.
    - [ ] E2E Tests.
    - [ ] Low-Level API Tests.
    - [ ] High-Level API Tests.
    - [ ] User Scenarios Tests.
  - [ ] `CODE_OF_CONDUCT.md`
  - [ ] `CONTRIBUTING.md`.
  - [ ] `README.md`.
  - [ ] `CHANGELOG.md`.
  - [ ] `LICENSE`
  - [ ] Release Notes and Automating it.

## Tutorial

- Copier:
  - [12rambau/pypackage: The skeleton of a python package](https://github.com/12rambau/pypackage), bunu forklayıp geliştirmek daha mantıklı görünüyor.
- Cookiecutter:
  - [audreyfeldroy/cookiecutter-pypackage: Cookiecutter template for a Python package.](https://github.com/audreyfeldroy/cookiecutter-pypackage)
  - [tomchristie/cookiecutter-pypackage: A cookiecutter template for creating PyPI packages.](https://github.com/tomchristie/cookiecutter-pypackage)
  - [daleal/cookiecutter-pypackage: A cookiecutter to start a Python package with flawless practices and a magical workflow 🧙🏼‍♂️](https://github.com/daleal/cookiecutter-pypackage)
  - [Wh1isper/pypi-hatch-pytest-cookiecutter](https://github.com/Wh1isper/pypi-hatch-pytest-cookiecutter)
  - [frankie567/cookiecutter-hipster-pypackage: Cookiecutter template for a cutting-edge Python package: Hatch, ruff, mypy, GitHub Actions and more!](https://github.com/frankie567/cookiecutter-hipster-pypackage)
  - [FlorianWilhelm/the-hatchlor: 🌹 Cookiecutter template featuring the modern and extensible Python project manager hatch](https://github.com/FlorianWilhelm/the-hatchlor)
- Packages:
  - [AlexIoannides/registerit: Have an idea for a Python package? Register the name on PyPI 💡](https://github.com/AlexIoannides/registerit)
  - [shobrook/PyReserve: Generate a project template and reserve a name on PyPi with one command](https://github.com/shobrook/PyReserve)
- Alternatives:
  - [BrianPugh/python-template: Python project and library template for clean, reliable, open-source projects.](https://github.com/BrianPugh/python-template)
  - [Kludex/python-template: A template for Python packages that makes you go from 🥵 to 😎!](https://github.com/Kludex/python-template)
  - [jacebrowning/template-python: My template for new Python libraries.](https://github.com/jacebrowning/template-python)
  - [raiyanyahya/pypi-register: A quick way to book and reserve your package name on pypi.](https://github.com/raiyanyahya/pypi-register): Single-file Python script.
  - [AlyShmahell/stubwheel: a script that reserves a project name on pypi](https://github.com/AlyShmahell/stubwheel)
- Readings:
  - [python - Register an internal package on Pypi - Stack Overflow](https://stackoverflow.com/questions/47676721/register-an-internal-package-on-pypi)
  - [Bootstrap a Scientific Python Library — Scientific Python Cookiecutter 0.1 documentation](https://nsls-ii.github.io/scientific-python-cookiecutter/)
  - [using python-poetry to publish to test.pypi.org - Stack Overflow](https://stackoverflow.com/questions/68882603/using-python-poetry-to-publish-to-test-pypi-org)
  - [Upload to TestPyPI silently failed. · Issue #742 · python-poetry/poetry](https://github.com/python-poetry/poetry/issues/742)
  - [Documentation / configuration around publishing packages is very unclear · Issue #6659 · python-poetry/poetry](https://github.com/python-poetry/poetry/issues/6659)
  - [Software Pragmatism - How To Use Poetry to Publish a Python Package on PyPI](https://www.softwarepragmatism.com/publish-python-to-pypi-with-poetry)
  - [Making Python Packages Part 1: How to Publish A Python Package to PyPI | by Skylar Kerzner | Medium](https://medium.com/@skylar.kerzner/publish-your-first-python-package-to-pypi-8d08d6399c2f)
  - [Making Python Packages Part 2: How to Publish & Test Your Package on PyPI with Poetry | by Skylar Kerzner | Towards Data Science](https://towardsdatascience.com/packages-part-2-how-to-publish-test-your-package-on-pypi-with-poetry-9fc7295df1a5)

## Preparations

Create a `README.md` file.

```markdown
<h1 align="center">
    <strong>my-project</strong>
</h1>
<p align="center">
    <a href="https://github.com/my-username/my-project" target="_blank">
        <img src="https://img.shields.io/github/last-commit/my-username/my-project" alt="Latest Commit">
    </a>
        <img src="https://img.shields.io/github/workflow/status/my-username/my-project/Test">
        <img src="https://img.shields.io/codecov/c/github/my-username/my-project">
    <br />
    <a href="https://pypi.org/project/my-project" target="_blank">
        <img src="https://img.shields.io/pypi/v/my-project" alt="Package version">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/my-project">
    <img src="https://img.shields.io/github/license/my-username/my-project">
</p>
```

## Hatch

Create a project

```bash
hatch new my-project
```

Change directory

```bash
cd my-project
```

...

## Poetry

Create a project

```bash
poetry new my-project
```

Change directory

```bash
cd my-project
```

Edit `pyproject.toml`

```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["Hasan Sezer Taşan <hasansezertasan@gmail.com>"]
maintainers = ["Hasan Sezer Taşan <hasansezertasan@gmail.com>"]
readme = "README.md"
license = "MIT"  # If you're using a different license, change this
keywords = ["template"]
classifiers = [
    "Development Status :: 1 - Planning",
    "License :: OSI Approved :: MIT License",  # If you're using a different license, change this
]

[tool.poetry.dependencies]
python = "^3"  # Specify your Python version here


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Publish to PyPI

```bash
poetry publish --build
```

## Setup Tools

- Create a `setup.py` file.

```python
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="my-project",
    version="0.1.0",
    description="",
    long_description=long_description,
    url="https://github.com/my-username/my-project.git",
    author="My Name",
    author_email="my-username@example.com",
    maintainer="My Name",
    maintainer_email="my-username@example.com",
    packages=[],  # Add your packages here
    keywords=["template"],
    license="MIT",  # If you're using a different license, change this
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",  # If you're using a different license, change this
    ],
)
```

Create a `setup.cfg` file.

```ini
[metadata]
license_files = LICENSE
```

Install

``` bash
pip install my-project
```

Build

```bash
python setup.py bdist_wheel upload
```

Publish to PyPI with twine

```bash
twine upload dist/*
```

Publish to TestPyPI with twine

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload --repository testpypi dist/*
```

Publish to PyPI with poetry

```bash
poetry publish
```

Publish to TestPyPI with poetry

```bash
poetry publish -r testpypi
```
