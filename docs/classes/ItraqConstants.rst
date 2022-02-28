ItraqConstants
==============

.. py:class:: ItraqConstants


   Bases: :py:class:`object`


Cython implementation of _ItraqConstants


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ItraqConstants.html


 Some constants used throughout iTRAQ classes
 -----
 Constants for iTRAQ experiments and a ChannelInfo structure to store information about a single channel




.. py:method:: ItraqConstants.getIsotopeMatrixAsStringList


Cython signature: StringList getIsotopeMatrixAsStringList(int itraq_type, libcpp_vector[MatrixDouble] & isotope_corrections)


Convert isotope correction matrix to stringlist
-----
Each line is converted into a string of the format channel:-2Da/-1Da/+1Da/+2Da ; e.g. '114:0/0.3/4/0'
Useful for creating parameters or debug output
-----
:param itraq_type: Which matrix to stringify. Should be of values from enum ITRAQ_TYPES
:param isotope_corrections: Vector of the two matrices (4plex, 8plex)




.. py:method:: ItraqConstants.translateIsotopeMatrix


Cython signature: MatrixDouble translateIsotopeMatrix(int & itraq_type, libcpp_vector[MatrixDouble] & isotope_corrections)




.. py:method:: ItraqConstants.updateIsotopeMatrixFromStringList


Cython signature: void updateIsotopeMatrixFromStringList(int itraq_type, StringList & channels, libcpp_vector[MatrixDouble] & isotope_corrections)


Convert strings to isotope correction matrix rows
-----
Each string of format channel:-2Da/-1Da/+1Da/+2Da ; e.g. '114:0/0.3/4/0'
is parsed and the corresponding channel(row) in the matrix is updated
Not all channels need to be present, missing channels will be left untouched
Useful to update the matrix with user isotope correction values
-----
:param itraq_type: Which matrix to stringify. Should be of values from enum ITRAQ_TYPES
:param channels: New channel isotope values as strings
:param isotope_corrections: Vector of the two matrices (4plex, 8plex)




