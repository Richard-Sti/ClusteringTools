# ClusteringTools

This repository contains Python tools for analyzing clustering of galaxies and haloes, with a particular emphasis on the kNN (k-nearest neighbours) and 2PCF (2-point correlation function) calculations.

## Overview

1. **kNN-CDF Calculation**: A module that provides tools to calculate the 1-dimensional kNN-CDF statistic.
2. **2PCF Calculation**: A module to calculate the 2PCF from 3D pair counts.
3. **Random Point Generation**: Tools to generate random points in various geometric configurations, including within a sphere, within a box, and on the surface of a sphere.

## Prerequisites
   - Python 3.x
   - numpy
   - scipy
   - Corrfunc

## Installation

   - **Clone the repository** :
      ```bash
      git clone [your-repository-link]
      cd [repository-name]
      ```

   - **Set up a virtual environment**:
     ```bash
     python -m venv venv_clusteringtools
     source venv_clusteringtools/bin/activate
     ```

   - **Install the package**:
     ```bash
     pip install -e .
     ```

The flag `-e` installs the code in a development mode, meaning that any changes you make to the code will be immediately available without reinstalling the package. To deactivate the virtual environment when you're done:
   ```bash
   deactivate
   ```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
