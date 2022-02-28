PosteriorErrorProbabilityModel
==============================

.. py:class:: PosteriorErrorProbabilityModel


   Bases: :py:class:`object`


Cython implementation of _PosteriorErrorProbabilityModel


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::Math_1_1PosteriorErrorProbabilityModel.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: PosteriorErrorProbabilityModel.computeLogLikelihood


Cython signature: double computeLogLikelihood(libcpp_vector[double] & incorrect_density, libcpp_vector[double] & correct_density)
Computes the Maximum Likelihood with a log-likelihood function




.. py:method:: PosteriorErrorProbabilityModel.computeProbability


Cython signature: double computeProbability(double score)
Returns the computed posterior error probability for a given score




.. py:method:: PosteriorErrorProbabilityModel.fillDensities


Cython signature: void fillDensities(libcpp_vector[double] & x_scores, libcpp_vector[double] & incorrect_density, libcpp_vector[double] & correct_density)
Writes the distributions densities into the two vectors for a set of scores. Incorrect_densities represent the incorrectly assigned sequences




.. py:method:: PosteriorErrorProbabilityModel.fillLogDensities


Cython signature: void fillLogDensities(libcpp_vector[double] & x_scores, libcpp_vector[double] & incorrect_density, libcpp_vector[double] & correct_density)
Writes the log distributions densities into the two vectors for a set of scores. Incorrect_densities represent the incorrectly assigned sequences




.. py:method:: PosteriorErrorProbabilityModel.fit


         - Cython signature: bool fit(libcpp_vector[double] & search_engine_scores, String outlier_handling)


Fits the distributions to the data points(search_engine_scores). Estimated parameters for the distributions are saved in member variables
computeProbability can be used afterwards
Uses two Gaussians to fit. And Gauss+Gauss or Gumbel+Gauss to plot and calculate final probabilities
-----
:param search_engine_scores: A vector which holds the data points
:returns: `true` if algorithm has run through. Else false will be returned. In that case no plot and no probabilities are calculated
         - Cython signature: bool fit(libcpp_vector[double] & search_engine_scores, libcpp_vector[double] & probabilities, String outlier_handling)


Fits the distributions to the data points(search_engine_scores). Estimated parameters for the distributions are saved in member variables
computeProbability can be used afterwards
Uses two Gaussians to fit. And Gauss+Gauss or Gumbel+Gauss to plot and calculate final probabilities
-----
:param search_engine_scores: A vector which holds the data points
:param probabilities a vector which holds the probability for each data point after running this function. If it has some content it will be overwritten
:returns: `true` if algorithm has run through. Else false will be returned. In that case no plot and no probabilities are calculated




.. py:method:: PosteriorErrorProbabilityModel.getBothGnuplotFormula


Cython signature: String getBothGnuplotFormula(GaussFitResult & incorrect, GaussFitResult & correct)
Returns the gnuplot formula of the fitted mixture distribution




.. py:method:: PosteriorErrorProbabilityModel.getCorrectlyAssignedFitResult


Cython signature: GaussFitResult getCorrectlyAssignedFitResult()
Returns estimated parameters for correctly assigned sequences. Fit should be used before




.. py:method:: PosteriorErrorProbabilityModel.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PosteriorErrorProbabilityModel.getGaussGnuplotFormula


Cython signature: String getGaussGnuplotFormula(GaussFitResult & params)
Returns the gnuplot formula of the fitted gauss distribution




.. py:method:: PosteriorErrorProbabilityModel.getGumbelGnuplotFormula


Cython signature: String getGumbelGnuplotFormula(GaussFitResult & params)
Returns the gnuplot formula of the fitted gumbel distribution




.. py:method:: PosteriorErrorProbabilityModel.getIncorrectlyAssignedFitResult


Cython signature: GaussFitResult getIncorrectlyAssignedFitResult()
Returns estimated parameters for correctly assigned sequences. Fit should be used before




.. py:method:: PosteriorErrorProbabilityModel.getName


Cython signature: String getName()
Returns the name




.. py:method:: PosteriorErrorProbabilityModel.getNegativePrior


Cython signature: double getNegativePrior()
Returns the estimated negative prior probability




.. py:method:: PosteriorErrorProbabilityModel.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PosteriorErrorProbabilityModel.getSmallestScore


Cython signature: double getSmallestScore()
Returns the smallest score used in the last fit




.. py:method:: PosteriorErrorProbabilityModel.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PosteriorErrorProbabilityModel.initPlots


Cython signature: TextFile initPlots(libcpp_vector[double] & x_scores)
Initializes the plots




.. py:method:: PosteriorErrorProbabilityModel.plotTargetDecoyEstimation


Cython signature: void plotTargetDecoyEstimation(libcpp_vector[double] & target, libcpp_vector[double] & decoy)
Plots the estimated distribution against target and decoy hits




.. py:method:: PosteriorErrorProbabilityModel.pos_neg_mean_weighted_posteriors


Cython signature: libcpp_pair[double,double] pos_neg_mean_weighted_posteriors(libcpp_vector[double] & x_scores, libcpp_vector[double] & incorrect_posteriors)




.. py:method:: PosteriorErrorProbabilityModel.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PosteriorErrorProbabilityModel.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: PosteriorErrorProbabilityModel.tryGnuplot


Cython signature: void tryGnuplot(const String & gp_file)




