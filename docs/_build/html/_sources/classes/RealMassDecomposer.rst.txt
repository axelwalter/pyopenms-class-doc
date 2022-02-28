RealMassDecomposer
==================

.. py:class:: RealMassDecomposer


   Bases: :py:class:`object`


Cython implementation of _RealMassDecomposer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::ims_1_1RealMassDecomposer.html




.. py:method:: RealMassDecomposer.getNumberOfDecompositions


Cython signature: uint64_t getNumberOfDecompositions(double mass, double error)


Gets a number of all decompositions for amass with an error
allowed. It's similar to thegetDecompositions(double,double) function
but less space consuming, since doesn't use container to store decompositions
-----
:param mass: Mass to be decomposed
:param error: Error allowed between given and result decomposition
:returns: Number of all decompositions for a given mass and error




