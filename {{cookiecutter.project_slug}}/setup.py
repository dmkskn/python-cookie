from pathlib import Path

from setuptools import setup


def get_long_description() -> str:
    with open(Path(__file__).parent / "README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    author="{{cookiecutter.author_full_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="https://github.com/{{cookiecutter.author_github_username}}/{{cookiecutter.project_slug}}",
    description="{{cookiecutter.package_description}}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="{{cookiecutter.license}}",
    python_requires=">=3.7",
    packages=["{{cookiecutter.package_slug}}"],
    package_data={"{{cookiecutter.package_slug}}": ["py.typed"]},
    keywords=[],  # TODO
)

