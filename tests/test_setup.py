def test_setup_name(cookies):
    result = cookies.bake({"package_name": "foo foo"})
    assert 'name="foo-foo"' in result.project.join("setup.py").read()


def test_setup_version(cookies):
    result = cookies.bake()
    assert 'version="0.1.0"' in result.project.join("setup.py").read()


def test_setup_author(cookies):
    result = cookies.bake({"author_full_name": "John Doe"})
    assert 'author="John Doe"' in result.project.join("setup.py").read()


def test_setup_author_email(cookies):
    result = cookies.bake({"author_email": "john@doe.com"})
    assert 'author_email="john@doe.com"' in result.project.join("setup.py").read()


def test_setup_url(cookies):
    result = cookies.bake({"author_github_username": "johndoe", "package_name": "foo"})
    setup_file = result.project.join("setup.py").read()
    assert 'url="https://github.com/johndoe/foo"' in setup_file


def test_setup_description(cookies):
    test_description = "Test Description"
    result = cookies.bake({"package_description": test_description})
    setup_file = result.project.join("setup.py").read()
    assert f'description="{test_description}"' in setup_file


def test_setup_license(cookies):
    result = cookies.bake({"license": "Unlicense"})
    setup_file = result.project.join("setup.py").read()
    assert 'license="Unlicense"' in setup_file

    result = cookies.bake({"license": "MIT license"})
    setup_file = result.project.join("setup.py").read()
    assert 'license="MIT license"' in setup_file


def test_setup_package(cookies):
    result = cookies.bake({"package_name": "foo foo"})
    setup_file = result.project.join("setup.py").read()
    assert 'packages=["foo_foo"]' in setup_file


def test_setup_package_data(cookies):
    result = cookies.bake({"package_name": "foo foo"})
    setup_file = result.project.join("setup.py").read()
    assert 'package_data={"foo_foo": ["py.typed"]}' in setup_file
