from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name             = 'query-mapper',
    version          = '0.9',
    description      = 'stop writing sql query in your code .. use this pakcage',
    author           = 'bgm5768',
    author_email     = 'bgm5768@gmail.com',
    url              = 'https://github.com/gaco456/query_mapper',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages         = find_packages(),
    keywords         = ['mapper', 'query' , 'sql' , 'mysql' , 'collect'],
    python_requires  = '>=3',
    classifiers      = [
        'Programming Language :: Python :: 3.7'
    ]
)