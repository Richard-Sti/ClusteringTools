# Copyright (C) 2023 Richard Stiskalek
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""Generation of random points."""
from abc import ABC, abstractmethod

import numpy


class BaseRVS(ABC):
    """
    Base RVS generator to enforce the same interface for all generators.
    """
    _radius = None
    _boxsize = None

    @property
    def radius(self):
        if self._radius is None:
            raise RuntimeError("Radius is not set.")
        return self._radius

    @radius.setter
    def radius(self, value):
        assert value > 0, "Radius must be positive."
        self._radius = value

    @property
    def boxsize(self):
        if self._boxsize is None:
            raise RuntimeError("Box size is not set.")
        return self._boxsize

    @boxsize.setter
    def boxsize(self, value):
        assert value > 0, "Box size must be positive."
        self._boxsize = value

    @abstractmethod
    def __call__(self, nsamples, random_state, dtype):
        """
        Generate RVS.

        Parameters
        ----------
        nsamples : int
            Number of samples to generate.
        random_state : int, optional
            Random state for the random number generator.
        dtype : numpy dtype, optional
            Data type, by default `numpy.float32`.

        Returns
        -------
        samples : 2-dimensional array of shape `(nsamples, ndim)`
        """
        pass


class RVSinsphere(BaseRVS):
    """
    Generator of uniform RVS in a sphere in Cartesian coordinates centered at
    the centre of the box.

    Parameters
    ----------
    radius : float
        Sphere radius.
    boxsize : float
        Size of the box within which the sphere is placed.
    """

    def __init__(self, radius, boxsize):
        self.radius = radius
        self.boxsize = boxsize

    def __call__(self, nsamples, random_state=42, dtype=numpy.float32):
        gen = numpy.random.default_rng(random_state)

        r = gen.random(nsamples, dtype=dtype)**(1 / 3) * self.R
        theta = numpy.arccos(1 - 2 * gen.random(nsamples, dtype=dtype))
        phi = 2 * numpy.pi * gen.random(nsamples, dtype=dtype)

        stheta = numpy.sin(theta)
        out = numpy.vstack([stheta * numpy.cos(phi),
                            stheta * numpy.sin(phi),
                            numpy.cos(theta)]).T
        return r * out + self.boxsize / 2


class RVSinbox(BaseRVS):
    """
    Generator of uniform RVS in a box of size `L` in Cartesian coordinates in
    [0, L].

    Parameters
    ----------
    boxsize : float
        Size of the box.
    """
    def __init__(self, boxsize):
        self.boxsize = boxsize

    def __call__(self, nsamples, random_state=42, dtype=numpy.float32):
        gen = numpy.random.default_rng(random_state)

        out = numpy.vstack([gen.random(nsamples, dtype=dtype),
                            gen.random(nsamples, dtype=dtype),
                            gen.random(nsamples, dtype=dtype)]).T
        return self.boxsize * out


class RVSonsphere(BaseRVS):
    """
    Generator of uniform RVS on the surface of a unit sphere. RA is in
    [0, 2pi) and dec in [-pi / 2, pi / 2], respectively.
    """

    def __call__(self, nsamples, random_state=42, dtype=numpy.float32):
        gen = numpy.random.default_rng(random_state)

        return numpy.vstack(
            [2 * numpy.pi * gen.random(nsamples, dtype=dtype),
             numpy.arcsin(2 * (gen.random(nsamples, dtype=dtype) - 0.5))]).T
