from setuptools import setup, find_packages

setup(
    name='clusteringtools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'Corrfunc'
    ],
    author='Richard Stiskalek',
    author_email='richard.stiskalek@protonmail.com',
    description='Clustering Analysis tools for galaxies and haloes focusing on kNN and 2PCF calculations.',
    license='GNU General Public License v3.0',
    url='https://github.com/Richard-Sti/ClusteringTools',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
)
