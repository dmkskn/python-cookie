def test_project_contains_package_folder(cookies):
    result = cookies.bake({"package_name": "Hello World"})
    assert "hello_world" in [f.basename for f in result.project.listdir()]
    assert result.project.join("hello_world").isdir()


def test_project_and_package_names(cookies):
    result = cookies.bake({"package_name": "Hello World"})
    assert result.project.basename == "hello-world"
    assert "hello_world" in [f.basename for f in result.project.listdir()]


def test_project_contains_editorconfig(cookies):
    result = cookies.bake()
    assert ".editorconfig" in [f.basename for f in result.project.listdir()]


def test_project_contains_gitignore(cookies):
    result = cookies.bake()
    assert ".gitignore" in [f.basename for f in result.project.listdir()]


def test_project_contains_tests_folder(cookies):
    result = cookies.bake()
    assert "tests" in [f.basename for f in result.project.listdir()]


def test_project_contains_readme(cookies):
    result = cookies.bake()
    assert "README.md" in [f.basename for f in result.project.listdir()]


def test_package_contains_py_typed_marker(cookies):
    result = cookies.bake({"package_name": "foo"})
    assert "py.typed" in [f.basename for f in result.project.join("foo").listdir()]


def test_package_contains_setup(cookies):
    result = cookies.bake()
    assert "setup.py" in [f.basename for f in result.project.listdir()]


def test_package_contains_requirements_dev(cookies):
    result = cookies.bake()
    assert "requirements_dev.txt" in [f.basename for f in result.project.listdir()]


def test_package_contains_coveragerc(cookies):
    result = cookies.bake()
    assert ".coveragerc" in [f.basename for f in result.project.listdir()]


def test_package_contains_makefile(cookies):
    result = cookies.bake()
    assert "Makefile" in [f.basename for f in result.project.listdir()]


def test_package_contains_pre_commit_config_yaml(cookies):
    result = cookies.bake()
    assert ".pre-commit-config.yaml" in [f.basename for f in result.project.listdir()]
