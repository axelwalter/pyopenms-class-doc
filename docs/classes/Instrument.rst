Instrument
==========

.. py:class:: Instrument


   Bases: :py:class:`object`


Cython implementation of _Instrument


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Instrument.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: Instrument.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Instrument.getCustomizations


Cython signature: String getCustomizations()
Returns a description of customizations




.. py:method:: Instrument.getIonDetectors


Cython signature: libcpp_vector[IonDetector] getIonDetectors()
Returns the ion detector list




.. py:method:: Instrument.getIonOptics


Cython signature: IonOpticsType getIonOptics()
Returns the ion optics type




.. py:method:: Instrument.getIonSources


Cython signature: libcpp_vector[IonSource] getIonSources()
Returns the ion source list




.. py:method:: Instrument.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Instrument.getMassAnalyzers


Cython signature: libcpp_vector[MassAnalyzer] getMassAnalyzers()
Returns the mass analyzer list




.. py:method:: Instrument.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Instrument.getModel


Cython signature: String getModel()
Returns the instrument model




.. py:method:: Instrument.getName


Cython signature: String getName()
Returns the name of the instrument




.. py:method:: Instrument.getSoftware


Cython signature: Software getSoftware()
Returns the instrument software




.. py:method:: Instrument.getVendor


Cython signature: String getVendor()
Returns the instrument vendor




.. py:method:: Instrument.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Instrument.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Instrument.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: Instrument.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Instrument.setCustomizations


Cython signature: void setCustomizations(String customizations)
Sets the a description of customizations




.. py:method:: Instrument.setIonDetectors


Cython signature: void setIonDetectors(libcpp_vector[IonDetector] ion_detectors)
Sets the ion detector list




.. py:method:: Instrument.setIonOptics


Cython signature: void setIonOptics(IonOpticsType ion_optics)
Sets the ion optics type




.. py:method:: Instrument.setIonSources


Cython signature: void setIonSources(libcpp_vector[IonSource] ion_sources)
Sets the ion source list




.. py:method:: Instrument.setMassAnalyzers


Cython signature: void setMassAnalyzers(libcpp_vector[MassAnalyzer] mass_analyzers)
Sets the mass analyzer list




.. py:method:: Instrument.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: Instrument.setModel


Cython signature: void setModel(String model)
Sets the instrument model




.. py:method:: Instrument.setName


Cython signature: void setName(String name)
Sets the name of the instrument




.. py:method:: Instrument.setSoftware


Cython signature: void setSoftware(Software software)
Sets the instrument software




.. py:method:: Instrument.setVendor


Cython signature: void setVendor(String vendor)
Sets the instrument vendor




