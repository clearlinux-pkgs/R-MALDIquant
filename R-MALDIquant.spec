#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-MALDIquant
Version  : 1.19.3
Release  : 13
URL      : https://cran.r-project.org/src/contrib/MALDIquant_1.19.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MALDIquant_1.19.3.tar.gz
Summary  : Quantitative Analysis of Mass Spectrometry Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-MALDIquant-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
desorption/ionization-time-of-flight (MALDI-TOF) and other
        two-dimensional mass spectrometry data. In addition to commonly
        used plotting and processing methods it includes distinctive
        features, namely baseline subtraction methods such as
        morphological filters (TopHat) or the statistics-sensitive
        non-linear iterative peak-clipping algorithm (SNIP), peak
        alignment using warping functions, handling of replicated
        measurements as well as allowing spectra with different
        resolutions.

%package lib
Summary: lib components for the R-MALDIquant package.
Group: Libraries

%description lib
lib components for the R-MALDIquant package.


%prep
%setup -q -c -n MALDIquant

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557764015

%install
export SOURCE_DATE_EPOCH=1557764015
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MALDIquant
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MALDIquant
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MALDIquant
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc MALDIquant || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MALDIquant/CITATION
/usr/lib64/R/library/MALDIquant/DESCRIPTION
/usr/lib64/R/library/MALDIquant/INDEX
/usr/lib64/R/library/MALDIquant/Meta/Rd.rds
/usr/lib64/R/library/MALDIquant/Meta/data.rds
/usr/lib64/R/library/MALDIquant/Meta/demo.rds
/usr/lib64/R/library/MALDIquant/Meta/features.rds
/usr/lib64/R/library/MALDIquant/Meta/hsearch.rds
/usr/lib64/R/library/MALDIquant/Meta/links.rds
/usr/lib64/R/library/MALDIquant/Meta/nsInfo.rds
/usr/lib64/R/library/MALDIquant/Meta/package.rds
/usr/lib64/R/library/MALDIquant/Meta/vignette.rds
/usr/lib64/R/library/MALDIquant/NAMESPACE
/usr/lib64/R/library/MALDIquant/NEWS
/usr/lib64/R/library/MALDIquant/R/MALDIquant
/usr/lib64/R/library/MALDIquant/R/MALDIquant.rdb
/usr/lib64/R/library/MALDIquant/R/MALDIquant.rdx
/usr/lib64/R/library/MALDIquant/data/fiedler2009subset.RData
/usr/lib64/R/library/MALDIquant/demo/MALDIquant.R
/usr/lib64/R/library/MALDIquant/demo/baseline.R
/usr/lib64/R/library/MALDIquant/demo/peaks.R
/usr/lib64/R/library/MALDIquant/demo/warping.R
/usr/lib64/R/library/MALDIquant/demo/workflow.R
/usr/lib64/R/library/MALDIquant/doc/MALDIquant-intro.R
/usr/lib64/R/library/MALDIquant/doc/MALDIquant-intro.Rnw
/usr/lib64/R/library/MALDIquant/doc/MALDIquant-intro.pdf
/usr/lib64/R/library/MALDIquant/doc/index.html
/usr/lib64/R/library/MALDIquant/help/AnIndex
/usr/lib64/R/library/MALDIquant/help/MALDIquant.rdb
/usr/lib64/R/library/MALDIquant/help/MALDIquant.rdx
/usr/lib64/R/library/MALDIquant/help/aliases.rds
/usr/lib64/R/library/MALDIquant/help/paths.rds
/usr/lib64/R/library/MALDIquant/html/00Index.html
/usr/lib64/R/library/MALDIquant/html/R.css
/usr/lib64/R/library/MALDIquant/tests/testthat.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_alignSpectra-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_approxfun-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_as-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_as.matrix-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_as.matrix-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_averageMassSpectra-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_binPeaks-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_calculateLabelPositions-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_calibrateIntensity-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_colMedians-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_constructor-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_coordinates-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_deprecated-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_detectPeaks-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_determineWarpingFunctions-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_doByLabel-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_estimateBaseline-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_estimateNoise-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_filterPeaks-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_findEmptyMassObjects-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_findLocalMaximaLogical-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_grouper-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_intensity-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_intensityMatrix-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_irregular-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_isEmpty-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_isMassObject-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_isMassObjectList-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_isRegular-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_labelPeaks-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_length-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_localMaxima-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_mapply-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_mass-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_match.closest-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_merge-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_metaData-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_monoisotopic-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_monoisotopicPeaks-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_morphologicalFilter-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_msiSlices-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_mz-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_plotMsiSlice-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_plotMsiSlice-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_range-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_referencePeaks-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_removeBaseline-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_removeEmptyMassObjects-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_reorder.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_replaceNegativeIntensityValues.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_show-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_smoothIntensity-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_smoothingFilters-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_snr-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_subset-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_totalIonCurrent-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_transformIntensity-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_trim-methods.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_unlist-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_valid-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_warp-functions.R
/usr/lib64/R/library/MALDIquant/tests/testthat/test_warpingFunctions-functions.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/MALDIquant/libs/MALDIquant.so
/usr/lib64/R/library/MALDIquant/libs/MALDIquant.so.avx2
/usr/lib64/R/library/MALDIquant/libs/MALDIquant.so.avx512
