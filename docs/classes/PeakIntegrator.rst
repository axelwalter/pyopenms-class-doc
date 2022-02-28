PeakIntegrator
==============

.. py:class:: PeakIntegrator


   Bases: :py:class:`object`


Cython implementation of _PeakIntegrator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakIntegrator.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: PeakIntegrator.calculatePeakShapeMetrics


- Cython signature: PI_PeakShapeMetrics calculatePeakShapeMetrics(MSChromatogram & chromatogram, double left, double right, double peak_height, double peak_apex_pos)
- Cython signature: PI_PeakShapeMetrics calculatePeakShapeMetrics(MSSpectrum & spectrum, double left, double right, double peak_height, double peak_apex_pos)




.. py:method:: PeakIntegrator.estimateBackground


- Cython signature: PI_PeakBackground estimateBackground(MSChromatogram & chromatogram, double left, double right, double peak_apex_pos)
- Cython signature: PI_PeakBackground estimateBackground(MSSpectrum & spectrum, double left, double right, double peak_apex_pos)




.. py:method:: PeakIntegrator.getDefaultParameters


Cython signature: void getDefaultParameters(Param)




.. py:method:: PeakIntegrator.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PeakIntegrator.getName


Cython signature: String getName()
Returns the name




.. py:method:: PeakIntegrator.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PeakIntegrator.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PeakIntegrator.integratePeak


- Cython signature: PI_PeakArea integratePeak(MSChromatogram & chromatogram, double left, double right)
- Cython signature: PI_PeakArea integratePeak(MSSpectrum & spectrum, double left, double right)




.. py:method:: PeakIntegrator.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PeakIntegrator.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




