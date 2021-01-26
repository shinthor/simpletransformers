from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simpletransformers",
    version="0.51.15",
    author="Thilina Rajapakse",
    author_email="chaturangarajapakshe@gmail.com",
    description="An easy-to-use wrapper library for the Transformers library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThilinaRajapakse/simpletransformers/",
    packages=find_packages(),
    scripts=["bin/simple-viewer"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "requests",
        "tqdm>=4.47.0",
        "regex",
        "transformers>=4.0.0",
        "scipy",
        "scikit-learn",
        "seqeval",
        "tensorboardx",
        "pandas",
        "tokenizers",
        "wandb",
        "streamlit",
        "sentencepiece",
        "torch>=1.6.0"
    ],
)
