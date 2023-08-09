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
"""Utility functions for clustering."""
import numpy


def normalised_marks(x, y, bins):
    """
    Calculate the normalised marks of `y` binned by `x`. Within bins, `y` is
    sorted and the marks are assigned in ascending order and normalised to
    [0, 1].

    For example, a mark of 0.5 corresponds to the median value of
    `y` in the bin.

    Parameters
    ----------
    x : 1-dimensional array
        Binning variable.
    y : 1-dimensional array
        The variable to be marked.
    bins : int
        Bins of `x`.

    Returns
    -------
    marks : 1-dimensional array
    """
    assert bins.ndim == x.ndim == y.ndim == 1, "Only 1D arrays are supported."

    if not numpy.issubdtype(y.dtype, numpy.floating):
        raise NotImplementedError("Integer marks are not supported.")

    marks = numpy.full_like(y, numpy.nan)

    for i in range(bins.size):
        m = (x >= bins[i]) & (x < bins[i + 1])

        _marks = numpy.full(numpy.sum(m), numpy.nan, dtype=marks.dtype)
        for n, ind in enumerate(numpy.argsort(y[m])):
            _marks[ind] = n
        _marks /= numpy.nanmax(_marks)

        marks[m] = _marks

    return marks
