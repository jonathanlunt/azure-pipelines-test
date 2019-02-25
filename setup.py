from setuptools import setup

setup(
    name="example",
    version="0.0.1",
    packages=["example"],
    extras_require={
        'tests': [
            'pytest',
        ],
    },
)
