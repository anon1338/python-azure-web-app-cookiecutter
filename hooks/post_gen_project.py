python_version = "{{ cookiecutter.python_version }}"
cpu_arch = "{{ cookiecutter.cpu_arch }}"

site_extensions_base_url = "{}"
extension_name = "Python{}{}".format(python_version.replace(".", ""), cpu_arch)

print()
print("**NOTE**: Don't forget to install the proper Python site extension: "
      "http://www.siteextensions.net/packages/{}".format(extension_name))