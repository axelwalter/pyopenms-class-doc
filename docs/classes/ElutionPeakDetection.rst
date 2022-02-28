ElutionPeakDetection
====================

.. py:class:: ElutionPeakDetection


   Bases: :py:class:`object`


Cython implementation of _ElutionPeakDetection


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ElutionPeakDetection.html
 -- Inherits from ['ProgressLogger', 'DefaultParamHandler']




.. py:method:: ElutionPeakDetection.computeApexSNR


Cython signature: double computeApexSNR(Kernel_MassTrace &)
Compute the signal to noise ratio at the apex (estimated by computeMassTraceNoise)




.. py:method:: ElutionPeakDetection.computeMassTraceNoise


Cython signature: double computeMassTraceNoise(Kernel_MassTrace &)
Compute noise level (as RMSE of the actual signal and the smoothed signal)




.. py:method:: ElutionPeakDetection.computeMassTraceSNR


Cython signature: double computeMassTraceSNR(Kernel_MassTrace &)
Compute the signal to noise ratio (estimated by computeMassTraceNoise)




.. py:method:: ElutionPeakDetection.detectPeaks


- Cython signature: void detectPeaks(Kernel_MassTrace & in_, libcpp_vector[Kernel_MassTrace] & out)
- Cython signature: void detectPeaks(libcpp_vector[Kernel_MassTrace] & in_, libcpp_vector[Kernel_MassTrace] & out)




.. py:method:: ElutionPeakDetection.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: ElutionPeakDetection.filterByPeakWidth


Cython signature: void filterByPeakWidth(libcpp_vector[Kernel_MassTrace] & in_, libcpp_vector[Kernel_MassTrace] & out)




.. py:method:: ElutionPeakDetection.findLocalExtrema


Cython signature: void findLocalExtrema(Kernel_MassTrace &, size_t &, libcpp_vector[size_t] &, libcpp_vector[size_t] &)




.. py:method:: ElutionPeakDetection.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: ElutionPeakDetection.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: ElutionPeakDetection.getName


Cython signature: String getName()
Returns the name




.. py:method:: ElutionPeakDetection.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: ElutionPeakDetection.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: ElutionPeakDetection.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: ElutionPeakDetection.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: ElutionPeakDetection.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: ElutionPeakDetection.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: ElutionPeakDetection.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: ElutionPeakDetection.smoothData


Cython signature: void smoothData(Kernel_MassTrace & mt, int win_size)




.. py:method:: ElutionPeakDetection.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




