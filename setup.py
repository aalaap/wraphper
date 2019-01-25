import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wraphper",
    version="0.0.1",
    author="Aalaap Ghag",
    description="Python wrappers for PHP functions, when you just can't shake it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aalaap/wraphper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)