FeatureFinder
=============

.. py:class:: FeatureFinder


   Bases: :py:class:`object`


Cython implementation of _FeatureFinder


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFinder.html
 -- Inherits from ['ProgressLogger']




.. py:method:: FeatureFinder.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: FeatureFinder.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: FeatureFinder.getParameters


Cython signature: Param getParameters(String algorithm_name)
Returns the default parameters for the algorithm with name `algorithm_name`




.. py:method:: FeatureFinder.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: FeatureFinder.run


Cython signature: void run(String algorithm_name, MSExperiment & input_map, FeatureMap & feats, Param & param, FeatureMap & seeds)


Executes the FeatureFinder using the given algorithm
-----
There are several constraints for the `input_map`.  They are tested before the algorithm starts.  It must only contain MS 1 level scans and you have to call updateRanges() before passing it to this method
The input map is sorted by RT & m/z if that's not the case
Furthermore we throw an Exception if the data contains negative m/z values,
as this will disturb most algorithms
-----
:param algorithm_name: Name of the feature finding algorithm to use
:param input_map: Input peak map
:param features: Output feature map
:param param: Algorithm parameters
:param seeds: List of seeds to use




.. py:method:: FeatureFinder.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: FeatureFinder.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: FeatureFinder.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




