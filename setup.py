
import setuptools
import re
import os

setuptools.setup(
	name="extension_ace_step",
    packages=setuptools.find_namespace_packages(),
    version="0.4.0",
	author="rsxdalv",
	description="AceStep: A Step Towards Music - Vocal Generation.",
	url="https://github.com/rsxdalv/extension_ace_step",
    project_urls={},
    scripts=[],
    install_requires=[
        "gradio",
        "ace-step @ git+https://github.com/rsxdalv/ACE-Step@loose-3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
