TransitionPQPFile
=================

.. py:class:: TransitionPQPFile


   Bases: :py:class:`object`


Cython implementation of _TransitionPQPFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TransitionPQPFile.html




.. py:method:: TransitionPQPFile.convertPQPToTargetedExperiment


         - Cython signature: void convertPQPToTargetedExperiment(char * filename, TargetedExperiment & targeted_exp, bool legacy_traml_id)


Read in a PQP file and construct a targeted experiment (TraML structure)
-----
:param filename: The input file
:param targeted_exp: The output targeted experiment
:param legacy_traml_id: Should legacy TraML IDs be used (boolean)?
         - Cython signature: void convertPQPToTargetedExperiment(char * filename, LightTargetedExperiment & targeted_exp, bool legacy_traml_id)


Read in a PQP file and construct a targeted experiment (Light transition structure)
-----
:param filename: The input file
:param targeted_exp: The output targeted experiment
:param legacy_traml_id: Should legacy TraML IDs be used (boolean)?




.. py:method:: TransitionPQPFile.convertTSVToTargetedExperiment


- Cython signature: void convertTSVToTargetedExperiment(char * filename, FileType filetype, TargetedExperiment & targeted_exp)
- Cython signature: void convertTSVToTargetedExperiment(char * filename, FileType filetype, LightTargetedExperiment & targeted_exp)




.. py:method:: TransitionPQPFile.convertTargetedExperimentToPQP


Cython signature: void convertTargetedExperimentToPQP(char * filename, TargetedExperiment & targeted_exp)


Write out a targeted experiment (TraML structure) into a PQP file
-----
:param filename: The output file
:param targeted_exp: The targeted experiment




.. py:method:: TransitionPQPFile.convertTargetedExperimentToTSV


Cython signature: void convertTargetedExperimentToTSV(char * filename, TargetedExperiment & targeted_exp)




.. py:method:: TransitionPQPFile.validateTargetedExperiment


Cython signature: void validateTargetedExperiment(TargetedExperiment targeted_exp)




