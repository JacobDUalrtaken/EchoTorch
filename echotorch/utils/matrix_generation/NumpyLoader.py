# -*- coding: utf-8 -*-
#
# File : echotorch/utils/matrix_generation/MatrixGenerator.py
# Description : Matrix generator base class.
# Date : 29th of October, 2019
#
# This file is part of EchoTorch.  EchoTorch is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Nils Schaetti <nils.schaetti@unine.ch>

# Import
import torch
import scipy.io as io
import numpy as np
from .MatrixGenerator import MatrixGenerator
from .MatrixFactory import matrix_factory
import scipy.sparse


# Load matrix from Numpy file
class NumpyLoader(MatrixGenerator):
    """
    Load matrix from Numpy file
    """

    ################
    # PUBLIC
    ################

    # Generate the matrix
    def generate(self, size, dtype=torch.float64):
        """
        Generate the matrix
        :param size: Matrix size (ignored)
        :param dtype: Data type
        :return: Generated matrix
        """
        # Params
        file_name = self.get_parameter('file_name')

        # Load matrix
        loaded_matrix = np.load(file_name)

        # Reshape
        if 'shape' in self._parameters.keys():
            loaded_matrix = np.reshape(loaded_matrix, self.get_parameter('shape'))
        # end if

        # Dense or not
        if isinstance(loaded_matrix, scipy.sparse.csc_matrix):
            return torch.from_numpy(loaded_matrix.todense()).type(dtype)
        else:
            return torch.from_numpy(loaded_matrix).type(dtype)
        # end if
    # end generate

# end MatlabLoader


# Add
matrix_factory.register_generator("numpy", NumpyLoader)
