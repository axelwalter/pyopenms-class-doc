ChromatogramSettings
====================

.. py:class:: ChromatogramSettings


   Bases: :py:class:`object`


Cython implementation of _ChromatogramSettings


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChromatogramSettings.html
 -- Inherits from ['MetaInfoInterface']


 Description of the chromatogram settings, provides meta-information
 about a single chromatogram.




.. py:attribute:: ChromatogramSettings.ChromatogramType


alias of :py:class:`pyopenms.pyopenms_4.__ChromatogramType`


.. py:method:: ChromatogramSettings.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: ChromatogramSettings.getAcquisitionInfo


Cython signature: AcquisitionInfo getAcquisitionInfo()
Returns the acquisition info




.. py:method:: ChromatogramSettings.getChromatogramType


Cython signature: ChromatogramType getChromatogramType()
Get the chromatogram type




.. py:method:: ChromatogramSettings.getComment


Cython signature: String getComment()
Returns the free-text comment




.. py:method:: ChromatogramSettings.getDataProcessing


Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
Returns the description of the applied processing




.. py:method:: ChromatogramSettings.getInstrumentSettings


Cython signature: InstrumentSettings getInstrumentSettings()
Returns the instrument settings of the current spectrum




.. py:method:: ChromatogramSettings.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ChromatogramSettings.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ChromatogramSettings.getNativeID


Cython signature: String getNativeID()
Returns the native identifier for the spectrum, used by the acquisition software.




.. py:method:: ChromatogramSettings.getPrecursor


Cython signature: Precursor getPrecursor()
Returns the precursors




.. py:method:: ChromatogramSettings.getProduct


Cython signature: Product getProduct()
Returns the product ion




.. py:method:: ChromatogramSettings.getSourceFile


Cython signature: SourceFile getSourceFile()
Returns the source file




.. py:method:: ChromatogramSettings.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ChromatogramSettings.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ChromatogramSettings.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ChromatogramSettings.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ChromatogramSettings.setAcquisitionInfo


Cython signature: void setAcquisitionInfo(AcquisitionInfo acquisition_info)
Sets the acquisition info




.. py:method:: ChromatogramSettings.setChromatogramType


Cython signature: void setChromatogramType(ChromatogramType type)
Sets the chromatogram type




.. py:method:: ChromatogramSettings.setComment


Cython signature: void setComment(String comment)
Sets the free-text comment




.. py:method:: ChromatogramSettings.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
Sets the description of the applied processing




.. py:method:: ChromatogramSettings.setInstrumentSettings


Cython signature: void setInstrumentSettings(InstrumentSettings instrument_settings)
Sets the instrument settings of the current spectrum




.. py:method:: ChromatogramSettings.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: ChromatogramSettings.setNativeID


Cython signature: void setNativeID(String native_id)
Sets the native identifier for the spectrum, used by the acquisition software.




.. py:method:: ChromatogramSettings.setPrecursor


Cython signature: void setPrecursor(Precursor precursor)
Sets the precursors




.. py:method:: ChromatogramSettings.setProduct


Cython signature: void setProduct(Product p)
Sets the product ion




.. py:method:: ChromatogramSettings.setSourceFile


Cython signature: void setSourceFile(SourceFile source_file)
Sets the source file




