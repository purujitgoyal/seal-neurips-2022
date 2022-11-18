from setuptools import setup, find_packages
import os

PATH_ROOT = os.path.dirname(__file__)
with open("README.md", "r") as fh:
    long_description = fh.read()


def load_requirements(path_dir=PATH_ROOT, comment_char="#"):
    all_reqs = []
    for file in Path(path_dir).glob("*_requirements.txt"):
        with open(os.path.join(path_dir, "core_requirements.txt"), "r") as file:
            lines = [ln.strip() for ln in file.readlines()]
        reqs = []

        for ln in lines:
            # filer all comments

            if comment_char in ln:
                ln = ln[: ln.index(comment_char)]

            if ln:  # if requirement is not empty
                reqs.append(ln)
        all_reqs.extend(reqs)

    return all_reqs


install_requires = load_requirements()

setup(
    name="seal",
    version="0.0.1",
    author="Dhruvesh Patel",
    author_email="1793dnp@gmail.com",
    description="This is the official implementation for the paper [Structured Energy Network As a Loss](https://openreview.net/pdf?id=F0DowhX7_x).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Documentation": "",
        "Source Code": "",
    },
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "examples"]
    ),
    package_data={"structure_prediction_baselines": ["py.typed"]},
    install_requires=install_requires,
    keywords=["pytorch", "AI", "ML", "Machine Learning", "Deep Learning"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha" "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6",
)



