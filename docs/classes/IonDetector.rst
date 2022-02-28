IonDetector
===========

.. py:class:: IonDetector


   Bases: :py:class:`object`


Cython implementation of _IonDetector


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IonDetector.html
 -- Inherits from ['MetaInfoInterface']




.. py:attribute:: IonDetector.AcquisitionMode


alias of :py:class:`pyopenms.pyopenms_8.__AcquisitionMode`


.. py:attribute:: IonDetector.Type_IonDetector


alias of :py:class:`pyopenms.pyopenms_8.__Type_IonDetector`


.. py:method:: IonDetector.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: IonDetector.getADCSamplingFrequency


Cython signature: double getADCSamplingFrequency()
Returns the analog-to-digital converter sampling frequency (in Hz)




.. py:method:: IonDetector.getAcquisitionMode


Cython signature: AcquisitionMode getAcquisitionMode()
Returns the acquisition mode




.. py:method:: IonDetector.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: IonDetector.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: IonDetector.getOrder


Cython signature: int getOrder()
Returns the order




.. py:method:: IonDetector.getResolution


Cython signature: double getResolution()
Returns the resolution (in ns)




.. py:method:: IonDetector.getType


Cython signature: Type_IonDetector getType()
Returns the detector type




.. py:method:: IonDetector.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: IonDetector.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: IonDetector.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: IonDetector.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: IonDetector.setADCSamplingFrequency


Cython signature: void setADCSamplingFrequency(double ADC_sampling_frequency)
Sets the analog-to-digital converter sampling frequency (in Hz)




.. py:method:: IonDetector.setAcquisitionMode


Cython signature: void setAcquisitionMode(AcquisitionMode acquisition_mode)
Sets the acquisition mode




.. py:method:: IonDetector.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: IonDetector.setOrder


Cython signature: void setOrder(int order)
Sets the order




.. py:method:: IonDetector.setResolution


Cython signature: void setResolution(double resolution)
Sets the resolution (in ns)




.. py:method:: IonDetector.setType


Cython signature: void setType(Type_IonDetector type_)
Sets the detector type




