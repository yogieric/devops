from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="devopsutil",
    version="0.0.1",
    author="Eric Brown",
    author_email="yogieric@gmail.com",
    description="A collection of devops utilities",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/yogieric/devops/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
