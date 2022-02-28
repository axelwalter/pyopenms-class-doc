SwathFile
=========

.. py:class:: SwathFile


   Bases: :py:class:`object`


Cython implementation of _SwathFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SwathFile.html
 -- Inherits from ['ProgressLogger']




.. py:method:: SwathFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: SwathFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: SwathFile.loadMzML


Cython signature: libcpp_vector[SwathMap] loadMzML(String file_, String tmp, shared_ptr[ExperimentalSettings] exp_meta, String readoptions)


Loads a Swath run from a single mzML file
-----
Using the `plugin_consumer`, you can provide a custom consumer which will be chained
into the process of loading the data and making it available (depending on `readoptions`).
This is useful if you want to modify the data a priori or extract some other information using
MSDataTransformingConsumer (for example). Make sure it leaves the data intact, such that the
returned SwathMaps are actually useful
-----
:param file: Input filename
:param tmp: Temporary directory (for cached data)
:param exp_meta: Experimental metadata from mzML file
:param readoptions: How are spectra accessed after reading - tradeoff between memory usage and time (disk caching)
:param plugin_consumer: An intermediate custom consumer
:returns: Swath maps for MS2 and MS1 (unless readoptions == split, which returns no data)




.. py:method:: SwathFile.loadMzXML


Cython signature: libcpp_vector[SwathMap] loadMzXML(String file_, String tmp, shared_ptr[ExperimentalSettings] exp_meta, String readoptions)
Loads a Swath run from a single mzXML file




.. py:method:: SwathFile.loadSplit


Cython signature: libcpp_vector[SwathMap] loadSplit(StringList file_list, String tmp, shared_ptr[ExperimentalSettings] exp_meta, String readoptions)
Loads a Swath run from a list of split mzML files




.. py:method:: SwathFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: SwathFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: SwathFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: SwathFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




