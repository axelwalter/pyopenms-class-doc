TransitionTSVFile
=================

.. py:class:: TransitionTSVFile


   Bases: :py:class:`object`


Cython implementation of _TransitionTSVFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TransitionTSVFile.html
 -- Inherits from ['ProgressLogger']




.. py:method:: TransitionTSVFile.convertTSVToTargetedExperiment


- Cython signature: void convertTSVToTargetedExperiment(char * filename, FileType filetype, TargetedExperiment & targeted_exp)
  Read in a tsv/mrm file and construct a targeted experiment (TraML structure)


- Cython signature: void convertTSVToTargetedExperiment(char * filename, FileType filetype, LightTargetedExperiment & targeted_exp)
  Read in a tsv file and construct a targeted experiment (Light transition structure)




.. py:method:: TransitionTSVFile.convertTargetedExperimentToTSV


Cython signature: void convertTargetedExperimentToTSV(char * filename, TargetedExperiment & targeted_exp)
Write out a targeted experiment (TraML structure) into a tsv file




.. py:method:: TransitionTSVFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: TransitionTSVFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: TransitionTSVFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: TransitionTSVFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: TransitionTSVFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: TransitionTSVFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: TransitionTSVFile.validateTargetedExperiment


Cython signature: void validateTargetedExperiment(TargetedExperiment targeted_exp)
Validate a TargetedExperiment (check that all ids are unique)




.. py:module:: pyopenms.pyopenms_7




