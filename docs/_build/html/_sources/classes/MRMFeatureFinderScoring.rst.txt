MRMFeatureFinderScoring
=======================

.. py:class:: MRMFeatureFinderScoring


   Bases: :py:class:`object`


Cython implementation of _MRMFeatureFinderScoring


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFeatureFinderScoring.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: MRMFeatureFinderScoring.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MRMFeatureFinderScoring.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MRMFeatureFinderScoring.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MRMFeatureFinderScoring.getName


Cython signature: String getName()
Returns the name




.. py:method:: MRMFeatureFinderScoring.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MRMFeatureFinderScoring.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MRMFeatureFinderScoring.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MRMFeatureFinderScoring.pickExperiment


Cython signature: void pickExperiment(MSExperiment & chromatograms, FeatureMap & output, TargetedExperiment & transition_exp_, TransformationDescription trafo, MSExperiment & swath_map)


Pick features in one experiment containing chromatogram
-----
Function for for wrapping in Python, only uses OpenMS datastructures and does not return the map
-----
:param chromatograms: The input chromatograms
:param output: The output features with corresponding scores
:param transition_exp: The transition list describing the experiment
:param trafo: Optional transformation of the experimental retention time to the normalized retention time space used in the transition list
:param swath_map: Optional SWATH-MS (DIA) map corresponding from which the chromatograms were extracted




.. py:method:: MRMFeatureFinderScoring.prepareProteinPeptideMaps_


Cython signature: void prepareProteinPeptideMaps_(LightTargetedExperiment & transition_exp)


Prepares the internal mappings of peptides and proteins
-----
Calling this method _is_ required before calling scorePeakgroups
-----
:param transition_exp: The transition list describing the experiment




.. py:method:: MRMFeatureFinderScoring.scorePeakgroups


Cython signature: void scorePeakgroups(LightMRMTransitionGroupCP transition_group, TransformationDescription trafo, libcpp_vector[SwathMap] swath_maps, FeatureMap & output, bool ms1only)


Score all peak groups of a transition group
-----
Iterate through all features found along the chromatograms of the transition group and score each one individually
-----
:param transition_group: The MRMTransitionGroup to be scored (input)
:param trafo: Optional transformation of the experimental retention time
            to the normalized retention time space used in the
            transition list
:param swath_maps: Optional SWATH-MS (DIA) map corresponding from which
                 the chromatograms were extracted. Use empty map if no
                 data is available
:param output: The output features with corresponding scores (the found
             features will be added to this FeatureMap)
:param ms1only: Whether to only do MS1 scoring and skip all MS2 scoring




.. py:method:: MRMFeatureFinderScoring.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MRMFeatureFinderScoring.setMS1Map


- Cython signature: void setMS1Map(shared_ptr[SpectrumAccessOpenMS] ms1_map)
- Cython signature: void setMS1Map(shared_ptr[SpectrumAccessOpenMSCached] ms1_map)




.. py:method:: MRMFeatureFinderScoring.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MRMFeatureFinderScoring.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MRMFeatureFinderScoring.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MRMFeatureFinderScoring.setStrictFlag


Cython signature: void setStrictFlag(bool flag)




.. py:method:: MRMFeatureFinderScoring.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




