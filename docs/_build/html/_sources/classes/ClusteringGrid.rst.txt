ClusteringGrid
==============

.. py:class:: ClusteringGrid


   Bases: :py:class:`object`


Cython implementation of _ClusteringGrid


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ClusteringGrid.html




.. py:method:: ClusteringGrid.addCluster


Cython signature: void addCluster(libcpp_pair[int,int] cell_index, int & cluster_index)
Adds a cluster to this grid cell




.. py:method:: ClusteringGrid.getCellCount


Cython signature: int getCellCount()
Returns number of grid cells occupied by one or more clusters




.. py:method:: ClusteringGrid.getGridSpacingX


Cython signature: libcpp_vector[double] getGridSpacingX()




.. py:method:: ClusteringGrid.getGridSpacingY


Cython signature: libcpp_vector[double] getGridSpacingY()




.. py:method:: ClusteringGrid.getIndex


Cython signature: libcpp_pair[int,int] getIndex(DPosition2 position)




.. py:method:: ClusteringGrid.isNonEmptyCell


Cython signature: bool isNonEmptyCell(libcpp_pair[int,int] cell_index)
Checks if there are clusters at this cell index




.. py:method:: ClusteringGrid.removeAllClusters


Cython signature: void removeAllClusters()
Removes all clusters from this grid (and hence all cells)




.. py:method:: ClusteringGrid.removeCluster


Cython signature: void removeCluster(libcpp_pair[int,int] cell_index, int & cluster_index)
Removes a cluster from this grid cell and removes the cell if no other cluster left




