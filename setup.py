from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="dfgraph",
    install_requires=[
        "sqlalchemy>=1.4.10",
    ],
    extras_require={
    },
)