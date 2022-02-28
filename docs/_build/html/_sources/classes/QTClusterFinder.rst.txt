QTClusterFinder
===============

.. py:class:: QTClusterFinder


   Bases: :py:class:`object`


Cython implementation of _QTClusterFinder


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1QTClusterFinder.html
 -- Inherits from ['BaseGroupFinder']




.. py:method:: QTClusterFinder.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: QTClusterFinder.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: QTClusterFinder.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: QTClusterFinder.getName


Cython signature: String getName()
Returns the name




.. py:method:: QTClusterFinder.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: QTClusterFinder.getProductName


Cython signature: String getProductName()
Returns the name of the product




.. py:method:: QTClusterFinder.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: QTClusterFinder.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: QTClusterFinder.registerChildren


Cython signature: void registerChildren()
Register all derived classes here




.. py:method:: QTClusterFinder.run


- Cython signature: void run(libcpp_vector[ConsensusMap] & input_maps, ConsensusMap & result_map)
- Cython signature: void run(libcpp_vector[FeatureMap] & input_maps, ConsensusMap & result_map)




.. py:method:: QTClusterFinder.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: QTClusterFinder.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: QTClusterFinder.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: QTClusterFinder.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: QTClusterFinder.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




