def test_readme_starts_with_package_name_headline(cookies):
    result = cookies.bake({"package_name": "Hello World"})
    readme = result.project.join("README.md").read()
    assert readme.startswith("# Hello World")


def test_readme_contain_package_description(cookies):
    test_description = "Test description"
    result = cookies.bake({"package_description": test_description})
    readme = result.project.join("README.md").read()
    assert test_description in readme
