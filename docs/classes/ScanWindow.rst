ScanWindow
==========

.. py:class:: ScanWindow


   Bases: :py:class:`object`


Cython implementation of _ScanWindow


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ScanWindow.html
 -- Inherits from ['MetaInfoInterface']




.. py:attribute:: ScanWindow.begin




.. py:method:: ScanWindow.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:attribute:: ScanWindow.end




.. py:method:: ScanWindow.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ScanWindow.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ScanWindow.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ScanWindow.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ScanWindow.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ScanWindow.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ScanWindow.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




