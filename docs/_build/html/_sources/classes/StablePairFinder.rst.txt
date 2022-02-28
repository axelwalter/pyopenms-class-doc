StablePairFinder
================

.. py:class:: StablePairFinder


   Bases: :py:class:`object`


Cython implementation of _StablePairFinder


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1StablePairFinder.html
 -- Inherits from ['BaseGroupFinder']




.. py:method:: StablePairFinder.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: StablePairFinder.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: StablePairFinder.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: StablePairFinder.getName


Cython signature: String getName()
Returns the name




.. py:method:: StablePairFinder.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: StablePairFinder.getProductName


Cython signature: String getProductName()




.. py:method:: StablePairFinder.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: StablePairFinder.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: StablePairFinder.registerChildren


Cython signature: void registerChildren()
Register all derived classes here




.. py:method:: StablePairFinder.run


Cython signature: void run(libcpp_vector[ConsensusMap] & input_maps, ConsensusMap & result_map)




.. py:method:: StablePairFinder.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: StablePairFinder.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: StablePairFinder.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: StablePairFinder.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: StablePairFinder.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




