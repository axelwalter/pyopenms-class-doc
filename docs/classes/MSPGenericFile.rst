MSPGenericFile
==============

.. py:class:: MSPGenericFile


   Bases: :py:class:`object`


Cython implementation of _MSPGenericFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSPGenericFile.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: MSPGenericFile.getDefaultParameters


Cython signature: void getDefaultParameters(Param & params)
Returns the class' default parameters




.. py:method:: MSPGenericFile.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MSPGenericFile.getName


Cython signature: String getName()
Returns the name




.. py:method:: MSPGenericFile.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MSPGenericFile.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MSPGenericFile.load


Cython signature: void load(const String & filename, MSExperiment & library)


Load the file's data and metadata, and save it into an `MSExperiment`
-----
:param filename: Path to the MSP input file
:param library: The variable into which the extracted information will be saved
:raises:
  Exception: FileNotFound If the file could not be found




.. py:method:: MSPGenericFile.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MSPGenericFile.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MSPGenericFile.store


Cython signature: void store(const String & filename, const MSExperiment & library)


Save data and metadata into a file
-----
:param filename: Path to the MSP input file
:param library: The variable from which extracted information will be saved
:raises:
  Exception: FileNotWritable If the file is not writable




