"""
Setup script for packaging Git Laugh Track as a Python CLI tool.
Allows installation via `pip install .`
"""

from setuptools import setup, find_packages

setup(
    name="git-laugh-track",  # Package name on PyPI
    version="0.1.1",
    description="Play sounds on git commit and push events 🎶",
    author="Gyarsilal Solanki",
    author_email="gyarsilalsolanki011@gmail.com",  # <-- replace with your email
    url="https://github.com/eleven-dev-cafe/git-laugh-track",
    packages=find_packages(include=["git_laugh", "git_laugh.*"]),
    install_requires=[
        "playsound==1.2.2",   # To play audio files
        "click>=8.0"          # For CLI commands
    ],
    entry_points={
        "console_scripts": [
            # After installation, `git-laugh` will call git_laugh.cli:cli
            "git-laugh=git_laugh.cli:cli",
        ],
    },
    python_requires=">=3.6",
    license="BSD-3-Clause",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
