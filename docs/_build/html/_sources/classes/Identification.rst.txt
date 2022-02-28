Identification
==============

.. py:class:: Identification


   Bases: :py:class:`object`


Cython implementation of _Identification


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Identification.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: Identification.addSpectrumIdentification


Cython signature: void addSpectrumIdentification(SpectrumIdentification & id)
Adds a spectrum identification




.. py:method:: Identification.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Identification.getCreationDate


Cython signature: DateTime getCreationDate()
Returns the date and time the file was created




.. py:method:: Identification.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Identification.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Identification.getSpectrumIdentifications


Cython signature: libcpp_vector[SpectrumIdentification] getSpectrumIdentifications()
Returns the spectrum identifications stored




.. py:method:: Identification.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Identification.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Identification.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: Identification.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Identification.setCreationDate


Cython signature: void setCreationDate(DateTime date)
Sets the date and time the file was written




.. py:method:: Identification.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: Identification.setSpectrumIdentifications


Cython signature: void setSpectrumIdentifications(libcpp_vector[SpectrumIdentification] & ids)
Sets the spectrum identifications




