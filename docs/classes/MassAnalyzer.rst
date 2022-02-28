MassAnalyzer
============

.. py:class:: MassAnalyzer


   Bases: :py:class:`object`


Cython implementation of _MassAnalyzer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MassAnalyzer.html
 -- Inherits from ['MetaInfoInterface']




.. py:attribute:: MassAnalyzer.AnalyzerType


alias of :py:class:`pyopenms.pyopenms_2.__AnalyzerType`


.. py:attribute:: MassAnalyzer.ReflectronState


alias of :py:class:`pyopenms.pyopenms_2.__ReflectronState`


.. py:attribute:: MassAnalyzer.ResolutionMethod


alias of :py:class:`pyopenms.pyopenms_2.__ResolutionMethod`


.. py:attribute:: MassAnalyzer.ResolutionType


alias of :py:class:`pyopenms.pyopenms_2.__ResolutionType`


.. py:attribute:: MassAnalyzer.ScanDirection


alias of :py:class:`pyopenms.pyopenms_2.__ScanDirection`


.. py:attribute:: MassAnalyzer.ScanLaw


alias of :py:class:`pyopenms.pyopenms_2.__ScanLaw`


.. py:method:: MassAnalyzer.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: MassAnalyzer.getAccuracy


Cython signature: double getAccuracy()
Returns the mass accuracy i.e. how much the theoretical mass may differ from the measured mass (in ppm)




.. py:method:: MassAnalyzer.getFinalMSExponent


Cython signature: int getFinalMSExponent()
Returns the final MS exponent




.. py:method:: MassAnalyzer.getIsolationWidth


Cython signature: double getIsolationWidth()
Returns the isolation width i.e. in which m/z range the precursor ion is selected for MS to the n (in m/z)




.. py:method:: MassAnalyzer.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MassAnalyzer.getMagneticFieldStrength


Cython signature: double getMagneticFieldStrength()
Returns the strength of the magnetic field (in T)




.. py:method:: MassAnalyzer.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: MassAnalyzer.getOrder


Cython signature: int getOrder()
Returns the position of this part in the whole Instrument




.. py:method:: MassAnalyzer.getReflectronState


Cython signature: ReflectronState getReflectronState()
Returns the reflectron state (for TOF)




.. py:method:: MassAnalyzer.getResolution


Cython signature: double getResolution()
Returns the resolution. The maximum m/z value at which two peaks can be resolved, according to one of the standard measures




.. py:method:: MassAnalyzer.getResolutionMethod


Cython signature: ResolutionMethod getResolutionMethod()
Returns the method used for determination of the resolution




.. py:method:: MassAnalyzer.getResolutionType


Cython signature: ResolutionType getResolutionType()
Returns the resolution type




.. py:method:: MassAnalyzer.getScanDirection


Cython signature: ScanDirection getScanDirection()
Returns the direction of scanning




.. py:method:: MassAnalyzer.getScanLaw


Cython signature: ScanLaw getScanLaw()
Returns the scan law




.. py:method:: MassAnalyzer.getScanRate


Cython signature: double getScanRate()
Returns the scan rate (in s)




.. py:method:: MassAnalyzer.getScanTime


Cython signature: double getScanTime()
Returns the scan time for a single scan (in s)




.. py:method:: MassAnalyzer.getTOFTotalPathLength


Cython signature: double getTOFTotalPathLength()
Returns the path length for a TOF mass analyzer (in meter)




.. py:method:: MassAnalyzer.getType


Cython signature: AnalyzerType getType()
Returns the analyzer type




.. py:method:: MassAnalyzer.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: MassAnalyzer.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: MassAnalyzer.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: MassAnalyzer.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: MassAnalyzer.setAccuracy


Cython signature: void setAccuracy(double accuracy)
Sets the accuracy i.e. how much the theoretical mass may differ from the measured mass (in ppm)




.. py:method:: MassAnalyzer.setFinalMSExponent


Cython signature: void setFinalMSExponent(int final_MS_exponent)
Sets the final MS exponent




.. py:method:: MassAnalyzer.setIsolationWidth


Cython signature: void setIsolationWidth(double isolation_width)
Sets the isolation width i.e. in which m/z range the precursor ion is selected for MS to the n (in m/z)




.. py:method:: MassAnalyzer.setMagneticFieldStrength


Cython signature: void setMagneticFieldStrength(double magnetic_field_strength)
Sets the strength of the magnetic field (in T)




.. py:method:: MassAnalyzer.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: MassAnalyzer.setOrder


Cython signature: void setOrder(int order)
Sets the order




.. py:method:: MassAnalyzer.setReflectronState


Cython signature: void setReflectronState(ReflectronState reflecton_state)
Sets the reflectron state (for TOF)




.. py:method:: MassAnalyzer.setResolution


Cython signature: void setResolution(double resolution)
Sets the resolution




.. py:method:: MassAnalyzer.setResolutionMethod


Cython signature: void setResolutionMethod(ResolutionMethod resolution_method)
Sets the method used for determination of the resolution




.. py:method:: MassAnalyzer.setResolutionType


Cython signature: void setResolutionType(ResolutionType resolution_type)
Sets the resolution type




.. py:method:: MassAnalyzer.setScanDirection


Cython signature: void setScanDirection(ScanDirection scan_direction)
Sets the direction of scanning




.. py:method:: MassAnalyzer.setScanLaw


Cython signature: void setScanLaw(ScanLaw scan_law)
Sets the scan law




.. py:method:: MassAnalyzer.setScanRate


Cython signature: void setScanRate(double scan_rate)
Sets the scan rate (in s)




.. py:method:: MassAnalyzer.setScanTime


Cython signature: void setScanTime(double scan_time)
Sets the scan time for a single scan (in s)




.. py:method:: MassAnalyzer.setTOFTotalPathLength


Cython signature: void setTOFTotalPathLength(double TOF_total_path_length)
Sets the path length for a TOF mass analyzer (in meter)




.. py:method:: MassAnalyzer.setType


Cython signature: void setType(AnalyzerType type)
Sets the analyzer type




