def test_project_and_package_names(cookies):
    result = cookies.bake({"package_name": "Hello World"})
    assert result.project.basename == "hello-world"
    assert "hello_world" in [f.basename for f in result.project.listdir()]
