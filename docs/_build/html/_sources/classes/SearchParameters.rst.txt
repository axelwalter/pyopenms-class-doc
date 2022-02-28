SearchParameters
================

.. py:class:: SearchParameters


   Bases: :py:class:`object`


Cython implementation of _SearchParameters


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SearchParameters.html
 -- Inherits from ['MetaInfoInterface']




.. py:attribute:: SearchParameters.charges




.. py:method:: SearchParameters.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:attribute:: SearchParameters.db




.. py:attribute:: SearchParameters.db_version




.. py:attribute:: SearchParameters.digestion_enzyme




.. py:attribute:: SearchParameters.fixed_modifications




.. py:attribute:: SearchParameters.fragment_mass_tolerance




.. py:attribute:: SearchParameters.fragment_mass_tolerance_ppm




.. py:method:: SearchParameters.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: SearchParameters.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: SearchParameters.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:attribute:: SearchParameters.mass_type




.. py:method:: SearchParameters.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: SearchParameters.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:attribute:: SearchParameters.missed_cleavages




.. py:attribute:: SearchParameters.precursor_mass_tolerance




.. py:attribute:: SearchParameters.precursor_mass_tolerance_ppm




.. py:method:: SearchParameters.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: SearchParameters.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:attribute:: SearchParameters.taxonomy




.. py:attribute:: SearchParameters.variable_modifications




