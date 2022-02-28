MassTraceDetection
==================

.. py:class:: MassTraceDetection


   Bases: :py:class:`object`


Cython implementation of _MassTraceDetection


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MassTraceDetection.html
 -- Inherits from ['ProgressLogger', 'DefaultParamHandler']




.. py:method:: MassTraceDetection.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MassTraceDetection.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MassTraceDetection.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MassTraceDetection.getName


Cython signature: String getName()
Returns the name




.. py:method:: MassTraceDetection.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MassTraceDetection.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MassTraceDetection.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MassTraceDetection.run


Cython signature: void run(MSExperiment & input_map, libcpp_vector[Kernel_MassTrace] & traces, size_t max_traces)




.. py:method:: MassTraceDetection.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MassTraceDetection.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MassTraceDetection.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MassTraceDetection.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MassTraceDetection.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




