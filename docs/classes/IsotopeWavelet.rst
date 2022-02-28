IsotopeWavelet
==============

.. py:class:: IsotopeWavelet


   Bases: :py:class:`object`


Cython implementation of _IsotopeWavelet


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeWavelet.html




.. py:method:: IsotopeWavelet.destroy


Cython signature: void destroy()
Deletes the singleton instance




.. py:method:: IsotopeWavelet.getExpTableMaxIndex


Cython signature: size_t getExpTableMaxIndex()
Returns the largest possible index for the pre-sampled exp table




.. py:method:: IsotopeWavelet.getGammaTableMaxIndex


Cython signature: size_t getGammaTableMaxIndex()
Returns the largest possible index for the pre-sampled gamma table




.. py:method:: IsotopeWavelet.getInvTableSteps


Cython signature: double getInvTableSteps()
Returns the inv_table_steps_ parameter




.. py:method:: IsotopeWavelet.getLambdaL


Cython signature: double getLambdaL(double m)
Returns the mass-parameter lambda (linear fit)




.. py:method:: IsotopeWavelet.getMaxCharge


Cython signature: unsigned int getMaxCharge()
Returns the largest charge state we will consider




.. py:method:: IsotopeWavelet.getMzPeakCutOffAtMonoPos


Cython signature: unsigned int getMzPeakCutOffAtMonoPos(double mass, unsigned int z)




.. py:method:: IsotopeWavelet.getNumPeakCutOff


- Cython signature: unsigned int getNumPeakCutOff(double mass, unsigned int z)
- Cython signature: unsigned int getNumPeakCutOff(double mz)




.. py:method:: IsotopeWavelet.getTableSteps


Cython signature: double getTableSteps()
Returns the table_steps_ parameter




.. py:method:: IsotopeWavelet.getValueByLambda


Cython signature: double getValueByLambda(double lambda_, double tz1)


Returns the value of the isotope wavelet at position `t` via a fast table lookup
-----
Usually, you do not need to call this function
Please use `sampleTheWavelet` instead
Note that this functions returns the pure function value of psi and not the normalized (average=0)
value given by Psi
-----
:param lambda: The mass-parameter lambda
:param tz1: t (the position) times the charge (z) plus 1




.. py:method:: IsotopeWavelet.getValueByLambdaExact


Cython signature: double getValueByLambdaExact(double lambda_, double tz1)




.. py:method:: IsotopeWavelet.getValueByLambdaExtrapol


Cython signature: double getValueByLambdaExtrapol(double lambda_, double tz1)


Returns the value of the isotope wavelet at position `t`
-----
This function is usually significantly slower than the table lookup performed in @see getValueByLambda
Nevertheless, it might be necessary to call this function due to extrapolating reasons caused by the
alignment of the wavelet
-----
Usually, you do not need to call this function
Please use `sampleTheWavelet` instead
Note that this functions returns the pure function value of psi and not the normalized (average=0)
value given by Psi
-----
:param lambda: The mass-parameter lambda
:param tz1: t (the position) times the charge (z) plus 1




.. py:method:: IsotopeWavelet.getValueByMass


Cython signature: double getValueByMass(double t, double m, unsigned int z, int mode)


Returns the value of the isotope wavelet at position `t`. Usually, you do not need to call this function
-----
Note that this functions returns the pure function value of psi and not the normalized (average=0)
value given by Psi
-----
:param t: The position at which the wavelet has to be drawn (within the coordinate system of the wavelet)
:param m: The m/z position within the signal (i.e. the mass not de-charged) within the signal
:param z: The charge `z` we want to detect
:param mode: Indicates whether positive mode (+1) or negative mode (-1) has been used for ionization




.. py:method:: IsotopeWavelet.myPow


Cython signature: float myPow(float a, float b)
Internally used function; uses register shifts for fast computation of the power function




.. py:method:: IsotopeWavelet.setMaxCharge


Cython signature: void setMaxCharge(unsigned int max_charge)
Sets the `max_charge` parameter




.. py:method:: IsotopeWavelet.setTableSteps


Cython signature: void setTableSteps(double table_steps)
Sets the `table_steps` parameter




