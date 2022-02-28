KDTreeFeatureMaps
=================

.. py:class:: KDTreeFeatureMaps


   Bases: :py:class:`object`


Cython implementation of _KDTreeFeatureMaps


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1KDTreeFeatureMaps.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: KDTreeFeatureMaps.addMaps


- Cython signature: void addMaps(libcpp_vector[FeatureMap] & maps)
  Add `maps` and balance kd-tree


- Cython signature: void addMaps(libcpp_vector[ConsensusMap] & maps)




.. py:method:: KDTreeFeatureMaps.charge


Cython signature: int charge(size_t i)




.. py:method:: KDTreeFeatureMaps.clear


Cython signature: void clear()




.. py:method:: KDTreeFeatureMaps.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: KDTreeFeatureMaps.getName


Cython signature: String getName()
Returns the name




.. py:method:: KDTreeFeatureMaps.getNeighborhood


Cython signature: void getNeighborhood(size_t index, libcpp_vector[size_t] & result_indices, double rt_tol, double mz_tol, bool mz_ppm, bool include_features_from_same_map, double max_pairwise_log_fc)
Fill `result` with indices of all features compatible (wrt. RT, m/z, map index) to the feature with `index`




.. py:method:: KDTreeFeatureMaps.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: KDTreeFeatureMaps.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: KDTreeFeatureMaps.intensity


Cython signature: float intensity(size_t i)




.. py:method:: KDTreeFeatureMaps.mapIndex


Cython signature: size_t mapIndex(size_t i)




.. py:method:: KDTreeFeatureMaps.mz


Cython signature: double mz(size_t i)




.. py:method:: KDTreeFeatureMaps.numMaps


Cython signature: size_t numMaps()




.. py:method:: KDTreeFeatureMaps.optimizeTree


Cython signature: void optimizeTree()




.. py:method:: KDTreeFeatureMaps.queryRegion


Cython signature: void queryRegion(double rt_low, double rt_high, double mz_low, double mz_high, libcpp_vector[size_t] & result_indices, size_t ignored_map_index)




.. py:method:: KDTreeFeatureMaps.rt


Cython signature: double rt(size_t i)




.. py:method:: KDTreeFeatureMaps.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: KDTreeFeatureMaps.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: KDTreeFeatureMaps.size


Cython signature: size_t size()




.. py:method:: KDTreeFeatureMaps.treeSize


Cython signature: size_t treeSize()




