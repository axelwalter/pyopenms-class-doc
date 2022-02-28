MapAlignmentAlgorithmPoseClustering
===================================

.. py:class:: MapAlignmentAlgorithmPoseClustering


   Bases: :py:class:`object`


Cython implementation of _MapAlignmentAlgorithmPoseClustering


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MapAlignmentAlgorithmPoseClustering.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: MapAlignmentAlgorithmPoseClustering.align


- Cython signature: void align(FeatureMap, TransformationDescription &)
- Cython signature: void align(MSExperiment, TransformationDescription &)




.. py:method:: MapAlignmentAlgorithmPoseClustering.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MapAlignmentAlgorithmPoseClustering.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MapAlignmentAlgorithmPoseClustering.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MapAlignmentAlgorithmPoseClustering.getName


Cython signature: String getName()
Returns the name




.. py:method:: MapAlignmentAlgorithmPoseClustering.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MapAlignmentAlgorithmPoseClustering.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MapAlignmentAlgorithmPoseClustering.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MapAlignmentAlgorithmPoseClustering.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MapAlignmentAlgorithmPoseClustering.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MapAlignmentAlgorithmPoseClustering.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MapAlignmentAlgorithmPoseClustering.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MapAlignmentAlgorithmPoseClustering.setReference


- Cython signature: void setReference(FeatureMap)
  Sets the reference for the alignment


- Cython signature: void setReference(MSExperiment)




.. py:method:: MapAlignmentAlgorithmPoseClustering.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




