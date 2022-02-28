MzMLSpectrumDecoder
===================

.. py:class:: MzMLSpectrumDecoder


   Bases: :py:class:`object`


Cython implementation of _MzMLSpectrumDecoder


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzMLSpectrumDecoder.html


 A class to decode input strings that contain an mzML chromatogram or spectrum tag
 -----
 It uses xercesc to parse a string containing either a exactly one mzML
 spectrum or chromatogram (from <chromatogram> to </chromatogram> or
 <spectrum> to </spectrum> tag). It returns the data contained in the
 binaryDataArray for Intensity / mass-to-charge or Intensity / time




.. py:method:: MzMLSpectrumDecoder.domParseChromatogram


Cython signature: void domParseChromatogram(String in_, shared_ptr[_Interfaces_Chromatogram] & cptr)


Extract data from a string which contains a full mzML chromatogram
-----
Extracts data from the input string which is expected to contain exactly
one <chromatogram> tag (from <chromatogram> to </chromatogram>). This
function will extract the contained binaryDataArray and provide the
result as Chromatogram
-----
:param in: Input string containing the raw XML
:param cptr: Resulting chromatogram




.. py:method:: MzMLSpectrumDecoder.domParseSpectrum


Cython signature: void domParseSpectrum(String in_, shared_ptr[_Interfaces_Spectrum] & cptr)


Extract data from a string which contains a full mzML spectrum
-----
Extracts data from the input string which is expected to contain exactly
one <spectrum> tag (from <spectrum> to </spectrum>). This function will
extract the contained binaryDataArray and provide the result as Spectrum
-----
:param in: Input string containing the raw XML
:param cptr: Resulting spectrum




.. py:method:: MzMLSpectrumDecoder.setSkipXMLChecks


Cython signature: void setSkipXMLChecks(bool only)
Whether to skip some XML checks (e.g. removing whitespace inside base64 arrays) and be fast instead




