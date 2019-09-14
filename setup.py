#  Drakkar-Software OctoBot-Backtesting
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
# from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import find_packages
from setuptools import setup, Extension

from octobot_backtesting import PROJECT_NAME, VERSION

PACKAGES = find_packages(exclude=["tests"])

packages_list = ["octobot_backtesting.backtesting",
                 "octobot_backtesting.collectors.data_collector",
                 "octobot_backtesting.collectors.exchanges.exchange_collector",
                 "octobot_backtesting.collectors.exchanges.exchange_live_collector",
                 "octobot_backtesting.collectors.exchanges.exchange_history_collector",
                 "octobot_backtesting.collectors.social.social_collector",
                 "octobot_backtesting.data.data_file_manager",
                 "octobot_backtesting.data.database",
                 "octobot_backtesting.importers.data_importer",
                 "octobot_backtesting.importers.exchanges.exchange_importer",
                 "octobot_backtesting.importers.social.social_importer"]

ext_modules = [
    Extension(package, [f"{package.replace('.', '/')}.py"])
    for package in packages_list]

# long description from README file
# with open('README.md', encoding='utf-8') as f:
#     DESCRIPTION = f.read()

REQUIRED = open('requirements.txt').read()
REQUIRES_PYTHON = '>=3.7'

setup(
    name=PROJECT_NAME,
    version=VERSION,
    url='https://github.com/Drakkar-Software/OctoBot-Backtesting',
    license='LGPL-3.0',
    author='Drakkar-Software',
    author_email='drakkar-software@protonmail.com',
    description='OctoBot project backtesting engine',
    packages=PACKAGES,
    include_package_data=True,
    # long_description=DESCRIPTION,
    install_requires=REQUIRED,
    cmdclass={'build_ext': build_ext},
    tests_require=["pytest"],
    test_suite="tests",
    zip_safe=False,
    data_files=[],
    setup_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    ext_modules=cythonize(ext_modules),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Cython',
    ],
)
