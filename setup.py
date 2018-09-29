import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Application name:
    name="macvpnhelper",

    # Version number (initial):
    version="0.0.3",

    # Application author details:
    author="Ryan Shea",
    author_email="rshea@aviatainc.com",

    # Packages
    #packages=["macvpnhelper"],
    packages=setuptools.find_packages(),
    
    # Include additional files into the package
    #include_package_data=True,

    url="https://test.pypi.org/project/examplepkgllungingllama/",

    license="LICENSE",

    description="App to restart mac vpn as specified.",

    long_description=long_description,
    long_description_content_type="text/markdown",


    scripts=['bin/macvpnhelper'],
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
     #Dependency packages (distributions)
    install_requires=[
        "keyring",
    ],
)
