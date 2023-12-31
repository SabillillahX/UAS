from setuptools import setup
from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'Menghitung Golden Ratio'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

setup(
    name="gold33423322",
    version= VERSION,
    author="SabillillahX",
    author_email="<sabillillahxtkj@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/SabillillahX/anjay',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['math', 'goldratio'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)
