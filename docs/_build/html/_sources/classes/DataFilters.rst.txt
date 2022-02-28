DataFilters
===========

.. py:class:: DataFilters


   Bases: :py:class:`object`


Cython implementation of _DataFilters


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1DataFilters.html




.. py:attribute:: DataFilters.FilterOperation


alias of :py:class:`pyopenms.pyopenms_1.__FilterOperation`


.. py:attribute:: DataFilters.FilterType


alias of :py:class:`pyopenms.pyopenms_1.__FilterType`


.. py:method:: DataFilters.add


Cython signature: void add(DataFilter & filter_)




.. py:method:: DataFilters.clear


Cython signature: void clear()




.. py:method:: DataFilters.isActive


Cython signature: bool isActive()




.. py:method:: DataFilters.passes


- Cython signature: bool passes(Feature & feature)
- Cython signature: bool passes(ConsensusFeature & consensus_feature)
- Cython signature: bool passes(MSSpectrum & spectrum, size_t peak_index)




.. py:method:: DataFilters.remove


Cython signature: void remove(size_t index)




.. py:method:: DataFilters.replace


Cython signature: void replace(size_t index, DataFilter & filter_)




.. py:method:: DataFilters.setActive


Cython signature: void setActive(bool is_active)




.. py:method:: DataFilters.size


Cython signature: size_t size()




