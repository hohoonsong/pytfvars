import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytfvars",
    version="1.0.2",
    author="hohoonsong",
    author_email="hohoonsong@gmail.com",
    description="convert python dictionary to tfvars(hcl lang) formatted string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hohoonsong/pytfvars",
    project_urls={
        "Bug Tracker": "https://github.com/hohoonsong/pytfvars/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
