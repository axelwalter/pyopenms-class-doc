InstrumentSettings
==================

.. py:class:: InstrumentSettings


   Bases: :py:class:`object`


Cython implementation of _InstrumentSettings


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1InstrumentSettings.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: InstrumentSettings.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: InstrumentSettings.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: InstrumentSettings.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: InstrumentSettings.getPolarity


Cython signature: Polarity getPolarity()
Returns the polarity




.. py:method:: InstrumentSettings.getScanMode


Cython signature: ScanMode getScanMode()
Returns the scan mode




.. py:method:: InstrumentSettings.getScanWindows


Cython signature: libcpp_vector[ScanWindow] getScanWindows()
Returns the m/z scan windows




.. py:method:: InstrumentSettings.getZoomScan


Cython signature: bool getZoomScan()
Returns if this scan is a zoom (enhanced resolution) scan




.. py:method:: InstrumentSettings.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: InstrumentSettings.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: InstrumentSettings.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: InstrumentSettings.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: InstrumentSettings.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: InstrumentSettings.setPolarity


Cython signature: void setPolarity(Polarity)
Sets the polarity




.. py:method:: InstrumentSettings.setScanMode


Cython signature: void setScanMode(ScanMode scan_mode)
Sets the scan mode




.. py:method:: InstrumentSettings.setScanWindows


Cython signature: void setScanWindows(libcpp_vector[ScanWindow] scan_windows)
Sets the m/z scan windows




.. py:method:: InstrumentSettings.setZoomScan


Cython signature: void setZoomScan(bool zoom_scan)
Sets if this scan is a zoom (enhanced resolution) scan




