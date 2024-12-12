from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="code-promptify",
    version="0.7.0",
    packages=find_packages(),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "promptify=promptify.main:main",
        ],
    },
    author="Victor Dantas",
    author_email="vmehmeri@hotmail.com",
    description="A CLI utility for aggregating file contents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vmehmeri/code-promptify",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)