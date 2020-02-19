import datetime


def test_choose_right_license(cookies):
    result = cookies.bake(extra_context={"license": "Unlicense"})
    license_file = result.project.join("LICENSE").read()
    assert "<https://unlicense.org>" in license_file
    assert "MIT License" not in license_file

    result = cookies.bake(extra_context={"license": "MIT license"})
    license_file = result.project.join("LICENSE").read()
    assert "MIT License" in license_file
    assert "<https://unlicense.org>" not in license_file


def test_year_and_name_in_mit_license(cookies):
    result = cookies.bake(extra_context={"license": "MIT license"})
    license_file = result.project.join("LICENSE").read()
    copyright_line = f"Copyright (c) {datetime.datetime.now().year}, John Doe"
    assert copyright_line in license_file
