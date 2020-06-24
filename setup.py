import setuptools
with open('requirements.txt') as f:
    reqs = f.readlines()

setuptools.setup(
    name="stlabutils",
    package_dir={'stlabutils': ''},
    packages= ['stlabutils'],
    install_requires = reqs
)