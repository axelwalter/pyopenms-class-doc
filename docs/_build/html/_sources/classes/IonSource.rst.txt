IonSource
=========

.. py:class:: IonSource


   Bases: :py:class:`object`


Cython implementation of _IonSource


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IonSource.html
 -- Inherits from ['MetaInfoInterface']




.. py:attribute:: IonSource.InletType


alias of :py:class:`pyopenms.pyopenms_4.__InletType`


.. py:attribute:: IonSource.IonizationMethod


alias of :py:class:`pyopenms.pyopenms_4.__IonizationMethod`


.. py:attribute:: IonSource.Polarity


alias of :py:class:`pyopenms.pyopenms_4.__Polarity`


.. py:method:: IonSource.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: IonSource.getInletType


Cython signature: InletType getInletType()
Returns the inlet type




.. py:method:: IonSource.getIonizationMethod


Cython signature: IonizationMethod getIonizationMethod()
Returns the ionization method




.. py:method:: IonSource.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: IonSource.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: IonSource.getOrder


Cython signature: int getOrder()


Returns the position of this part in the whole Instrument
-----
Order can be ignored, as long the instrument has this default setup:
  - one ion source
  - one or many mass analyzers
  - one ion detector
-----
For more complex instruments, the order should be defined.




.. py:method:: IonSource.getPolarity


Cython signature: Polarity getPolarity()
Returns the ionization mode




.. py:method:: IonSource.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: IonSource.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: IonSource.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: IonSource.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: IonSource.setInletType


Cython signature: void setInletType(InletType inlet_type)
Sets the inlet type




.. py:method:: IonSource.setIonizationMethod


Cython signature: void setIonizationMethod(IonizationMethod ionization_type)
Sets the ionization method




.. py:method:: IonSource.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: IonSource.setOrder


Cython signature: void setOrder(int order)
Sets the order




.. py:method:: IonSource.setPolarity


Cython signature: void setPolarity(Polarity polarity)
Sets the ionization mode




