QTCluster
=========

.. py:class:: QTCluster


   Bases: :py:class:`object`


Cython implementation of _QTCluster


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1QTCluster.html




.. py:method:: QTCluster.finalizeCluster


Cython signature: void finalizeCluster()
Has to be called after adding elements (after calling




.. py:method:: QTCluster.getAnnotations


Cython signature: libcpp_set[AASequence] getAnnotations()
Returns the set of peptide sequences annotated to the cluster center




.. py:method:: QTCluster.getCenterMZ


Cython signature: double getCenterMZ()
Returns the m/z value of the cluster center




.. py:method:: QTCluster.getCenterRT


Cython signature: double getCenterRT()
Returns the RT value of the cluster




.. py:method:: QTCluster.getQuality


Cython signature: double getQuality()
Returns the cluster quality and recomputes if necessary




.. py:method:: QTCluster.getXCoord


Cython signature: int getXCoord()
Returns the x coordinate in the grid




.. py:method:: QTCluster.getYCoord


Cython signature: int getYCoord()
Returns the y coordinate in the grid




.. py:method:: QTCluster.initializeCluster


Cython signature: void initializeCluster()
Has to be called before adding elements (calling




.. py:method:: QTCluster.isInvalid


Cython signature: bool isInvalid()
Whether current cluster is invalid




.. py:method:: QTCluster.setInvalid


Cython signature: void setInvalid()
Sets current cluster as invalid (also frees some memory)




.. py:method:: QTCluster.size


Cython signature: size_t size()
Returns the size of the cluster (number of elements, incl. center)




