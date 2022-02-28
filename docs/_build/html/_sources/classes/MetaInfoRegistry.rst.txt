MetaInfoRegistry
================

.. py:class:: MetaInfoRegistry


   Bases: :py:class:`object`


Cython implementation of _MetaInfoRegistry


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaInfoRegistry.html


 Registry which assigns unique integer indices to strings
 -----
 When registering a new name an index >= 1024 is assigned.
 Indices from 1 to 1023 are reserved for fast access and will never change:
 1 - isotopic_range
 2 - cluster_id
 3 - label
 4 - icon
 5 - color
 6 - RT
 7 - MZ
 8 - predicted_RT
 9 - predicted_RT_p_value
 10 - spectrum_reference
 11 - ID
 12 - low_quality
 13 - charge




.. py:method:: MetaInfoRegistry.getDescription


- Cython signature: String getDescription(unsigned int index)
  Returns the description of an index


- Cython signature: String getDescription(const String & name)
  Returns the description of a name




.. py:method:: MetaInfoRegistry.getIndex


Cython signature: unsigned int getIndex(const String & name)
Returns the integer index corresponding to a string. If the string is not registered, returns UInt(-1) (= UINT_MAX)




.. py:method:: MetaInfoRegistry.getName


Cython signature: String getName(unsigned int index)
Returns the corresponding name to an index




.. py:method:: MetaInfoRegistry.getUnit


- Cython signature: String getUnit(unsigned int index)
  Returns the unit of an index


- Cython signature: String getUnit(const String & name)
  Returns the unit of a name




.. py:method:: MetaInfoRegistry.registerName


Cython signature: unsigned int registerName(const String & name, const String & description, const String & unit)
Registers a string, stores its description and unit, and returns the corresponding index. If the string is already registered, it returns the index of the string




.. py:method:: MetaInfoRegistry.setDescription


- Cython signature: void setDescription(unsigned int index, const String & description)
  Sets the description (String), corresponding to an index


- Cython signature: void setDescription(const String & name, const String & description)
  Sets the description (String), corresponding to a name




.. py:method:: MetaInfoRegistry.setUnit


- Cython signature: void setUnit(unsigned int index, const String & unit)
  Sets the unit (String), corresponding to an index


- Cython signature: void setUnit(const String & name, const String & unit)
  Sets the unit (String), corresponding to a name




