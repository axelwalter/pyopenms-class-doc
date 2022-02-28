SpectrumSettings
================

.. py:class:: SpectrumSettings


   Bases: :py:class:`object`


Cython implementation of _SpectrumSettings


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumSettings.html
 -- Inherits from ['MetaInfoInterface']




.. py:attribute:: SpectrumSettings.SpectrumType


alias of :py:class:`pyopenms.pyopenms_2.__SpectrumType`


.. py:method:: SpectrumSettings.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: SpectrumSettings.getAcquisitionInfo


Cython signature: AcquisitionInfo getAcquisitionInfo()
Returns a const reference to the acquisition info




.. py:method:: SpectrumSettings.getComment


Cython signature: String getComment()
Returns the free-text comment




.. py:method:: SpectrumSettings.getDataProcessing


Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()




.. py:method:: SpectrumSettings.getInstrumentSettings


Cython signature: InstrumentSettings getInstrumentSettings()
Returns a const reference to the instrument settings of the current spectrum




.. py:method:: SpectrumSettings.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: SpectrumSettings.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: SpectrumSettings.getNativeID


Cython signature: String getNativeID()
Returns the native identifier for the spectrum, used by the acquisition software




.. py:method:: SpectrumSettings.getPeptideIdentifications


Cython signature: libcpp_vector[PeptideIdentification] getPeptideIdentifications()
Returns a const reference to the PeptideIdentification vector




.. py:method:: SpectrumSettings.getPrecursors


Cython signature: libcpp_vector[Precursor] getPrecursors()
Returns a const reference to the precursors




.. py:method:: SpectrumSettings.getProducts


Cython signature: libcpp_vector[Product] getProducts()
Returns a const reference to the products




.. py:method:: SpectrumSettings.getSourceFile


Cython signature: SourceFile getSourceFile()
Returns a const reference to the source file




.. py:method:: SpectrumSettings.getType


Cython signature: int getType()
Returns the spectrum type (centroided (PEAKS) or profile data (RAW))




.. py:method:: SpectrumSettings.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: SpectrumSettings.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: SpectrumSettings.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: SpectrumSettings.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: SpectrumSettings.setAcquisitionInfo


Cython signature: void setAcquisitionInfo(AcquisitionInfo)
Sets the acquisition info




.. py:method:: SpectrumSettings.setComment


Cython signature: void setComment(String)
Sets the free-text comment




.. py:method:: SpectrumSettings.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])




.. py:method:: SpectrumSettings.setInstrumentSettings


Cython signature: void setInstrumentSettings(InstrumentSettings)
Sets the instrument settings of the current spectrum




.. py:method:: SpectrumSettings.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: SpectrumSettings.setNativeID


Cython signature: void setNativeID(String)
Sets the native identifier for the spectrum, used by the acquisition software




.. py:method:: SpectrumSettings.setPeptideIdentifications


Cython signature: void setPeptideIdentifications(libcpp_vector[PeptideIdentification])
Sets the PeptideIdentification vector




.. py:method:: SpectrumSettings.setPrecursors


Cython signature: void setPrecursors(libcpp_vector[Precursor])
Sets the precursors




.. py:method:: SpectrumSettings.setProducts


Cython signature: void setProducts(libcpp_vector[Product])
Sets the products




.. py:method:: SpectrumSettings.setSourceFile


Cython signature: void setSourceFile(SourceFile)
Sets the source file




.. py:method:: SpectrumSettings.setType


Cython signature: void setType(SpectrumType)
Sets the spectrum type




.. py:method:: SpectrumSettings.unify


Cython signature: void unify(SpectrumSettings)




