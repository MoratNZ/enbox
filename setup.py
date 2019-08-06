import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enbox",
    version="0.0.1",
    author="David Maclagan",
    author_email="dmaclagan@vital.co.nz",
    description="Tooling for linting NetBox contents, with an eye on easing import of brown-fields networks into NetBox.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MoratNZ/enbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)