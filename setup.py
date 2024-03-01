from setuptools import setup


setup(
    name='thonny-subway-surfers',
    version='0.1',
    author='McBigBob',
    author_email='none',
    description='Subway surfers gamplay for Thonny IDE',
    long_description=open('README.md').read(),
    url='none',
    license='MIT',
    packages=['thonnycontrib.thonny-subway-surfers'],
    include_package_data = True,
    install_requires=['thonny >= 3.0.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Software Development',
        'Topic :: Software Development :: Embedded Systems',
    ],
    keywords='Subway surfers gameplay for Thonny IDE',
    platforms=['Windows', 'macOS', 'Linux'],
)