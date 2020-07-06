import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyInstagram", # Replace with your own username
    version="0.0.1",
    author="Gokula Krishna",
    author_email="trgokul99@gmail.com",
    description="A small Instagram bot package that uses some basic functions. Download and have fun",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Krish-ds/Instagram_Bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     python_requires='>=3.6',
)