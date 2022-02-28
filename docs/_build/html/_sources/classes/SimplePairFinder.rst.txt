SimplePairFinder
================

.. py:class:: SimplePairFinder


   Bases: :py:class:`object`


Cython implementation of _SimplePairFinder


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SimplePairFinder.html
 -- Inherits from ['BaseGroupFinder']




.. py:method:: SimplePairFinder.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: SimplePairFinder.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: SimplePairFinder.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: SimplePairFinder.getName


Cython signature: String getName()
Returns the name




.. py:method:: SimplePairFinder.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: SimplePairFinder.getProductName


Cython signature: String getProductName()
Returns the name of this module




.. py:method:: SimplePairFinder.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: SimplePairFinder.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: SimplePairFinder.registerChildren


Cython signature: void registerChildren()
Register all derived classes here




.. py:method:: SimplePairFinder.run


Cython signature: void run(libcpp_vector[ConsensusMap] & input_maps, ConsensusMap & result_map)




.. py:method:: SimplePairFinder.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: SimplePairFinder.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: SimplePairFinder.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: SimplePairFinder.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: SimplePairFinder.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




