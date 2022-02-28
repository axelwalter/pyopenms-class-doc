TOFCalibration
==============

.. py:class:: TOFCalibration


   Bases: :py:class:`object`


Cython implementation of _TOFCalibration


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TOFCalibration.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: TOFCalibration.calibrate


Cython signature: void calibrate(MSExperiment & input, MSExperiment & output, libcpp_vector[double] & exp_masses)




.. py:method:: TOFCalibration.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: TOFCalibration.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: TOFCalibration.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: TOFCalibration.getML1s


Cython signature: libcpp_vector[double] getML1s()
Returns the first calibration constant




.. py:method:: TOFCalibration.getML2s


Cython signature: libcpp_vector[double] getML2s()




.. py:method:: TOFCalibration.getML3s


Cython signature: libcpp_vector[double] getML3s()




.. py:method:: TOFCalibration.getName


Cython signature: String getName()
Returns the name




.. py:method:: TOFCalibration.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: TOFCalibration.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: TOFCalibration.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: TOFCalibration.pickAndCalibrate


Cython signature: void pickAndCalibrate(MSExperiment & input, MSExperiment & output, libcpp_vector[double] & exp_masses)




.. py:method:: TOFCalibration.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: TOFCalibration.setML1s


Cython signature: void setML1s(libcpp_vector[double] & ml1s)




.. py:method:: TOFCalibration.setML2s


Cython signature: void setML2s(libcpp_vector[double] & ml2s)
Returns the second calibration constant




.. py:method:: TOFCalibration.setML3s


Cython signature: void setML3s(libcpp_vector[double] & ml3s)
Returns the third calibration constant




.. py:method:: TOFCalibration.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: TOFCalibration.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: TOFCalibration.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: TOFCalibration.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




