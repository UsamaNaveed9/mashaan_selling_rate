from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mashaan_selling_rate/__init__.py
from mashaan_selling_rate import __version__ as version

setup(
	name="mashaan_selling_rate",
	version=version,
	description="Mashaan Item Selling price calculation on the basis of margin",
	author="smb",
	author_email="usamanaveed9263@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
