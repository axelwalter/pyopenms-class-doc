MapAlignmentAlgorithmIdentification
===================================

.. py:class:: MapAlignmentAlgorithmIdentification


   Bases: :py:class:`object`


Cython implementation of _MapAlignmentAlgorithmIdentification


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MapAlignmentAlgorithmIdentification.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: MapAlignmentAlgorithmIdentification.align


- Cython signature: void align(libcpp_vector[MSExperiment] &, libcpp_vector[TransformationDescription] &, int)
- Cython signature: void align(libcpp_vector[FeatureMap] &, libcpp_vector[TransformationDescription] &, int)
- Cython signature: void align(libcpp_vector[ConsensusMap] &, libcpp_vector[TransformationDescription] &, int)




.. py:method:: MapAlignmentAlgorithmIdentification.align_4


Parameters:
ids (list): list of lists of PeptideIdentification objects
trafos (list): list of TransformationDescription objects
ref_index (int)




.. py:method:: MapAlignmentAlgorithmIdentification.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MapAlignmentAlgorithmIdentification.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MapAlignmentAlgorithmIdentification.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MapAlignmentAlgorithmIdentification.getName


Cython signature: String getName()
Returns the name




.. py:method:: MapAlignmentAlgorithmIdentification.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MapAlignmentAlgorithmIdentification.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MapAlignmentAlgorithmIdentification.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MapAlignmentAlgorithmIdentification.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MapAlignmentAlgorithmIdentification.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MapAlignmentAlgorithmIdentification.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MapAlignmentAlgorithmIdentification.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MapAlignmentAlgorithmIdentification.setReference


- Cython signature: void setReference(MSExperiment &)
- Cython signature: void setReference(FeatureMap &)
- Cython signature: void setReference(ConsensusMap &)
- Cython signature: void setReference(libcpp_vector[PeptideIdentification] &)




.. py:method:: MapAlignmentAlgorithmIdentification.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




