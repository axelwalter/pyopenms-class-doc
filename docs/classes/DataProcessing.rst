DataProcessing
==============

.. py:class:: DataProcessing


   Bases: :py:class:`object`


Cython implementation of _DataProcessing


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1DataProcessing.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: DataProcessing.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: DataProcessing.getCompletionTime


Cython signature: DateTime getCompletionTime()




.. py:method:: DataProcessing.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: DataProcessing.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: DataProcessing.getProcessingActions


Cython signature: libcpp_set[ProcessingAction] getProcessingActions()




.. py:method:: DataProcessing.getSoftware


Cython signature: Software getSoftware()




.. py:method:: DataProcessing.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: DataProcessing.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: DataProcessing.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: DataProcessing.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: DataProcessing.setCompletionTime


Cython signature: void setCompletionTime(DateTime t)




.. py:method:: DataProcessing.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: DataProcessing.setProcessingActions


Cython signature: void setProcessingActions(libcpp_set[ProcessingAction])




.. py:method:: DataProcessing.setSoftware


Cython signature: void setSoftware(Software s)




