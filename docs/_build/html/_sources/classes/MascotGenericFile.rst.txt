MascotGenericFile
=================

.. py:class:: MascotGenericFile


   Bases: :py:class:`object`


Cython implementation of _MascotGenericFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MascotGenericFile.html
 -- Inherits from ['ProgressLogger', 'DefaultParamHandler']




.. py:method:: MascotGenericFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MascotGenericFile.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MascotGenericFile.getHTTPPeakListEnclosure


Cython signature: libcpp_pair[String,String] getHTTPPeakListEnclosure(const String & filename)


Enclosing Strings of the peak list body for HTTP submission
-----
Can be used to embed custom content into HTTP submission (when writing only the MGF header in HTTP format and then
adding the peaks (in whatever format, e.g. mzXML) enclosed in this body
The `filename` can later be found in the Mascot response




.. py:method:: MascotGenericFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MascotGenericFile.getName


Cython signature: String getName()
Returns the name




.. py:method:: MascotGenericFile.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MascotGenericFile.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MascotGenericFile.load


Cython signature: void load(const String & filename, MSExperiment & exp)


Loads a Mascot Generic File into a PeakMap
-----
:param filename: File name which the map should be read from
:param exp: The map which is filled with the data from the given file
:raises:
  Exception: FileNotFound is thrown if the given file could not be found




.. py:method:: MascotGenericFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MascotGenericFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MascotGenericFile.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MascotGenericFile.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MascotGenericFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MascotGenericFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: MascotGenericFile.store


Cython signature: void store(const String & filename, MSExperiment & experiment)




.. py:method:: MascotGenericFile.updateMembers_


Cython signature: void updateMembers_()
Docu in base class




