MassDecomposition
=================

.. py:class:: MassDecomposition


   Bases: :py:class:`object`


Cython implementation of _MassDecomposition


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MassDecomposition.html


 Class represents a decomposition of a mass into amino acids
 -----
 This class represents a mass decomposition into amino acids. A
 decomposition are amino acids given with frequencies which add
 up to a specific mass.




.. py:method:: MassDecomposition.compatible


Cython signature: bool compatible(MassDecomposition & deco)
Returns true if the mass decomposition if contained in this instance




.. py:method:: MassDecomposition.containsTag


Cython signature: bool containsTag(const String & tag)
Returns true if tag is contained in the mass decomposition




.. py:method:: MassDecomposition.getNumberOfMaxAA


Cython signature: size_t getNumberOfMaxAA()
Returns the max frequency of this composition




.. py:method:: MassDecomposition.toExpandedString


Cython signature: String toExpandedString()
Returns the decomposition as a string; instead of frequencies the amino acids are repeated




.. py:method:: MassDecomposition.toString


Cython signature: String toString()
Returns the decomposition as a string




