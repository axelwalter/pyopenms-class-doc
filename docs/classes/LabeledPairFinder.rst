LabeledPairFinder
=================

.. py:class:: LabeledPairFinder


   Bases: :py:class:`object`


Cython implementation of _LabeledPairFinder


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1LabeledPairFinder.html
 -- Inherits from ['BaseGroupFinder']


 The LabeledPairFinder allows the matching of labeled features (features with a fixed distance)
 -----
 Finds feature pairs that have a defined distance in RT and m/z in the same map




.. py:method:: LabeledPairFinder.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: LabeledPairFinder.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: LabeledPairFinder.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: LabeledPairFinder.getName


Cython signature: String getName()
Returns the name




.. py:method:: LabeledPairFinder.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: LabeledPairFinder.getProductName


Cython signature: String getProductName()
Returns the name of this module




.. py:method:: LabeledPairFinder.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: LabeledPairFinder.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: LabeledPairFinder.registerChildren


Cython signature: void registerChildren()
Register all derived classes here




.. py:method:: LabeledPairFinder.run


Cython signature: void run(libcpp_vector[ConsensusMap] & input_maps, ConsensusMap & result_map)
Runs the LabeledPairFinder algorithm




.. py:method:: LabeledPairFinder.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: LabeledPairFinder.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: LabeledPairFinder.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: LabeledPairFinder.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: LabeledPairFinder.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




