%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-r
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source0222:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plain.tar.xz
Source0668:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf.tar.xz
Source0669:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf.doc.tar.xz
Source1504:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/perception.tar.xz
Source1505:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/perception.doc.tar.xz
Source1506:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pnas2009.tar.xz
Source2007:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pacioli.tar.xz
Source2008:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pacioli.doc.tar.xz
Source2010:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paratype.tar.xz
Source2011:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paratype.doc.tar.xz
Source2012:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phaistos.tar.xz
Source2013:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phaistos.doc.tar.xz
Source2015:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phonetic.tar.xz
Source2016:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phonetic.doc.tar.xz
Source2017:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pigpen.tar.xz
Source2018:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pigpen.doc.tar.xz
Source2019:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/playfair.tar.xz
Source2020:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/playfair.doc.tar.xz
Source2021:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poltawski.tar.xz
Source2022:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poltawski.doc.tar.xz
Source2139:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/palatino.tar.xz
Source2237:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pas-crosswords.tar.xz
Source2238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pas-crosswords.doc.tar.xz
Source2316:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdf-trans.tar.xz
Source2317:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdf-trans.doc.tar.xz
Source2318:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plainpkg.tar.xz
Source2319:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plainpkg.doc.tar.xz
Source2355:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/path.tar.xz
Source2356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/path.doc.tar.xz
Source2364:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/passivetex.tar.xz
Source2431:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parallel.tar.xz
Source2432:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parallel.doc.tar.xz
Source2434:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parrun.tar.xz
Source2435:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parrun.doc.tar.xz
Source2437:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phonrule.tar.xz
Source2438:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phonrule.doc.tar.xz
Source2439:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plari.tar.xz
Source2440:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plari.doc.tar.xz
Source2442:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/play.tar.xz
Source2443:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/play.doc.tar.xz
Source2445:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poemscol.tar.xz
Source2446:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poemscol.doc.tar.xz
Source2448:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poetrytex.tar.xz
Source2449:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poetrytex.doc.tar.xz
Source2502:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/persian-bib.tar.xz
Source2503:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/persian-bib.doc.tar.xz
Source2646:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/patgen2-tutorial.doc.tar.xz
Source2647:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pictexsum.doc.tar.xz
Source2648:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plain-doc.doc.tar.xz
Source2957:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pl.tar.xz
Source2958:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pl.doc.tar.xz
Source2962:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polski.tar.xz
Source2963:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polski.doc.tar.xz
Source3068:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parskip.tar.xz
Source3069:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parskip.doc.tar.xz
Source3070:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfpages.tar.xz
Source3071:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfpages.doc.tar.xz
Source3073:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/powerdot.tar.xz
Source3074:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/powerdot.doc.tar.xz
Source3214:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pb-diagram.tar.xz
Source3215:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pb-diagram.doc.tar.xz
Source3218:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-blur.tar.xz
Source3219:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-blur.doc.tar.xz
Source3221:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-soroban.tar.xz
Source3222:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-soroban.doc.tar.xz
Source3223:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-umlcd.tar.xz
Source3224:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-umlcd.doc.tar.xz
Source3225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-umlsd.tar.xz
Source3226:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-umlsd.doc.tar.xz
Source3227:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfgantt.tar.xz
Source3228:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfgantt.doc.tar.xz
Source3230:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfkeyx.tar.xz
Source3231:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfkeyx.doc.tar.xz
Source3232:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfmolbio.tar.xz
Source3233:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfmolbio.doc.tar.xz
Source3235:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfopts.tar.xz
Source3236:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfopts.doc.tar.xz
Source3238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfplots.tar.xz
Source3239:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfplots.doc.tar.xz
Source3241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/picinpar.tar.xz
Source3242:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/picinpar.doc.tar.xz
Source3243:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pict2e.tar.xz
Source3244:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pict2e.doc.tar.xz
Source3246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pictex.tar.xz
Source3247:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pictex.doc.tar.xz
Source3248:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pictex2.tar.xz
Source3249:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pinlabel.tar.xz
Source3250:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pinlabel.doc.tar.xz
Source3251:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pmgraph.tar.xz
Source3252:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pmgraph.doc.tar.xz
Source3375:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paralist.tar.xz
Source3376:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paralist.doc.tar.xz
Source3381:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/placeins.tar.xz
Source3382:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/placeins.doc.tar.xz
Source4853:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pagecolor.tar.xz
Source4854:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pagecolor.doc.tar.xz
Source4856:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pagecont.tar.xz
Source4857:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pagecont.doc.tar.xz
Source4859:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pagenote.tar.xz
Source4860:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pagenote.doc.tar.xz
Source4862:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pagerange.tar.xz
Source4863:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pagerange.doc.tar.xz
Source4864:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pageslts.tar.xz
Source4865:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pageslts.doc.tar.xz
Source4867:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paper.tar.xz
Source4868:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paper.doc.tar.xz
Source4870:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/papercdcase.tar.xz
Source4871:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/papercdcase.doc.tar.xz
Source4873:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/papermas.tar.xz
Source4874:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/papermas.doc.tar.xz
Source4876:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/papertex.tar.xz
Source4877:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/papertex.doc.tar.xz
Source4879:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paracol.tar.xz
Source4880:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paracol.doc.tar.xz
Source4882:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paresse.tar.xz
Source4883:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/paresse.doc.tar.xz
Source4885:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parnotes.tar.xz
Source4886:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parnotes.doc.tar.xz
Source4887:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parselines.tar.xz
Source4888:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parselines.doc.tar.xz
Source4890:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pas-cours.tar.xz
Source4891:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pas-cours.doc.tar.xz
Source4892:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pas-cv.tar.xz
Source4893:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pas-cv.doc.tar.xz
Source4894:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pas-tableur.tar.xz
Source4895:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pas-tableur.doc.tar.xz
Source4896:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/patchcmd.tar.xz
Source4897:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/patchcmd.doc.tar.xz
Source4899:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pauldoc.tar.xz
Source4900:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pauldoc.doc.tar.xz
Source4902:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pawpict.tar.xz
Source4903:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pawpict.doc.tar.xz
Source4908:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pbox.tar.xz
Source4909:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pbox.doc.tar.xz
Source4911:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pbsheet.tar.xz
Source4912:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pbsheet.doc.tar.xz
Source4914:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdf14.tar.xz
Source4915:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdf14.doc.tar.xz
Source4917:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfcomment.tar.xz
Source4918:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfcomment.doc.tar.xz
Source4919:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfcprot.tar.xz
Source4920:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfcprot.doc.tar.xz
Source4922:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfmarginpar.tar.xz
Source4923:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfmarginpar.doc.tar.xz
Source4924:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfpagediff.tar.xz
Source4925:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfpagediff.doc.tar.xz
Source4926:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfscreen.tar.xz
Source4927:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfscreen.doc.tar.xz
Source4928:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfslide.tar.xz
Source4929:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfslide.doc.tar.xz
Source4930:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfsync.tar.xz
Source4931:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfsync.doc.tar.xz
Source4932:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfwin.tar.xz
Source4933:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfwin.doc.tar.xz
Source4934:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfx.tar.xz
Source4935:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfx.doc.tar.xz
Source4937:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pecha.tar.xz
Source4938:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pecha.doc.tar.xz
Source4942:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/permute.tar.xz
Source4943:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/permute.doc.tar.xz
Source4945:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/petiteannonce.tar.xz
Source4946:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/petiteannonce.doc.tar.xz
Source4947:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/philex.tar.xz
Source4948:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/philex.doc.tar.xz
Source4949:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/photo.tar.xz
Source4950:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/photo.doc.tar.xz
Source4952:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/piff.tar.xz
Source4953:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/piff.doc.tar.xz
Source4954:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pkgloader.tar.xz
Source4955:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pkgloader.doc.tar.xz
Source4956:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plantslabels.tar.xz
Source4957:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plantslabels.doc.tar.xz
Source4958:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plates.tar.xz
Source4959:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plates.doc.tar.xz
Source4960:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plweb.tar.xz
Source4961:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plweb.doc.tar.xz
Source4963:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polynom.tar.xz
Source4964:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polynom.doc.tar.xz
Source4966:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polynomial.tar.xz
Source4967:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polynomial.doc.tar.xz
Source4969:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polytable.tar.xz
Source4970:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polytable.doc.tar.xz
Source4972:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/postcards.tar.xz
Source4973:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/postcards.doc.tar.xz
Source4974:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poster-mac.tar.xz
Source4975:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poster-mac.doc.tar.xz
Source4976:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ppr-prv.tar.xz
Source4977:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ppr-prv.doc.tar.xz
Source5812:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/placeat.tar.xz
Source5813:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/placeat.doc.tar.xz
Source5884:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/perfectcut.tar.xz
Source5885:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/perfectcut.doc.tar.xz
Source6001:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/piechartmp.tar.xz
Source6002:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/piechartmp.doc.tar.xz
Source6053:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/piano.tar.xz
Source6054:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/piano.doc.tar.xz
Source6099:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pitex.tar.xz
Source6100:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pitex.doc.tar.xz
Source6101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/placeins-plain.tar.xz
Source6102:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plipsum.tar.xz
Source6103:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plipsum.doc.tar.xz
Source6104:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plnfss.tar.xz
Source6105:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plnfss.doc.tar.xz
Source6106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plstmary.tar.xz
Source6107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plstmary.doc.tar.xz
Source6124:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdftricks.tar.xz
Source6125:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdftricks.doc.tar.xz
Source6126:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdftricks2.tar.xz
Source6127:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdftricks2.doc.tar.xz
Source6471:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/philosophersimprint.tar.xz
Source6472:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/philosophersimprint.doc.tar.xz
Source6474:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pittetd.tar.xz
Source6475:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pittetd.doc.tar.xz
Source6477:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pkuthss.tar.xz
Source6478:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pkuthss.doc.tar.xz
Source6479:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/powerdot-FUBerlin.tar.xz
Source6480:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/powerdot-FUBerlin.doc.tar.xz
Source6707:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/physics.tar.xz
Source6708:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/physics.doc.tar.xz
Source6762:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/philokalia.tar.xz
Source6763:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/philokalia.doc.tar.xz
Source6765:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polyglossia.tar.xz
Source6766:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polyglossia.doc.tar.xz
Source7470:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parades.tar.xz
Source7471:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/parades.doc.tar.xz
Source7473:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pbibtex-base.tar.xz
Source7474:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pbibtex-base.doc.tar.xz
Source7478:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfornament.tar.xz
Source7479:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfornament.doc.tar.xz
Source7480:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-spectra.tar.xz
Source7481:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgf-spectra.doc.tar.xz
Source7482:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/platex.tar.xz
Source7483:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/platex.doc.tar.xz
Source7888:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/padauk.tar.xz
Source7889:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/padauk.doc.tar.xz
Source7892:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfreview.tar.xz
Source7893:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfreview.doc.tar.xz
Source7894:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phffullpagefigure.tar.xz
Source7895:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phffullpagefigure.doc.tar.xz
Source7896:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfnote.tar.xz
Source7897:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfnote.doc.tar.xz
Source7898:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfparen.tar.xz
Source7899:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfparen.doc.tar.xz
Source7900:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfqit.tar.xz
Source7901:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfqit.doc.tar.xz
Source7902:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfquotetext.tar.xz
Source7903:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfquotetext.doc.tar.xz
Source7904:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfsvnwatermark.tar.xz
Source7905:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfsvnwatermark.doc.tar.xz
Source7906:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfthm.tar.xz
Source7907:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phfthm.doc.tar.xz
Source7908:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phonenumbers.tar.xz
Source7909:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/phonenumbers.doc.tar.xz
Source7910:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/platex-tools.tar.xz
Source7911:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/platex-tools.doc.tar.xz
Source7912:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/platexcheat.doc.tar.xz
Source7913:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poetry.tar.xz
Source7914:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/poetry.doc.tar.xz
Source8254:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/padcount.tar.xz
Source8255:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/padcount.doc.tar.xz
Source8256:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfoverlay.tar.xz
Source8257:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfoverlay.doc.tar.xz
Source8258:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfpc-movie.tar.xz
Source8259:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfpc-movie.doc.tar.xz
Source8260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfprivacy.tar.xz
Source8261:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfprivacy.doc.tar.xz
Source8262:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/penrose.tar.xz
Source8263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/penrose.doc.tar.xz
Source8264:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfornament-han.tar.xz
Source8265:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pgfornament-han.doc.tar.xz
Source8266:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pixelart.tar.xz
Source8267:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pixelart.doc.tar.xz
Source8268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plantuml.tar.xz
Source8269:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plantuml.doc.tar.xz
Source8270:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plex.tar.xz
Source8271:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plex.doc.tar.xz
Source8272:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plex-otf.tar.xz
Source8273:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/plex-otf.doc.tar.xz
Source8274:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pm-isomath.tar.xz
Source8275:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pm-isomath.doc.tar.xz
Source8276:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polexpr.tar.xz
Source8277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/polexpr.doc.tar.xz
Source8278:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/postage.tar.xz
Source8279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/postage.doc.tar.xz
Source8280:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/powerdot-tuliplab.tar.xz
Source8281:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/powerdot-tuliplab.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-pslatex
Provides:       tex-pslatex = %{tl_version}
License:        LPPL
Summary:        Use PostScript fonts by default
Version:        svn16416.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pcrr8rn.map) = %{tl_version}, tex(pcrr7tn.tfm) = %{tl_version}
Provides:       tex(pcrr8rn.tfm) = %{tl_version}, tex(pcrr8tn.tfm) = %{tl_version}
Provides:       tex(pcrr7tn.vf) = %{tl_version}, tex(pcrr8tn.vf) = %{tl_version}
Provides:       tex(pslatex.sty) = %{tl_version}

%description -n texlive-pslatex
A small package that makes LaTeX default to 'standard'
PostScript fonts. It is basically a merger of the times and the
(obsolete) mathptm packages from the psnfss suite. You must
have installed standard LaTeX and the psnfss PostScript fonts
to use this package. The main novel feature is that the pslatex
package tries to compensate for the visual differences between
the Adobe fonts by scaling Helvetica by 90%, and 'condensing'
Courier (i.e. scaling horizontally) by 85%. The package is
supplied with a (unix) shell file for a 'pslatex' command that
allows standard LaTeX documents to be processed, without
needing to edit the file. Note that current psnfss uses a
different technique for scaling Helvetica, and treats Courier
as a lost cause (there are better free fixed-width available
now, than there were when pslatex was designed). As a result,
pslatex is widely considered obsolete.

%package -n texlive-psnfss
Provides:       tex-psnfss = %{tl_version}
License:        LPPL
Summary:        Font support for common PostScript fonts
Version:        svn33946.9.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-graphics, tex(keyval.sty)
Provides:       tex(charter.map) = %{tl_version}, tex(fpls.map) = %{tl_version}
Provides:       tex(pazo.map) = %{tl_version}, tex(psnfss.map) = %{tl_version}
Provides:       tex(utopia.map) = %{tl_version}, tex(8rbch.fd) = %{tl_version}
Provides:       tex(8rpag.fd) = %{tl_version}, tex(8rpbk.fd) = %{tl_version}
Provides:       tex(8rpcr.fd) = %{tl_version}, tex(8rphv.fd) = %{tl_version}
Provides:       tex(8rpnc.fd) = %{tl_version}, tex(8rppl.fd) = %{tl_version}
Provides:       tex(8rptm.fd) = %{tl_version}, tex(8rput.fd) = %{tl_version}
Provides:       tex(8rpzc.fd) = %{tl_version}, tex(avant.sty) = %{tl_version}
Provides:       tex(bookman.sty) = %{tl_version}, tex(chancery.sty) = %{tl_version}
Provides:       tex(charter.sty) = %{tl_version}, tex(courier.sty) = %{tl_version}
Provides:       tex(helvet.sty) = %{tl_version}, tex(mathpazo.sty) = %{tl_version}
Provides:       tex(mathpple.sty) = %{tl_version}, tex(mathptm.sty) = %{tl_version}
Provides:       tex(mathptmx.sty) = %{tl_version}, tex(newcent.sty) = %{tl_version}
Provides:       tex(omlbch.fd) = %{tl_version}, tex(omlpag.fd) = %{tl_version}
Provides:       tex(omlpbk.fd) = %{tl_version}, tex(omlpcr.fd) = %{tl_version}
Provides:       tex(omlphv.fd) = %{tl_version}, tex(omlpnc.fd) = %{tl_version}
Provides:       tex(omlppl.fd) = %{tl_version}, tex(omlptm.fd) = %{tl_version}
Provides:       tex(omlptmcm.fd) = %{tl_version}, tex(omlput.fd) = %{tl_version}
Provides:       tex(omlpzc.fd) = %{tl_version}, tex(omlzplm.fd) = %{tl_version}
Provides:       tex(omlzpple.fd) = %{tl_version}, tex(omlztmcm.fd) = %{tl_version}
Provides:       tex(omsbch.fd) = %{tl_version}, tex(omspag.fd) = %{tl_version}
Provides:       tex(omspbk.fd) = %{tl_version}, tex(omspcr.fd) = %{tl_version}
Provides:       tex(omsphv.fd) = %{tl_version}, tex(omspnc.fd) = %{tl_version}
Provides:       tex(omsppl.fd) = %{tl_version}, tex(omsptm.fd) = %{tl_version}
Provides:       tex(omsput.fd) = %{tl_version}, tex(omspzc.fd) = %{tl_version}
Provides:       tex(omspzccm.fd) = %{tl_version}, tex(omszplm.fd) = %{tl_version}
Provides:       tex(omszpple.fd) = %{tl_version}, tex(omsztmcm.fd) = %{tl_version}
Provides:       tex(omxpsycm.fd) = %{tl_version}, tex(omxzplm.fd) = %{tl_version}
Provides:       tex(omxzpple.fd) = %{tl_version}, tex(omxztmcm.fd) = %{tl_version}
Provides:       tex(ot1bch.fd) = %{tl_version}, tex(ot1pag.fd) = %{tl_version}
Provides:       tex(ot1pbk.fd) = %{tl_version}, tex(ot1pcr.fd) = %{tl_version}
Provides:       tex(ot1phv.fd) = %{tl_version}, tex(ot1pnc.fd) = %{tl_version}
Provides:       tex(ot1ppl.fd) = %{tl_version}, tex(ot1pplj.fd) = %{tl_version}
Provides:       tex(ot1pplx.fd) = %{tl_version}, tex(ot1ptm.fd) = %{tl_version}
Provides:       tex(ot1ptmcm.fd) = %{tl_version}, tex(ot1put.fd) = %{tl_version}
Provides:       tex(ot1pzc.fd) = %{tl_version}, tex(ot1zplm.fd) = %{tl_version}
Provides:       tex(ot1zpple.fd) = %{tl_version}, tex(ot1ztmcm.fd) = %{tl_version}
Provides:       tex(palatino.sty) = %{tl_version}, tex(pifont.sty) = %{tl_version}
Provides:       tex(t1bch.fd) = %{tl_version}, tex(t1pag.fd) = %{tl_version}
Provides:       tex(t1pbk.fd) = %{tl_version}, tex(t1pcr.fd) = %{tl_version}
Provides:       tex(t1phv.fd) = %{tl_version}, tex(t1pnc.fd) = %{tl_version}
Provides:       tex(t1ppl.fd) = %{tl_version}, tex(t1pplj.fd) = %{tl_version}
Provides:       tex(t1pplx.fd) = %{tl_version}, tex(t1ptm.fd) = %{tl_version}
Provides:       tex(t1put.fd) = %{tl_version}, tex(t1pzc.fd) = %{tl_version}
Provides:       tex(times.sty) = %{tl_version}, tex(ts1bch.fd) = %{tl_version}
Provides:       tex(ts1pag.fd) = %{tl_version}, tex(ts1pbk.fd) = %{tl_version}
Provides:       tex(ts1pcr.fd) = %{tl_version}, tex(ts1phv.fd) = %{tl_version}
Provides:       tex(ts1pnc.fd) = %{tl_version}, tex(ts1ppl.fd) = %{tl_version}
Provides:       tex(ts1pplj.fd) = %{tl_version}, tex(ts1pplx.fd) = %{tl_version}
Provides:       tex(ts1ptm.fd) = %{tl_version}, tex(ts1put.fd) = %{tl_version}
Provides:       tex(ts1pzc.fd) = %{tl_version}, tex(ufplm.fd) = %{tl_version}
Provides:       tex(ufplmbb.fd) = %{tl_version}, tex(upsy.fd) = %{tl_version}
Provides:       tex(upzd.fd) = %{tl_version}, tex(utopia.sty) = %{tl_version}

%description -n texlive-psnfss
Font definition files, macros and font metrics for freely-
available Adobe Type 1 fonts. The font set consists of the
'LaserWriter 35' set (originally 'freely available' because
embedded in PostScript printers), and a variety of other free
fonts, together with some additions. Note that while many of
the fonts are available in PostScript (and other) printers,
most publishers require fonts embedded in documents, which
requires that you have the fonts in your TeX system.
Fortunately, there are free versions of the fonts from URW
(available in the URW base5 bundle). The base set of text fonts
covered by PSNFSS are: AvantGarde, Bookman, Courier, Helvetica,
New Century Schoolbook, Palatino, Symbol, Times Roman and Zapf
Dingbats. In addition, the fonts Bitstream Charter and Adobe
Utopia are covered (those fonts were contributed to the Public
Domain by their commercial foundries). Separate packages are
provided to load each font for use as main text font. The
packages helvet (which allows Helvetica to be loaded with its
size scaled to something more nearly appropriate for its use as
a Sans-Serif font to match Times) and pifont (which provides
the means to select single glyphs from symbol fonts) are
tailored to special requirements of their fonts. Mathematics
are covered by the mathptmx package, which constructs passable
mathematics from a combination of Times Roman, Symbol and some
glyphs from Computer Modern, and by Pazo Math (optionally
extended with the fpl small-caps and old-style figures fonts)
which uses Palatino as base font, with the mathpazo fonts. The
bundle as a whole is part of the LaTeX 'required' set of
packages.

%package -n texlive-psnfss-doc
Summary:        Documentation for psnfss
Version:        svn33946.9.2a

Provides:       tex-psnfss-doc
AutoReqProv:    No
Requires:       tex-graphics-doc

%description -n texlive-psnfss-doc
Documentation for psnfss

%package -n texlive-pspicture
Provides:       tex-pspicture = %{tl_version}
License:        LPPL
Summary:        PostScript picture support
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pspicture.sty) = %{tl_version}

%description -n texlive-pspicture
A replacement for LaTeX's picture macros, that uses PostScript
\special commands. The package is now largely superseded by
pict2e.

%package -n texlive-pspicture-doc
Summary:        Documentation for pspicture
Version:        svn15878.0

Provides:       tex-pspicture-doc
AutoReqProv:    No

%description -n texlive-pspicture-doc
Documentation for pspicture

%package -n texlive-plain
Provides:       tex-plain = %{tl_version}
License:        Knuth
Summary:        The Plain TeX format
Version:        svn43076
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(fontchart.tex) = %{tl_version}, tex(gkpmac.tex) = %{tl_version}
Provides:       tex(letter.tex) = %{tl_version}, tex(list.tex) = %{tl_version}
Provides:       tex(llist.tex) = %{tl_version}, tex(mptmac.tex) = %{tl_version}
Provides:       tex(picmac.tex) = %{tl_version}, tex(plain.tex) = %{tl_version}
Provides:       tex(wlist.tex) = %{tl_version}, tex(pdftexmagfix.tex) = %{tl_version}
Provides:       tex(unicode-letters.def) = %{tl_version}

%description -n texlive-plain
Contains files used to build the Plain TeX format, as described
in the TeXbook, together with various supporting files (some
also discussed in the book).

%package -n texlive-pgf
Provides:       tex-pgf = %{tl_version}
License:        LPPL 1.3
Summary:        Create PostScript and PDF graphics in TeX
Version:        svn44231
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-xkeyval, tex(pgfcomp-version-0-65.sty)
Requires:       tex(pgfcore.sty), tex(graphicx.sty), tex(keyval.sty), tex(xcolor.sty)
Provides:       tex(t-pgf.tex) = %{tl_version}, tex(t-pgfbim.tex) = %{tl_version}
Provides:       tex(t-pgfbla.tex) = %{tl_version}, tex(t-pgfbma.tex) = %{tl_version}
Provides:       tex(t-pgfbpl.tex) = %{tl_version}, tex(t-pgfbpt.tex) = %{tl_version}
Provides:       tex(t-pgfbsh.tex) = %{tl_version}, tex(t-pgfbsn.tex) = %{tl_version}
Provides:       tex(t-pgfcor.tex) = %{tl_version}, tex(t-tikz.tex) = %{tl_version}
Provides:       tex(t-pgfmat.tex) = %{tl_version}, tex(t-pgfsys.tex) = %{tl_version}
Provides:       tex(t-pgfcal.tex) = %{tl_version}, tex(t-pgffor.tex) = %{tl_version}
Provides:       tex(t-pgfkey.tex) = %{tl_version}, tex(t-pgfmod.tex) = %{tl_version}
Provides:       tex(t-pgfrcs.tex) = %{tl_version}, tex(pgfcore.code.tex) = %{tl_version}
Provides:       tex(pgfcorearrows.code.tex) = %{tl_version}
Provides:       tex(pgfcoreexternal.code.tex) = %{tl_version}
Provides:       tex(pgfcoregraphicstate.code.tex) = %{tl_version}
Provides:       tex(pgfcoreimage.code.tex) = %{tl_version}
Provides:       tex(pgfcorelayers.code.tex) = %{tl_version}
Provides:       tex(pgfcoreobjects.code.tex) = %{tl_version}
Provides:       tex(pgfcorepathconstruct.code.tex) = %{tl_version}
Provides:       tex(pgfcorepathprocessing.code.tex) = %{tl_version}
Provides:       tex(pgfcorepathusage.code.tex) = %{tl_version}
Provides:       tex(pgfcorepatterns.code.tex) = %{tl_version}
Provides:       tex(pgfcorepoints.code.tex) = %{tl_version}
Provides:       tex(pgfcorequick.code.tex) = %{tl_version}
Provides:       tex(pgfcorescopes.code.tex) = %{tl_version}
Provides:       tex(pgfcoreshade.code.tex) = %{tl_version}
Provides:       tex(pgfcoretransformations.code.tex) = %{tl_version}
Provides:       tex(pgfcoretransparency.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.ee.IEC.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.ee.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.logic.CDH.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.logic.IEC.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.logic.US.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycircuits.logic.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.3d.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.barcharts.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.formats.functions.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.polar.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydatavisualization.sparklines.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarygraphs.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarygraphs.standard.code.tex) = %{tl_version}
Provides:       tex(tikzexternalshared.code.tex) = %{tl_version}
Provides:       tex(tikzlibrary3d.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryangles.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryarrows.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryautomata.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarybabel.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarybackgrounds.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarybending.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycalc.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarycalendar.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarychains.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.footprints.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.fractals.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.markings.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.pathmorphing.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.pathreplacing.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.shapes.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.text.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryer.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfadings.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfit.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfixedpointarithmetic.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfolding.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfpu.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryintersections.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarylindenmayersystems.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarymath.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarymatrix.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarymindmap.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypatterns.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypatterns.meta.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypetri.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryplothandlers.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryplotmarks.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypositioning.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryquotes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryscopes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshadings.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshadows.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.arrows.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.callouts.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.gates.logic.IEC.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.gates.logic.US.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.geometric.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.misc.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.multipart.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryshapes.symbols.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarysnakes.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryspy.code.tex) = %{tl_version}

Provides:       tex(tikzlibrarysvg.path.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarythrough.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytopaths.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarytrees.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryturtle.code.tex) = %{tl_version}
Provides:       tex(tikz.code.tex) = %{tl_version}, tex(pgflibrarygraphdrawing.circular.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.examples.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.force.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.layered.code.tex) = %{tl_version}
Provides:       tex(pgflibrarygraphdrawing.trees.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarygraphdrawing.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydatavisualization.barcharts.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydatavisualization.formats.functions.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydatavisualization.polar.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.footprints.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.fractals.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.markings.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.pathmorphing.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.pathreplacing.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.shapes.code.tex) = %{tl_version}
Provides:       tex(pgflibrarydecorations.text.code.tex) = %{tl_version}
Provides:       tex(pgflibraryluamath.code.tex) = %{tl_version}
Provides:       tex(pgflibraryarrows.code.tex) = %{tl_version}
Provides:       tex(pgflibraryarrows.meta.code.tex) = %{tl_version}
Provides:       tex(pgflibraryarrows.spaced.code.tex) = %{tl_version}
Provides:       tex(pgflibrarycurvilinear.code.tex) = %{tl_version}
Provides:       tex(pgflibraryfadings.code.tex) = %{tl_version}
Provides:       tex(pgflibraryfixedpointarithmetic.code.tex) = %{tl_version}
Provides:       tex(pgflibraryfpu.code.tex) = %{tl_version}
Provides:       tex(pgflibraryintersections.code.tex) = %{tl_version}
Provides:       tex(pgflibrarylindenmayersystems.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypatterns.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypatterns.meta.code.tex) = %{tl_version}
Provides:       tex(pgflibraryplothandlers.code.tex) = %{tl_version}
Provides:       tex(pgflibraryplotmarks.code.tex) = %{tl_version}
Provides:       tex(pgflibraryprofiler.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshadings.code.tex) = %{tl_version}
Provides:       tex(pgflibrarysnakes.code.tex) = %{tl_version}
Provides:       tex(pgflibrarysvg.path.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.ee.IEC.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.ee.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.logic.IEC.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.logic.US.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.gates.logic.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.arrows.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.callouts.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.misc.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.geometric.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.misc.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.geometric.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.misc.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.multipart.code.tex) = %{tl_version}
Provides:       tex(pgflibraryshapes.symbols.code.tex) = %{tl_version}
Provides:       tex(pgfmath.code.tex) = %{tl_version}, tex(pgfmathcalc.code.tex) = %{tl_version}
Provides:       tex(pgfmathfloat.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.base.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.basic.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.comparison.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.integerarithmetics.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.misc.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.random.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.round.code.tex) = %{tl_version}
Provides:       tex(pgfmathfunctions.trigonometric.code.tex) = %{tl_version}
Provides:       tex(pgfmathode.code.tex) = %{tl_version}
Provides:       tex(pgfmathparser.code.tex) = %{tl_version}
Provides:       tex(pgfmathutil.code.tex) = %{tl_version}
Provides:       tex(pgfmodulebending.code.tex) = %{tl_version}
Provides:       tex(pgfmoduledatavisualization.code.tex) = %{tl_version}
Provides:       tex(pgfmoduledecorations.code.tex) = %{tl_version}
Provides:       tex(pgfmodulematrix.code.tex) = %{tl_version}
Provides:       tex(pgfmodulenonlineartransformations.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleoo.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleparser.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleplot.code.tex) = %{tl_version}
Provides:       tex(pgfmoduleshapes.code.tex) = %{tl_version}
Provides:       tex(pgfmodulesnakes.code.tex) = %{tl_version}
Provides:       tex(pgfmodulesorting.code.tex) = %{tl_version}
Provides:       tex(pgf.cfg) = %{tl_version}, tex(pgfsys-common-pdf-via-dvi.def) = %{tl_version}
Provides:       tex(pgfsys-common-pdf.def) = %{tl_version}
Provides:       tex(pgfsys-common-postscript.def) = %{tl_version}
Provides:       tex(pgfsys-common-svg.def) = %{tl_version}
Provides:       tex(pgfsys-dvi.def) = %{tl_version}, tex(pgfsys-dvipdfm.def) = %{tl_version}
Provides:       tex(pgfsys-dvipdfmx.def) = %{tl_version}
Provides:       tex(pgfsys-dvips.def) = %{tl_version}, tex(pgfsys-dvisvgm.def) = %{tl_version}
Provides:       tex(pgfsys-pdftex.def) = %{tl_version}, tex(pgfsys-tex4ht.def) = %{tl_version}
Provides:       tex(pgfsys-textures.def) = %{tl_version}
Provides:       tex(pgfsys-vtex.def) = %{tl_version}, tex(pgfsys-xetex.def) = %{tl_version}
Provides:       tex(pgfsys.code.tex) = %{tl_version}, tex(pgfsysprotocol.code.tex) = %{tl_version}
Provides:       tex(pgfsyssoftpath.code.tex) = %{tl_version}
Provides:       tex(pgfcalendar.code.tex) = %{tl_version}
Provides:       tex(pgfexternal.tex) = %{tl_version}, tex(pgfexternalwithdepth.tex) = %{tl_version}
Provides:       tex(pgffor.code.tex) = %{tl_version}, tex(pgfkeys.code.tex) = %{tl_version}
Provides:       tex(pgfkeysfiltered.code.tex) = %{tl_version}
Provides:       tex(pgfrcs.code.tex) = %{tl_version}, tex(pgfutil-common-lists.tex) = %{tl_version}
Provides:       tex(pgfutil-common.tex) = %{tl_version}, tex(pgfutil-context.def) = %{tl_version}
Provides:       tex(pgfutil-latex.def) = %{tl_version}, tex(pgfutil-plain.def) = %{tl_version}
Provides:       tex(pgf.sty) = %{tl_version}, tex(pgfbaseimage.sty) = %{tl_version}
Provides:       tex(pgfbaselayers.sty) = %{tl_version}, tex(pgfbasematrix.sty) = %{tl_version}
Provides:       tex(pgfbasepatterns.sty) = %{tl_version}
Provides:       tex(pgfbaseplot.sty) = %{tl_version}, tex(pgfbaseshapes.sty) = %{tl_version}
Provides:       tex(pgfbasesnakes.sty) = %{tl_version}, tex(pgfcore.sty) = %{tl_version}
Provides:       tex(pgfarrows.sty) = %{tl_version}, tex(pgfautomata.sty) = %{tl_version}
Provides:       tex(pgfcomp-version-0-65.sty) = %{tl_version}
Provides:       tex(pgfcomp-version-1-18.sty) = %{tl_version}
Provides:       tex(pgfheaps.sty) = %{tl_version}, tex(pgflibraryarrows.sty) = %{tl_version}
Provides:       tex(pgflibraryautomata.sty) = %{tl_version}
Provides:       tex(pgflibraryplothandlers.sty) = %{tl_version}
Provides:       tex(pgflibraryplotmarks.sty) = %{tl_version}
Provides:       tex(pgflibraryshapes.sty) = %{tl_version}
Provides:       tex(pgflibrarysnakes.sty) = %{tl_version}
Provides:       tex(pgflibrarytikzbackgrounds.sty) = %{tl_version}
Provides:       tex(pgflibrarytikztrees.sty) = %{tl_version}
Provides:       tex(pgfnodes.sty) = %{tl_version}, tex(pgfshade.sty) = %{tl_version}
Provides:       tex(pgfmanual.code.tex) = %{tl_version}, tex(pgfmanual.pdflinks.code.tex) = %{tl_version}
Provides:       tex(pgfmanual.prettyprinter.code.tex) = %{tl_version}
Provides:       tex(pgfmanual.sty) = %{tl_version}, tex(tikzlibraryexternal.code.tex) = %{tl_version}
Provides:       tex(pgfpict2e.sty) = %{tl_version}, tex(tikz.sty) = %{tl_version}
Provides:       tex(pgfmath.sty) = %{tl_version}, tex(pgfsys.sty) = %{tl_version}
Provides:       tex(pgfcalendar.sty) = %{tl_version}, tex(pgffor.sty) = %{tl_version}
Provides:       tex(pgfkeys.sty) = %{tl_version}, tex(pgfpages.sty) = %{tl_version}
Provides:       tex(pgfrcs.sty) = %{tl_version}, tex(tikzexternal.sty) = %{tl_version}
Provides:       tex(xxcolor.sty) = %{tl_version}, tex(pgf.tex) = %{tl_version}
Provides:       tex(pgfbaseimage.tex) = %{tl_version}, tex(pgfbaselayers.tex) = %{tl_version}
Provides:       tex(pgfbasematrix.tex) = %{tl_version}, tex(pgfbasepatterns.tex) = %{tl_version}
Provides:       tex(pgfbaseplot.tex) = %{tl_version}, tex(pgfbaseshapes.tex) = %{tl_version}
Provides:       tex(pgfbasesnakes.tex) = %{tl_version}, tex(pgfcore.tex) = %{tl_version}
Provides:       tex(tikz.tex) = %{tl_version}, tex(pgfmath.tex) = %{tl_version}
Provides:       tex(pgfsys.tex) = %{tl_version}, tex(pgfcalendar.tex) = %{tl_version}
Provides:       tex(pgffor.tex) = %{tl_version}, tex(pgfkeys.tex) = %{tl_version}
Provides:       tex(pgfrcs.tex) = %{tl_version}

%description -n texlive-pgf
PGF is a macro package for creating graphics. It is platform-
and format-independent and works together with the most
important TeX backend drivers, including pdfTeX and dvips. It
comes with a user-friendly syntax layer called TikZ. Its usage
is similar to pstricks and the standard picture environment.
PGF works with plain (pdf-)TeX, (pdf-)LaTeX, and ConTeXt.
Unlike pstricks, it can produce either PostScript or PDF
output.

%package -n texlive-pgf-doc
Summary:        Documentation for pgf
Version:        svn44231
Provides:       tex-pgf-doc
AutoReqProv:    No
Requires:       tex-xkeyval-doc

%description -n texlive-pgf-doc
Documentation for pgf

%package -n texlive-perception
Provides:       tex-perception = %{tl_version}
License:        LPPL
Summary:        BibTeX style for the journal Perception
Version:        svn42683
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-perception
A product of custom-bib, provided simply to save others' time.

%package -n texlive-perception-doc
Summary:        Documentation for perception
Version:        svn42683
Provides:       tex-perception-doc
AutoReqProv:    No

%description -n texlive-perception-doc
Documentation for perception

%package -n texlive-pnas2009
Provides:       tex-pnas2009 = %{tl_version}
License:        Bibtex
Summary:        Bibtex style for PNAS
Version:        svn16287.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-pnas2009
This style produces bibliographies in the format of
"Proceedings of the National Academy of Sciences, USA". The
style was derived from the standard unsrt.bst and adapted to
the new (2009) formatting rules.

%package -n texlive-pacioli
Provides:       tex-pacioli = %{tl_version}
License:        LPPL
Summary:        Fonts designed by Fra Luca de Pacioli in 1497
Version:        svn24947.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cpcr10.tfm) = %{tl_version}, tex(cpcsl10.tfm) = %{tl_version}
Provides:       tex(ot1cpc.fd) = %{tl_version}, tex(pacioli.sty) = %{tl_version}
Provides:       tex(t1cpc.fd) = %{tl_version}

%description -n texlive-pacioli
Pacioli was a c.15 mathematician, and his font was designed
according to 'the divine proportion'. The font is uppercase
letters together with punctuation and some analphabetics; no
lowercase or digits. The Metafont source is distributed in a
.dtx file, together with LaTeX support.

%package -n texlive-pacioli-doc
Summary:        Documentation for pacioli
Version:        svn24947.0

Provides:       tex-pacioli-doc
AutoReqProv:    No

%description -n texlive-pacioli-doc
Documentation for pacioli

%package -n texlive-paratype
Provides:       tex-paratype = %{tl_version}
License:        LPPL
Summary:        LaTeX support for free fonts by ParaType
Version:        svn32859.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(keyval.sty)
Provides:       tex(ptmono_il2.enc) = %{tl_version}, tex(ptmono_ot1.enc) = %{tl_version}
Provides:       tex(ptmono_ot2.enc) = %{tl_version}, tex(ptmono_t1.enc) = %{tl_version}
Provides:       tex(ptmono_t2a.enc) = %{tl_version}, tex(ptmono_t2b.enc) = %{tl_version}
Provides:       tex(ptmono_t2c.enc) = %{tl_version}, tex(ptmono_ts1.enc) = %{tl_version}
Provides:       tex(ptmono_x2.enc) = %{tl_version}, tex(ptsans_il2.enc) = %{tl_version}
Provides:       tex(ptsans_ot1.enc) = %{tl_version}, tex(ptsans_ot2.enc) = %{tl_version}
Provides:       tex(ptsans_t1.enc) = %{tl_version}, tex(ptsans_t2a.enc) = %{tl_version}
Provides:       tex(ptsans_t2b.enc) = %{tl_version}, tex(ptsans_t2c.enc) = %{tl_version}
Provides:       tex(ptsans_ts1.enc) = %{tl_version}, tex(ptsans_x2.enc) = %{tl_version}
Provides:       tex(ptserif_il2.enc) = %{tl_version}, tex(ptserif_ot1.enc) = %{tl_version}
Provides:       tex(ptserif_ot2.enc) = %{tl_version}, tex(ptserif_t1.enc) = %{tl_version}
Provides:       tex(ptserif_t2a.enc) = %{tl_version}, tex(ptserif_t2b.enc) = %{tl_version}
Provides:       tex(ptserif_t2c.enc) = %{tl_version}, tex(ptserif_ts1.enc) = %{tl_version}
Provides:       tex(ptserif_x2.enc) = %{tl_version}, tex(paratype-truetype.map) = %{tl_version}
Provides:       tex(paratype-type1.map) = %{tl_version}, tex(PTMono-Bold-tlf-il2--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-il2--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(PTM55F.ttf) = %{tl_version}, tex(PTM75F.ttf) = %{tl_version}
Provides:       tex(PTC55F.ttf) = %{tl_version}, tex(PTC75F.ttf) = %{tl_version}
Provides:       tex(PTN57F.ttf) = %{tl_version}, tex(PTN77F.ttf) = %{tl_version}
Provides:       tex(PTS55F.ttf) = %{tl_version}, tex(PTS56F.ttf) = %{tl_version}
Provides:       tex(PTS75F.ttf) = %{tl_version}, tex(PTS76F.ttf) = %{tl_version}
Provides:       tex(PTF55F.ttf) = %{tl_version}, tex(PTF56F.ttf) = %{tl_version}
Provides:       tex(PTF75F.ttf) = %{tl_version}, tex(PTF76F.ttf) = %{tl_version}
Provides:       tex(PTZ55F.ttf) = %{tl_version}, tex(PTZ56F.ttf) = %{tl_version}
Provides:       tex(PTM55F.pfb) = %{tl_version}, tex(PTM75F.pfb) = %{tl_version}
Provides:       tex(PTC55F.pfb) = %{tl_version}, tex(PTC75F.pfb) = %{tl_version}
Provides:       tex(PTN57F.pfb) = %{tl_version}, tex(PTN77F.pfb) = %{tl_version}
Provides:       tex(PTS55F.pfb) = %{tl_version}, tex(PTS56F.pfb) = %{tl_version}
Provides:       tex(PTS75F.pfb) = %{tl_version}, tex(PTS76F.pfb) = %{tl_version}
Provides:       tex(PTF55F.pfb) = %{tl_version}, tex(PTF56F.pfb) = %{tl_version}
Provides:       tex(PTF75F.pfb) = %{tl_version}, tex(PTF76F.pfb) = %{tl_version}
Provides:       tex(PTZ55F.pfb) = %{tl_version}, tex(PTZ56F.pfb) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-il2.vf) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTMono-Bold-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTMono-BoldSlanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-il2.vf) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-ot1.vf) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTMono-Regular-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTMono-Slanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-Bold-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-BoldItalic-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-Caption-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBold-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-CaptionSlanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-Italic-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-Narrow-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBold-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-NarrowSlanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSans-Regular-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-Bold-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldItalic-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldSlanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-BoldUprightItalic-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-Caption-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionItalic-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionSlanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-Italic-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-Regular-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-Slanted-tlf-x2.vf) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2b.vf) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-t2c.vf) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(PTSerif-UprightItalic-tlf-x2.vf) = %{tl_version}
Provides:       tex(IL2PTMono-TLF.fd) = %{tl_version}, tex(IL2PTSans-TLF.fd) = %{tl_version}
Provides:       tex(IL2PTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(IL2PTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(IL2PTSerif-TLF.fd) = %{tl_version}, tex(IL2PTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(OT1PTMono-TLF.fd) = %{tl_version}, tex(OT1PTSans-TLF.fd) = %{tl_version}
Provides:       tex(OT1PTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(OT1PTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(OT1PTSerif-TLF.fd) = %{tl_version}, tex(OT1PTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(OT2PTMono-TLF.fd) = %{tl_version}, tex(OT2PTSans-TLF.fd) = %{tl_version}
Provides:       tex(OT2PTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(OT2PTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(OT2PTSerif-TLF.fd) = %{tl_version}, tex(OT2PTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(PTMono.sty) = %{tl_version}, tex(PTSans.sty) = %{tl_version}
Provides:       tex(PTSansCaption.sty) = %{tl_version}, tex(PTSansNarrow.sty) = %{tl_version}
Provides:       tex(PTSerif.sty) = %{tl_version}, tex(PTSerifCaption.sty) = %{tl_version}
Provides:       tex(T1PTMono-TLF.fd) = %{tl_version}, tex(T1PTSans-TLF.fd) = %{tl_version}
Provides:       tex(T1PTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(T1PTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(T1PTSerif-TLF.fd) = %{tl_version}, tex(T1PTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(T2APTMono-TLF.fd) = %{tl_version}, tex(T2APTSans-TLF.fd) = %{tl_version}
Provides:       tex(T2APTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(T2APTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(T2APTSerif-TLF.fd) = %{tl_version}, tex(T2APTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(T2BPTMono-TLF.fd) = %{tl_version}, tex(T2BPTSans-TLF.fd) = %{tl_version}
Provides:       tex(T2BPTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(T2BPTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(T2BPTSerif-TLF.fd) = %{tl_version}, tex(T2BPTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(T2CPTMono-TLF.fd) = %{tl_version}, tex(T2CPTSans-TLF.fd) = %{tl_version}
Provides:       tex(T2CPTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(T2CPTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(T2CPTSerif-TLF.fd) = %{tl_version}, tex(T2CPTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(TS1PTMono-TLF.fd) = %{tl_version}, tex(TS1PTSans-TLF.fd) = %{tl_version}
Provides:       tex(TS1PTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(TS1PTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(TS1PTSerif-TLF.fd) = %{tl_version}, tex(TS1PTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(X2PTMono-TLF.fd) = %{tl_version}, tex(X2PTSans-TLF.fd) = %{tl_version}
Provides:       tex(X2PTSansCaption-TLF.fd) = %{tl_version}
Provides:       tex(X2PTSansNarrow-TLF.fd) = %{tl_version}
Provides:       tex(X2PTSerif-TLF.fd) = %{tl_version}, tex(X2PTSerifCaption-TLF.fd) = %{tl_version}
Provides:       tex(paratype.sty) = %{tl_version}

%description -n texlive-paratype
The package offers LaTeX support for the fonts PT Sans, PT
Serif and PT Mono developed by ParaType for the project "Public
Types of Russian Federation", and released under an open user
license. The fonts themselves are provided in both the TrueType
and Type 1 formats, both created by ParaType). The fonts
provide encodings OT1, T1, IL2, TS1, T2* and X2. The package
provides a convenient replacement of the two packages ptsans
and ptserif.

%package -n texlive-paratype-doc
Summary:        Documentation for paratype
Version:        svn32859.0

Provides:       tex-paratype-doc
AutoReqProv:    No

%description -n texlive-paratype-doc
Documentation for paratype

%package -n texlive-phaistos
Provides:       tex-phaistos = %{tl_version}
License:        LPPL
Summary:        Disk of Phaistos font
Version:        svn18651.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(phaistos.map) = %{tl_version}, tex(Phaistos.otf) = %{tl_version}
Provides:       tex(phaistos.tfm) = %{tl_version}, tex(phaistos.pfb) = %{tl_version}
Provides:       tex(phaistos.sty) = %{tl_version}

%description -n texlive-phaistos
A font that contains all the symbols of the famous Disc of
Phaistos, together with a LaTeX package. The disc was 'printed'
by stamping the wet clay with some sort of punches, probably
around 1700 BCE. The font is available in Adobe Type 1 and
OpenType formats (the latter using the Unicode positions for
the symbols). There are those who believe that this Cretan
script was used to 'write' Greek (it is known, for example,
that the rather later Cretan Linear B script was used to write
Greek), but arguments for other languages have been presented.

%package -n texlive-phaistos-doc
Summary:        Documentation for phaistos
Version:        svn18651.1.0

Provides:       tex-phaistos-doc
AutoReqProv:    No

%description -n texlive-phaistos-doc
Documentation for phaistos

%package -n texlive-phonetic
Provides:       tex-phonetic = %{tl_version}
License:        LPPL
Summary:        Metafont Phonetic fonts, based on Computer Modern
Version:        svn21871.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmph10.tfm) = %{tl_version}, tex(cmph5.tfm) = %{tl_version}
Provides:       tex(cmph6.tfm) = %{tl_version}, tex(cmph7.tfm) = %{tl_version}
Provides:       tex(cmph8.tfm) = %{tl_version}, tex(cmph9.tfm) = %{tl_version}
Provides:       tex(cmphb10.tfm) = %{tl_version}, tex(cmphi10.tfm) = %{tl_version}
Provides:       tex(cmphi7.tfm) = %{tl_version}, tex(cmphi8.tfm) = %{tl_version}
Provides:       tex(cmphi9.tfm) = %{tl_version}, tex(Uphon.fd) = %{tl_version}
Provides:       tex(phonetic.sty) = %{tl_version}

%description -n texlive-phonetic
The fonts are based on Computer Modern, and specified in
Metafont. Macros for the fonts' use are provided, both for
LaTeX 2.09 and for current LaTeX.

%package -n texlive-phonetic-doc
Summary:        Documentation for phonetic
Version:        svn21871.0

Provides:       tex-phonetic-doc
AutoReqProv:    No

%description -n texlive-phonetic-doc
Documentation for phonetic

%package -n texlive-pigpen
Provides:       tex-pigpen = %{tl_version}
License:        LPPL
Summary:        A font for the pigpen (or masonic) cipher
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(pigpen.map) = %{tl_version}, tex(pigpen.tfm) = %{tl_version}
Provides:       tex(pigpen.pfa) = %{tl_version}, tex(pigpen.sty) = %{tl_version}
Provides:       tex(pigpen.tex) = %{tl_version}

%description -n texlive-pigpen
The Pigpen cipher package provides the font and the necessary
wrappers (style file, etc.) in order to write Pigpen ciphers, a
simple substitution cipher. The package provides a font
(available both as Metafont source, and as an Adobe Type 1
file), and macros for its use.

%package -n texlive-pigpen-doc
Summary:        Documentation for pigpen
Version:        svn15878.0.2

Provides:       tex-pigpen-doc
AutoReqProv:    No

%description -n texlive-pigpen-doc
Documentation for pigpen

%package -n texlive-playfair
Provides:       tex-playfair = %{tl_version}
License:        OFL
Summary:        Playfair Display fonts with LaTeX support
Version:        svn34236.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(plf_5ewtu2.enc) = %{tl_version}, tex(plf_6bqc7d.enc) = %{tl_version}
Provides:       tex(plf_723q3k.enc) = %{tl_version}, tex(plf_aehru5.enc) = %{tl_version}
Provides:       tex(plf_apfun2.enc) = %{tl_version}, tex(plf_c2cruh.enc) = %{tl_version}
Provides:       tex(plf_cgf2ku.enc) = %{tl_version}, tex(plf_ev34te.enc) = %{tl_version}
Provides:       tex(plf_ilriiw.enc) = %{tl_version}, tex(plf_j6ohis.enc) = %{tl_version}
Provides:       tex(plf_ouuek2.enc) = %{tl_version}, tex(plf_qjvs44.enc) = %{tl_version}
Provides:       tex(plf_rmgfzq.enc) = %{tl_version}, tex(plf_tcbmed.enc) = %{tl_version}
Provides:       tex(plf_tff5oq.enc) = %{tl_version}, tex(plf_ujy7vm.enc) = %{tl_version}
Provides:       tex(plf_vgw77z.enc) = %{tl_version}, tex(plf_vw64ij.enc) = %{tl_version}
Provides:       tex(plf_ybdqh4.enc) = %{tl_version}, tex(plf_zcb4ya.enc) = %{tl_version}
Provides:       tex(PlayfairDisplay.map) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black.otf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic.otf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold.otf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic.otf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic.otf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular.otf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black.pfb) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic.pfb) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold.pfb) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic.pfb) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic.pfb) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular.pfb) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BlackItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(PlayfairDisplay-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(LY1PlayfairDisplay-LF.fd) = %{tl_version}
Provides:       tex(LY1PlayfairDisplay-OsF.fd) = %{tl_version}
Provides:       tex(LY1PlayfairDisplay-Sup.fd) = %{tl_version}
Provides:       tex(OT1PlayfairDisplay-LF.fd) = %{tl_version}
Provides:       tex(OT1PlayfairDisplay-OsF.fd) = %{tl_version}
Provides:       tex(OT1PlayfairDisplay-Sup.fd) = %{tl_version}
Provides:       tex(PlayfairDisplay.sty) = %{tl_version}
Provides:       tex(T1PlayfairDisplay-LF.fd) = %{tl_version}
Provides:       tex(T1PlayfairDisplay-OsF.fd) = %{tl_version}
Provides:       tex(T1PlayfairDisplay-Sup.fd) = %{tl_version}
Provides:       tex(TS1PlayfairDisplay-LF.fd) = %{tl_version}
Provides:       tex(TS1PlayfairDisplay-OsF.fd) = %{tl_version}

%description -n texlive-playfair
Playfair Display is well suited for titling and headlines. It
has an extra large x-height and short descenders. It can be set
with no leading if space is tight, for instance in news
headlines, or for stylistic effect in titles. Capitals are
extra short, and only very slightly heavier than the lowercase
characters. This helps achieve a more even typographical colour
when typesetting proper nouns and initialisms.

%package -n texlive-playfair-doc
Summary:        Documentation for playfair
Version:        svn34236.0

Provides:       tex-playfair-doc
AutoReqProv:    No

%description -n texlive-playfair-doc
Documentation for playfair

%package -n texlive-poltawski
Provides:       tex-poltawski = %{tl_version}
License:        GFSL
Summary:        Antykwa Poltawskiego Family of Fonts
Version:        svn20075.1.101

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(ap-cs-sc.enc) = %{tl_version}, tex(ap-cs.enc) = %{tl_version}
Provides:       tex(ap-ec-sc.enc) = %{tl_version}, tex(ap-ec.enc) = %{tl_version}
Provides:       tex(ap-l7x-sc.enc) = %{tl_version}, tex(ap-l7x.enc) = %{tl_version}
Provides:       tex(ap-qx-sc.enc) = %{tl_version}, tex(ap-qx.enc) = %{tl_version}
Provides:       tex(ap-rm-sc.enc) = %{tl_version}, tex(ap-rm.enc) = %{tl_version}
Provides:       tex(ap-t5-sc.enc) = %{tl_version}, tex(ap-t5.enc) = %{tl_version}
Provides:       tex(ap-texnansi-sc.enc) = %{tl_version}, tex(ap-texnansi.enc) = %{tl_version}
Provides:       tex(ap-ts1.enc) = %{tl_version}, tex(ap-cs.map) = %{tl_version}
Provides:       tex(ap-ec.map) = %{tl_version}, tex(ap-l7x.map) = %{tl_version}
Provides:       tex(ap-qx.map) = %{tl_version}, tex(ap-rm.map) = %{tl_version}
Provides:       tex(ap-t5.map) = %{tl_version}, tex(ap-texnansi.map) = %{tl_version}
Provides:       tex(ap-ts1.map) = %{tl_version}, tex(ap.map) = %{tl_version}
Provides:       tex(antpolt-bold.otf) = %{tl_version}, tex(antpolt-bolditalic.otf) = %{tl_version}
Provides:       tex(antpolt-italic.otf) = %{tl_version}, tex(antpolt-regular.otf) = %{tl_version}
Provides:       tex(antpoltcond-bold.otf) = %{tl_version}
Provides:       tex(antpoltcond-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltcond-italic.otf) = %{tl_version}
Provides:       tex(antpoltcond-regular.otf) = %{tl_version}
Provides:       tex(antpoltexpd-bold.otf) = %{tl_version}
Provides:       tex(antpoltexpd-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltexpd-italic.otf) = %{tl_version}
Provides:       tex(antpoltexpd-regular.otf) = %{tl_version}
Provides:       tex(antpoltlt-bold.otf) = %{tl_version}, tex(antpoltlt-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltlt-italic.otf) = %{tl_version}
Provides:       tex(antpoltlt-regular.otf) = %{tl_version}
Provides:       tex(antpoltltcond-bold.otf) = %{tl_version}
Provides:       tex(antpoltltcond-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltltcond-italic.otf) = %{tl_version}
Provides:       tex(antpoltltcond-regular.otf) = %{tl_version}
Provides:       tex(antpoltltexpd-bold.otf) = %{tl_version}
Provides:       tex(antpoltltexpd-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltltexpd-italic.otf) = %{tl_version}
Provides:       tex(antpoltltexpd-regular.otf) = %{tl_version}
Provides:       tex(antpoltltsemicond-bold.otf) = %{tl_version}
Provides:       tex(antpoltltsemicond-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltltsemicond-italic.otf) = %{tl_version}
Provides:       tex(antpoltltsemicond-regular.otf) = %{tl_version}
Provides:       tex(antpoltltsemiexpd-bold.otf) = %{tl_version}
Provides:       tex(antpoltltsemiexpd-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltltsemiexpd-italic.otf) = %{tl_version}
Provides:       tex(antpoltltsemiexpd-regular.otf) = %{tl_version}
Provides:       tex(antpoltsemicond-bold.otf) = %{tl_version}
Provides:       tex(antpoltsemicond-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltsemicond-italic.otf) = %{tl_version}
Provides:       tex(antpoltsemicond-regular.otf) = %{tl_version}
Provides:       tex(antpoltsemiexpd-bold.otf) = %{tl_version}
Provides:       tex(antpoltsemiexpd-bolditalic.otf) = %{tl_version}
Provides:       tex(antpoltsemiexpd-italic.otf) = %{tl_version}
Provides:       tex(antpoltsemiexpd-regular.otf) = %{tl_version}
Provides:       tex(cs-antpb10-sc.tfm) = %{tl_version}, tex(cs-antpb10.tfm) = %{tl_version}
Provides:       tex(cs-antpb12-sc.tfm) = %{tl_version}, tex(cs-antpb12.tfm) = %{tl_version}
Provides:       tex(cs-antpb17-sc.tfm) = %{tl_version}, tex(cs-antpb17.tfm) = %{tl_version}
Provides:       tex(cs-antpb6-sc.tfm) = %{tl_version}, tex(cs-antpb6.tfm) = %{tl_version}
Provides:       tex(cs-antpb8-sc.tfm) = %{tl_version}, tex(cs-antpb8.tfm) = %{tl_version}
Provides:       tex(cs-antpbi10-sc.tfm) = %{tl_version}, tex(cs-antpbi10.tfm) = %{tl_version}
Provides:       tex(cs-antpbi12-sc.tfm) = %{tl_version}, tex(cs-antpbi12.tfm) = %{tl_version}
Provides:       tex(cs-antpbi17-sc.tfm) = %{tl_version}, tex(cs-antpbi17.tfm) = %{tl_version}
Provides:       tex(cs-antpbi6-sc.tfm) = %{tl_version}, tex(cs-antpbi6.tfm) = %{tl_version}
Provides:       tex(cs-antpbi8-sc.tfm) = %{tl_version}, tex(cs-antpbi8.tfm) = %{tl_version}
Provides:       tex(cs-antpl10-sc.tfm) = %{tl_version}, tex(cs-antpl10.tfm) = %{tl_version}
Provides:       tex(cs-antpl12-sc.tfm) = %{tl_version}, tex(cs-antpl12.tfm) = %{tl_version}
Provides:       tex(cs-antpl17-sc.tfm) = %{tl_version}, tex(cs-antpl17.tfm) = %{tl_version}
Provides:       tex(cs-antpl6-sc.tfm) = %{tl_version}, tex(cs-antpl6.tfm) = %{tl_version}
Provides:       tex(cs-antpl8-sc.tfm) = %{tl_version}, tex(cs-antpl8.tfm) = %{tl_version}
Provides:       tex(cs-antpli10-sc.tfm) = %{tl_version}, tex(cs-antpli10.tfm) = %{tl_version}
Provides:       tex(cs-antpli12-sc.tfm) = %{tl_version}, tex(cs-antpli12.tfm) = %{tl_version}
Provides:       tex(cs-antpli17-sc.tfm) = %{tl_version}, tex(cs-antpli17.tfm) = %{tl_version}
Provides:       tex(cs-antpli6-sc.tfm) = %{tl_version}, tex(cs-antpli6.tfm) = %{tl_version}
Provides:       tex(cs-antpli8-sc.tfm) = %{tl_version}, tex(cs-antpli8.tfm) = %{tl_version}
Provides:       tex(cs-antpm10-sc.tfm) = %{tl_version}, tex(cs-antpm10.tfm) = %{tl_version}
Provides:       tex(cs-antpm12-sc.tfm) = %{tl_version}, tex(cs-antpm12.tfm) = %{tl_version}
Provides:       tex(cs-antpm17-sc.tfm) = %{tl_version}, tex(cs-antpm17.tfm) = %{tl_version}
Provides:       tex(cs-antpm6-sc.tfm) = %{tl_version}, tex(cs-antpm6.tfm) = %{tl_version}
Provides:       tex(cs-antpm8-sc.tfm) = %{tl_version}, tex(cs-antpm8.tfm) = %{tl_version}
Provides:       tex(cs-antpmi10-sc.tfm) = %{tl_version}, tex(cs-antpmi10.tfm) = %{tl_version}
Provides:       tex(cs-antpmi12-sc.tfm) = %{tl_version}, tex(cs-antpmi12.tfm) = %{tl_version}
Provides:       tex(cs-antpmi17-sc.tfm) = %{tl_version}, tex(cs-antpmi17.tfm) = %{tl_version}
Provides:       tex(cs-antpmi6-sc.tfm) = %{tl_version}, tex(cs-antpmi6.tfm) = %{tl_version}
Provides:       tex(cs-antpmi8-sc.tfm) = %{tl_version}, tex(cs-antpmi8.tfm) = %{tl_version}
Provides:       tex(cs-antpr10-sc.tfm) = %{tl_version}, tex(cs-antpr10.tfm) = %{tl_version}
Provides:       tex(cs-antpr12-sc.tfm) = %{tl_version}, tex(cs-antpr12.tfm) = %{tl_version}
Provides:       tex(cs-antpr17-sc.tfm) = %{tl_version}, tex(cs-antpr17.tfm) = %{tl_version}
Provides:       tex(cs-antpr6-sc.tfm) = %{tl_version}, tex(cs-antpr6.tfm) = %{tl_version}
Provides:       tex(cs-antpr8-sc.tfm) = %{tl_version}, tex(cs-antpr8.tfm) = %{tl_version}
Provides:       tex(cs-antpri10-sc.tfm) = %{tl_version}, tex(cs-antpri10.tfm) = %{tl_version}
Provides:       tex(cs-antpri12-sc.tfm) = %{tl_version}, tex(cs-antpri12.tfm) = %{tl_version}
Provides:       tex(cs-antpri17-sc.tfm) = %{tl_version}, tex(cs-antpri17.tfm) = %{tl_version}
Provides:       tex(cs-antpri6-sc.tfm) = %{tl_version}, tex(cs-antpri6.tfm) = %{tl_version}
Provides:       tex(cs-antpri8-sc.tfm) = %{tl_version}, tex(cs-antpri8.tfm) = %{tl_version}
Provides:       tex(ec-antpb10-sc.tfm) = %{tl_version}, tex(ec-antpb10.tfm) = %{tl_version}
Provides:       tex(ec-antpb12-sc.tfm) = %{tl_version}, tex(ec-antpb12.tfm) = %{tl_version}
Provides:       tex(ec-antpb17-sc.tfm) = %{tl_version}, tex(ec-antpb17.tfm) = %{tl_version}
Provides:       tex(ec-antpb6-sc.tfm) = %{tl_version}, tex(ec-antpb6.tfm) = %{tl_version}
Provides:       tex(ec-antpb8-sc.tfm) = %{tl_version}, tex(ec-antpb8.tfm) = %{tl_version}
Provides:       tex(ec-antpbi10-sc.tfm) = %{tl_version}, tex(ec-antpbi10.tfm) = %{tl_version}
Provides:       tex(ec-antpbi12-sc.tfm) = %{tl_version}, tex(ec-antpbi12.tfm) = %{tl_version}
Provides:       tex(ec-antpbi17-sc.tfm) = %{tl_version}, tex(ec-antpbi17.tfm) = %{tl_version}
Provides:       tex(ec-antpbi6-sc.tfm) = %{tl_version}, tex(ec-antpbi6.tfm) = %{tl_version}
Provides:       tex(ec-antpbi8-sc.tfm) = %{tl_version}, tex(ec-antpbi8.tfm) = %{tl_version}
Provides:       tex(ec-antpl10-sc.tfm) = %{tl_version}, tex(ec-antpl10.tfm) = %{tl_version}
Provides:       tex(ec-antpl12-sc.tfm) = %{tl_version}, tex(ec-antpl12.tfm) = %{tl_version}
Provides:       tex(ec-antpl17-sc.tfm) = %{tl_version}, tex(ec-antpl17.tfm) = %{tl_version}
Provides:       tex(ec-antpl6-sc.tfm) = %{tl_version}, tex(ec-antpl6.tfm) = %{tl_version}
Provides:       tex(ec-antpl8-sc.tfm) = %{tl_version}, tex(ec-antpl8.tfm) = %{tl_version}
Provides:       tex(ec-antpli10-sc.tfm) = %{tl_version}, tex(ec-antpli10.tfm) = %{tl_version}
Provides:       tex(ec-antpli12-sc.tfm) = %{tl_version}, tex(ec-antpli12.tfm) = %{tl_version}
Provides:       tex(ec-antpli17-sc.tfm) = %{tl_version}, tex(ec-antpli17.tfm) = %{tl_version}
Provides:       tex(ec-antpli6-sc.tfm) = %{tl_version}, tex(ec-antpli6.tfm) = %{tl_version}
Provides:       tex(ec-antpli8-sc.tfm) = %{tl_version}, tex(ec-antpli8.tfm) = %{tl_version}
Provides:       tex(ec-antpm10-sc.tfm) = %{tl_version}, tex(ec-antpm10.tfm) = %{tl_version}
Provides:       tex(ec-antpm12-sc.tfm) = %{tl_version}, tex(ec-antpm12.tfm) = %{tl_version}
Provides:       tex(ec-antpm17-sc.tfm) = %{tl_version}, tex(ec-antpm17.tfm) = %{tl_version}
Provides:       tex(ec-antpm6-sc.tfm) = %{tl_version}, tex(ec-antpm6.tfm) = %{tl_version}
Provides:       tex(ec-antpm8-sc.tfm) = %{tl_version}, tex(ec-antpm8.tfm) = %{tl_version}
Provides:       tex(ec-antpmi10-sc.tfm) = %{tl_version}, tex(ec-antpmi10.tfm) = %{tl_version}
Provides:       tex(ec-antpmi12-sc.tfm) = %{tl_version}, tex(ec-antpmi12.tfm) = %{tl_version}
Provides:       tex(ec-antpmi17-sc.tfm) = %{tl_version}, tex(ec-antpmi17.tfm) = %{tl_version}
Provides:       tex(ec-antpmi6-sc.tfm) = %{tl_version}, tex(ec-antpmi6.tfm) = %{tl_version}
Provides:       tex(ec-antpmi8-sc.tfm) = %{tl_version}, tex(ec-antpmi8.tfm) = %{tl_version}
Provides:       tex(ec-antpr10-sc.tfm) = %{tl_version}, tex(ec-antpr10.tfm) = %{tl_version}
Provides:       tex(ec-antpr12-sc.tfm) = %{tl_version}, tex(ec-antpr12.tfm) = %{tl_version}
Provides:       tex(ec-antpr17-sc.tfm) = %{tl_version}, tex(ec-antpr17.tfm) = %{tl_version}
Provides:       tex(ec-antpr6-sc.tfm) = %{tl_version}, tex(ec-antpr6.tfm) = %{tl_version}
Provides:       tex(ec-antpr8-sc.tfm) = %{tl_version}, tex(ec-antpr8.tfm) = %{tl_version}
Provides:       tex(ec-antpri10-sc.tfm) = %{tl_version}, tex(ec-antpri10.tfm) = %{tl_version}
Provides:       tex(ec-antpri12-sc.tfm) = %{tl_version}, tex(ec-antpri12.tfm) = %{tl_version}
Provides:       tex(ec-antpri17-sc.tfm) = %{tl_version}, tex(ec-antpri17.tfm) = %{tl_version}
Provides:       tex(ec-antpri6-sc.tfm) = %{tl_version}, tex(ec-antpri6.tfm) = %{tl_version}
Provides:       tex(ec-antpri8-sc.tfm) = %{tl_version}, tex(ec-antpri8.tfm) = %{tl_version}
Provides:       tex(l7x-antpb10-sc.tfm) = %{tl_version}, tex(l7x-antpb10.tfm) = %{tl_version}
Provides:       tex(l7x-antpb12-sc.tfm) = %{tl_version}, tex(l7x-antpb12.tfm) = %{tl_version}
Provides:       tex(l7x-antpb17-sc.tfm) = %{tl_version}, tex(l7x-antpb17.tfm) = %{tl_version}
Provides:       tex(l7x-antpb6-sc.tfm) = %{tl_version}, tex(l7x-antpb6.tfm) = %{tl_version}
Provides:       tex(l7x-antpb8-sc.tfm) = %{tl_version}, tex(l7x-antpb8.tfm) = %{tl_version}
Provides:       tex(l7x-antpbi10-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpbi10.tfm) = %{tl_version}, tex(l7x-antpbi12-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpbi12.tfm) = %{tl_version}, tex(l7x-antpbi17-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpbi17.tfm) = %{tl_version}, tex(l7x-antpbi6-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpbi6.tfm) = %{tl_version}, tex(l7x-antpbi8-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpbi8.tfm) = %{tl_version}, tex(l7x-antpl10-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpl10.tfm) = %{tl_version}, tex(l7x-antpl12-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpl12.tfm) = %{tl_version}, tex(l7x-antpl17-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpl17.tfm) = %{tl_version}, tex(l7x-antpl6-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpl6.tfm) = %{tl_version}, tex(l7x-antpl8-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpl8.tfm) = %{tl_version}, tex(l7x-antpli10-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpli10.tfm) = %{tl_version}, tex(l7x-antpli12-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpli12.tfm) = %{tl_version}, tex(l7x-antpli17-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpli17.tfm) = %{tl_version}, tex(l7x-antpli6-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpli6.tfm) = %{tl_version}, tex(l7x-antpli8-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpli8.tfm) = %{tl_version}, tex(l7x-antpm10-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpm10.tfm) = %{tl_version}, tex(l7x-antpm12-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpm12.tfm) = %{tl_version}, tex(l7x-antpm17-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpm17.tfm) = %{tl_version}, tex(l7x-antpm6-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpm6.tfm) = %{tl_version}, tex(l7x-antpm8-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpm8.tfm) = %{tl_version}, tex(l7x-antpmi10-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpmi10.tfm) = %{tl_version}, tex(l7x-antpmi12-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpmi12.tfm) = %{tl_version}, tex(l7x-antpmi17-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpmi17.tfm) = %{tl_version}, tex(l7x-antpmi6-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpmi6.tfm) = %{tl_version}, tex(l7x-antpmi8-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpmi8.tfm) = %{tl_version}, tex(l7x-antpr10-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpr10.tfm) = %{tl_version}, tex(l7x-antpr12-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpr12.tfm) = %{tl_version}, tex(l7x-antpr17-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpr17.tfm) = %{tl_version}, tex(l7x-antpr6-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpr6.tfm) = %{tl_version}, tex(l7x-antpr8-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpr8.tfm) = %{tl_version}, tex(l7x-antpri10-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpri10.tfm) = %{tl_version}, tex(l7x-antpri12-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpri12.tfm) = %{tl_version}, tex(l7x-antpri17-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpri17.tfm) = %{tl_version}, tex(l7x-antpri6-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpri6.tfm) = %{tl_version}, tex(l7x-antpri8-sc.tfm) = %{tl_version}
Provides:       tex(l7x-antpri8.tfm) = %{tl_version}, tex(qx-antpb10-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpb10.tfm) = %{tl_version}, tex(qx-antpb12-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpb12.tfm) = %{tl_version}, tex(qx-antpb17-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpb17.tfm) = %{tl_version}, tex(qx-antpb6-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpb6.tfm) = %{tl_version}, tex(qx-antpb8-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpb8.tfm) = %{tl_version}, tex(qx-antpbi10-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpbi10.tfm) = %{tl_version}, tex(qx-antpbi12-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpbi12.tfm) = %{tl_version}, tex(qx-antpbi17-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpbi17.tfm) = %{tl_version}, tex(qx-antpbi6-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpbi6.tfm) = %{tl_version}, tex(qx-antpbi8-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpbi8.tfm) = %{tl_version}, tex(qx-antpl10-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpl10.tfm) = %{tl_version}, tex(qx-antpl12-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpl12.tfm) = %{tl_version}, tex(qx-antpl17-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpl17.tfm) = %{tl_version}, tex(qx-antpl6-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpl6.tfm) = %{tl_version}, tex(qx-antpl8-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpl8.tfm) = %{tl_version}, tex(qx-antpli10-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpli10.tfm) = %{tl_version}, tex(qx-antpli12-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpli12.tfm) = %{tl_version}, tex(qx-antpli17-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpli17.tfm) = %{tl_version}, tex(qx-antpli6-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpli6.tfm) = %{tl_version}, tex(qx-antpli8-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpli8.tfm) = %{tl_version}, tex(qx-antpm10-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpm10.tfm) = %{tl_version}, tex(qx-antpm12-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpm12.tfm) = %{tl_version}, tex(qx-antpm17-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpm17.tfm) = %{tl_version}, tex(qx-antpm6-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpm6.tfm) = %{tl_version}, tex(qx-antpm8-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpm8.tfm) = %{tl_version}, tex(qx-antpmi10-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpmi10.tfm) = %{tl_version}, tex(qx-antpmi12-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpmi12.tfm) = %{tl_version}, tex(qx-antpmi17-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpmi17.tfm) = %{tl_version}, tex(qx-antpmi6-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpmi6.tfm) = %{tl_version}, tex(qx-antpmi8-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpmi8.tfm) = %{tl_version}, tex(qx-antpr10-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpr10.tfm) = %{tl_version}, tex(qx-antpr12-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpr12.tfm) = %{tl_version}, tex(qx-antpr17-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpr17.tfm) = %{tl_version}, tex(qx-antpr6-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpr6.tfm) = %{tl_version}, tex(qx-antpr8-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpr8.tfm) = %{tl_version}, tex(qx-antpri10-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpri10.tfm) = %{tl_version}, tex(qx-antpri12-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpri12.tfm) = %{tl_version}, tex(qx-antpri17-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpri17.tfm) = %{tl_version}, tex(qx-antpri6-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpri6.tfm) = %{tl_version}, tex(qx-antpri8-sc.tfm) = %{tl_version}
Provides:       tex(qx-antpri8.tfm) = %{tl_version}, tex(rm-antpb10-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpb10.tfm) = %{tl_version}, tex(rm-antpb12-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpb12.tfm) = %{tl_version}, tex(rm-antpb17-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpb17.tfm) = %{tl_version}, tex(rm-antpb6-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpb6.tfm) = %{tl_version}, tex(rm-antpb8-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpb8.tfm) = %{tl_version}, tex(rm-antpbi10-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpbi10.tfm) = %{tl_version}, tex(rm-antpbi12-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpbi12.tfm) = %{tl_version}, tex(rm-antpbi17-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpbi17.tfm) = %{tl_version}, tex(rm-antpbi6-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpbi6.tfm) = %{tl_version}, tex(rm-antpbi8-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpbi8.tfm) = %{tl_version}, tex(rm-antpl10-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpl10.tfm) = %{tl_version}, tex(rm-antpl12-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpl12.tfm) = %{tl_version}, tex(rm-antpl17-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpl17.tfm) = %{tl_version}, tex(rm-antpl6-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpl6.tfm) = %{tl_version}, tex(rm-antpl8-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpl8.tfm) = %{tl_version}, tex(rm-antpli10-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpli10.tfm) = %{tl_version}, tex(rm-antpli12-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpli12.tfm) = %{tl_version}, tex(rm-antpli17-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpli17.tfm) = %{tl_version}, tex(rm-antpli6-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpli6.tfm) = %{tl_version}, tex(rm-antpli8-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpli8.tfm) = %{tl_version}, tex(rm-antpm10-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpm10.tfm) = %{tl_version}, tex(rm-antpm12-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpm12.tfm) = %{tl_version}, tex(rm-antpm17-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpm17.tfm) = %{tl_version}, tex(rm-antpm6-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpm6.tfm) = %{tl_version}, tex(rm-antpm8-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpm8.tfm) = %{tl_version}, tex(rm-antpmi10-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpmi10.tfm) = %{tl_version}, tex(rm-antpmi12-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpmi12.tfm) = %{tl_version}, tex(rm-antpmi17-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpmi17.tfm) = %{tl_version}, tex(rm-antpmi6-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpmi6.tfm) = %{tl_version}, tex(rm-antpmi8-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpmi8.tfm) = %{tl_version}, tex(rm-antpr10-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpr10.tfm) = %{tl_version}, tex(rm-antpr12-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpr12.tfm) = %{tl_version}, tex(rm-antpr17-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpr17.tfm) = %{tl_version}, tex(rm-antpr6-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpr6.tfm) = %{tl_version}, tex(rm-antpr8-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpr8.tfm) = %{tl_version}, tex(rm-antpri10-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpri10.tfm) = %{tl_version}, tex(rm-antpri12-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpri12.tfm) = %{tl_version}, tex(rm-antpri17-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpri17.tfm) = %{tl_version}, tex(rm-antpri6-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpri6.tfm) = %{tl_version}, tex(rm-antpri8-sc.tfm) = %{tl_version}
Provides:       tex(rm-antpri8.tfm) = %{tl_version}, tex(t5-antpb10-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpb10.tfm) = %{tl_version}, tex(t5-antpb12-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpb12.tfm) = %{tl_version}, tex(t5-antpb17-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpb17.tfm) = %{tl_version}, tex(t5-antpb6-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpb6.tfm) = %{tl_version}, tex(t5-antpb8-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpb8.tfm) = %{tl_version}, tex(t5-antpbi10-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpbi10.tfm) = %{tl_version}, tex(t5-antpbi12-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpbi12.tfm) = %{tl_version}, tex(t5-antpbi17-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpbi17.tfm) = %{tl_version}, tex(t5-antpbi6-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpbi6.tfm) = %{tl_version}, tex(t5-antpbi8-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpbi8.tfm) = %{tl_version}, tex(t5-antpl10-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpl10.tfm) = %{tl_version}, tex(t5-antpl12-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpl12.tfm) = %{tl_version}, tex(t5-antpl17-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpl17.tfm) = %{tl_version}, tex(t5-antpl6-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpl6.tfm) = %{tl_version}, tex(t5-antpl8-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpl8.tfm) = %{tl_version}, tex(t5-antpli10-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpli10.tfm) = %{tl_version}, tex(t5-antpli12-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpli12.tfm) = %{tl_version}, tex(t5-antpli17-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpli17.tfm) = %{tl_version}, tex(t5-antpli6-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpli6.tfm) = %{tl_version}, tex(t5-antpli8-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpli8.tfm) = %{tl_version}, tex(t5-antpm10-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpm10.tfm) = %{tl_version}, tex(t5-antpm12-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpm12.tfm) = %{tl_version}, tex(t5-antpm17-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpm17.tfm) = %{tl_version}, tex(t5-antpm6-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpm6.tfm) = %{tl_version}, tex(t5-antpm8-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpm8.tfm) = %{tl_version}, tex(t5-antpmi10-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpmi10.tfm) = %{tl_version}, tex(t5-antpmi12-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpmi12.tfm) = %{tl_version}, tex(t5-antpmi17-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpmi17.tfm) = %{tl_version}, tex(t5-antpmi6-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpmi6.tfm) = %{tl_version}, tex(t5-antpmi8-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpmi8.tfm) = %{tl_version}, tex(t5-antpr10-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpr10.tfm) = %{tl_version}, tex(t5-antpr12-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpr12.tfm) = %{tl_version}, tex(t5-antpr17-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpr17.tfm) = %{tl_version}, tex(t5-antpr6-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpr6.tfm) = %{tl_version}, tex(t5-antpr8-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpr8.tfm) = %{tl_version}, tex(t5-antpri10-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpri10.tfm) = %{tl_version}, tex(t5-antpri12-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpri12.tfm) = %{tl_version}, tex(t5-antpri17-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpri17.tfm) = %{tl_version}, tex(t5-antpri6-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpri6.tfm) = %{tl_version}, tex(t5-antpri8-sc.tfm) = %{tl_version}
Provides:       tex(t5-antpri8.tfm) = %{tl_version}, tex(texnansi-antpb10-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb10.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb12-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb12.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb17-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb17.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb6-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb6.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb8-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpb8.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi10-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi10.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi12-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi12.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi17-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi17.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi6-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi6.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi8-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpbi8.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl10-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl10.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl12-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl12.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl17-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl17.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl6-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl6.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl8-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpl8.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli10-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli10.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli12-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli12.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli17-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli17.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli6-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli6.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli8-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpli8.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm10-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm10.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm12-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm12.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm17-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm17.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm6-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm6.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm8-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpm8.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi10-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi10.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi12-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi12.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi17-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi17.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi6-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi6.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi8-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpmi8.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr10-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr10.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr12-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr12.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr17-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr17.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr6-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr6.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr8-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpr8.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri10-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri10.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri12-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri12.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri17-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri17.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri6-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri6.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri8-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-antpri8.tfm) = %{tl_version}
Provides:       tex(ts1-antpb10.tfm) = %{tl_version}, tex(ts1-antpb12.tfm) = %{tl_version}
Provides:       tex(ts1-antpb17.tfm) = %{tl_version}, tex(ts1-antpb6.tfm) = %{tl_version}
Provides:       tex(ts1-antpb8.tfm) = %{tl_version}, tex(ts1-antpbi10.tfm) = %{tl_version}
Provides:       tex(ts1-antpbi12.tfm) = %{tl_version}, tex(ts1-antpbi17.tfm) = %{tl_version}
Provides:       tex(ts1-antpbi6.tfm) = %{tl_version}, tex(ts1-antpbi8.tfm) = %{tl_version}
Provides:       tex(ts1-antpl10.tfm) = %{tl_version}, tex(ts1-antpl12.tfm) = %{tl_version}
Provides:       tex(ts1-antpl17.tfm) = %{tl_version}, tex(ts1-antpl6.tfm) = %{tl_version}
Provides:       tex(ts1-antpl8.tfm) = %{tl_version}, tex(ts1-antpli10.tfm) = %{tl_version}
Provides:       tex(ts1-antpli12.tfm) = %{tl_version}, tex(ts1-antpli17.tfm) = %{tl_version}
Provides:       tex(ts1-antpli6.tfm) = %{tl_version}, tex(ts1-antpli8.tfm) = %{tl_version}
Provides:       tex(ts1-antpm10.tfm) = %{tl_version}, tex(ts1-antpm12.tfm) = %{tl_version}
Provides:       tex(ts1-antpm17.tfm) = %{tl_version}, tex(ts1-antpm6.tfm) = %{tl_version}
Provides:       tex(ts1-antpm8.tfm) = %{tl_version}, tex(ts1-antpmi10.tfm) = %{tl_version}
Provides:       tex(ts1-antpmi12.tfm) = %{tl_version}, tex(ts1-antpmi17.tfm) = %{tl_version}
Provides:       tex(ts1-antpmi6.tfm) = %{tl_version}, tex(ts1-antpmi8.tfm) = %{tl_version}
Provides:       tex(ts1-antpr10.tfm) = %{tl_version}, tex(ts1-antpr12.tfm) = %{tl_version}
Provides:       tex(ts1-antpr17.tfm) = %{tl_version}, tex(ts1-antpr6.tfm) = %{tl_version}
Provides:       tex(ts1-antpr8.tfm) = %{tl_version}, tex(ts1-antpri10.tfm) = %{tl_version}
Provides:       tex(ts1-antpri12.tfm) = %{tl_version}, tex(ts1-antpri17.tfm) = %{tl_version}
Provides:       tex(ts1-antpri6.tfm) = %{tl_version}, tex(ts1-antpri8.tfm) = %{tl_version}
Provides:       tex(antpb10.pfb) = %{tl_version}, tex(antpb12.pfb) = %{tl_version}
Provides:       tex(antpb17.pfb) = %{tl_version}, tex(antpb6.pfb) = %{tl_version}
Provides:       tex(antpb8.pfb) = %{tl_version}, tex(antpbi10.pfb) = %{tl_version}
Provides:       tex(antpbi12.pfb) = %{tl_version}, tex(antpbi17.pfb) = %{tl_version}
Provides:       tex(antpbi6.pfb) = %{tl_version}, tex(antpbi8.pfb) = %{tl_version}
Provides:       tex(antpl10.pfb) = %{tl_version}, tex(antpl12.pfb) = %{tl_version}
Provides:       tex(antpl17.pfb) = %{tl_version}, tex(antpl6.pfb) = %{tl_version}
Provides:       tex(antpl8.pfb) = %{tl_version}, tex(antpli10.pfb) = %{tl_version}
Provides:       tex(antpli12.pfb) = %{tl_version}, tex(antpli17.pfb) = %{tl_version}
Provides:       tex(antpli6.pfb) = %{tl_version}, tex(antpli8.pfb) = %{tl_version}
Provides:       tex(antpm10.pfb) = %{tl_version}, tex(antpm12.pfb) = %{tl_version}
Provides:       tex(antpm17.pfb) = %{tl_version}, tex(antpm6.pfb) = %{tl_version}
Provides:       tex(antpm8.pfb) = %{tl_version}, tex(antpmi10.pfb) = %{tl_version}
Provides:       tex(antpmi12.pfb) = %{tl_version}, tex(antpmi17.pfb) = %{tl_version}
Provides:       tex(antpmi6.pfb) = %{tl_version}, tex(antpmi8.pfb) = %{tl_version}
Provides:       tex(antpr10.pfb) = %{tl_version}, tex(antpr12.pfb) = %{tl_version}
Provides:       tex(antpr17.pfb) = %{tl_version}, tex(antpr6.pfb) = %{tl_version}
Provides:       tex(antpr8.pfb) = %{tl_version}, tex(antpri10.pfb) = %{tl_version}
Provides:       tex(antpri12.pfb) = %{tl_version}, tex(antpri17.pfb) = %{tl_version}
Provides:       tex(antpri6.pfb) = %{tl_version}, tex(antpri8.pfb) = %{tl_version}
Provides:       tex(antpolt.sty) = %{tl_version}, tex(il2antp.fd) = %{tl_version}
Provides:       tex(il2antpl.fd) = %{tl_version}, tex(l7xantp.fd) = %{tl_version}
Provides:       tex(l7xantpl.fd) = %{tl_version}, tex(ly1antp.fd) = %{tl_version}
Provides:       tex(ly1antpl.fd) = %{tl_version}, tex(ot1antp.fd) = %{tl_version}
Provides:       tex(ot1antpl.fd) = %{tl_version}, tex(ot4antp.fd) = %{tl_version}
Provides:       tex(ot4antpl.fd) = %{tl_version}, tex(qxantp.fd) = %{tl_version}
Provides:       tex(qxantpl.fd) = %{tl_version}, tex(t1antp.fd) = %{tl_version}
Provides:       tex(t1antpl.fd) = %{tl_version}, tex(t5antp.fd) = %{tl_version}
Provides:       tex(t5antpl.fd) = %{tl_version}, tex(ts1antp.fd) = %{tl_version}
Provides:       tex(ts1antpl.fd) = %{tl_version}

%description -n texlive-poltawski
The package contains the Antykwa Poltawskiego family of fonts
in the PostScript Type 1 and OpenType formats. The original
font was designed in the twenties of the XX century by the
Polish typographer Adam Poltawski(1881-1952). Following the
route set out by the Latin Modern and TeX Gyre projects
(http://www.gust.org.pl/projects/e-foundry), the Antykwa
Poltawskiego digitisation project aims at providing a rich
collection of diacritical characters in the attempt to cover as
many Latin-based scripts as possible. To our knowledge, the
repertoire of characters covers all European languages as well
as some other Latin-based alphabets such as Vietnamese and
Navajo; at the request of users, recent extensions (following
the enhancement of the Latin Modern collection) provide glyphs
sufficient for typesetting of romanized transliterations of
Arabic and Sanskrit scripts. The Antykwa Poltawskiego family
consists of 4 weights (light, normal, medium, bold), each
having upright and italic forms and one of 5 design sizes: 6,
8, 10, 12 and 17pt. Altogether, the collection comprises 40
font files, containing the same repertoire of 1126 characters.
The preliminary version of Antykwa Poltawskiego (antp package)
released in 2000 is rendered obsolete by this package.

%package -n texlive-poltawski-doc
Summary:        Documentation for poltawski
Version:        svn20075.1.101

Provides:       tex-poltawski-doc
AutoReqProv:    No

%description -n texlive-poltawski-doc
Documentation for poltawski

%package -n texlive-palatino
Provides:       tex-palatino = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn31835.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(upl.map) = %{tl_version}, tex(eurbo10.tfm) = %{tl_version}
Provides:       tex(eurmo10.tfm) = %{tl_version}, tex(pplb.tfm) = %{tl_version}
Provides:       tex(pplb7t.tfm) = %{tl_version}, tex(pplb8c.tfm) = %{tl_version}
Provides:       tex(pplb8r.tfm) = %{tl_version}, tex(pplb8t.tfm) = %{tl_version}
Provides:       tex(pplb9c.tfm) = %{tl_version}, tex(pplb9d.tfm) = %{tl_version}
Provides:       tex(pplb9e.tfm) = %{tl_version}, tex(pplb9o.tfm) = %{tl_version}
Provides:       tex(pplb9t.tfm) = %{tl_version}, tex(pplbc.tfm) = %{tl_version}
Provides:       tex(pplbc7t.tfm) = %{tl_version}, tex(pplbc8t.tfm) = %{tl_version}
Provides:       tex(pplbi.tfm) = %{tl_version}, tex(pplbi7t.tfm) = %{tl_version}
Provides:       tex(pplbi8c.tfm) = %{tl_version}, tex(pplbi8r.tfm) = %{tl_version}
Provides:       tex(pplbi8t.tfm) = %{tl_version}, tex(pplbi9c.tfm) = %{tl_version}
Provides:       tex(pplbi9d.tfm) = %{tl_version}, tex(pplbi9e.tfm) = %{tl_version}
Provides:       tex(pplbi9o.tfm) = %{tl_version}, tex(pplbi9t.tfm) = %{tl_version}
Provides:       tex(pplbij8r.tfm) = %{tl_version}, tex(pplbj8r.tfm) = %{tl_version}
Provides:       tex(pplbo.tfm) = %{tl_version}, tex(pplbo7t.tfm) = %{tl_version}
Provides:       tex(pplbo8c.tfm) = %{tl_version}, tex(pplbo8r.tfm) = %{tl_version}
Provides:       tex(pplbo8t.tfm) = %{tl_version}, tex(pplbu.tfm) = %{tl_version}
Provides:       tex(pplbu8r.tfm) = %{tl_version}, tex(pplr.tfm) = %{tl_version}
Provides:       tex(pplr7t.tfm) = %{tl_version}, tex(pplr8c.tfm) = %{tl_version}
Provides:       tex(pplr8r.tfm) = %{tl_version}, tex(pplr8rn.tfm) = %{tl_version}
Provides:       tex(pplr8t.tfm) = %{tl_version}, tex(pplr9c.tfm) = %{tl_version}
Provides:       tex(pplr9d.tfm) = %{tl_version}, tex(pplr9e.tfm) = %{tl_version}
Provides:       tex(pplr9o.tfm) = %{tl_version}, tex(pplr9t.tfm) = %{tl_version}
Provides:       tex(pplrc.tfm) = %{tl_version}, tex(pplrc7t.tfm) = %{tl_version}
Provides:       tex(pplrc8r.tfm) = %{tl_version}, tex(pplrc8t.tfm) = %{tl_version}
Provides:       tex(pplrc9d.tfm) = %{tl_version}, tex(pplrc9e.tfm) = %{tl_version}
Provides:       tex(pplrc9o.tfm) = %{tl_version}, tex(pplrc9t.tfm) = %{tl_version}
Provides:       tex(pplri.tfm) = %{tl_version}, tex(pplri7t.tfm) = %{tl_version}
Provides:       tex(pplri8c.tfm) = %{tl_version}, tex(pplri8r.tfm) = %{tl_version}
Provides:       tex(pplri8t.tfm) = %{tl_version}, tex(pplri9c.tfm) = %{tl_version}
Provides:       tex(pplri9d.tfm) = %{tl_version}, tex(pplri9e.tfm) = %{tl_version}
Provides:       tex(pplri9o.tfm) = %{tl_version}, tex(pplri9t.tfm) = %{tl_version}
Provides:       tex(pplrij8r.tfm) = %{tl_version}, tex(pplro.tfm) = %{tl_version}
Provides:       tex(pplro7t.tfm) = %{tl_version}, tex(pplro8c.tfm) = %{tl_version}
Provides:       tex(pplro8r.tfm) = %{tl_version}, tex(pplro8t.tfm) = %{tl_version}
Provides:       tex(pplrr8re.tfm) = %{tl_version}, tex(pplrre.tfm) = %{tl_version}
Provides:       tex(pplrrn.tfm) = %{tl_version}, tex(pplru.tfm) = %{tl_version}
Provides:       tex(pplru8r.tfm) = %{tl_version}, tex(zppleb7m.tfm) = %{tl_version}
Provides:       tex(zppleb7t.tfm) = %{tl_version}, tex(zppleb7y.tfm) = %{tl_version}
Provides:       tex(zppler7m.tfm) = %{tl_version}, tex(zppler7t.tfm) = %{tl_version}
Provides:       tex(zppler7v.tfm) = %{tl_version}, tex(zppler7y.tfm) = %{tl_version}
Provides:       tex(uplb7t.tfm) = %{tl_version}, tex(uplb8c.tfm) = %{tl_version}
Provides:       tex(uplb8r.tfm) = %{tl_version}, tex(uplb8t.tfm) = %{tl_version}
Provides:       tex(uplbc7t.tfm) = %{tl_version}, tex(uplbc8t.tfm) = %{tl_version}
Provides:       tex(uplbi7t.tfm) = %{tl_version}, tex(uplbi8c.tfm) = %{tl_version}
Provides:       tex(uplbi8r.tfm) = %{tl_version}, tex(uplbi8t.tfm) = %{tl_version}
Provides:       tex(uplbo7t.tfm) = %{tl_version}, tex(uplbo8c.tfm) = %{tl_version}
Provides:       tex(uplbo8r.tfm) = %{tl_version}, tex(uplbo8t.tfm) = %{tl_version}
Provides:       tex(uplr7t.tfm) = %{tl_version}, tex(uplr8c.tfm) = %{tl_version}
Provides:       tex(uplr8r.tfm) = %{tl_version}, tex(uplr8t.tfm) = %{tl_version}
Provides:       tex(uplrc7t.tfm) = %{tl_version}, tex(uplrc8t.tfm) = %{tl_version}
Provides:       tex(uplri7t.tfm) = %{tl_version}, tex(uplri8c.tfm) = %{tl_version}
Provides:       tex(uplri8r.tfm) = %{tl_version}, tex(uplri8t.tfm) = %{tl_version}
Provides:       tex(uplro7t.tfm) = %{tl_version}, tex(uplro8c.tfm) = %{tl_version}
Provides:       tex(uplro8r.tfm) = %{tl_version}, tex(uplro8t.tfm) = %{tl_version}
Provides:       tex(uplb8a.pfb) = %{tl_version}, tex(uplbi8a.pfb) = %{tl_version}
Provides:       tex(uplr8a.pfb) = %{tl_version}, tex(uplri8a.pfb) = %{tl_version}
Provides:       tex(pplb.vf) = %{tl_version}, tex(pplb7t.vf) = %{tl_version}
Provides:       tex(pplb8c.vf) = %{tl_version}, tex(pplb8t.vf) = %{tl_version}
Provides:       tex(pplb9c.vf) = %{tl_version}, tex(pplb9d.vf) = %{tl_version}
Provides:       tex(pplb9e.vf) = %{tl_version}, tex(pplb9o.vf) = %{tl_version}
Provides:       tex(pplb9t.vf) = %{tl_version}, tex(pplbc.vf) = %{tl_version}
Provides:       tex(pplbc7t.vf) = %{tl_version}, tex(pplbc8t.vf) = %{tl_version}
Provides:       tex(pplbi.vf) = %{tl_version}, tex(pplbi7t.vf) = %{tl_version}
Provides:       tex(pplbi8c.vf) = %{tl_version}, tex(pplbi8t.vf) = %{tl_version}
Provides:       tex(pplbi9c.vf) = %{tl_version}, tex(pplbi9d.vf) = %{tl_version}
Provides:       tex(pplbi9e.vf) = %{tl_version}, tex(pplbi9o.vf) = %{tl_version}
Provides:       tex(pplbi9t.vf) = %{tl_version}, tex(pplbo.vf) = %{tl_version}
Provides:       tex(pplbo7t.vf) = %{tl_version}, tex(pplbo8c.vf) = %{tl_version}
Provides:       tex(pplbo8t.vf) = %{tl_version}, tex(pplbu.vf) = %{tl_version}
Provides:       tex(pplr.vf) = %{tl_version}, tex(pplr7t.vf) = %{tl_version}
Provides:       tex(pplr8c.vf) = %{tl_version}, tex(pplr8t.vf) = %{tl_version}
Provides:       tex(pplr9c.vf) = %{tl_version}, tex(pplr9d.vf) = %{tl_version}
Provides:       tex(pplr9e.vf) = %{tl_version}, tex(pplr9o.vf) = %{tl_version}
Provides:       tex(pplr9t.vf) = %{tl_version}, tex(pplrc.vf) = %{tl_version}
Provides:       tex(pplrc7t.vf) = %{tl_version}, tex(pplrc8t.vf) = %{tl_version}
Provides:       tex(pplrc9d.vf) = %{tl_version}, tex(pplrc9e.vf) = %{tl_version}
Provides:       tex(pplrc9o.vf) = %{tl_version}, tex(pplrc9t.vf) = %{tl_version}
Provides:       tex(pplri.vf) = %{tl_version}, tex(pplri7t.vf) = %{tl_version}
Provides:       tex(pplri8c.vf) = %{tl_version}, tex(pplri8t.vf) = %{tl_version}
Provides:       tex(pplri9c.vf) = %{tl_version}, tex(pplri9d.vf) = %{tl_version}
Provides:       tex(pplri9e.vf) = %{tl_version}, tex(pplri9o.vf) = %{tl_version}
Provides:       tex(pplri9t.vf) = %{tl_version}, tex(pplro.vf) = %{tl_version}
Provides:       tex(pplro7t.vf) = %{tl_version}, tex(pplro8c.vf) = %{tl_version}
Provides:       tex(pplro8t.vf) = %{tl_version}, tex(pplrre.vf) = %{tl_version}
Provides:       tex(pplrrn.vf) = %{tl_version}, tex(pplru.vf) = %{tl_version}
Provides:       tex(zppleb7m.vf) = %{tl_version}, tex(zppleb7t.vf) = %{tl_version}
Provides:       tex(zppleb7y.vf) = %{tl_version}, tex(zppler7m.vf) = %{tl_version}
Provides:       tex(zppler7t.vf) = %{tl_version}, tex(zppler7v.vf) = %{tl_version}
Provides:       tex(zppler7y.vf) = %{tl_version}, tex(uplb7t.vf) = %{tl_version}
Provides:       tex(uplb8c.vf) = %{tl_version}, tex(uplb8t.vf) = %{tl_version}
Provides:       tex(uplbc7t.vf) = %{tl_version}, tex(uplbc8t.vf) = %{tl_version}
Provides:       tex(uplbi7t.vf) = %{tl_version}, tex(uplbi8c.vf) = %{tl_version}
Provides:       tex(uplbi8t.vf) = %{tl_version}, tex(uplbo7t.vf) = %{tl_version}
Provides:       tex(uplbo8c.vf) = %{tl_version}, tex(uplbo8t.vf) = %{tl_version}
Provides:       tex(uplr7t.vf) = %{tl_version}, tex(uplr8c.vf) = %{tl_version}
Provides:       tex(uplr8t.vf) = %{tl_version}, tex(uplrc7t.vf) = %{tl_version}
Provides:       tex(uplrc8t.vf) = %{tl_version}, tex(uplri7t.vf) = %{tl_version}
Provides:       tex(uplri8c.vf) = %{tl_version}, tex(uplri8t.vf) = %{tl_version}
Provides:       tex(uplro7t.vf) = %{tl_version}, tex(uplro8c.vf) = %{tl_version}
Provides:       tex(uplro8t.vf) = %{tl_version}, tex(8rupl.fd) = %{tl_version}
Provides:       tex(omlupl.fd) = %{tl_version}, tex(omsupl.fd) = %{tl_version}
Provides:       tex(ot1upl.fd) = %{tl_version}, tex(t1upl.fd) = %{tl_version}
Provides:       tex(ts1upl.fd) = %{tl_version}

%description -n texlive-palatino
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-pxfonts
Provides:       tex-pxfonts = %{tl_version}
License:        GPL+
Summary:        Palatino-like fonts in support of mathematics
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(pxfonts.map) = %{tl_version}, tex(pxr.map) = %{tl_version}
Provides:       tex(pxr1.map) = %{tl_version}, tex(pxr2.map) = %{tl_version}
Provides:       tex(pxr3.map) = %{tl_version}, tex(p1xb.tfm) = %{tl_version}
Provides:       tex(p1xbi.tfm) = %{tl_version}, tex(p1xbsc.tfm) = %{tl_version}
Provides:       tex(p1xbsl.tfm) = %{tl_version}, tex(p1xi.tfm) = %{tl_version}
Provides:       tex(p1xr.tfm) = %{tl_version}, tex(p1xsc.tfm) = %{tl_version}
Provides:       tex(p1xsl.tfm) = %{tl_version}, tex(pcxb.tfm) = %{tl_version}
Provides:       tex(pcxbi.tfm) = %{tl_version}, tex(pcxbsl.tfm) = %{tl_version}
Provides:       tex(pcxi.tfm) = %{tl_version}, tex(pcxr.tfm) = %{tl_version}
Provides:       tex(pcxsl.tfm) = %{tl_version}, tex(pxb.tfm) = %{tl_version}
Provides:       tex(pxbex.tfm) = %{tl_version}, tex(pxbexa.tfm) = %{tl_version}
Provides:       tex(pxbi.tfm) = %{tl_version}, tex(pxbmi.tfm) = %{tl_version}
Provides:       tex(pxbmi1.tfm) = %{tl_version}, tex(pxbmia.tfm) = %{tl_version}
Provides:       tex(pxbsc.tfm) = %{tl_version}, tex(pxbsl.tfm) = %{tl_version}
Provides:       tex(pxbsy.tfm) = %{tl_version}, tex(pxbsya.tfm) = %{tl_version}
Provides:       tex(pxbsyb.tfm) = %{tl_version}, tex(pxbsyc.tfm) = %{tl_version}
Provides:       tex(pxex.tfm) = %{tl_version}, tex(pxexa.tfm) = %{tl_version}
Provides:       tex(pxi.tfm) = %{tl_version}, tex(pxmi.tfm) = %{tl_version}
Provides:       tex(pxmi1.tfm) = %{tl_version}, tex(pxmia.tfm) = %{tl_version}
Provides:       tex(pxr.tfm) = %{tl_version}, tex(pxsc.tfm) = %{tl_version}
Provides:       tex(pxsl.tfm) = %{tl_version}, tex(pxsy.tfm) = %{tl_version}
Provides:       tex(pxsya.tfm) = %{tl_version}, tex(pxsyb.tfm) = %{tl_version}
Provides:       tex(pxsyc.tfm) = %{tl_version}, tex(rpcxb.tfm) = %{tl_version}
Provides:       tex(rpcxbi.tfm) = %{tl_version}, tex(rpcxbsl.tfm) = %{tl_version}
Provides:       tex(rpcxi.tfm) = %{tl_version}, tex(rpcxr.tfm) = %{tl_version}
Provides:       tex(rpcxsl.tfm) = %{tl_version}, tex(rpxb.tfm) = %{tl_version}
Provides:       tex(rpxbi.tfm) = %{tl_version}, tex(rpxbmi.tfm) = %{tl_version}
Provides:       tex(rpxbsc.tfm) = %{tl_version}, tex(rpxbsl.tfm) = %{tl_version}
Provides:       tex(rpxi.tfm) = %{tl_version}, tex(rpxmi.tfm) = %{tl_version}
Provides:       tex(rpxpplb.tfm) = %{tl_version}, tex(rpxpplbi.tfm) = %{tl_version}
Provides:       tex(rpxpplbo.tfm) = %{tl_version}, tex(rpxpplr.tfm) = %{tl_version}
Provides:       tex(rpxpplri.tfm) = %{tl_version}, tex(rpxpplro.tfm) = %{tl_version}
Provides:       tex(rpxr.tfm) = %{tl_version}, tex(rpxsc.tfm) = %{tl_version}
Provides:       tex(rpxsl.tfm) = %{tl_version}, tex(pxbex.pfb) = %{tl_version}
Provides:       tex(pxbexa.pfb) = %{tl_version}, tex(pxbmia.pfb) = %{tl_version}
Provides:       tex(pxbsy.pfb) = %{tl_version}, tex(pxbsya.pfb) = %{tl_version}
Provides:       tex(pxbsyb.pfb) = %{tl_version}, tex(pxbsyc.pfb) = %{tl_version}
Provides:       tex(pxex.pfb) = %{tl_version}, tex(pxexa.pfb) = %{tl_version}
Provides:       tex(pxmia.pfb) = %{tl_version}, tex(pxsy.pfb) = %{tl_version}
Provides:       tex(pxsya.pfb) = %{tl_version}, tex(pxsyb.pfb) = %{tl_version}
Provides:       tex(pxsyc.pfb) = %{tl_version}, tex(rpcxb.pfb) = %{tl_version}
Provides:       tex(rpcxbi.pfb) = %{tl_version}, tex(rpcxi.pfb) = %{tl_version}
Provides:       tex(rpcxr.pfb) = %{tl_version}, tex(rpxb.pfb) = %{tl_version}
Provides:       tex(rpxbi.pfb) = %{tl_version}, tex(rpxbmi.pfb) = %{tl_version}
Provides:       tex(rpxbsc.pfb) = %{tl_version}, tex(rpxi.pfb) = %{tl_version}
Provides:       tex(rpxmi.pfb) = %{tl_version}, tex(rpxr.pfb) = %{tl_version}
Provides:       tex(rpxsc.pfb) = %{tl_version}, tex(p1xb.vf) = %{tl_version}
Provides:       tex(p1xbi.vf) = %{tl_version}, tex(p1xbsc.vf) = %{tl_version}
Provides:       tex(p1xbsl.vf) = %{tl_version}, tex(p1xi.vf) = %{tl_version}
Provides:       tex(p1xr.vf) = %{tl_version}, tex(p1xsc.vf) = %{tl_version}
Provides:       tex(p1xsl.vf) = %{tl_version}, tex(pcxb.vf) = %{tl_version}
Provides:       tex(pcxbi.vf) = %{tl_version}, tex(pcxbsl.vf) = %{tl_version}
Provides:       tex(pcxi.vf) = %{tl_version}, tex(pcxr.vf) = %{tl_version}
Provides:       tex(pcxsl.vf) = %{tl_version}, tex(pxb.vf) = %{tl_version}
Provides:       tex(pxbi.vf) = %{tl_version}, tex(pxbmi.vf) = %{tl_version}
Provides:       tex(pxbmi1.vf) = %{tl_version}, tex(pxbsc.vf) = %{tl_version}
Provides:       tex(pxbsl.vf) = %{tl_version}, tex(pxi.vf) = %{tl_version}
Provides:       tex(pxmi.vf) = %{tl_version}, tex(pxmi1.vf) = %{tl_version}
Provides:       tex(pxr.vf) = %{tl_version}, tex(pxsc.vf) = %{tl_version}
Provides:       tex(pxsl.vf) = %{tl_version}, tex(omlpxmi.fd) = %{tl_version}
Provides:       tex(omlpxr.fd) = %{tl_version}, tex(omspxr.fd) = %{tl_version}
Provides:       tex(omspxsy.fd) = %{tl_version}, tex(omxpxex.fd) = %{tl_version}
Provides:       tex(ot1pxr.fd) = %{tl_version}, tex(ot1pxss.fd) = %{tl_version}
Provides:       tex(ot1pxtt.fd) = %{tl_version}, tex(pxfonts.sty) = %{tl_version}
Provides:       tex(t1pxr.fd) = %{tl_version}, tex(t1pxss.fd) = %{tl_version}
Provides:       tex(t1pxtt.fd) = %{tl_version}, tex(ts1pxr.fd) = %{tl_version}
Provides:       tex(ts1pxss.fd) = %{tl_version}, tex(ts1pxtt.fd) = %{tl_version}
Provides:       tex(upxexa.fd) = %{tl_version}, tex(upxmia.fd) = %{tl_version}
Provides:       tex(upxr.fd) = %{tl_version}, tex(upxss.fd) = %{tl_version}
Provides:       tex(upxsya.fd) = %{tl_version}, tex(upxsyb.fd) = %{tl_version}
Provides:       tex(upxsyc.fd) = %{tl_version}, tex(upxtt.fd) = %{tl_version}

%description -n texlive-pxfonts
Pxfonts supplies virtual text roman fonts using Adobe Palatino
(or URWPalladioL) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Palatino/Palladio; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set
derived from the parallel TX font set. All the fonts are in
Type 1 format (AFM and PFB files), and are supported by TeX
metrics (VF and TFM files) and macros for use with LaTeX.

%package -n texlive-pxfonts-doc
Summary:        Documentation for pxfonts
Version:        svn15878.0

Provides:       tex-pxfonts-doc
AutoReqProv:    No

%description -n texlive-pxfonts-doc
Documentation for pxfonts

%package -n texlive-pas-crosswords
Provides:       tex-pas-crosswords = %{tl_version}
License:        LPPL
Summary:        Creating crossword grids, using TikZ
Version:        svn32313.1.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(xstring.sty), tex(tikz.sty), tex(multido.sty)
Requires:       tex(fp.sty)
Provides:       tex(pas-crosswords.sty) = %{tl_version}

%description -n texlive-pas-crosswords
The package produces crossword grids, using a wide variety of
colours and decorations of the grids and the text in them. The
package uses TikZ for its graphical output.

%package -n texlive-pas-crosswords-doc
Summary:        Documentation for pas-crosswords
Version:        svn32313.1.03

Provides:       tex-pas-crosswords-doc
AutoReqProv:    No

%description -n texlive-pas-crosswords-doc
Documentation for pas-crosswords

%package -n texlive-psgo
Provides:       tex-psgo = %{tl_version}
License:        LPPL
Summary:        Typeset go diagrams with PSTricks
Version:        svn15878.0.17

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-node.sty), tex(calc.sty), tex(ifthen.sty)
Provides:       tex(psgo.sty) = %{tl_version}

%description -n texlive-psgo
psgo package

%package -n texlive-psgo-doc
Summary:        Documentation for psgo
Version:        svn15878.0.17

Provides:       tex-psgo-doc
AutoReqProv:    No

%description -n texlive-psgo-doc
Documentation for psgo

%package -n texlive-pdf-trans
Provides:       tex-pdf-trans = %{tl_version}
License:        Public Domain
Summary:        A set of macros for various transformations of TeX boxes
Version:        svn32809.2.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pdf-trans.tex) = %{tl_version}

%description -n texlive-pdf-trans
pdf-trans is a set of macros offering various transformations
of TeX boxes (based on plain and pdfeTeX primitives). It was
initially inspired by trans.tex, remade to work with pdfTeX.

%package -n texlive-pdf-trans-doc
Summary:        Documentation for pdf-trans
Version:        svn32809.2.4

Provides:       tex-pdf-trans-doc
AutoReqProv:    No

%description -n texlive-pdf-trans-doc
Documentation for pdf-trans

%package -n texlive-plainpkg
Provides:       tex-plainpkg = %{tl_version}
License:        LPPL 1.3
Summary:        A minimal method for making generic packages
Version:        svn27765.0.4a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(plainpkg.tex) = %{tl_version}

%description -n texlive-plainpkg
The package provides a minimal method for making generic (i.e.,
TeX-format-independent) packaged, combining maybeload
functionality, fallback definitions for LaTeX \ProvidesPackage
and \RequirePackage functionality, and handling of arbitrary
(multiple) "private letters" (analagous LaTeX packages' use of
"@") in nested package files. The documentation contains a
central reference for making and using generic packages based
on the package.

%package -n texlive-plainpkg-doc
Summary:        Documentation for plainpkg
Version:        svn27765.0.4a

Provides:       tex-plainpkg-doc
AutoReqProv:    No

%description -n texlive-plainpkg-doc
Documentation for plainpkg

%package -n texlive-path
Provides:       tex-path = %{tl_version}
License:        Bibtex
Summary:        Typeset paths, making them breakable
Version:        svn22045.3.05

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(path.sty) = %{tl_version}

%description -n texlive-path
Defines a macro \path|...|, similar to the LaTeX \verb|...|,
that sets the text in typewriter font and allows hyphen-less
breaks at punctuation characters. The set of characters to be
regarded as punctuation may be changed from the package's
default.

%package -n texlive-path-doc
Summary:        Documentation for path
Version:        svn22045.3.05

Provides:       tex-path-doc
AutoReqProv:    No

%description -n texlive-path-doc
Documentation for path

%package -n texlive-passivetex
Provides:       tex-passivetex = %{tl_version}
License:        MIT
Summary:        Support package for XML/SGML typesetting
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(multicol.sty), tex(rotating.sty), tex(array.sty)
Requires:       tex(amsmath.sty), tex(longtable.sty), tex(url.sty), tex(ulem.sty)
Requires:       tex(color.sty), tex(times.sty), tex(unicode.sty), tex(marvosym.sty)
Requires:       tex(nameref.sty), tex(hyperref.sty), tex(ifthen.sty), tex(fontenc.sty)
Requires:       tex(tipa.sty), tex(tone.sty), tex(amssymb.sty), tex(bm.sty)
Requires:       tex(textcomp.sty), tex(pifont.sty)
Provides:       tex(dummyels.sty) = %{tl_version}, tex(fotex.sty) = %{tl_version}
Provides:       tex(mlnames.sty) = %{tl_version}, tex(teixml.sty) = %{tl_version}
Provides:       tex(teixmlslides.sty) = %{tl_version}, tex(ucharacters.sty) = %{tl_version}
Provides:       tex(unicode.sty) = %{tl_version}

%description -n texlive-passivetex
Packages providing XML parsing, UTF-8 parsing, Unicode
entities, and common formatting object definitions for jadetex.

%package -n texlive-parallel
Provides:       tex-parallel = %{tl_version}
License:        LPPL
Summary:        Typeset parallel texts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(parallel.sty) = %{tl_version}

%description -n texlive-parallel
Provides a parallel environment which allows two potentially
different texts to be typeset in two columns, while maintaining
alignment. The two columns may be on the same page, or on
facing pages. This arrangement of text is commonly used when
typesetting translations, but it can have value when comparing
any two texts.

%package -n texlive-parallel-doc
Summary:        Documentation for parallel
Version:        svn15878.0

Provides:       tex-parallel-doc
AutoReqProv:    No

%description -n texlive-parallel-doc
Documentation for parallel

%package -n texlive-parrun
Provides:       tex-parrun = %{tl_version}
License:        LPPL
Summary:        Typesets (two) streams of text running parallel
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty)
Provides:       tex(parrun.sty) = %{tl_version}

%description -n texlive-parrun
For typesetting translated text and the original source,
parallel on the same page, one above the other.

%package -n texlive-parrun-doc
Summary:        Documentation for parrun
Version:        svn15878.0

Provides:       tex-parrun-doc
AutoReqProv:    No

%description -n texlive-parrun-doc
Documentation for parrun

%package -n texlive-phonrule
Provides:       tex-phonrule = %{tl_version}
License:        LPPL
Summary:        Typeset linear phonological rules
Version:        svn43963
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pbox.sty)
Provides:       tex(phonrule.sty) = %{tl_version}

%description -n texlive-phonrule
The package provides macros for typesetting phonological rules
like those in 'Sound Pattern of English' (Chomsky and Halle
1968).

%package -n texlive-phonrule-doc
Summary:        Documentation for phonrule
Version:        svn43963
Provides:       tex-phonrule-doc
AutoReqProv:    No

%description -n texlive-phonrule-doc
Documentation for phonrule

%package -n texlive-plari
Provides:       tex-plari = %{tl_version}
License:        GPL+
Summary:        Typesetting stageplay scripts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(plari.cls) = %{tl_version}

%description -n texlive-plari
Plari (the name comes from the Finnish usage for the working
copy of a play) is a report-alike class, without section
headings, and with paragraphs vertically separated rather than
indented.

%package -n texlive-plari-doc
Summary:        Documentation for plari
Version:        svn15878.0

Provides:       tex-plari-doc
AutoReqProv:    No

%description -n texlive-plari-doc
Documentation for plari

%package -n texlive-play
Provides:       tex-play = %{tl_version}
License:        LPPL
Summary:        Typeset drama using LaTeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(play.cls) = %{tl_version}, tex(play.sty) = %{tl_version}

%description -n texlive-play
A class and style file that supports the typesetting of plays,
including options for line numbering.

%package -n texlive-play-doc
Summary:        Documentation for play
Version:        svn15878.0

Provides:       tex-play-doc
AutoReqProv:    No

%description -n texlive-play-doc
Documentation for play

%package -n texlive-poemscol
Provides:       tex-poemscol = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting Critical Editions of Poetry
Version:        svn46433
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(poemscol.sty) = %{tl_version}

%description -n texlive-poemscol
The package offers LaTeX macros for typesetting critical
editions of poetry. Its features include automatic
linenumbering, generation of separate endnotes sections for
emendations, textual collations, and explanatory notes, special
marking for cases in which page breaks occur during stanza
breaks, running headers of the form 'Notes to pp. xx-yy' for
the notes sections, index of titles and first lines, and
automatic generation of a table of contents.

%package -n texlive-poemscol-doc
Summary:        Documentation for poemscol
Version:        svn46433
Provides:       tex-poemscol-doc
AutoReqProv:    No

%description -n texlive-poemscol-doc
Documentation for poemscol

%package -n texlive-poetrytex
Provides:       tex-poetrytex = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset anthologies of poetry
Version:        svn39921

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(tocloft.sty)
Provides:       tex(poetrytex.sty) = %{tl_version}

%description -n texlive-poetrytex
The package is designed to aid in the management and formatting
of anthologies of poetry and other writings; it does not
concern itself with actually typesettinig the verse itself.

%package -n texlive-poetrytex-doc
Summary:        Documentation for poetrytex
Version:        svn39921

Provides:       tex-poetrytex-doc
AutoReqProv:    No

%description -n texlive-poetrytex-doc
Documentation for poetrytex

%package -n texlive-persian-bib
Provides:       tex-persian-bib = %{tl_version}
License:        LPPL 1.3
Summary:        Persian translations of classic BibTeX styles
Version:        svn37297.0.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-persian-bib
Currently 9 files: acm-fa.bst, asa-fa.bst, chicago-fa.bst,
ieeetr-fa.bst, plain-fa-inLTR-beamer.bst, plain-fa-inLTR.bst,
plain-fa.bst, plainnat-fa.bst and unsrt-fa.bst are modified for
Persian documents prepared with XePersian (which the present
package depends on). The Persian .bst files can simultaneously
handle both Latin and Persian references. A file cp1256fa.csf
is provided for correct sorting of Persian references and three
fields LANGUAGE, TRANSLATOR and AUTHORFA are defined.

%package -n texlive-persian-bib-doc
Summary:        Documentation for persian-bib
Version:        svn37297.0.9

Provides:       tex-persian-bib-doc
AutoReqProv:    No

%description -n texlive-persian-bib-doc
Documentation for persian-bib

%package -n texlive-pst-eucl-translation-bg-doc
Summary:        Documentation for pst-eucl-translation-bg
Version:        svn19296.1.3.2

Provides:       tex-pst-eucl-translation-bg-doc
AutoReqProv:    No

%description -n texlive-pst-eucl-translation-bg-doc
Documentation for pst-eucl-translation-bg

%package -n texlive-patgen2-tutorial-doc
Summary:        Documentation for patgen2-tutorial
Version:        svn16490.0

Provides:       tex-patgen2-tutorial-doc
AutoReqProv:    No

%description -n texlive-patgen2-tutorial-doc
Documentation for patgen2-tutorial

%package -n texlive-pictexsum-doc
Summary:        Documentation for pictexsum
Version:        svn24965.0

Provides:       tex-pictexsum-doc
AutoReqProv:    No

%description -n texlive-pictexsum-doc
Documentation for pictexsum

%package -n texlive-plain-doc-doc
Summary:        Documentation for plain-doc
Version:        svn28424.0

Provides:       tex-plain-doc-doc
AutoReqProv:    No

%description -n texlive-plain-doc-doc
Documentation for plain-doc

%package -n texlive-pl
Provides:       tex-pl = %{tl_version}
License:        Public Domain
Summary:        Polish extension of Computer Modern fonts
Version:        svn36012.1.09

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(plin.enc) = %{tl_version}, tex(plit.enc) = %{tl_version}
Provides:       tex(plitt.enc) = %{tl_version}, tex(plme.enc) = %{tl_version}
Provides:       tex(plmi.enc) = %{tl_version}, tex(plms.enc) = %{tl_version}
Provides:       tex(plrm.enc) = %{tl_version}, tex(plsc.enc) = %{tl_version}
Provides:       tex(plte.enc) = %{tl_version}, tex(pltt.enc) = %{tl_version}
Provides:       tex(plother.map) = %{tl_version}, tex(pltext.map) = %{tl_version}
Provides:       tex(plb10.tfm) = %{tl_version}, tex(plbsy10.tfm) = %{tl_version}
Provides:       tex(plbsy5.tfm) = %{tl_version}, tex(plbsy7.tfm) = %{tl_version}
Provides:       tex(plbx10.tfm) = %{tl_version}, tex(plbx12.tfm) = %{tl_version}
Provides:       tex(plbx5.tfm) = %{tl_version}, tex(plbx6.tfm) = %{tl_version}
Provides:       tex(plbx7.tfm) = %{tl_version}, tex(plbx8.tfm) = %{tl_version}
Provides:       tex(plbx9.tfm) = %{tl_version}, tex(plbxsl10.tfm) = %{tl_version}
Provides:       tex(plbxti10.tfm) = %{tl_version}, tex(plcsc10.tfm) = %{tl_version}
Provides:       tex(pldunh10.tfm) = %{tl_version}, tex(plex10.tfm) = %{tl_version}
Provides:       tex(plex9.tfm) = %{tl_version}, tex(plff10.tfm) = %{tl_version}
Provides:       tex(plfi10.tfm) = %{tl_version}, tex(plfib8.tfm) = %{tl_version}
Provides:       tex(plinch.tfm) = %{tl_version}, tex(plitt10.tfm) = %{tl_version}
Provides:       tex(plmi10.tfm) = %{tl_version}, tex(plmi12.tfm) = %{tl_version}
Provides:       tex(plmi5.tfm) = %{tl_version}, tex(plmi6.tfm) = %{tl_version}
Provides:       tex(plmi7.tfm) = %{tl_version}, tex(plmi8.tfm) = %{tl_version}
Provides:       tex(plmi9.tfm) = %{tl_version}, tex(plmib10.tfm) = %{tl_version}
Provides:       tex(plmib5.tfm) = %{tl_version}, tex(plmib7.tfm) = %{tl_version}
Provides:       tex(plr10.tfm) = %{tl_version}, tex(plr12.tfm) = %{tl_version}
Provides:       tex(plr17.tfm) = %{tl_version}, tex(plr5.tfm) = %{tl_version}
Provides:       tex(plr6.tfm) = %{tl_version}, tex(plr7.tfm) = %{tl_version}
Provides:       tex(plr8.tfm) = %{tl_version}, tex(plr9.tfm) = %{tl_version}
Provides:       tex(plsl10.tfm) = %{tl_version}, tex(plsl12.tfm) = %{tl_version}
Provides:       tex(plsl8.tfm) = %{tl_version}, tex(plsl9.tfm) = %{tl_version}
Provides:       tex(plsltt10.tfm) = %{tl_version}, tex(plss10.tfm) = %{tl_version}
Provides:       tex(plss12.tfm) = %{tl_version}, tex(plss17.tfm) = %{tl_version}
Provides:       tex(plss8.tfm) = %{tl_version}, tex(plss9.tfm) = %{tl_version}
Provides:       tex(plssbi10.tfm) = %{tl_version}, tex(plssbx10.tfm) = %{tl_version}
Provides:       tex(plssdc10.tfm) = %{tl_version}, tex(plssi10.tfm) = %{tl_version}
Provides:       tex(plssi12.tfm) = %{tl_version}, tex(plssi17.tfm) = %{tl_version}
Provides:       tex(plssi8.tfm) = %{tl_version}, tex(plssi9.tfm) = %{tl_version}
Provides:       tex(plssq8.tfm) = %{tl_version}, tex(plssqi8.tfm) = %{tl_version}
Provides:       tex(plsy10.tfm) = %{tl_version}, tex(plsy5.tfm) = %{tl_version}
Provides:       tex(plsy6.tfm) = %{tl_version}, tex(plsy7.tfm) = %{tl_version}
Provides:       tex(plsy8.tfm) = %{tl_version}, tex(plsy9.tfm) = %{tl_version}
Provides:       tex(pltcsc10.tfm) = %{tl_version}, tex(pltex10.tfm) = %{tl_version}
Provides:       tex(pltex8.tfm) = %{tl_version}, tex(pltex9.tfm) = %{tl_version}
Provides:       tex(plti10.tfm) = %{tl_version}, tex(plti12.tfm) = %{tl_version}
Provides:       tex(plti7.tfm) = %{tl_version}, tex(plti8.tfm) = %{tl_version}
Provides:       tex(plti9.tfm) = %{tl_version}, tex(pltt10.tfm) = %{tl_version}
Provides:       tex(pltt12.tfm) = %{tl_version}, tex(pltt8.tfm) = %{tl_version}
Provides:       tex(pltt9.tfm) = %{tl_version}, tex(plu10.tfm) = %{tl_version}
Provides:       tex(plvtt10.tfm) = %{tl_version}, tex(plb10.pfb) = %{tl_version}
Provides:       tex(plbsy10.pfb) = %{tl_version}, tex(plbx10.pfb) = %{tl_version}
Provides:       tex(plbx12.pfb) = %{tl_version}, tex(plbx5.pfb) = %{tl_version}
Provides:       tex(plbx6.pfb) = %{tl_version}, tex(plbx7.pfb) = %{tl_version}
Provides:       tex(plbx8.pfb) = %{tl_version}, tex(plbx9.pfb) = %{tl_version}
Provides:       tex(plbxsl10.pfb) = %{tl_version}, tex(plbxti10.pfb) = %{tl_version}
Provides:       tex(plcsc10.pfb) = %{tl_version}, tex(pldunh10.pfb) = %{tl_version}
Provides:       tex(plex10.pfb) = %{tl_version}, tex(plex9.pfb) = %{tl_version}
Provides:       tex(plff10.pfb) = %{tl_version}, tex(plfi10.pfb) = %{tl_version}
Provides:       tex(plfib8.pfb) = %{tl_version}, tex(plinch.pfb) = %{tl_version}
Provides:       tex(plitt10.pfb) = %{tl_version}, tex(plmi10.pfb) = %{tl_version}
Provides:       tex(plmi12.pfb) = %{tl_version}, tex(plmi5.pfb) = %{tl_version}
Provides:       tex(plmi6.pfb) = %{tl_version}, tex(plmi7.pfb) = %{tl_version}
Provides:       tex(plmi8.pfb) = %{tl_version}, tex(plmi9.pfb) = %{tl_version}
Provides:       tex(plmib10.pfb) = %{tl_version}, tex(plr10.pfb) = %{tl_version}
Provides:       tex(plr12.pfb) = %{tl_version}, tex(plr17.pfb) = %{tl_version}
Provides:       tex(plr5.pfb) = %{tl_version}, tex(plr6.pfb) = %{tl_version}
Provides:       tex(plr7.pfb) = %{tl_version}, tex(plr8.pfb) = %{tl_version}
Provides:       tex(plr9.pfb) = %{tl_version}, tex(plsl10.pfb) = %{tl_version}
Provides:       tex(plsl12.pfb) = %{tl_version}, tex(plsl8.pfb) = %{tl_version}
Provides:       tex(plsl9.pfb) = %{tl_version}, tex(plsltt10.pfb) = %{tl_version}
Provides:       tex(plss10.pfb) = %{tl_version}, tex(plss12.pfb) = %{tl_version}
Provides:       tex(plss17.pfb) = %{tl_version}, tex(plss8.pfb) = %{tl_version}
Provides:       tex(plss9.pfb) = %{tl_version}, tex(plssbi10.pfb) = %{tl_version}
Provides:       tex(plssbx10.pfb) = %{tl_version}, tex(plssdc10.pfb) = %{tl_version}
Provides:       tex(plssi10.pfb) = %{tl_version}, tex(plssi12.pfb) = %{tl_version}
Provides:       tex(plssi17.pfb) = %{tl_version}, tex(plssi8.pfb) = %{tl_version}
Provides:       tex(plssi9.pfb) = %{tl_version}, tex(plssq8.pfb) = %{tl_version}
Provides:       tex(plssqi8.pfb) = %{tl_version}, tex(plsy10.pfb) = %{tl_version}
Provides:       tex(plsy5.pfb) = %{tl_version}, tex(plsy6.pfb) = %{tl_version}
Provides:       tex(plsy7.pfb) = %{tl_version}, tex(plsy8.pfb) = %{tl_version}
Provides:       tex(plsy9.pfb) = %{tl_version}, tex(pltcsc10.pfb) = %{tl_version}
Provides:       tex(pltex10.pfb) = %{tl_version}, tex(pltex8.pfb) = %{tl_version}
Provides:       tex(pltex9.pfb) = %{tl_version}, tex(plti10.pfb) = %{tl_version}
Provides:       tex(plti12.pfb) = %{tl_version}, tex(plti7.pfb) = %{tl_version}
Provides:       tex(plti8.pfb) = %{tl_version}, tex(plti9.pfb) = %{tl_version}
Provides:       tex(pltt10.pfb) = %{tl_version}, tex(pltt12.pfb) = %{tl_version}
Provides:       tex(pltt8.pfb) = %{tl_version}, tex(pltt9.pfb) = %{tl_version}
Provides:       tex(plu10.pfb) = %{tl_version}, tex(plvtt10.pfb) = %{tl_version}

%description -n texlive-pl
The Polish extension of the Computer Modern fonts (compatible
with CM itself) for use with Polish TeX formats. The fonts were
originally a part of the MeX distribution (and they are still
available that way).

%package -n texlive-pl-doc
Summary:        Documentation for pl
Version:        svn36012.1.09

Provides:       tex-pl-doc
AutoReqProv:    No

%description -n texlive-pl-doc
Documentation for pl

%package -n texlive-polski
Provides:       tex-polski = %{tl_version}
License:        LPPL 1.2
Summary:        Typeset Polish documents with LaTeX and Polish fonts
Version:        svn44213
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-pl, tex-hyphen-polish
Provides:       tex(amigapl.def) = %{tl_version}, tex(mazovia.def) = %{tl_version}
Provides:       tex(omlplcm.fd) = %{tl_version}, tex(omlplm.fd) = %{tl_version}
Provides:       tex(omsplsy.fd) = %{tl_version}, tex(omxplex.fd) = %{tl_version}
Provides:       tex(ot1patch.sty) = %{tl_version}, tex(ot4ccr.fd) = %{tl_version}
Provides:       tex(ot4cmdh.fd) = %{tl_version}, tex(ot4cmfib.fd) = %{tl_version}
Provides:       tex(ot4cmfr.fd) = %{tl_version}, tex(ot4cmr.fd) = %{tl_version}
Provides:       tex(ot4cmss.fd) = %{tl_version}, tex(ot4cmtt.fd) = %{tl_version}
Provides:       tex(plprefix.sty) = %{tl_version}, tex(polski.sty) = %{tl_version}
Provides:       tex(qxenc.def) = %{tl_version}

%description -n texlive-polski
Tools to typeset documents in Polish using LaTeX2e with Polish
fonts (the so-called PL fonts), EC fonts or CM fonts. (This
package was previously known as platex, but has been renamed to
resolve a name clash.)

%package -n texlive-polski-doc
Summary:        Documentation for polski
Version:        svn44213
Provides:       tex-polski-doc
AutoReqProv:    No
Requires:       tex-pl-doc

%description -n texlive-polski-doc
Documentation for polski

%package -n texlive-parskip
Provides:       tex-parskip = %{tl_version}
License:        LPPL
Summary:        Layout with zero \parindent, non-zero \parskip
Version:        svn19963.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(parskip.sty) = %{tl_version}

%description -n texlive-parskip
Simply changing \parskip and \parindent leaves a layout that is
untidy; this package (though it is no substitute for a properly-
designed class) helps alleviate this untidiness

%package -n texlive-parskip-doc
Summary:        Documentation for parskip
Version:        svn19963.2.0

Provides:       tex-parskip-doc
AutoReqProv:    No

%description -n texlive-parskip-doc
Documentation for parskip

%package -n texlive-pdfpages
Provides:       tex-pdfpages = %{tl_version}
License:        LPPL 1.3
Summary:        Include PDF documents in LaTeX
Version:        svn45659
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-eso-pic, tex(ifthen.sty), tex(calc.sty), tex(eso-pic.sty)
Requires:       tex(graphicx.sty), tex(count1to.sty), tex(pdflscape.sty)
Provides:       tex(pdfpages.sty) = %{tl_version}, tex(ppdvipdfmx.def) = %{tl_version}
Provides:       tex(ppdvips.def) = %{tl_version}, tex(ppluatex.def) = %{tl_version}
Provides:       tex(ppnull.def) = %{tl_version}, tex(pppdftex.def) = %{tl_version}
Provides:       tex(ppvtex.def) = %{tl_version}, tex(ppxetex.def) = %{tl_version}

%description -n texlive-pdfpages
This package simplifies the inclusion of external multi-page
PDF documents in LaTeX documents. Pages may be freely selected
and similar to psnup it is possible to put several logical
pages onto each sheet of paper. Furthermore a lot of hypertext
features like hyperlinks and article threads are provided. The
package supports pdfTeX (pdfLaTeX) and VTeX. With VTeX it is
even possible to use this package to insert PostScript files,
in addition to PDF files.

%package -n texlive-pdfpages-doc
Summary:        Documentation for pdfpages
Version:        svn45659
Provides:       tex-pdfpages-doc
AutoReqProv:    No
Requires:       tex-eso-pic-doc

%description -n texlive-pdfpages-doc
Documentation for pdfpages

%package -n texlive-powerdot
Provides:       tex-powerdot = %{tl_version}
License:        LPPL 1.3
Summary:        A presentation class
Version:        svn45165
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(times.sty), tex(pifont.sty), tex(pst-grad.sty), tex(pst-blur.sty)
Requires:       tex(calc.sty), tex(pst-slpe.sty), tex(pst-char.sty), tex(type1cm.sty)
Requires:       tex(amssymb.sty), tex(xkeyval.sty), tex(geometry.sty), tex(ifxetex.sty)
Requires:       tex(hyperref.sty), tex(graphicx.sty), tex(pstricks.sty), tex(xcolor.sty)
Requires:       tex(enumitem.sty), tex(verbatim.sty)
Provides:       tex(powerdot-aggie.sty) = %{tl_version}, tex(powerdot-bframe.sty) = %{tl_version}
Provides:       tex(powerdot-ciment.sty) = %{tl_version}
Provides:       tex(powerdot-default.sty) = %{tl_version}
Provides:       tex(powerdot-elcolors.sty) = %{tl_version}
Provides:       tex(powerdot-fyma.sty) = %{tl_version}, tex(powerdot-horatio.sty) = %{tl_version}
Provides:       tex(powerdot-husky.sty) = %{tl_version}, tex(powerdot-ikeda.sty) = %{tl_version}
Provides:       tex(powerdot-jefka.sty) = %{tl_version}, tex(powerdot-klope.sty) = %{tl_version}
Provides:       tex(powerdot-paintings.sty) = %{tl_version}
Provides:       tex(powerdot-pazik.sty) = %{tl_version}, tex(powerdot-sailor.sty) = %{tl_version}
Provides:       tex(powerdot-simple.sty) = %{tl_version}
Provides:       tex(powerdot-tycja.sty) = %{tl_version}, tex(powerdot-upen.sty) = %{tl_version}
Provides:       tex(powerdot.cls) = %{tl_version}

%description -n texlive-powerdot
Powerdot is a presentation class for LaTeX that allows for the
quick and easy development of professional presentations. It
comes with many tools that enhance presentations and aid the
presenter. Examples are automatic overlays, personal notes and
a handout mode. To view a presentation, DVI, PS or PDF output
can be used. A powerful template system is available to easily
develop new styles. A LyX layout file is provided.

%package -n texlive-powerdot-doc
Summary:        Documentation for powerdot
Version:        svn45165
Provides:       tex-powerdot-doc
AutoReqProv:    No

%description -n texlive-powerdot-doc
Documentation for powerdot

%package -n texlive-psfrag
Provides:       tex-psfrag = %{tl_version}
License:        psfrag
Summary:        Replace strings in encapsulated PostScript figures
Version:        svn15878.3.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(psfrag.sty) = %{tl_version}

%description -n texlive-psfrag
Allows LaTeX constructions (equations, picture environments,
etc.) to be precisely superimposed over Encapsulated PostScript
figures, using your own favorite drawing tool to create an EPS
figure and placing simple text 'tags' where each replacement is
to be placed, with PSfrag automatically removing these tags
from the figure and replacing them with a user specified LaTeX
construction, properly aligned, scaled, and/or rotated.

%package -n texlive-psfrag-doc
Summary:        Documentation for psfrag
Version:        svn15878.3.04

Provides:       tex-psfrag-doc
AutoReqProv:    No

%description -n texlive-psfrag-doc
Documentation for psfrag

%package -n texlive-pb-diagram
Provides:       tex-pb-diagram = %{tl_version}
License:        GPLv2+
Summary:        A commutative diagram package using LAMSTeX or Xy-pic fonts
Version:        svn15878.5.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lamsarrow.sty) = %{tl_version}, tex(pb-diagram.sty) = %{tl_version}
Provides:       tex(pb-lams.sty) = %{tl_version}, tex(pb-xy.sty) = %{tl_version}

%description -n texlive-pb-diagram
pb-diagram package

%package -n texlive-pb-diagram-doc
Summary:        Documentation for pb-diagram
Version:        svn15878.5.0

Provides:       tex-pb-diagram-doc
AutoReqProv:    No

%description -n texlive-pb-diagram-doc
Documentation for pb-diagram

%package -n texlive-pgf-blur
Provides:       tex-pgf-blur = %{tl_version}
License:        LPPL
Summary:        PGF/TikZ package for "blurred" shadows
Version:        svn31693.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tikzlibraryshadows.blur.code.tex) = %{tl_version}

%description -n texlive-pgf-blur
The package adds blurred/faded/fuzzy shadows to PGF/TikZ
pictures. It is configured as a TikZ/PGF library module. The
method is similar to that of the author's pst-blur package for
PSTricks.

%package -n texlive-pgf-blur-doc
Summary:        Documentation for pgf-blur
Version:        svn31693.1.01

Provides:       tex-pgf-blur-doc
AutoReqProv:    No

%description -n texlive-pgf-blur-doc
Documentation for pgf-blur

%package -n texlive-pgf-soroban
Provides:       tex-pgf-soroban = %{tl_version}
License:        LPPL
Summary:        Create images of the soroban using TikZ/PGF
Version:        svn32269.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(ifthen.sty), tex(tikz.sty)
Provides:       tex(pgf-soroban.sty) = %{tl_version}

%description -n texlive-pgf-soroban
The package makes it possible to create pictures of the soroban
(Japanese abacus) using PGF/TikZ

%package -n texlive-pgf-soroban-doc
Summary:        Documentation for pgf-soroban
Version:        svn32269.1.1

Provides:       tex-pgf-soroban-doc
AutoReqProv:    No

%description -n texlive-pgf-soroban-doc
Documentation for pgf-soroban

%package -n texlive-pgf-umlcd
Provides:       tex-pgf-umlcd = %{tl_version}
License:        GPL+
Summary:        Some LaTeX macros for UML Class Diagrams
Version:        svn33307.0.2.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(pgf-umlcd.sty) = %{tl_version}

%description -n texlive-pgf-umlcd
Some LaTeX macros for UML Class Diagrams.pgf

%package -n texlive-pgf-umlcd-doc
Summary:        Documentation for pgf-umlcd
Version:        svn33307.0.2.1.1

Provides:       tex-pgf-umlcd-doc
AutoReqProv:    No

%description -n texlive-pgf-umlcd-doc
Documentation for pgf-umlcd

%package -n texlive-pgf-umlsd
Provides:       tex-pgf-umlsd = %{tl_version}
License:        GPL+
Summary:        Draw UML Sequence Diagrams
Version:        svn33045.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty)
Provides:       tex(pgf-umlsd.sty) = %{tl_version}

%description -n texlive-pgf-umlsd
LaTeX macros to draw UML diagrams using pgf

%package -n texlive-pgf-umlsd-doc
Summary:        Documentation for pgf-umlsd
Version:        svn33045.0.7

Provides:       tex-pgf-umlsd-doc
AutoReqProv:    No

%description -n texlive-pgf-umlsd-doc
Documentation for pgf-umlsd

%package -n texlive-pgfgantt
Provides:       tex-pgfgantt = %{tl_version}
License:        LPPL 1.3
Summary:        Draw Gantt charts with TikZ
Version:        svn46280
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(pgfcalendar.sty)
Provides:       tex(pgfgantt.sty) = %{tl_version}

%description -n texlive-pgfgantt
The package provides an environment for drawing Gantt charts
that contain various elements (titles, bars, milestones, groups
and links). Several keys customize the appearance of the chart
elements.

%package -n texlive-pgfgantt-doc
Summary:        Documentation for pgfgantt
Version:        svn46280
Provides:       tex-pgfgantt-doc
AutoReqProv:    No

%description -n texlive-pgfgantt-doc
Documentation for pgfgantt

%package -n texlive-pgfkeyx
Provides:       tex-pgfkeyx = %{tl_version}
License:        LPPL 1.3
Summary:        Extended and more robust version of pgfkeys
Version:        svn26093.0.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pdftexcmds.sty)
Provides:       tex(pgfkeyx.sty) = %{tl_version}

%description -n texlive-pgfkeyx
The package extends and improves the robustness of the pgfkeys
package. In particular, it can deal with active comma, equality
sign, and slash in key parsing. The difficulty with active
characters has long been a problem with the pgfkeys package.
The package also introduces handlers beyond those that pgfkeys
can offer.

%package -n texlive-pgfkeyx-doc
Summary:        Documentation for pgfkeyx
Version:        svn26093.0.0.1

Provides:       tex-pgfkeyx-doc
AutoReqProv:    No

%description -n texlive-pgfkeyx-doc
Documentation for pgfkeyx

%package -n texlive-pgfmolbio
Provides:       tex-pgfmolbio = %{tl_version}
License:        LPPL 1.3
Summary:        Draw graphs typically found in molecular biology texts
Version:        svn35152.0.21

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(luatexbase-modutils.sty)
Requires:       tex(xcolor.sty), tex(tikz.sty)
Provides:       tex(pgfmolbio.chromatogram.tex) = %{tl_version}
Provides:       tex(pgfmolbio.convert.tex) = %{tl_version}
Provides:       tex(pgfmolbio.domains.tex) = %{tl_version}
Provides:       tex(pgfmolbio.sty) = %{tl_version}

%description -n texlive-pgfmolbio
The package draws graphs typically found in molecular biology
texts. Currently, the package contains modules for drawing DNA
sequencing chromatograms and protein domain diagrams.

%package -n texlive-pgfmolbio-doc
Summary:        Documentation for pgfmolbio
Version:        svn35152.0.21

Provides:       tex-pgfmolbio-doc
AutoReqProv:    No

%description -n texlive-pgfmolbio-doc
Documentation for pgfmolbio

%package -n texlive-pgfopts
Provides:       tex-pgfopts = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX package options with pgfkeys
Version:        svn34573.2.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pgfkeys.sty)
Provides:       tex(pgfopts.sty) = %{tl_version}

%description -n texlive-pgfopts
The pgfkeys package (part of the pgf distribution) is a well-
designed way of defining and using large numbers of keys for
key-value syntaxes. However, pgfkeys itself does not offer
means of handling LaTeX class and package options. This package
adds such option handling to pgfkeys, in the same way that
kvoptions adds the same facility to the LaTeX standard keyval
package.

%package -n texlive-pgfopts-doc
Summary:        Documentation for pgfopts
Version:        svn34573.2.1a

Provides:       tex-pgfopts-doc
AutoReqProv:    No

%description -n texlive-pgfopts-doc
Documentation for pgfopts

%package -n texlive-pgfplots
Provides:       tex-pgfplots = %{tl_version}
License:        GPLv3+
Summary:        Create normal/logarithmic plots in two and three dimensions
Version:        svn47373
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty), tex(listings.sty), tex(hyperref.sty), tex(tikz.sty)
Requires:       tex(luatexbase.sty), tex(array.sty)
Provides:       tex(t-pgfplots.tex) = %{tl_version}, tex(t-pgfplotstable.tex) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.code.tex) = %{tl_version}
Provides:       tex(pgfplotslibrary.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.colormaps.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.dateplot.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.decorations.softclip.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.external.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.fillbetween.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.groupplots.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.patchplots.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.polar.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.smithchart.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.statistics.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.ternary.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplots.units.code.tex) = %{tl_version}
Provides:       tex(pgfplotsarray.code.tex) = %{tl_version}
Provides:       tex(pgfplotsdeque.code.tex) = %{tl_version}
Provides:       tex(pgfplotsliststructure.code.tex) = %{tl_version}
Provides:       tex(pgfplotsliststructureext.code.tex) = %{tl_version}
Provides:       tex(pgfplotsmatrix.code.tex) = %{tl_version}
Provides:       tex(pgfplotstable.code.tex) = %{tl_version}
Provides:       tex(pgfplotstable.coltype.code.tex) = %{tl_version}
Provides:       tex(pgfplotstableshared.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_loader.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_misc.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfcoreexternal.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfcoreimage.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfcorelayers.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfcorescopes.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfkeys.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfkeysfiltered.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryfpu.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryintersections.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryluamath.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryplothandlers.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.pdflinks.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.prettyprinter.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfmathfloat.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_pgfutil-common-lists.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_tikzexternal.sty) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_tikzexternalshared.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_tikzlibraryexternal.code.tex) = %{tl_version}
Provides:       tex(pgfplotsoldpgfsupp_trig_format.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydateplot.code.tex) = %{tl_version}
Provides:       tex(pgflibraryfillbetween.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarydecorations.softclip.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfillbetween.code.tex) = %{tl_version}
Provides:       tex(pgfplots.code.tex) = %{tl_version}, tex(pgfplots.errorbars.code.tex) = %{tl_version}
Provides:       tex(pgfplots.markers.code.tex) = %{tl_version}
Provides:       tex(pgfplots.paths.code.tex) = %{tl_version}
Provides:       tex(pgfplots.revision.tex) = %{tl_version}
Provides:       tex(pgfplots.scaling.code.tex) = %{tl_version}
Provides:       tex(pgfplotscoordprocessing.code.tex) = %{tl_version}
Provides:       tex(pgfplotscore.code.tex) = %{tl_version}
Provides:       tex(pgfplotsmeshplothandler.code.tex) = %{tl_version}
Provides:       tex(pgfplotsplothandlers.code.tex) = %{tl_version}
Provides:       tex(pgfplotsstackedplots.code.tex) = %{tl_version}
Provides:       tex(pgfplotsticks.code.tex) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-dvipdfmx.def) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-dvips.def) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-pdftex.def) = %{tl_version}
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-xetex.def) = %{tl_version}
Provides:       tex(pgfplotssysgeneric.code.tex) = %{tl_version}
Provides:       tex(pgfplots.assert.code.tex) = %{tl_version}
Provides:       tex(pgfplots.assert.sty) = %{tl_version}
Provides:       tex(pgfplotsbinary.code.tex) = %{tl_version}
Provides:       tex(pgfplotsbinary.data.code.tex) = %{tl_version}
Provides:       tex(pgfplotscolor.code.tex) = %{tl_version}
Provides:       tex(pgfplotscolormap.code.tex) = %{tl_version}
Provides:       tex(pgfplotsutil.code.tex) = %{tl_version}
Provides:       tex(pgfplotsutil.verb.code.tex) = %{tl_version}
Provides:       tex(bugtracker.sty) = %{tl_version}, tex(tikzlibrarypgfplots.clickable.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarypgfplotsclickable.code.tex) = %{tl_version}
Provides:       tex(pgfplots.sty) = %{tl_version}, tex(pgfplotstable.sty) = %{tl_version}
Provides:       tex(pgfregressiontest.sty) = %{tl_version}
Provides:       tex(pgfplots.tex) = %{tl_version}, tex(pgfplotstable.tex) = %{tl_version}

%description -n texlive-pgfplots
PGFPlots draws high-quality function plots in normal or
logarithmic scaling with a user-friendly interface directly in
TeX. The user supplies axis labels, legend entries and the plot
coordinates for one or more plots and PGFPlots applies axis
scaling, computes any logarithms and axis ticks and draws the
plots, supporting line plots, scatter plots, piecewise constant
plots, bar plots, area plots, mesh-- and surface plots and some
more. Pgfplots is based on PGF/TikZ (pgf); it runs equally for
LaTeX/TeX/ConTeXt.

%package -n texlive-pgfplots-doc
Summary:        Documentation for pgfplots
Version:        svn47373
Provides:       tex-pgfplots-doc
AutoReqProv:    No

%description -n texlive-pgfplots-doc
Documentation for pgfplots

%package -n texlive-picinpar
Provides:       tex-picinpar = %{tl_version}
License:        GPL+
Summary:        Insert pictures into paragraphs
Version:        svn20374.1.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(picinpar.sty) = %{tl_version}

%description -n texlive-picinpar
A legacy package for creating 'windows' in paragraphs, for
inserting graphics, etc. (including "dropped capitals"). Users
should note that Piet van Oostrum (in a published review of
packages of this sort) does not recommend this package; Picins
is recommended instead.

%package -n texlive-picinpar-doc
Summary:        Documentation for picinpar
Version:        svn20374.1.2a

Provides:       tex-picinpar-doc
AutoReqProv:    No

%description -n texlive-picinpar-doc
Documentation for picinpar

%package -n texlive-pict2e
Provides:       tex-pict2e = %{tl_version}
License:        LPPL
Summary:        New implementation of picture commands
Version:        svn39591

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(trig.sty)
Provides:       tex(p2e-dvipdfm.def) = %{tl_version}, tex(p2e-dvipdfmx.def) = %{tl_version}
Provides:       tex(p2e-dvips.def) = %{tl_version}, tex(p2e-pctex32.def) = %{tl_version}
Provides:       tex(p2e-pctexps.def) = %{tl_version}, tex(p2e-pdftex.def) = %{tl_version}
Provides:       tex(p2e-textures.def) = %{tl_version}, tex(p2e-vtex.def) = %{tl_version}
Provides:       tex(p2e-xetex.def) = %{tl_version}, tex(pict2e.cfg) = %{tl_version}
Provides:       tex(pict2e.sty) = %{tl_version}

%description -n texlive-pict2e
This package was described in the 2nd edition of 'LaTeX: A
Document Preparation System', but the LaTeX project team
declined to produce the package. For a long time, LaTeX has
included a 'pict2e package' that merely produced an apologetic
error message. The new package extends the existing LaTeX
picture environment, using the familiar technique (cf. the
graphics and color packages) of driver files (at present,
drivers for PostScript output from LaTeX, and for use with
PDFLaTeX are available). The package documentation has a fair
number of examples of use, showing where things are improved by
comparison with the LaTeX picture environment.

%package -n texlive-pict2e-doc
Summary:        Documentation for pict2e
Version:        svn39591

Provides:       tex-pict2e-doc
AutoReqProv:    No

%description -n texlive-pict2e-doc
Documentation for pict2e

%package -n texlive-pictex
Provides:       tex-pictex = %{tl_version}
License:        LPPL
Summary:        Picture drawing macros for TeX and LaTeX
Version:        svn21943.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(errorbars.tex) = %{tl_version}, tex(latexpicobjs.tex) = %{tl_version}
Provides:       tex(piccorr.sty) = %{tl_version}, tex(picmore.tex) = %{tl_version}
Provides:       tex(pictex.sty) = %{tl_version}, tex(pictex.tex) = %{tl_version}
Provides:       tex(pictexwd.sty) = %{tl_version}, tex(pictexwd.tex) = %{tl_version}
Provides:       tex(pointers.tex) = %{tl_version}, tex(postpictex.tex) = %{tl_version}
Provides:       tex(prepictex.tex) = %{tl_version}, tex(texpictex.tex) = %{tl_version}
Provides:       tex(tree.sty) = %{tl_version}

%description -n texlive-pictex
PicTeX is an early, and very comprehensive drawing package,
that mostly draws by placing myriads of small dots to make up
pictures. It has a tendency to run out of space, most
especially of allowable dimensions registers; packages m-pictex
and pictexwd deal with the register problem, in different ways.
Note that full documentation may be bought via the PC-TeX site,
though a command summary is available as free software.
Alternatively, a front-end package such as mathsPiC, which
covers all of PicTeX and has a complete and free manual, could
be used.

%package -n texlive-pictex-doc
Summary:        Documentation for pictex
Version:        svn21943.1.1

Provides:       tex-pictex-doc
AutoReqProv:    No

%description -n texlive-pictex-doc
Documentation for pictex

%package -n texlive-pictex2
Provides:       tex-pictex2 = %{tl_version}
License:        LPPL
Summary:        Adds relative coordinates and improves the \plot command
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pictex.sty)
Provides:       tex(pictex2.sty) = %{tl_version}

%description -n texlive-pictex2
Adds two user commands to standard PiCTeX. One command uses
relative coordinates, thus eliminating the need to calculate
the coordinate of every point manually as in standard PiCTeX.
The other command modifies \plot to use a rule instead of dots
if the line segment is horizontal or vertical.

%package -n texlive-pinlabel
Provides:       tex-pinlabel = %{tl_version}
License:        LPPL
Summary:        A TeX labelling package
Version:        svn24769.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty)
Provides:       tex(pinlabel.sty) = %{tl_version}

%description -n texlive-pinlabel
Pinlabel is a labelling package for attaching perfectly
formatted TeX labels to figures and diagrams in both eps and
pdf formats. It is suitable both for labelling a new diagram
and for relabelling an existing diagram. The package uses
coordinates derived from GhostView (or gv) and labels are
placed with automatic and consistent spacing relative to the
object labelled.

%package -n texlive-pinlabel-doc
Summary:        Documentation for pinlabel
Version:        svn24769.1.2

Provides:       tex-pinlabel-doc
AutoReqProv:    No

%description -n texlive-pinlabel-doc
Documentation for pinlabel

%package -n texlive-pmgraph
Provides:       tex-pmgraph = %{tl_version}
License:        GPL+
Summary:        "Poor man's" graphics
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pmgraph.sty) = %{tl_version}

%description -n texlive-pmgraph
A set of extensions to LaTeX picture environment, including a
wider range of vectors, and a lot more box frame styles.

%package -n texlive-pmgraph-doc
Summary:        Documentation for pmgraph
Version:        svn15878.1.0

Provides:       tex-pmgraph-doc
AutoReqProv:    No

%description -n texlive-pmgraph-doc
Documentation for pmgraph

%package -n texlive-paralist
Provides:       tex-paralist = %{tl_version}
License:        LPPL
Summary:        Enumerate and itemize within paragraphs
Version:        svn43021
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(paralist.sty) = %{tl_version}

%description -n texlive-paralist
Provides enumerate and itemize environments that can be used
within paragraphs to format the items either as running text or
as separate paragraphs with a preceding number or symbol. Also
provides compacted versions of enumerate and itemize.

%package -n texlive-paralist-doc
Summary:        Documentation for paralist
Version:        svn43021
Provides:       tex-paralist-doc
AutoReqProv:    No

%description -n texlive-paralist-doc
Documentation for paralist

%package -n texlive-placeins
Provides:       tex-placeins = %{tl_version}
License:        Public Domain
Summary:        Control float placement
Version:        svn19848.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(placeins.sty) = %{tl_version}

%description -n texlive-placeins
Defines a \FloatBarrier command, beyond which floats may not
pass; useful, for example, to ensure all floats for a section
appear before the next \section command.

%package -n texlive-placeins-doc
Summary:        Documentation for placeins
Version:        svn19848.2.2

Provides:       tex-placeins-doc
AutoReqProv:    No

%description -n texlive-placeins-doc
Documentation for placeins

%package -n texlive-pagecolor
Provides:       tex-pagecolor = %{tl_version}
License:        LPPL 1.3
Summary:        Interrogate page colour
Version:        svn44487
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty), tex(color.sty), tex(xcolor.sty), tex(ifpdf.sty)
Requires:       tex(ifluatex.sty)
Provides:       tex(pagecolor.sty) = %{tl_version}

%description -n texlive-pagecolor
This package provides the command \thepagecolor, which gives
the current page (background) colour, i. e. the argument used
with the most recent call of \pagecolor{...}. The command
\thepagecolornone gives the same colour as \thepagecolor,
except when the page background colour is "none" (e.g., as a
result of using the \nopagecolor command). In that case
\thepagecolor is "white" and \thepagecolornone is "none".

%package -n texlive-pagecolor-doc
Summary:        Documentation for pagecolor
Version:        svn44487
Provides:       tex-pagecolor-doc
AutoReqProv:    No

%description -n texlive-pagecolor-doc
Documentation for pagecolor

%package -n texlive-pagecont
Provides:       tex-pagecont = %{tl_version}
License:        LPPL
Summary:        Page numbering that continues between documents
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(pagecont.sty) = %{tl_version}

%description -n texlive-pagecont
The package provides the facility that several documents can be
typeset independently with page numbers in sequence, as if they
were a single document.

%package -n texlive-pagecont-doc
Summary:        Documentation for pagecont
Version:        svn15878.1.0

Provides:       tex-pagecont-doc
AutoReqProv:    No

%description -n texlive-pagecont-doc
Documentation for pagecont

%package -n texlive-pagenote
Provides:       tex-pagenote = %{tl_version}
License:        LPPL 1.3
Summary:        Notes at end of document
Version:        svn15878.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifmtarg.sty)
Provides:       tex(pagenote.sty) = %{tl_version}

%description -n texlive-pagenote
The pagenote package provides tagged notes on a separate page
(also known as 'end notes'). Unless the memoir class is used,
the package requires the ifmtarg package.

%package -n texlive-pagenote-doc
Summary:        Documentation for pagenote
Version:        svn15878.1.1a

Provides:       tex-pagenote-doc
AutoReqProv:    No

%description -n texlive-pagenote-doc
Documentation for pagenote

%package -n texlive-pagerange
Provides:       tex-pagerange = %{tl_version}
License:        LPPL
Summary:        Flexible and configurable page range typesetting
Version:        svn16915.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(lastpage.sty), tex(xkeyval.sty)
Provides:       tex(pagerange-guide.cfg) = %{tl_version}
Provides:       tex(pagerange.sty) = %{tl_version}

%description -n texlive-pagerange
The package defines a command \pagerange that typesets ranges
of page numbers, expanding them (e.g., adding first or last
page numbers) and standardising them.

%package -n texlive-pagerange-doc
Summary:        Documentation for pagerange
Version:        svn16915.0.5

Provides:       tex-pagerange-doc
AutoReqProv:    No

%description -n texlive-pagerange-doc
Documentation for pagerange

%package -n texlive-pageslts
Provides:       tex-pageslts = %{tl_version}
License:        LPPL 1.3
Summary:        Variants of last page labels
Version:        svn39164

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ltxcmds.sty), tex(atveryend.sty), tex(everyshi.sty), tex(letltxmacro.sty)
Requires:       tex(kvoptions.sty), tex(undolabl.sty), tex(rerunfilecheck.sty), tex(alphalph.sty)
Provides:       tex(pageslts.sty) = %{tl_version}

%description -n texlive-pageslts
The package was designed as an extension of the lastpage
package -- as well as that package's LastPage label (created
\AtEndDocument) it adds a VeryLastPage (created
\AfterLastShipout). When more than one page numbering scheme is
in operation (as in a book class document with frontmatter),
the labels above do not give the total number of pages, so the
package also provides labels pagesLTS.<numbering scheme>, where
the numbering scheme is arabic, roman, etc. The package relies
on the undolabl package.

%package -n texlive-pageslts-doc
Summary:        Documentation for pageslts
Version:        svn39164

Provides:       tex-pageslts-doc
AutoReqProv:    No

%description -n texlive-pageslts-doc
Documentation for pageslts

%package -n texlive-paper
Provides:       tex-paper = %{tl_version}
License:        GPL+
Summary:        Versions of article class, tuned for scholarly publications
Version:        svn34521.1.0l

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(journal.cls) = %{tl_version}, tex(journal.sty) = %{tl_version}
Provides:       tex(paper.cls) = %{tl_version}, tex(paper.sty) = %{tl_version}

%description -n texlive-paper
A pair of classes derived from article, tuned for producing
papers for journals. The classes introduce new layout options
and font commands for sections/parts, and define a new keywords
environment, subtitle and institution commands for the title
section and new commands for revisions.

%package -n texlive-paper-doc
Summary:        Documentation for paper
Version:        svn34521.1.0l

Provides:       tex-paper-doc
AutoReqProv:    No

%description -n texlive-paper-doc
Documentation for paper

%package -n texlive-papercdcase
Provides:       tex-papercdcase = %{tl_version}
License:        LPPL
Summary:        Origami-style folding paper CD case
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(calc.sty)
Provides:       tex(papercdcase.sty) = %{tl_version}

%description -n texlive-papercdcase
This package implements a LaTeX style file to produce origami-
style folding paper CD cases.

%package -n texlive-papercdcase-doc
Summary:        Documentation for papercdcase
Version:        svn15878.0

Provides:       tex-papercdcase-doc
AutoReqProv:    No

%description -n texlive-papercdcase-doc
Documentation for papercdcase

%package -n texlive-papermas
Provides:       tex-papermas = %{tl_version}
License:        LPPL 1.3
Summary:        Compute the mass of a printed version of a document
Version:        svn23667.1.0h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(pageslts.sty), tex(intcalc.sty)
Provides:       tex(papermas.sty) = %{tl_version}

%description -n texlive-papermas
The package computes the number of sheets of paper used by, and
hence the mass of a document. This is useful (for example) when
calculating postal charges.

%package -n texlive-papermas-doc
Summary:        Documentation for papermas
Version:        svn23667.1.0h

Provides:       tex-papermas-doc
AutoReqProv:    No

%description -n texlive-papermas-doc
Documentation for papermas

%package -n texlive-papertex
Provides:       tex-papertex = %{tl_version}
License:        LPPL
Summary:        Class for newspapers, etc
Version:        svn19230.1.2b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(ifpdf.sty), tex(multido.sty), tex(datetime.sty)
Requires:       tex(multicol.sty), tex(fancyhdr.sty), tex(fancybox.sty), tex(geometry.sty)
Requires:       tex(graphicx.sty), tex(color.sty), tex(hyperref.sty), tex(textpos.sty)
Requires:       tex(hyphenat.sty), tex(wrapfig.sty), tex(lastpage.sty), tex(setspace.sty)
Requires:       tex(ragged2e.sty)
Provides:       tex(papertex.cls) = %{tl_version}

%description -n texlive-papertex
This class allows LaTeX users to create a paperTeX newspaper.
The final document has a front page and as many inner pages as
desired. News items appear one after another and the user can
choose the number of columns, style and so on. The class allows
users to create newsletters too.

%package -n texlive-papertex-doc
Summary:        Documentation for papertex
Version:        svn19230.1.2b

Provides:       tex-papertex-doc
AutoReqProv:    No

%description -n texlive-papertex-doc
Documentation for papertex

%package -n texlive-paracol
Provides:       tex-paracol = %{tl_version}
License:        LPPL
Summary:        Multiple columns with texts "in parallel"
Version:        svn47750
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(paracol.sty) = %{tl_version}

%description -n texlive-paracol
The package provides yet another multi-column typesetting
mechanism by which you produce multi-column (e.g., bilingual)
document switching and sychronizing each corresponding part in
"parallel".

%package -n texlive-paracol-doc
Summary:        Documentation for paracol
Version:        svn47750
Provides:       tex-paracol-doc
AutoReqProv:    No

%description -n texlive-paracol-doc
Documentation for paracol

%package -n texlive-paresse
Provides:       tex-paresse = %{tl_version}
License:        LPPL
Summary:        Define simple macros for greek letters
Version:        svn29803.4.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(skeyval-bc.sty), tex(ifluatex.sty), tex(ifxetex.sty)
Provides:       tex(paresse.sty) = %{tl_version}

%description -n texlive-paresse
The package defines macros using SS to type greek letters. so
that the user may (for example) type SSa to get the effect of
$\alpha$.

%package -n texlive-paresse-doc
Summary:        Documentation for paresse
Version:        svn29803.4.1

Provides:       tex-paresse-doc
AutoReqProv:    No

%description -n texlive-paresse-doc
Documentation for paresse

%package -n texlive-parnotes
Provides:       tex-parnotes = %{tl_version}
License:        LPPL 1.3
Summary:        Notes after every paragraph (or elsewhere)
Version:        svn41868
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(parnotes.sty) = %{tl_version}

%description -n texlive-parnotes
The package provides the \parnote command. The notes are set as
(normal) running paragraphs; placement is at the end of each
paragraph, or manually, using the \parnotes command.

%package -n texlive-parnotes-doc
Summary:        Documentation for parnotes
Version:        svn41868
Provides:       tex-parnotes-doc
AutoReqProv:    No

%description -n texlive-parnotes-doc
Documentation for parnotes

%package -n texlive-parselines
Provides:       tex-parselines = %{tl_version}
License:        LPPL 1.3
Summary:        Apply a macro to each line of an environment
Version:        svn21475.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(parselines.sty) = %{tl_version}

%description -n texlive-parselines
The package defines an environment "parse lines" which
processes each line of an environment with a macro. An example
of shading the lines of an environment is given.

%package -n texlive-parselines-doc
Summary:        Documentation for parselines
Version:        svn21475.1.4

Provides:       tex-parselines-doc
AutoReqProv:    No

%description -n texlive-parselines-doc
Documentation for parselines

%package -n texlive-pas-cours
Provides:       tex-pas-cours = %{tl_version}
License:        LPPL
Summary:        Macros useful in preparing teaching material
Version:        svn42036
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(xstring.sty), tex(amssymb.sty), tex(tikz.sty)
Requires:       tex(enumitem.sty)
Provides:       tex(pas-cours.sty) = %{tl_version}

%description -n texlive-pas-cours
Several groups of macros cover different branches of
mathematics.

%package -n texlive-pas-cours-doc
Summary:        Documentation for pas-cours
Version:        svn42036
Provides:       tex-pas-cours-doc
AutoReqProv:    No

%description -n texlive-pas-cours-doc
Documentation for pas-cours

%package -n texlive-pas-cv
Provides:       tex-pas-cv = %{tl_version}
License:        LPPL
Summary:        Flexible typesetting of Curricula Vitae
Version:        svn32263.2.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(graphicx.sty), tex(tikz.sty), tex(eso-pic.sty)
Requires:       tex(fp.sty), tex(geometry.sty)
Provides:       tex(macro-andromede.tex) = %{tl_version}
Provides:       tex(macro-architecte.tex) = %{tl_version}
Provides:       tex(macro-centaure.tex) = %{tl_version}, tex(macro-dynamique.tex) = %{tl_version}
Provides:       tex(macro-gaia.tex) = %{tl_version}, tex(macro-jupiter.tex) = %{tl_version}
Provides:       tex(macro-mars.tex) = %{tl_version}, tex(macro-neptune.tex) = %{tl_version}
Provides:       tex(macro-orion.tex) = %{tl_version}, tex(macro-pegase.tex) = %{tl_version}
Provides:       tex(macro-pluton.tex) = %{tl_version}, tex(macro-saturne.tex) = %{tl_version}
Provides:       tex(macro-univers.tex) = %{tl_version}, tex(macro-uranus.tex) = %{tl_version}
Provides:       tex(macro-venus.tex) = %{tl_version}, tex(pas-cv.sty) = %{tl_version}

%description -n texlive-pas-cv
The package provides the framework for typesetting a Curriculum
Vitae (composed in French), together with a number of "themes"
that may be used with the package. (The use of the themes may
be seen in the package's examples/ collection.) The author
hints that conversion for use with other languages (than
French) should be possible.

%package -n texlive-pas-cv-doc
Summary:        Documentation for pas-cv
Version:        svn32263.2.01

Provides:       tex-pas-cv-doc
AutoReqProv:    No

%description -n texlive-pas-cv-doc
Documentation for pas-cv

%package -n texlive-pas-tableur
Provides:       tex-pas-tableur = %{tl_version}
License:        LPPL
Summary:        Create a spreadsheet layout
Version:        svn39542

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(xstring.sty), tex(xkeyval.sty)
Provides:       tex(pas-tableur.sty) = %{tl_version}

%description -n texlive-pas-tableur
The package provides commands for creating a grid of
rectangles, and commands for populating locations in the grid.
PGF/TikZ is used for placement and population of the cells.

%package -n texlive-pas-tableur-doc
Summary:        Documentation for pas-tableur
Version:        svn39542

Provides:       tex-pas-tableur-doc
AutoReqProv:    No

%description -n texlive-pas-tableur-doc
Documentation for pas-tableur

%package -n texlive-patchcmd
Provides:       tex-patchcmd = %{tl_version}
License:        Public Domain
Summary:        Change the definition of an existing command
Version:        svn41379

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(patchcmd.sty) = %{tl_version}

%description -n texlive-patchcmd
The package provides a command \patchcommand that can be used
to add material at the beginning and/or the end of the
replacement text of an existing macro. It works for macros with
any number of normal arguments, including those that were
defined with \DeclareRobustCommand.

%package -n texlive-patchcmd-doc
Summary:        Documentation for patchcmd
Version:        svn41379

Provides:       tex-patchcmd-doc
AutoReqProv:    No

%description -n texlive-patchcmd-doc
Documentation for patchcmd

%package -n texlive-pauldoc
Provides:       tex-pauldoc = %{tl_version}
License:        LPPL
Summary:        German LaTeX package documentation
Version:        svn16005.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(inputenc.sty), tex(babel.sty), tex(fontenc.sty)
Provides:       tex(pauldoc.sty) = %{tl_version}

%description -n texlive-pauldoc
The package provides helpers for German language package
documentation.

%package -n texlive-pauldoc-doc
Summary:        Documentation for pauldoc
Version:        svn16005.0.5

Provides:       tex-pauldoc-doc
AutoReqProv:    No

%description -n texlive-pauldoc-doc
Documentation for pauldoc

%package -n texlive-pawpict
Provides:       tex-pawpict = %{tl_version}
License:        GPL+
Summary:        Using graphics from PAW
Version:        svn21629.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pawpict.sty) = %{tl_version}

%description -n texlive-pawpict
Support for the easy inclusion of graphics made by PAW (Physics
Analysis Workstation). You need to have PAW installed on your
system to benefit from this package.

%package -n texlive-pawpict-doc
Summary:        Documentation for pawpict
Version:        svn21629.1.0

Provides:       tex-pawpict-doc
AutoReqProv:    No

%description -n texlive-pawpict-doc
Documentation for pawpict

%package -n texlive-pbox
Provides:       tex-pbox = %{tl_version}
License:        GPLv2+
Summary:        A variable-width \parbox command
Version:        svn24807.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(ifthen.sty)
Provides:       tex(pbox.sty) = %{tl_version}

%description -n texlive-pbox
Defines a command \pbox{<max width>}{<text>} which adjusts its
width to that of the enclosed text, up to the maximum width
given. The package also defines some associated length
commands.

%package -n texlive-pbox-doc
Summary:        Documentation for pbox
Version:        svn24807.1.2

Provides:       tex-pbox-doc
AutoReqProv:    No

%description -n texlive-pbox-doc
Documentation for pbox

%package -n texlive-pbsheet
Provides:       tex-pbsheet = %{tl_version}
License:        LPPL
Summary:        Problem sheet class
Version:        svn24830.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(amsfonts.sty), tex(amssymb.sty), tex(amsthm.sty)
Requires:       tex(latexsym.sty), tex(geometry.sty), tex(rotating.sty), tex(moreverb.sty)
Requires:       tex(inputenc.sty), tex(xspace.sty), tex(babel.sty), tex(color.sty)
Requires:       tex(listings.sty)
Provides:       tex(pbsheet.cls) = %{tl_version}

%description -n texlive-pbsheet
This class is designed to simplify the typesetting of problem
sheets with Mathematics and Computer Science content. It is
currently customised towards teaching in French (and the
examples are in French).

%package -n texlive-pbsheet-doc
Summary:        Documentation for pbsheet
Version:        svn24830.0.1

Provides:       tex-pbsheet-doc
AutoReqProv:    No

%description -n texlive-pbsheet-doc
Documentation for pbsheet

%package -n texlive-pdf14
Provides:       tex-pdf14 = %{tl_version}
License:        LPPL 1.3
Summary:        Restore PDF 1.4 to a TeX live 2010 format
Version:        svn17583.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pdf14.sty) = %{tl_version}

%description -n texlive-pdf14
Starting with TeX Live 2010, the various formats, that directly
generate PDF, default to generating PDF 1.5. This is generally
a good thing, but it can lead to compatibility issues with some
older PDF viewers. This package changes the version of PDF
generated with formats (based on pdfTeX or LuaTeX in PDF mode),
back to 1.4 for documents that need to achieve maximal
compatibility with old viewers.

%package -n texlive-pdf14-doc
Summary:        Documentation for pdf14
Version:        svn17583.0.1

Provides:       tex-pdf14-doc
AutoReqProv:    No

%description -n texlive-pdf14-doc
Documentation for pdf14

%package -n texlive-pdfcomment
Provides:       tex-pdfcomment = %{tl_version}
License:        LPPL 1.3
Summary:        A user-friendly interface to pdf annotations
Version:        svn40166

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(zref-savepos.sty), tex(refcount.sty), tex(ifthen.sty)
Requires:       tex(calc.sty), tex(marginnote.sty), tex(ifpdf.sty), tex(datetime.sty)
Requires:       tex(soulpos.sty), tex(hyperref.sty)
Provides:       tex(pdfcomment.sty) = %{tl_version}

%description -n texlive-pdfcomment
For a long time pdfLaTeX has offered the command \pdfannot for
inserting arbitrary PDF annotations. However, the command is
presented in a form where additional knowledge of the
definition of the PDF format is indispensable. This package is
an answer to the - occasional - questions in newsgroups, about
how one could use the comment function of Adobe Reader. At
least for the writer of LaTeX code, the package offers a
convenient and user-friendly means of using \pdfannot to
provide comments in PDF files. Since version v1.1,
pdfcomment.sty also supports LaTeX - dvips - ps2pdf, LaTeX -
dvipdfmx, and XeLaTeX. Unfortunately, support of PDF
annotations by PDF viewers is sparse to nonexistent. The
reference viewer for the development of this package is Adobe
Reader.

%package -n texlive-pdfcomment-doc
Summary:        Documentation for pdfcomment
Version:        svn40166

Provides:       tex-pdfcomment-doc
AutoReqProv:    No

%description -n texlive-pdfcomment-doc
Documentation for pdfcomment

%package -n texlive-pdfcprot
Provides:       tex-pdfcprot = %{tl_version}
License:        LPPL
Summary:        Activating and setting of character protruding using pdflatex
Version:        svn18735.1.7a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(keyval.sty)
Provides:       tex(pdfcprot.sty) = %{tl_version}

%description -n texlive-pdfcprot
This package provides an easy interface to adjust the character
protrusion for different fonts and choosing the right
adjustment automatically depending on the font. The package is
largely superseded by microtype.

%package -n texlive-pdfcprot-doc
Summary:        Documentation for pdfcprot
Version:        svn18735.1.7a

Provides:       tex-pdfcprot-doc
AutoReqProv:    No

%description -n texlive-pdfcprot-doc
Documentation for pdfcprot

%package -n texlive-pdfmarginpar
Provides:       tex-pdfmarginpar = %{tl_version}
License:        GPL+
Summary:        Generate marginpar-equivalent PDF annotations
Version:        svn23492.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pgfkeys.sty)
Provides:       tex(pdfmarginpar.sty) = %{tl_version}

%description -n texlive-pdfmarginpar
The package provides the \pdfmarginpar command which is similar
in spirit to \marginpar. However, it creates PDF annotations
which may be viewed with Adobe Reader in place of marginal
texts. Small icons indicate the in-text position where the
message originates, popups provide the messages themselves.
Thus bugfixes and other such communications are clearly visible
together when viewing the document, while the document itself
is not obscured.

%package -n texlive-pdfmarginpar-doc
Summary:        Documentation for pdfmarginpar
Version:        svn23492.0.92

Provides:       tex-pdfmarginpar-doc
AutoReqProv:    No

%description -n texlive-pdfmarginpar-doc
Documentation for pdfmarginpar

%package -n texlive-pdfpagediff
Provides:       tex-pdfpagediff = %{tl_version}
License:        LPPL
Summary:        Find difference between two PDF's
Version:        svn37946.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(graphicx.sty), tex(color.sty), tex(substr.sty)
Provides:       tex(pdfpagediff.sty) = %{tl_version}

%description -n texlive-pdfpagediff
Find difference between two PDF's

%package -n texlive-pdfpagediff-doc
Summary:        Documentation for pdfpagediff
Version:        svn37946.1.4

Provides:       tex-pdfpagediff-doc
AutoReqProv:    No

%description -n texlive-pdfpagediff-doc
Documentation for pdfpagediff

%package -n texlive-pdfscreen
Provides:       tex-pdfscreen = %{tl_version}
License:        LPPL
Summary:        Support screen-based document design
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty), tex(color.sty), tex(calc.sty), tex(comment.sty)
Requires:       tex(hyperref.sty), tex(shortvrb.sty), tex(amssymb.sty), tex(amsbsy.sty)
Requires:       tex(truncate.sty), tex(fancybox.sty)
Provides:       tex(pdfscreen.sty) = %{tl_version}

%description -n texlive-pdfscreen
An extension of the hyperref package to provide a screen-based
document design. This package helps to generate pdf documents
that are readable on screen and will fit the screen's aspect
ratio. Also it can be used with various options to produce
regular print versions of the same document without any extra
effort.

%package -n texlive-pdfscreen-doc
Summary:        Documentation for pdfscreen
Version:        svn42428
Provides:       tex-pdfscreen-doc
AutoReqProv:    No

%description -n texlive-pdfscreen-doc
Documentation for pdfscreen

%package -n texlive-pdfslide
Provides:       tex-pdfslide = %{tl_version}
License:        LPPL
Summary:        Presentation slides using pdftex
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(colortbl.sty), tex(amssymb.sty), tex(amsbsy.sty)
Requires:       tex(fancybox.sty), tex(hyperref.sty), tex(ifthen.sty)
Provides:       tex(pdfslide.cfg) = %{tl_version}, tex(pdfslide.sty) = %{tl_version}
Provides:       tex(slide.clo) = %{tl_version}

%description -n texlive-pdfslide
This is a package for use with pdftex, to make nice
presentation slides. Its aims are: to devise a method for
easier technical presentation; to help the mix of mathematical
formulae with text and graphics which other present day
document processing tools fail to accomplish; to exploit the
platform independence of TeX so that presentation documents
become portable; and to offer the freedom and possibilities of
using various backgrounds and other embellishments that a user
can imagine to have in as presentation. The package can make
use of the facilities of the PPower4 post-processor.

%package -n texlive-pdfslide-doc
Summary:        Documentation for pdfslide
Version:        svn15878.0

Provides:       tex-pdfslide-doc
AutoReqProv:    No

%description -n texlive-pdfslide-doc
Documentation for pdfslide

%package -n texlive-pdfsync
Provides:       tex-pdfsync = %{tl_version}
License:        LPPL
Summary:        Provide links between source and PDF
Version:        svn20373.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pdfsync.sty) = %{tl_version}

%description -n texlive-pdfsync
The package runs with pdfTeX or XeTeX, and creates an auxiliary
file with geometrical information to permit references back and
forth between source and PDF, assuming a conforming editor and
PDF viewer.

%package -n texlive-pdfsync-doc
Summary:        Documentation for pdfsync
Version:        svn20373.0

Provides:       tex-pdfsync-doc
AutoReqProv:    No

%description -n texlive-pdfsync-doc
Documentation for pdfsync

%package -n texlive-pdfwin
Provides:       tex-pdfwin = %{tl_version}
License:        LPPL
Summary:        pdfwin package
Version:        svn45797
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(amssymb.sty), tex(keyval.sty), tex(graphicx.sty), tex(color.sty)
Requires:       tex(truncate.sty), tex(hyperref.sty)
Provides:       tex(pdfwin.cfg) = %{tl_version}, tex(pdfwin.sty) = %{tl_version}

%description -n texlive-pdfwin
pdfwin package

%package -n texlive-pdfwin-doc
Summary:        Documentation for pdfwin
Version:        svn45797

Provides:       tex-pdfwin-doc
AutoReqProv:    No

%description -n texlive-pdfwin-doc
Documentation for pdfwin

%package -n texlive-pdfx
Provides:       tex-pdfx = %{tl_version}
License:        LPPL
Summary:        PDF/X-1a and PDF/A-1b support for pdfTeX
Version:        svn44412
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(hyperref.sty), tex(inputenc.sty), tex(xmpincl.sty), tex(glyphtounicode.tex)
Provides:       tex(8bit.def) = %{tl_version}, tex(glyphtounicode-cmr.tex) = %{tl_version}
Provides:       tex(pdfx.sty) = %{tl_version}

%description -n texlive-pdfx
The package helps LaTeX users to create PDF/X-1a and PFD/A-1b
compliant pdf documents with pdfTeX.

%package -n texlive-pdfx-doc
Summary:        Documentation for pdfx
Version:        svn44412
Provides:       tex-pdfx-doc
AutoReqProv:    No

%description -n texlive-pdfx-doc
Documentation for pdfx

%package -n texlive-pecha
Provides:       tex-pecha = %{tl_version}
License:        GPL+
Summary:        Print Tibetan text in the classic pecha layout style
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(twoopt.sty), tex(relsize.sty), tex(calc.sty), tex(ctib.sty)
Requires:       tex(rotating.sty), tex(times.sty)
Provides:       tex(ctibmantra.sty) = %{tl_version}, tex(pecha.cls) = %{tl_version}

%description -n texlive-pecha
The pecha class provides an environment for writing Tibetan on
LaTeX2e in the traditional Tibetan Pecha layout used for
spiritual or philosophical texts, using the cTib4TeX package by
Oliver Corff. It provides features like headers in different
languages, page numbering in Tibetan and more.

%package -n texlive-pecha-doc
Summary:        Documentation for pecha
Version:        svn15878.0.1

Provides:       tex-pecha-doc
AutoReqProv:    No

%description -n texlive-pecha-doc
Documentation for pecha

%package -n texlive-permute
Provides:       tex-permute = %{tl_version}
License:        LPPL
Summary:        Support for symmetric groups
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(permute.sty) = %{tl_version}

%description -n texlive-permute
A package for symmetric groups, allowing you to input, output,
and calculate with them.

%package -n texlive-permute-doc
Summary:        Documentation for permute
Version:        svn15878.0

Provides:       tex-permute-doc
AutoReqProv:    No

%description -n texlive-permute-doc
Documentation for permute

%package -n texlive-petiteannonce
Provides:       tex-petiteannonce = %{tl_version}
License:        LPPL
Summary:        A class for small advertisements
Version:        svn25915.1.0001

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(keyval.sty)
Provides:       tex(petiteannonce.cls) = %{tl_version}

%description -n texlive-petiteannonce
The class enables you to create the sort of adverts that you
pin on a noticeboard, with tear-off strips at the bottom where
you can place contact details.

%package -n texlive-petiteannonce-doc
Summary:        Documentation for petiteannonce
Version:        svn25915.1.0001

Provides:       tex-petiteannonce-doc
AutoReqProv:    No

%description -n texlive-petiteannonce-doc
Documentation for petiteannonce

%package -n texlive-philex
Provides:       tex-philex = %{tl_version}
License:        LPPL
Summary:        Cross references for named and numbered environments
Version:        svn36396.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty), tex(calc.sty), tex(cgloss4e.sty), tex(linguex.sty)
Requires:       tex(ifthen.sty), tex(suffix.sty)
Provides:       tex(philex.sty) = %{tl_version}

%description -n texlive-philex
Philex provides means for creating and cross-referencing named
or numbered environments. Possible uses would be equations,
example sentences (as in linguistics or philosophy) or named
principles. Cross references may refer either to the number, or
to a short name of the target environment, or to the contents
of the environment. Philex builds on the facilities of the
linguex package.

%package -n texlive-philex-doc
Summary:        Documentation for philex
Version:        svn36396.1.3

Provides:       tex-philex-doc
AutoReqProv:    No

%description -n texlive-philex-doc
Documentation for philex

%package -n texlive-photo
Provides:       tex-photo = %{tl_version}
License:        LPPL
Summary:        A float environment for photographs
Version:        svn18739.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(photo.sty) = %{tl_version}

%description -n texlive-photo
This package introduces a new float type called photo which
works similar to the float types table and figure. Various
options exist for placing photos, captions, and a
"photographer" line. In twocolumn documents, a possibility
exists to generate double-column floats automatically if the
photo does not fit into one column. Photos do not have to be
placed as floats, they can also be placed as boxes, with
captions and photographer line still being available.

%package -n texlive-photo-doc
Summary:        Documentation for photo
Version:        svn18739.0

Provides:       tex-photo-doc
AutoReqProv:    No

%description -n texlive-photo-doc
Documentation for photo

%package -n texlive-piff
Provides:       tex-piff = %{tl_version}
License:        Public Domain
Summary:        Macro tools by Mike Piff
Version:        svn21894.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsfonts.sty)
Provides:       tex(duplicat.sty) = %{tl_version}, tex(newproof.sty) = %{tl_version}
Provides:       tex(onepagem.sty) = %{tl_version}, tex(time.sty) = %{tl_version}

%description -n texlive-piff
The set (now) consists of: a small package for dealing with
duplicate-numbered output pages; newproof, for defining
mathematical proof structures; onepagem for omitting the page
number in one-page documents and time, which prints a 12-hour
format time.

%package -n texlive-piff-doc
Summary:        Documentation for piff
Version:        svn21894.0

Provides:       tex-piff-doc
AutoReqProv:    No

%description -n texlive-piff-doc
Documentation for piff

%package -n texlive-pkgloader
Provides:       tex-pkgloader = %{tl_version}
License:        LPPL 1.3
Summary:        Managing the options and loading order of other packages
Version:        svn47486
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(filecontents.sty), tex(xparse.sty), tex(etoolbox.sty), tex(withargs.sty)
Requires:       tex(expl3.sty), tex(l3keys2e.sty), tex(l3regex.sty), tex(lt3graph.sty)
Provides:       tex(pkgloader-cls-pkg.sty) = %{tl_version}
Provides:       tex(pkgloader-dry.sty) = %{tl_version}, tex(dry.sty) = %{tl_version}
Provides:       tex(pkgloader-early.sty) = %{tl_version}
Provides:       tex(pkgloader-error.sty) = %{tl_version}
Provides:       tex(pkgloader-false.sty) = %{tl_version}
Provides:       tex(pkgloader-late.sty) = %{tl_version}, tex(pkgloader-recommended.sty) = %{tl_version}
Provides:       tex(pkgloader-true.sty) = %{tl_version}, tex(pkgloader.sty) = %{tl_version}

%description -n texlive-pkgloader
The package seeks to address the frustration caused by package
conflicts. It is in an early stage of its development, and
should probably not be used as a matter of course; however the
author welcomes feedback via the home page link given in this
catalogue entry. Nevertheless, the author urges users to try
the package and to report issues (or whatever) via the
package's repository.

%package -n texlive-pkgloader-doc
Summary:        Documentation for pkgloader
Version:        svn47486
Provides:       tex-pkgloader-doc
AutoReqProv:    No

%description -n texlive-pkgloader-doc
Documentation for pkgloader

%package -n texlive-plantslabels
Provides:       tex-plantslabels = %{tl_version}
License:        LPPL
Summary:        Write labels for plants
Version:        svn29803.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(labels.sty), tex(graphicx.sty)
Provides:       tex(plantslabels.sty) = %{tl_version}

%description -n texlive-plantslabels
The package defines a command \plant, which has three mandatory
and seven optional argument. The package uses the labels

%package -n texlive-plantslabels-doc
Summary:        Documentation for plantslabels
Version:        svn29803.1.0

Provides:       tex-plantslabels-doc
AutoReqProv:    No

%description -n texlive-plantslabels-doc
Documentation for plantslabels

%package -n texlive-plates
Provides:       tex-plates = %{tl_version}
License:        LPPL
Summary:        Arrange for "plates" sections of documents
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(endplate.sty) = %{tl_version}, tex(plates.sty) = %{tl_version}

%description -n texlive-plates
The plates package provides a simple facility for inserting
colour figures in a document when they should be gathered and
printed together as in a book's section of colour plates. The
package provides a plate environment that takes the place of
the figure environment for such colour images.

%package -n texlive-plates-doc
Summary:        Documentation for plates
Version:        svn15878.0.1

Provides:       tex-plates-doc
AutoReqProv:    No

%description -n texlive-plates-doc
Documentation for plates

%package -n texlive-plweb
Provides:       tex-plweb = %{tl_version}
License:        Copyright only
Summary:        Literate Programming for Prolog with LaTeX
Version:        svn15878.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pcode.sty) = %{tl_version}, tex(pl.cfg) = %{tl_version}
Provides:       tex(pl.sty) = %{tl_version}

%description -n texlive-plweb
Instead of having to transform the common source into program
or documentation, the central idea was to develop a method to
have one common source which can be interpreted by a Prolog
system as well as by LaTeX, whether that Prolog system be C-
Prolog, Quintus-Prolog, or ECLiPSe.

%package -n texlive-plweb-doc
Summary:        Documentation for plweb
Version:        svn15878.3.0

Provides:       tex-plweb-doc
AutoReqProv:    No

%description -n texlive-plweb-doc
Documentation for plweb

%package -n texlive-polynom
Provides:       tex-polynom = %{tl_version}
License:        LPPL
Summary:        Macros for manipulating polynomials
Version:        svn44832
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(polynom.sty) = %{tl_version}

%description -n texlive-polynom
The polynom package implements macros for manipulating
polynomials, for example it can typeset long polynomial
divisions. The main test case and application is the polynomial
ring in one variable with rational coefficients.

%package -n texlive-polynom-doc
Summary:        Documentation for polynom
Version:        svn44832
Provides:       tex-polynom-doc
AutoReqProv:    No

%description -n texlive-polynom-doc
Documentation for polynom

%package -n texlive-polynomial
Provides:       tex-polynomial = %{tl_version}
License:        LPPL
Summary:        Typeset (univariate) polynomials
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(polynomial.sty) = %{tl_version}

%description -n texlive-polynomial
The package offers an easy way to write (univariate)
polynomials and rational functions. It defines two commands,
one for polynomials \polynomial{coeffs} and one for rational
functions \polynomialfrac{Numerator}{Denominator}. Both
commands take lists of coefficients as arguments, and offer
limited optional behaviour.

%package -n texlive-polynomial-doc
Summary:        Documentation for polynomial
Version:        svn15878.1.0

Provides:       tex-polynomial-doc
AutoReqProv:    No

%description -n texlive-polynomial-doc
Documentation for polynomial

%package -n texlive-polytable
Provides:       tex-polytable = %{tl_version}
License:        LPPL
Summary:        Tabular-like environments with named columns
Version:        svn31235.0.8.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(lazylist.sty), tex(array.sty)
Provides:       tex(polytable.sty) = %{tl_version}

%description -n texlive-polytable
This package implements a variant of tabular-like environments
where columns can be given a name and entries can flexibly be
placed between arbitrary columns. Complex alignment-based
layouts, for example for program code, are possible.

%package -n texlive-polytable-doc
Summary:        Documentation for polytable
Version:        svn31235.0.8.2

Provides:       tex-polytable-doc
AutoReqProv:    No

%description -n texlive-polytable-doc
Documentation for polytable

%package -n texlive-postcards
Provides:       tex-postcards = %{tl_version}
License:        LPPL
Summary:        Facilitates mass-mailing of postcards (junkmail)
Version:        svn21641.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(envlab.sty), tex(mailing.sty)
Provides:       tex(postcards.cls) = %{tl_version}

%description -n texlive-postcards
A modification of the standard LaTeX letter class which prints
multiple, pre-stamped, 5.5" by 3.5" postcards (a US standard
size) via the envlab and mailing packages. An address database
is employed to address the front side of each postcard and a
message is printed on the back side of all. An illustrative
example is provided.

%package -n texlive-postcards-doc
Summary:        Documentation for postcards
Version:        svn21641.0

Provides:       tex-postcards-doc
AutoReqProv:    No

%description -n texlive-postcards-doc
Documentation for postcards

%package -n texlive-poster-mac
Provides:       tex-poster-mac = %{tl_version}
License:        LPPL
Summary:        Make posters and banners with TeX
Version:        svn18305.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(poster.sty) = %{tl_version}, tex(poster.tex) = %{tl_version}

%description -n texlive-poster-mac
The package offers macros for making posters and banners with
TeX. It is compatible with most TeX macro formats, including
Plain TeX, LaTeX, AmSTeX, and AmS-LaTeX. The package creates a
poster as huge box, which is then distributed over as many
printer pages as necessary. The only special requirement is
that your printer not be bothered by text that lies off the
page. This is true of most printers, including laser printers
and PostScript printers.

%package -n texlive-poster-mac-doc
Summary:        Documentation for poster-mac
Version:        svn18305.1.1

Provides:       tex-poster-mac-doc
AutoReqProv:    No

%description -n texlive-poster-mac-doc
Documentation for poster-mac

%package -n texlive-ppr-prv
Provides:       tex-ppr-prv = %{tl_version}
License:        LPPL
Summary:        Prosper preview
Version:        svn15878.0.13c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(textcomp.sty), tex(graphicx.sty), tex(geometry.sty)
Requires:       tex(keyval.sty), tex(ifpdf.sty), tex(hyperref.sty), tex(float.sty)
Provides:       tex(HAP-ppr-prv.def) = %{tl_version}, tex(ppr-prv.cls) = %{tl_version}

%description -n texlive-ppr-prv
This class is used with LaTeX presentations using the prosper
class. ppr-prv stands for 'Prosper Preview'. The aim of this
class is to produce a printable version of the slides written
with Prosper, with two slides per page.

%package -n texlive-ppr-prv-doc
Summary:        Documentation for ppr-prv
Version:        svn15878.0.13c

Provides:       tex-ppr-prv-doc
AutoReqProv:    No

%description -n texlive-ppr-prv-doc
Documentation for ppr-prv

%package -n texlive-placeat
Provides:       tex-placeat = %{tl_version}
License:        LPPL 1.3
Summary:        Absolute content positioning
Version:        svn45145
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(luatexbase.sty), tex(luacode.sty), tex(atbegshi.sty), tex(xparse.sty)
Provides:       tex(placeat.sty) = %{tl_version}

%description -n texlive-placeat
The package provides commands so that the user of LuaLaTeX may
position arbitrary content at any position specified by
absolute coordinates on the page. The package draws a grid on
each page of the document, to aid positioning (the grid may be
disabled, for 'final copy' using the command \placeatsetup).

%package -n texlive-placeat-doc
Summary:        Documentation for placeat
Version:        svn45145
Provides:       tex-placeat-doc
AutoReqProv:    No

%description -n texlive-placeat-doc
Documentation for placeat

%package -n texlive-perfectcut
Provides:       tex-perfectcut = %{tl_version}
License:        LPPL 1.3
Summary:        Brackets whose size adjusts to the nesting
Version:        svn44175
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty), tex(calc.sty), tex(mathstyle.sty)
Provides:       tex(perfectcut.sty) = %{tl_version}

%description -n texlive-perfectcut
The package defines the command \perfectcut#1#2 which displays
a bracket <#1||#2>. Its effect is to determine the size of the
bracket depending on the number of nested \perfectcut
(regardless of the contents). The command is intended for use:
In proof theory, for term notations of sequent calculus, In
computer science, for the modeling of abstract machines. The
package also offers a reimplementation of \big, \bigg, etc.,
into arbitrary-size variants.

%package -n texlive-perfectcut-doc
Summary:        Documentation for perfectcut
Version:        svn44175
Provides:       tex-perfectcut-doc
AutoReqProv:    No

%description -n texlive-perfectcut-doc
Documentation for perfectcut

%package -n texlive-piechartmp
Provides:       tex-piechartmp = %{tl_version}
License:        LPPL
Summary:        Draw pie-charts using MetaPost
Version:        svn19440.0.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-piechartmp
The piechartmp package is an easy way to draw pie-charts with
MetaPost. The package implements an interface that enables
users with little MetaPost experience to draw charts. A
highlight of the package is the possibility of suppressing some
segments of the chart, thus creating the possibility of several
charts from the same data.

%package -n texlive-piechartmp-doc
Summary:        Documentation for piechartmp
Version:        svn19440.0.3.0

Provides:       tex-piechartmp-doc
AutoReqProv:    No

%description -n texlive-piechartmp-doc
Documentation for piechartmp

%package -n texlive-piano
Provides:       tex-piano = %{tl_version}
License:        LPPL
Summary:        Typeset a basic 2-octave piano diagram
Version:        svn21574.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(piano.sty) = %{tl_version}

%description -n texlive-piano
This package adds the \keyboard[1][2]..[7] command to your
project. When used, it draws a small 2 octaves piano keyboard
on your document, with up to 7 keys highlighted. Keys go : Co,
Cso, Do, Dso, Eo, Fo, Fso, Go, Gso, Ao, Aso, Bo, Ct, Cst, Dt,
Dst, Et, Ft, Fst, Gt, Gst, At, Ast and Bt. (A working example
is included in the README file.)

%package -n texlive-piano-doc
Summary:        Documentation for piano
Version:        svn21574.1.0

Provides:       tex-piano-doc
AutoReqProv:    No

%description -n texlive-piano-doc
Documentation for piano

%package -n texlive-pitex
Provides:       tex-pitex = %{tl_version}
License:        LPPL
Summary:        Documentation macros
Version:        svn24731.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pitex.tex) = %{tl_version}

%description -n texlive-pitex
The bundle provides macros that the author uses when writing
documentation (for example, that of the texapi and yax
packages). The tools could be used by anyone, but there is no
documentation, and the macros are subject to change without
notice.

%package -n texlive-pitex-doc
Summary:        Documentation for pitex
Version:        svn24731.0

Provides:       tex-pitex-doc
AutoReqProv:    No

%description -n texlive-pitex-doc
Documentation for pitex

%package -n texlive-placeins-plain
Provides:       tex-placeins-plain = %{tl_version}
License:        Public Domain
Summary:        Insertions that keep their place
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(placeins.tex) = %{tl_version}

%description -n texlive-placeins-plain
This TeX file provides various mechanisms (for plain TeX and
close relatives) to let insertions (footnotes, topins, pageins,
etc.) float within their appropriate section, but to prevent
them from intruding into the following section, even when
sections do not normally begin a new page. (If your sections
normally begin a new page, just use \supereject to flush out
insertions.)

%package -n texlive-plipsum
Provides:       tex-plipsum = %{tl_version}
License:        LPPL
Summary:        'Lorem ipsum' for Plain TeX developers
Version:        svn30353.4.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(plipsum.tex) = %{tl_version}

%description -n texlive-plipsum
The package provides a paragraph generator designed for use in
Plain TeX documents. The paragraphs generated contain many 'f-
groups' (ff, fl etc.) so the text can act as a test of the
ligatures of the font in use.

%package -n texlive-plipsum-doc
Summary:        Documentation for plipsum
Version:        svn30353.4.3

Provides:       tex-plipsum-doc
AutoReqProv:    No

%description -n texlive-plipsum-doc
Documentation for plipsum

%package -n texlive-plnfss
Provides:       tex-plnfss = %{tl_version}
License:        LPPL
Summary:        Font selection for Plain TeX
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(MIKmathf.tex) = %{tl_version}, tex(plnfss.tex) = %{tl_version}

%description -n texlive-plnfss
Plnfss is a set of macros to provide easy font access (somewhat
similar to NFSS but with some limitations) with Plain TeX.
Plnfss can automatically make use of PSNFSS fd files, i.e.,
when an Adobe Type 1 is used the relevant fd file will be
loaded automatically. For cmr-like fonts (ec, vnr, csr or plr
fonts), a special format called pfd (plain fd) is required and
must be loaded manually. See ot1cmr.pfd for further
information.

%package -n texlive-plnfss-doc
Summary:        Documentation for plnfss
Version:        svn15878.1.1

Provides:       tex-plnfss-doc
AutoReqProv:    No

%description -n texlive-plnfss-doc
Documentation for plnfss

%package -n texlive-plstmary
Provides:       tex-plstmary = %{tl_version}
License:        Public Domain
Summary:        St. Mary's Road font support for plain TeX
Version:        svn31088.0.5c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(stmary.tex) = %{tl_version}

%description -n texlive-plstmary
The package provides commands to produce all the symbols of the
St Mary's Road fonts, in a Plain TeX environment.

%package -n texlive-plstmary-doc
Summary:        Documentation for plstmary
Version:        svn31088.0.5c

Provides:       tex-plstmary-doc
AutoReqProv:    No

%description -n texlive-plstmary-doc
Documentation for plstmary

%package -n texlive-pdftricks
Provides:       tex-pdftricks = %{tl_version}
License:        GPL+
Summary:        Support for pstricks in pdfTeX
Version:        svn15878.1.16

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(color.sty), tex(moreverb.sty), tex(keyval.sty)
Provides:       tex(pdftricks.sty) = %{tl_version}

%description -n texlive-pdftricks
The PSTricks macros cannot be used (directly) with pdfTeX,
since pstricks uses PostScript arithmetic, which isn't part of
PDF. This package circumvents this limitation so that the
extensive facilities offered by the powerful PSTricks package
can be made use of in a pdfTeX document. This is done using the
shell escape function available in current TeX implementations.
The package may also be used in support of other 'PostScript-
output-only' packages, such as PSfrag. For alternatives, users
may care to review the discussion in the PSTricks online
documentation.

%package -n texlive-pdftricks-doc
Summary:        Documentation for pdftricks
Version:        svn15878.1.16

Provides:       tex-pdftricks-doc
AutoReqProv:    No

%description -n texlive-pdftricks-doc
Documentation for pdftricks

%package -n texlive-pdftricks2
Provides:       tex-pdftricks2 = %{tl_version}
License:        GPLv2+
Summary:        Use pstricks in pdfTeX
Version:        svn31016.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(graphicx.sty), tex(ifpdf.sty), tex(moreverb.sty)
Requires:       tex(ifplatform.sty)
Provides:       tex(pdftricks2.sty) = %{tl_version}

%description -n texlive-pdftricks2
The package provides the means of processing documents (that
contain pstricks graphics specifications. The package is
inspired by pdftricks

%package -n texlive-pdftricks2-doc
Summary:        Documentation for pdftricks2
Version:        svn31016.1.01

Provides:       tex-pdftricks2-doc
AutoReqProv:    No

%description -n texlive-pdftricks2-doc
Documentation for pdftricks2

%package -n texlive-philosophersimprint
Provides:       tex-philosophersimprint = %{tl_version}
License:        LPPL
Summary:        Typesetting articles for "Philosophers' Imprint"
Version:        svn41788
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifpdf.sty), tex(color.sty), tex(graphicx.sty), tex(fancyhdr.sty)
Requires:       tex(mathpazo.sty), tex(courier.sty), tex(helvet.sty), tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(microtype.sty), tex(trajan.sty)
Provides:       tex(philosophersimprint.cls) = %{tl_version}

%description -n texlive-philosophersimprint
In its mission statement we read "Philosophers' Imprint is a
refereed series of original papers in philosophy, edited by
philosophy faculty at the University of Michigan, with the
advice of an international Board of Editors, and published on
the World Wide Web by the University of Michigan Digital
Library. The mission of the Imprint is to promote a future in
which funds currently spent on journal subscriptions are
redirected to the dissemination of scholarship for free, via
the Internet". The class helps authors to typeset their own
articles in "Web-ready" format. No assumption is made about the
fonts available to the author: the class itself is restricted
to freely available and freely distributed fonts, only.

%package -n texlive-philosophersimprint-doc
Summary:        Documentation for philosophersimprint
Version:        svn41788
Provides:       tex-philosophersimprint-doc
AutoReqProv:    No

%description -n texlive-philosophersimprint-doc
Documentation for philosophersimprint

%package -n texlive-pittetd
Provides:       tex-pittetd = %{tl_version}
License:        LPPL
Summary:        Electronic Theses and Dissertations at Pitt
Version:        svn15878.1.618

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pitetd10.clo) = %{tl_version}, tex(pitetd11.clo) = %{tl_version}
Provides:       tex(pitetd12.clo) = %{tl_version}, tex(pittetd.cls) = %{tl_version}

%description -n texlive-pittetd
A document class for theses and dissertations. Provides patch
files that enable pittetd to use files prepared for use with
the pittdiss or pitthesis classes. The manual provides a
detailed guide for users who wish to use the class to prepare
their thesis or dissertation.

%package -n texlive-pittetd-doc
Summary:        Documentation for pittetd
Version:        svn15878.1.618

Provides:       tex-pittetd-doc
AutoReqProv:    No

%description -n texlive-pittetd-doc
Documentation for pittetd

%package -n texlive-pkuthss
Provides:       tex-pkuthss = %{tl_version}
License:        LPPL
Summary:        LaTeX template for dissertations in Peking University
Version:        svn48124
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(scrextend.sty), tex(subfig.sty), tex(tocloft.sty)
Requires:       tex(caption.sty), tex(CJKspace.sty), tex(setspace.sty), tex(enumitem.sty)
Requires:       tex(keyval.sty), tex(graphicx.sty), tex(geometry.sty), tex(xCJK2uni.sty)
Provides:       tex(pkuthss-extra.sty) = %{tl_version}, tex(pkuthss-gbk.def) = %{tl_version}
Provides:       tex(pkuthss-utf8.def) = %{tl_version}, tex(pkuthss.cls) = %{tl_version}

%description -n texlive-pkuthss
The package provides a simple, clear and flexible LaTeX
template for dissertations in Peking University.

%package -n texlive-pkuthss-doc
Summary:        Documentation for pkuthss
Version:        svn48124
Provides:       tex-pkuthss-doc
AutoReqProv:    No

%description -n texlive-pkuthss-doc
Documentation for pkuthss

%package -n texlive-powerdot-FUBerlin
Provides:       tex-powerdot-FUBerlin = %{tl_version}
License:        LPPL
Summary:        Powerdot, using the style of FU Berlin
Version:        svn15878.0.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(babel.sty), tex(pifont.sty), tex(breakurl.sty)
Requires:       tex(graphicx.sty), tex(calc.sty), tex(tabularx.sty), tex(helvet.sty)
Requires:       tex(ragged2e.sty)
Provides:       tex(FUpowerdot.cls) = %{tl_version}, tex(powerdot-BerlinFU.sty) = %{tl_version}

%description -n texlive-powerdot-FUBerlin
The bundle provides a powerdot-derived class and a package for
use with powerdot to provide the corporate design of the Free
University in Berlin. Users may use the class itself
(FUpowerdot) or use the package in the usual way with
\style=BerlinFU as a class option. Examples of using both the
class and the package are provided; the PDF is visually
identical, so the catalogue only lists one; the sources of the
examples do of course differ.

%package -n texlive-powerdot-FUBerlin-doc
Summary:        Documentation for powerdot-FUBerlin
Version:        svn15878.0.01

Provides:       tex-powerdot-FUBerlin-doc
AutoReqProv:    No

%description -n texlive-powerdot-FUBerlin-doc
Documentation for powerdot-FUBerlin

%package -n texlive-physics
Provides:       tex-physics = %{tl_version}
License:        LPPL
Summary:        Macros supporting the Mathematics of Physics
Version:        svn28590.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xparse.sty), tex(amsmath.sty)
Provides:       tex(physics.sty) = %{tl_version}

%description -n texlive-physics
The package defines simple and flexible macros for typesetting
equations in the languages of vector calculus and linear
algebra, using Dirac notation.

%package -n texlive-physics-doc
Summary:        Documentation for physics
Version:        svn28590.1.3

Provides:       tex-physics-doc
AutoReqProv:    No

%description -n texlive-physics-doc
Documentation for physics

%package -n texlive-philokalia
Provides:       tex-philokalia = %{tl_version}
License:        OFL
Summary:        A font to typeset the Philokalia Books
Version:        svn45356
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontspec.sty), tex(xunicode.sty), tex(xltxtra.sty), tex(lettrine.sty)
Provides:       tex(Philokalia-Regular.otf) = %{tl_version}
Provides:       tex(eu1plk.fd) = %{tl_version}, tex(philokalia.sty) = %{tl_version}

%description -n texlive-philokalia
The philokalia package has been designed to ease the use of the
Philokalia-Regular OpenType font with XeLaTeX. The font started
as a project to digitize the typeface used to typeset the
Philokalia books.

%package -n texlive-philokalia-doc
Summary:        Documentation for philokalia
Version:        svn45356
Provides:       tex-philokalia-doc
AutoReqProv:    No

%description -n texlive-philokalia-doc
Documentation for philokalia

%package -n texlive-polyglossia
Provides:       tex-polyglossia = %{tl_version}
License:        LPPL 1.3
Summary:        An alternative to babel for XeLaTeX and LuaLaTeX
Version:        svn47392
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-etoolbox, tex-fontspec, tex-ifluatex, tex-makecmds
Requires:       tex-xkeyval, tex(luabidi.sty), tex(bidi.sty), tex(calc.sty)
Requires:       tex(hebrewcal.sty), tex(xkeyval.sty), tex(etoolbox.sty), tex(makecmds.sty)
Requires:       tex(fontspec.sty), tex(ifluatex.sty), tex(ifxetex.sty), tex(luatexbase.sty)
Provides:       tex(arabicdigits.map) = %{tl_version}, tex(bengalidigits.map) = %{tl_version}
Provides:       tex(devanagaridigits.map) = %{tl_version}
Provides:       tex(farsidigits.map) = %{tl_version}, tex(thaidigits.map) = %{tl_version}
Provides:       tex(arabicnumbers.sty) = %{tl_version}, tex(babel-hebrewalph.def) = %{tl_version}
Provides:       tex(babelsh.def) = %{tl_version}, tex(bengalidigits.sty) = %{tl_version}
Provides:       tex(cal-util.def) = %{tl_version}, tex(devanagaridigits.sty) = %{tl_version}
Provides:       tex(farsical.sty) = %{tl_version}, tex(gloss-albanian.ldf) = %{tl_version}
Provides:       tex(gloss-amharic.ldf) = %{tl_version}, tex(gloss-arabic.ldf) = %{tl_version}
Provides:       tex(gloss-armenian.ldf) = %{tl_version}, tex(gloss-asturian.ldf) = %{tl_version}
Provides:       tex(gloss-bahasai.ldf) = %{tl_version}, tex(gloss-bahasam.ldf) = %{tl_version}
Provides:       tex(gloss-basque.ldf) = %{tl_version}, tex(gloss-bengali.ldf) = %{tl_version}
Provides:       tex(gloss-brazil.ldf) = %{tl_version}, tex(gloss-breton.ldf) = %{tl_version}
Provides:       tex(gloss-bulgarian.ldf) = %{tl_version}
Provides:       tex(gloss-catalan.ldf) = %{tl_version}, tex(gloss-coptic.ldf) = %{tl_version}
Provides:       tex(gloss-croatian.ldf) = %{tl_version}, tex(gloss-czech.ldf) = %{tl_version}
Provides:       tex(gloss-danish.ldf) = %{tl_version}, tex(gloss-divehi.ldf) = %{tl_version}
Provides:       tex(gloss-dutch.ldf) = %{tl_version}, tex(gloss-english.ldf) = %{tl_version}
Provides:       tex(gloss-esperanto.ldf) = %{tl_version}
Provides:       tex(gloss-estonian.ldf) = %{tl_version}, tex(gloss-farsi.ldf) = %{tl_version}
Provides:       tex(gloss-finnish.ldf) = %{tl_version}, tex(gloss-french.ldf) = %{tl_version}
Provides:       tex(gloss-friulan.ldf) = %{tl_version}, tex(gloss-galician.ldf) = %{tl_version}
Provides:       tex(gloss-german.ldf) = %{tl_version}, tex(gloss-greek.ldf) = %{tl_version}
Provides:       tex(gloss-hebrew.ldf) = %{tl_version}, tex(gloss-hindi.ldf) = %{tl_version}
Provides:       tex(gloss-icelandic.ldf) = %{tl_version}
Provides:       tex(gloss-interlingua.ldf) = %{tl_version}
Provides:       tex(gloss-irish.ldf) = %{tl_version}, tex(gloss-italian.ldf) = %{tl_version}
Provides:       tex(gloss-kannada.ldf) = %{tl_version}, tex(gloss-khmer.ldf) = %{tl_version}
Provides:       tex(gloss-korean.ldf) = %{tl_version}, tex(gloss-lao.ldf) = %{tl_version}
Provides:       tex(gloss-latin.ldf) = %{tl_version}, tex(gloss-latvian.ldf) = %{tl_version}
Provides:       tex(gloss-lithuanian.ldf) = %{tl_version}
Provides:       tex(gloss-lsorbian.ldf) = %{tl_version}, tex(gloss-magyar.ldf) = %{tl_version}
Provides:       tex(gloss-malayalam.ldf) = %{tl_version}
Provides:       tex(gloss-marathi.ldf) = %{tl_version}, tex(gloss-nko.ldf) = %{tl_version}
Provides:       tex(gloss-norsk.ldf) = %{tl_version}, tex(gloss-nynorsk.ldf) = %{tl_version}
Provides:       tex(gloss-occitan.ldf) = %{tl_version}, tex(gloss-piedmontese.ldf) = %{tl_version}
Provides:       tex(gloss-polish.ldf) = %{tl_version}, tex(gloss-portuges.ldf) = %{tl_version}
Provides:       tex(gloss-romanian.ldf) = %{tl_version}, tex(gloss-romansh.ldf) = %{tl_version}
Provides:       tex(gloss-russian.ldf) = %{tl_version}, tex(gloss-samin.ldf) = %{tl_version}
Provides:       tex(gloss-sanskrit.ldf) = %{tl_version}, tex(gloss-scottish.ldf) = %{tl_version}
Provides:       tex(gloss-serbian.ldf) = %{tl_version}, tex(gloss-slovak.ldf) = %{tl_version}
Provides:       tex(gloss-slovenian.ldf) = %{tl_version}
Provides:       tex(gloss-spanish.ldf) = %{tl_version}, tex(gloss-swedish.ldf) = %{tl_version}
Provides:       tex(gloss-syriac.ldf) = %{tl_version}, tex(gloss-tamil.ldf) = %{tl_version}
Provides:       tex(gloss-telugu.ldf) = %{tl_version}, tex(gloss-thai.ldf) = %{tl_version}
Provides:       tex(gloss-tibetan.ldf) = %{tl_version}, tex(gloss-turkish.ldf) = %{tl_version}
Provides:       tex(gloss-turkmen.ldf) = %{tl_version}, tex(gloss-ukrainian.ldf) = %{tl_version}
Provides:       tex(gloss-urdu.ldf) = %{tl_version}, tex(gloss-usorbian.ldf) = %{tl_version}
Provides:       tex(gloss-vietnamese.ldf) = %{tl_version}
Provides:       tex(gloss-welsh.ldf) = %{tl_version}, tex(hebrewcal.sty) = %{tl_version}
Provides:       tex(hijrical.sty) = %{tl_version}, tex(nkonumbers.sty) = %{tl_version}
Provides:       tex(polyglossia.sty) = %{tl_version}, tex(xgreek-fixes.def) = %{tl_version}

%description -n texlive-polyglossia
This package provides a complete Babel replacement for users of
LuaLaTeX and XeLaTeX; it relies on the fontspec package,
version 2.0 at least. This is the first release that supports
use with LuaLaTeX; it should be considered "transitional" in
that role.

%package -n texlive-polyglossia-doc
Summary:        Documentation for polyglossia
Version:        svn47392
Provides:       tex-polyglossia-doc
AutoReqProv:    No
Requires:       tex-etoolbox-doc, tex-fontspec-doc, tex-ifluatex-doc, tex-makecmds-doc
Requires:       tex-xkeyval-doc

%description -n texlive-polyglossia-doc
Documentation for polyglossia

%package -n texlive-parades-doc
Provides:       tex-parades-doc = %{tl_version}
License:        LPPL
Summary:        doc files of parades
Version:        svn40042

AutoReqProv:    No

%description -n texlive-parades-doc
Documentation for parades

%package -n texlive-parades
Provides:       tex-parades = %{tl_version}
License:        LPPL
Summary:        Tabulators and space between paragraphs in galley approach
Version:        svn40042

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(paravesp.sty) = %{tl_version}

%description -n texlive-parades
The LaTeX package paravesp controls the spaces above and below
paragraphs. The python script parades.py generates paragraph
styles with support of space above, space below and tabulators.
The system imposes the galley approach on the document.

%package -n texlive-pbibtex-base-doc
Provides:       tex-pbibtex-base-doc = %{tl_version}
License:        BSD
Summary:        doc files of pbibtex-base
Version:        svn40986

AutoReqProv:    No

%description -n texlive-pbibtex-base-doc
Documentation for pbibtex-base

%package -n texlive-pbibtex-base
Provides:       tex-pbibtex-base = %{tl_version}
License:        BSD
Summary:        Bibliography styles and miscellaneous files for pBibTeX
Version:        svn40986

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-pbibtex-base
These are miscellaneous files, including bibliography styles
(.bst), for pBibTeX, which is a Japanese extended version of
BibTeX contained in TeX Live. The bundle is a redistribution
derived from the ptex-texmf distribution by ASCII MEDIA WORKS.

%package -n texlive-pgfornament-doc
Provides:       tex-pgfornament-doc = %{tl_version}
License:        LPPL
Summary:        doc files of pgfornament
Version:        svn39988

AutoReqProv:    No

%description -n texlive-pgfornament-doc
Documentation for pgfornament

%package -n texlive-pgfornament
Provides:       tex-pgfornament = %{tl_version}
License:        LPPL
Summary:        Drawing of Vectorian ornaments with PGF/TikZ
Version:        svn39988

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tikzrput.sty) = %{tl_version}, tex(pgfornament.sty) = %{tl_version}
Provides:       tex(pgflibraryam.code.tex) = %{tl_version}
Provides:       tex(pgflibraryvectorian.code.tex) = %{tl_version}

%description -n texlive-pgfornament
This package allows the drawing of Vectorian ornaments (196)
with PGF/TikZ. The documentation presents the syntax and
parameters of the macro "pgfornament".

%package -n texlive-pgf-spectra-doc
Provides:       tex-pgf-spectra-doc = %{tl_version}
License:        LPPL
Summary:        doc files of pgf-spectra
Version:        svn42986
AutoReqProv:    No

%description -n texlive-pgf-spectra-doc
Documentation for pgf-spectra

%package -n texlive-pgf-spectra
Provides:       tex-pgf-spectra = %{tl_version}
License:        LPPL
Summary:        Draw continuous or discrete spectra using PGF/TikZ
Version:        svn42986
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(pgf-spectra.sty) = %{tl_version}

%description -n texlive-pgf-spectra
The purpose of this package is to draw the spectra of elements
in a simple way. It is based on the package pst-spectra,
supporting the same options, but also adding some new options.
It relies on PGF/TikZ for drawing the desired spectrum,
continuous or discrete. As in pst-spectra, there are data
available for the spectra of 99 elements and their ions (from
the NASA database). It also allows the user to draw spectra
using their own data.

%package -n texlive-platex-doc
Provides:       tex-platex-doc = %{tl_version}
License:        BSD
Summary:        doc files of platex
Version:        svn48293
AutoReqProv:    No

%description -n texlive-platex-doc
Documentation for platex

%package -n texlive-platex
Provides:       tex-platex = %{tl_version}
License:        BSD
Summary:        pLaTeX2e and miscellaneous macros for pTeX
Version:        svn48293
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-platex-bin
Provides:       tex(jbook.cls) = %{tl_version}, tex(treport.cls) = %{tl_version}
Provides:       tex(jreport.cls) = %{tl_version}, tex(jltxdoc.cls) = %{tl_version}
Provides:       tex(jarticle.cls) = %{tl_version}, tex(tbook.cls) = %{tl_version}
Provides:       tex(tarticle.cls) = %{tl_version}, tex(pfltrace.sty) = %{tl_version}
Provides:       tex(jarticle.sty) = %{tl_version}, tex(jreport.sty) = %{tl_version}
Provides:       tex(platexrelease.sty) = %{tl_version}, tex(jbook.sty) = %{tl_version}
Provides:       tex(tarticle.sty) = %{tl_version}, tex(ptrace.sty) = %{tl_version}
Provides:       tex(tbook.sty) = %{tl_version}, tex(treport.sty) = %{tl_version}
Provides:       tex(oldpfont.sty) = %{tl_version}, tex(plext.sty) = %{tl_version}
Provides:       tex(kinsoku.tex) = %{tl_version}, tex(pl209.def) = %{tl_version}
Provides:       tex(jy1gt.fd) = %{tl_version}, tex(jt1gt.fd) = %{tl_version}
Provides:       tex(jt1mc.fd) = %{tl_version}, tex(jy1mc.fd) = %{tl_version}
Provides:       tex(jbk12.clo) = %{tl_version}, tex(jbk10.clo) = %{tl_version}
Provides:       tex(tsize11.clo) = %{tl_version}, tex(tsize12.clo) = %{tl_version}
Provides:       tex(jsize10.clo) = %{tl_version}, tex(jsize12.clo) = %{tl_version}
Provides:       tex(tsize10.clo) = %{tl_version}, tex(tbk12.clo) = %{tl_version}
Provides:       tex(jsize11.clo) = %{tl_version}, tex(tbk11.clo) = %{tl_version}
Provides:       tex(tbk10.clo) = %{tl_version}, tex(jbk11.clo) = %{tl_version}

%description -n texlive-platex
The bundle provides pLaTeX2e and miscellaneous macros for pTeX
and e-pTeX. This is a community edition forked from the
original ASCII edition (ptex-texmf-2.5).

%package -n texlive-padauk
Summary:        A high-quality TrueType font that supports Myanmar script
Version:        svn42617
License:        OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(Padauk-Bold.ttf) = %{tl_version}, tex(Padauk-Regular.ttf) = %{tl_version}
Provides:       tex(PadaukBook-Bold.ttf) = %{tl_version}
Provides:       tex(PadaukBook-Regular.ttf) = %{tl_version}

%description -n texlive-padauk
Padauk is a Unicode-based font family with broad support for
writing systems that use the Myanmar script.

%package -n texlive-pdfreview
Summary:        Annotate PDF files with margin notes
Version:        svn45391
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pdfreview.sty) = %{tl_version}

%description -n texlive-pdfreview
This package lets you add comments in the page margins of PDF
files, e.g. when reviewing manuscripts or grading reports. The
PDF file to be annotated is included, one page at a time, as
graphics, in a manner similar to the pdfpages package. Notes
are placed in the margin next to the included graphics using a
grid of help lines. Alternatively, only numbers are placed in
the page margins, and the notes are collected into a numbered
list at the end of the document. Note that this package is not
intended for adding notes directly to the LaTeX source of the
document that is being reviewed; instead, the document
undergoing review is already in PDF format and remains
unchanged. Also note that this package does not produce the
usual PDF "sticky notes" that must be opened by clicking on
them; instead, the notes are simply shown as text. This package
depends on the following other LaTeX package: adjustbox, calc,
geometry, graphicx, grffile, ifthen, kvoptions, tikz, ulem, and
xstring.

%package -n texlive-phffullpagefigure
Summary:        Figures which fill up a whole page
Version:        svn41857
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(phffullpagefigure.sty) = %{tl_version}

%description -n texlive-phffullpagefigure
This package defines a figure environment which provides the
figure content on its own page, with the corresponding caption
reading for example "Figure 3 (on next page): <caption>".

%package -n texlive-phfnote
Summary:        Basic formatting for short documents
Version:        svn41858
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(phfnote.sty) = %{tl_version}

%description -n texlive-phfnote
This package provides basic formatting for short documents such
as notes on a specific topic, short documentation, or quick
memos. It aims to cover all basic needs for such purposes:
include a standard set of relevant packages, a nice title which
doesn't take up too much space, better page margin sizes, and
some basic styling to make the note look nicer. At the same
time, it is highly flexible and customizable.

%package -n texlive-phfparen
Summary:        Parenthetic math expressions made simpler and less redundant
Version:        svn41859
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(phfparen.sty) = %{tl_version}

%description -n texlive-phfparen
This package provides a more condensed and flexible syntax for
parenthesis-delimited expressions in math mode which also
allows for an easier switching of brace sizes. For example, the
syntax " `\big( a + b ) " can be used to replace "\bigl( a + b
\bigr)".

%package -n texlive-phfqit
Summary:        Macros for typesetting Quantum Information Theory
Version:        svn45084
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(phfqit.sty) = %{tl_version}

%description -n texlive-phfqit
This package provides macros to typeset some general
mathematical operators (identity operator, trace, diagonal,
rank, ...), a powerful implementation of the bra-ket notation
(kets, bras, brakets, matrix elements etc. which can be sized
as required), delimited expressions such as averages and norms,
and some basic Lie algebra/group names. Macros for entropy
measures for quantum information theory (smooth min- and
max-entropy, smooth relative entropies, etc.) are also
provided.

%package -n texlive-phfquotetext
Summary:        Quote verbatim text without white space formatting
Version:        svn41869
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(phfquotetext.sty) = %{tl_version}

%description -n texlive-phfquotetext
This package provides an environment for displaying block text
with special characters, such as verbatim quotes from a referee
report which may contain pseudo-(La)TeX code. This behaves like
a verbatim environment, except that it displays its content as
normal paragraph content, ignoring any white space
preformatting.

%package -n texlive-phfsvnwatermark
Summary:        Watermarks with version control information from SVN
Version:        svn41870
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(phfsvnwatermark.sty) = %{tl_version}

%description -n texlive-phfsvnwatermark
This package allows you to add version control information as a
gray watermark on each page of your document. The SVN info is
read from keyword tags such as $Id$, $Date$, and $Author$ via
the svn or svn-multi packages.

%package -n texlive-phfthm
Summary:        Goodies for theorems and proofs
Version:        svn41871
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(phfthm.sty) = %{tl_version}

%description -n texlive-phfthm
This package provides enhanced theorem and proof environments
based on the amsthm original versions. It allows for hooks to
be placed, adds some default goodies and is highly
customizable. In particular, it can connect theorems to proofs,
automatically producing text such as "See proof on page XYZ"
and "Proof of Theorem 4: ...".

%package -n texlive-phonenumbers
Summary:        Typesetting telephone numbers with LaTeX.
Version:        svn48355
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(phn-AT_Ortsnamen.tex) = %{tl_version}
Provides:       tex(phn-AT_Vorwahlen.tex) = %{tl_version}
Provides:       tex(phn-DE_Ortsnamen.tex) = %{tl_version}
Provides:       tex(phn-DE_Vorwahlen.tex) = %{tl_version}
Provides:       tex(phn-FR_Ortsnamen.tex) = %{tl_version}
Provides:       tex(phn-FR_Vorwahlen.tex) = %{tl_version}
Provides:       tex(phn-Landeskennzahlen.tex) = %{tl_version}
Provides:       tex(phn-UK_Ortsnamen.tex) = %{tl_version}
Provides:       tex(phn-UK_Vorwahlen.tex) = %{tl_version}
Provides:       tex(phn-US_Ortsnamen.tex) = %{tl_version}
Provides:       tex(phn-US_Vorwahlen.tex) = %{tl_version}
Provides:       tex(phonenumbers.sty) = %{tl_version}

%description -n texlive-phonenumbers
The phonenumbers package makes it possible to typeset telephone
numbers according to different national conventions. German,
Austrian, French, British and North American phone numbers are
supported. Phone numbers from other countries are supported
rudimentarily. The user can select from various formatting
options, including the additional output of the country calling
code. The package is able to check if a phone number is valid
according to the national rules. It also allows to link phone
numbers using the hyperref package.

%package -n texlive-platexcheat-doc
Summary:        Japanese translation of LATEX cheat sheet
Version:        svn42918
License:        MIT

%description -n texlive-platexcheat-doc
This is a translation to Japanese of Winston Chang’s LATEX cheat sheet
(a reference sheet for writing scientific papers).

%package -n texlive-platex-tools
Summary:        pLaTeX standard tools bundle
Version:        svn46985
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bounddvi.sty) = %{tl_version}, tex(plarray.sty) = %{tl_version}
Provides:       tex(plextarray.sty) = %{tl_version}, tex(plextdelarray.sty) = %{tl_version}
Provides:       tex(pxeverysel.sty) = %{tl_version}, tex(pxeveryshi.sty) = %{tl_version}
Provides:       tex(pxftnright.sty) = %{tl_version}, tex(pxgentombow.sty) = %{tl_version}

%description -n texlive-platex-tools
This bundle is an extended version of the latex-tools bundle
developed by the LaTeX team, mainly intended to support
pLaTeX2e and upLaTeX2e. Currently patches for the latex-tools
bundle and Martin Schroder's ms bundle are included. It also
contains the package bounddvi, which sets the papersize special
in DVI files and can be used in both vertical and horizontal
writing directions.

%package -n texlive-poetry
Summary:        Facilities for typesetting poetry and poetical structure
Version:        svn44655
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(poetry.sty) = %{tl_version}

%description -n texlive-poetry
The poetry package provides some macros and general doodads for
typesetting poetry. There is, of course, already the excellent
verse package, and the poetrytex package provides some extra
functionality on top of it. But poetry provides much of the
same functionality in a bit of a different way, and with a few
additional abilities, such as facilities for a list of poems,
an index of first lines, and some structural commands.

%package -n texlive-padcount
Summary:        Pad numbers with arbitrary characters
Version:        svn47621
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(padcount.sty) = %{tl_version}

%description -n texlive-padcount
This package provides some simple macros which will pad numbers
(or, indeed, any expanded token) with your choice of character
(defaulting to "0") to your choice of number of places
(defaults to "2"). This works not only on arabic numerals, but
on any expanded list of tokens passed to it. This makes it
suitable for, among other things, counters of all kinds.

%package -n texlive-pdfoverlay
Summary:        A LaTeX style for overlaying text on a PDF
Version:        svn47657
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(xparse.sty)
Requires:       tex(everypage.sty), tex(pdfpages.sty)
Provides:       tex(pdfoverlay.sty) = %{tl_version}

%description -n texlive-pdfoverlay
It is often desirable to take an exisiting PDF and easily add
annotations or text overlaying the PDF. This might arise if you
wish to add comments to a PDF, fill in a PDF form, or add text
to a PDF where space has been left for notes. This package
provides a simple interface to do this without having to resort
to inserting one page at a time. Some or all of the pages of
the PDF can be included and not all pages of the PDF need have
overlayed text. It is also possible to include text between
pages of the PDF. Another advantage of this package is that the
overlayed text can be set as normal flowing from one page to
another or with manual page breaks if you wish. It is also
possible to use any standard method to position text at
arbitrary places on a given page. This package depends on
xparse, everypage, and pdfpages.

%package -n texlive-pdfpc-movie
Summary:        Pdfpc viewer-compatible hyperlinks to movies
Version:        svn48245
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(etoolbox.sty)
Requires:       tex(hyperref.sty), tex(pgfkeys.sty), pdfpc
Provides:       tex(pdfpc-movie.sty) = %{tl_version}

%description -n texlive-pdfpc-movie
This LaTeX2e package provides a command \pdfpcmovie for
embedding (hyperlinking) movies in a way compatible with the
PDF Presenter Console (pdfpc), a GPL2-licensed multi-monitor
PDF presentation viewer application available on GitHub and
shipped with some LINUX distributions such as Debian, Fedora,
and Arch. The package depends on etoolbox, hyperref, and
pgfkeys.

%package -n texlive-pdfprivacy
Summary:        A LaTeX package to remove or suppress pdf meta-data
Version:        svn45985
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pdfprivacy.sty) = %{tl_version}

%description -n texlive-pdfprivacy
Creating pdfs with pdfLaTeX populates several pdf meta-data
fields such as date/time of creation/modification, information
about the LaTeX installation (e.g., pdfTeX version), and the
relative paths of included pdfs. The pdfprivacy package
provides support for emptying several of these pdf meta-data
fields as well as suppressing some pdfTeX meta-data entries in
the resulting pdf.

%package -n texlive-penrose
Summary:        A TikZ library for producing Penrose tilings
Version:        svn48202
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzlibrarypenrose.code.tex) = %{tl_version}

%description -n texlive-penrose
This package provides a TikZ library for drawing Penrose tiles.
It currently supports the kite/dart, rhombus, and pentagon tile
sets. There are two main methods for their placement: one that
automatically generates a tiling, and one that allows for "by
hand" placement. Furthermore, the tiles themselves can be
deformed and will still (hopefully!) fit together in the
correct fashion.

%package -n texlive-pgfornament-han
Summary:        pgfornament library for Chinese traditional motifs and patterns
Version:        svn47789
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(beamerthemeHeavenlyClouds.sty) = %{tl_version}
Provides:       tex(beamerthemeXiaoshan.sty) = %{tl_version}
Provides:       tex(cncolours.sty) = %{tl_version}, tex(han1.pgf) = %{tl_version}
Provides:       tex(han10.pgf) = %{tl_version}, tex(han11.pgf) = %{tl_version}
Provides:       tex(han12.pgf) = %{tl_version}, tex(han13.pgf) = %{tl_version}
Provides:       tex(han14.pgf) = %{tl_version}, tex(han15.pgf) = %{tl_version}
Provides:       tex(han16.pgf) = %{tl_version}, tex(han17.pgf) = %{tl_version}
Provides:       tex(han18.pgf) = %{tl_version}, tex(han19.pgf) = %{tl_version}
Provides:       tex(han2.pgf) = %{tl_version}, tex(han20.pgf) = %{tl_version}
Provides:       tex(han21.pgf) = %{tl_version}, tex(han22.pgf) = %{tl_version}
Provides:       tex(han23.pgf) = %{tl_version}, tex(han24.pgf) = %{tl_version}
Provides:       tex(han25.pgf) = %{tl_version}, tex(han26.pgf) = %{tl_version}
Provides:       tex(han27.pgf) = %{tl_version}, tex(han28.pgf) = %{tl_version}
Provides:       tex(han29.pgf) = %{tl_version}, tex(han3.pgf) = %{tl_version}
Provides:       tex(han30.pgf) = %{tl_version}, tex(han31.pgf) = %{tl_version}
Provides:       tex(han32.pgf) = %{tl_version}, tex(han33.pgf) = %{tl_version}
Provides:       tex(han34.pgf) = %{tl_version}, tex(han35.pgf) = %{tl_version}
Provides:       tex(han36.pgf) = %{tl_version}, tex(han37.pgf) = %{tl_version}
Provides:       tex(han38.pgf) = %{tl_version}, tex(han39.pgf) = %{tl_version}
Provides:       tex(han4.pgf) = %{tl_version}, tex(han40.pgf) = %{tl_version}
Provides:       tex(han41.pgf) = %{tl_version}, tex(han42.pgf) = %{tl_version}
Provides:       tex(han43.pgf) = %{tl_version}, tex(han44.pgf) = %{tl_version}
Provides:       tex(han45.pgf) = %{tl_version}, tex(han46.pgf) = %{tl_version}
Provides:       tex(han47.pgf) = %{tl_version}, tex(han48.pgf) = %{tl_version}
Provides:       tex(han49.pgf) = %{tl_version}, tex(han5.pgf) = %{tl_version}
Provides:       tex(han50.pgf) = %{tl_version}, tex(han51.pgf) = %{tl_version}
Provides:       tex(han52.pgf) = %{tl_version}, tex(han53.pgf) = %{tl_version}
Provides:       tex(han54.pgf) = %{tl_version}, tex(han55.pgf) = %{tl_version}
Provides:       tex(han56.pgf) = %{tl_version}, tex(han57.pgf) = %{tl_version}
Provides:       tex(han58.pgf) = %{tl_version}, tex(han59.pgf) = %{tl_version}
Provides:       tex(han6.pgf) = %{tl_version}, tex(han60.pgf) = %{tl_version}
Provides:       tex(han61.pgf) = %{tl_version}, tex(han62.pgf) = %{tl_version}
Provides:       tex(han63.pgf) = %{tl_version}, tex(han64.pgf) = %{tl_version}
Provides:       tex(han65.pgf) = %{tl_version}, tex(han66.pgf) = %{tl_version}
Provides:       tex(han67.pgf) = %{tl_version}, tex(han68.pgf) = %{tl_version}
Provides:       tex(han69.pgf) = %{tl_version}, tex(han7.pgf) = %{tl_version}
Provides:       tex(han70.pgf) = %{tl_version}, tex(han71.pgf) = %{tl_version}
Provides:       tex(han72.pgf) = %{tl_version}, tex(han73.pgf) = %{tl_version}
Provides:       tex(han74.pgf) = %{tl_version}, tex(han75.pgf) = %{tl_version}
Provides:       tex(han76.pgf) = %{tl_version}, tex(han77.pgf) = %{tl_version}
Provides:       tex(han8.pgf) = %{tl_version}, tex(han9.pgf) = %{tl_version}
Provides:       tex(pgflibraryhan.code.tex) = %{tl_version}
Provides:       tex(pgfornament-han.sty) = %{tl_version}

%description -n texlive-pgfornament-han
This package provides a pgfornament library for Chinese
traditional motifs and patterns. The command \pgfornamenthan
takes the same options as \pgfornament from the pgfornament
package, but renders Chinese traditional motifs instead. The
list of supported motifs, as well as some examples, can be
found in the accompanying documentation.

%package -n texlive-pixelart
Summary:        A package to draw pixel-art pictures
Version:        svn46740
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pixelart.sty) = %{tl_version}

%description -n texlive-pixelart
A LaTeX package to draw single-color pixel-art pictures using
TikZ.

%package -n texlive-plantuml
Summary:        Support for rendering UML diagrams using the syntax and tool of PlantUML
Version:        svn47924
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(plantuml.lua) = %{tl_version}, tex(plantuml.sty) = %{tl_version}

%description -n texlive-plantuml
The package provides support for rendering UML diagrams using
the syntax and tools of PlantUML. The PlantUML syntax is very
short and thus enables quickly specifying UML diagrams. Using
dot, PlantUML layouts the diagrams.

%package -n texlive-plex
Summary:        Support for IBM Plex fonts
Version:        svn48332
License:        OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(plx_3iickh.enc) = %{tl_version}, tex(plx_6tuc4c.enc) = %{tl_version}
Provides:       tex(plx_ankagf.enc) = %{tl_version}, tex(plx_be3ach.enc) = %{tl_version}
Provides:       tex(plx_dqgnwu.enc) = %{tl_version}, tex(plx_eofykt.enc) = %{tl_version}
Provides:       tex(plx_errukl.enc) = %{tl_version}, tex(plx_i5ra6t.enc) = %{tl_version}
Provides:       tex(plx_its57d.enc) = %{tl_version}, tex(plx_jmvqu6.enc) = %{tl_version}
Provides:       tex(plx_m2a4iq.enc) = %{tl_version}, tex(plx_mlp3up.enc) = %{tl_version}
Provides:       tex(plx_nhokty.enc) = %{tl_version}, tex(plx_ojqnwd.enc) = %{tl_version}
Provides:       tex(plx_oqvkyq.enc) = %{tl_version}, tex(plx_pkz4m6.enc) = %{tl_version}
Provides:       tex(plx_til3jj.enc) = %{tl_version}, tex(plx_tire4t.enc) = %{tl_version}
Provides:       tex(plx_toaz2j.enc) = %{tl_version}, tex(plx_wvtw5j.enc) = %{tl_version}
Provides:       tex(plx_xl2q4z.enc) = %{tl_version}, tex(plx_y64dew.enc) = %{tl_version}
Provides:       tex(plex.map) = %{tl_version}, tex(IBMPlexMono-Bold.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-Light.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-Regular.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-Text.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-Light.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-Regular.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-Text.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin.otf) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-Bold.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-BoldItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-ExtraLight.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-ExtraLightItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-Italic.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-Light.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-LightItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-Medium.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-MediumItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-Regular.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-SemiBold.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-Text.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-TextItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-Thin.otf) = %{tl_version}
Provides:       tex(IBMPlexSansCondensed-ThinItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Regular.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin.otf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic.otf) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-sup-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-sup-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-sup-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-Light.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-Regular.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-Text.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-Light.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-Regular.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-Text.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin.pfb) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Regular.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin.pfb) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-Regular.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin.pfb) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic.pfb) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Text-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-TextItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexMono-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Text-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-TextItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSans-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Text-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSansCond-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Text-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-sup-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-sup-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-t1.vf) = %{tl_version}
Provides:       tex(IBMPlexSerif-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1IBMPlexMono-Sup.fd) = %{tl_version}
Provides:       tex(LY1IBMPlexMono-TLF.fd) = %{tl_version}
Provides:       tex(LY1IBMPlexSans-Sup.fd) = %{tl_version}
Provides:       tex(LY1IBMPlexSans-TLF.fd) = %{tl_version}
Provides:       tex(LY1IBMPlexSansCondensed-Sup.fd) = %{tl_version}
Provides:       tex(LY1IBMPlexSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(LY1IBMPlexSerif-Sup.fd) = %{tl_version}
Provides:       tex(LY1IBMPlexSerif-TLF.fd) = %{tl_version}
Provides:       tex(OT1IBMPlexMono-Sup.fd) = %{tl_version}
Provides:       tex(OT1IBMPlexMono-TLF.fd) = %{tl_version}
Provides:       tex(OT1IBMPlexSans-Sup.fd) = %{tl_version}
Provides:       tex(OT1IBMPlexSans-TLF.fd) = %{tl_version}
Provides:       tex(OT1IBMPlexSansCondensed-Sup.fd) = %{tl_version}
Provides:       tex(OT1IBMPlexSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(OT1IBMPlexSerif-Sup.fd) = %{tl_version}
Provides:       tex(OT1IBMPlexSerif-TLF.fd) = %{tl_version}
Provides:       tex(T1IBMPlexMono-Sup.fd) = %{tl_version}
Provides:       tex(T1IBMPlexMono-TLF.fd) = %{tl_version}
Provides:       tex(T1IBMPlexSans-Sup.fd) = %{tl_version}
Provides:       tex(T1IBMPlexSans-TLF.fd) = %{tl_version}
Provides:       tex(T1IBMPlexSansCondensed-Sup.fd) = %{tl_version}
Provides:       tex(T1IBMPlexSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T1IBMPlexSerif-Sup.fd) = %{tl_version}
Provides:       tex(T1IBMPlexSerif-TLF.fd) = %{tl_version}
Provides:       tex(TS1IBMPlexMono-TLF.fd) = %{tl_version}
Provides:       tex(TS1IBMPlexSans-TLF.fd) = %{tl_version}
Provides:       tex(TS1IBMPlexSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(TS1IBMPlexSerif-TLF.fd) = %{tl_version}
Provides:       tex(plex-mono.sty) = %{tl_version}, tex(plex-sans.sty) = %{tl_version}
Provides:       tex(plex-serif.sty) = %{tl_version}

%description -n texlive-plex
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the IBM Plex families of fonts. Serif, Sans and
Mono families are available in eight weights: Regular, Light,
ExtraLight, Thin, Bold, Text, Medium and SemiBold (with
corresponding italics).

%package -n texlive-plex-otf
Summary:        Support for the OpenType font IBM Plex
Version:        svn47562
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(plex-otf.sty) = %{tl_version}

%description -n texlive-plex-otf
This package supports the free otf fonts from the IBM Plex
project which are available from GitHub or already part of your
system (Windows/Linux/...). This package supports only XeLaTeX
or LuaLaTeX; for pdfLaTeX use plex-mono.sty, plex-sans.sty,
and/or plex-serif.sty from the plex package. IBM Plex has no
math symbols. You will have to use one of the existing math
fonts if you need them.

%package -n texlive-pm-isomath
Summary:        Poor man ISO math for pdfLaTeX users
Version:        svn46402
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pm-isomath.sty) = %{tl_version}

%description -n texlive-pm-isomath
This small package realizes a poor man approximation of the ISO
regulations for physical sciences and technology. Contrary to
other more elegant solutions, it does not load any math
alphabet, since pdfLaTeX can use only a maximum of such
alphabets. The necessary user macros are defined for typsetting
common math symbols that require specia ISO treatement.

%package -n texlive-polexpr
Summary:        A parser for polynomial expressions
Version:        svn47509
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(polexpr.sty) = %{tl_version}

%description -n texlive-polexpr
The package provides \poldef: a parser for polynomial
expressions based upon the \xintdeffunc mechanism of the
package xintexpr. The parsed expressions use the operations of
algebra (inclusive of composition of functions) with standard
operators, fractional numbers (possibly in scientific notation)
and previously defined polynomial functions or other constructs
as recognized by the \xintexpr numerical parser. The
polynomials are then not only genuine \xintexpr numerical
functions but additionally are also known to the package via
their coefficients. This allows dedicated macros to implement
polynomial algorithmics.

%package -n texlive-postage
Summary:        stamp letters with >>Deutsche Post<<'s service >>Internetmarke<<
Version:        svn47893
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(postage.sty) = %{tl_version}

%description -n texlive-postage
The postage package is used for franking letters with
>>Deutsche Post<<'s online postage service >>Internetmarke<<.
Note that in order to print valid stamps you must point to a
valid PDF of >>Deutsche Post<<'s >>Ausdruck 4-spaltig (DIN
A4)<<.

%package -n texlive-powerdot-tuliplab
Summary:        A style package for Powerdot to provide the design of TULIP Lab
Version:        svn47963
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tulip-logo.eps) = %{tl_version}, tex(tulip-wordmark.eps) = %{tl_version}
Provides:       tex(tulip.eps) = %{tl_version}, tex(tulip-wordmark0.eps) = %{tl_version}
Provides:       tex(tulip-wordmark1.eps) = %{tl_version}
Provides:       tex(tulip0.eps) = %{tl_version}, tex(tulip1.eps) = %{tl_version}
Provides:       tex(tulip2.eps) = %{tl_version}, tex(tulip3.eps) = %{tl_version}
Provides:       tex(powerdot-tuliplab.sty) = %{tl_version}

%description -n texlive-powerdot-tuliplab
powerdot-tuliplab is the LaTeX package used in TULIP Lab for
presentation drafting. It comes with several sample .tex files
so that you can quickly start working with it.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD

cd %{buildroot}%{_texdir}/texmf-dist/
sed -i 's|newline{\\Hnewline}|newline{^^J}|g' %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-tex4ht.def

install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="gust/poltawski public/phaistos public/philokalia \
public/playfair"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
cp -R %{buildroot}/%{_texdir}/texmf-dist/doc/man %{buildroot}/%{_datadir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man1/platex.*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*
rm -f %{buildroot}%{_datadir}/texlive/tlpkg/tlpobj/platex.*tlpobj


%files -n texlive-plain
%license knuth.txt
%{_texdir}/texmf-dist/makeindex/plain/
%{_texdir}/texmf-dist/tex/plain/

%files -n texlive-pgf
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/context/third/pgf/
%{_texdir}/texmf-dist/tex/generic/pgf/
%{_texdir}/texmf-dist/tex/latex/pgf/
%{_texdir}/texmf-dist/tex/plain/pgf/

%files -n texlive-pgf-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/pgf/

%files -n texlive-perception
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/perception/

%files -n texlive-perception-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/perception/

%files -n texlive-pnas2009
%{_texdir}/texmf-dist/bibtex/bst/pnas2009/

%files -n texlive-pacioli
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/pacioli/
%{_texdir}/texmf-dist/fonts/tfm/public/pacioli/
%{_texdir}/texmf-dist/tex/latex/pacioli/

%files -n texlive-pacioli-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/pacioli/

%files -n texlive-paratype
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/paratype/
%{_texdir}/texmf-dist/fonts/enc/dvips/paratype/
%{_texdir}/texmf-dist/fonts/map/dvips/paratype/
%{_texdir}/texmf-dist/fonts/tfm/paratype/
%{_texdir}/texmf-dist/fonts/truetype/paratype/
%{_texdir}/texmf-dist/fonts/type1/paratype/
%{_texdir}/texmf-dist/fonts/vf/paratype/
%{_texdir}/texmf-dist/tex/latex/paratype/

%files -n texlive-paratype-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/paratype/

%files -n texlive-phaistos
%license lppl1.txt
%{_datadir}/fonts/phaistos
%{_texdir}/texmf-dist/fonts/afm/public/phaistos/
%{_texdir}/texmf-dist/fonts/map/dvips/phaistos/
%{_texdir}/texmf-dist/fonts/opentype/public/phaistos/
%{_texdir}/texmf-dist/fonts/tfm/public/phaistos/
%{_texdir}/texmf-dist/fonts/type1/public/phaistos/
%{_texdir}/texmf-dist/tex/latex/phaistos/

%files -n texlive-phaistos-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/phaistos/

%files -n texlive-phonetic
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/phonetic/
%{_texdir}/texmf-dist/fonts/tfm/public/phonetic/
%{_texdir}/texmf-dist/tex/latex/phonetic/

%files -n texlive-phonetic-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/phonetic/

%files -n texlive-pigpen
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/pigpen/
%{_texdir}/texmf-dist/fonts/source/public/pigpen/
%{_texdir}/texmf-dist/fonts/tfm/public/pigpen/
%{_texdir}/texmf-dist/fonts/type1/public/pigpen/
%{_texdir}/texmf-dist/tex/latex/pigpen/

%files -n texlive-pigpen-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pigpen/

%files -n texlive-playfair
%license ofl.txt
%{_datadir}/fonts/playfair
%{_texdir}/texmf-dist/fonts/enc/dvips/playfair/
%{_texdir}/texmf-dist/fonts/map/dvips/playfair/
%{_texdir}/texmf-dist/fonts/opentype/public/playfair/
%{_texdir}/texmf-dist/fonts/tfm/public/playfair/
%{_texdir}/texmf-dist/fonts/type1/public/playfair/
%{_texdir}/texmf-dist/fonts/vf/public/playfair/
%{_texdir}/texmf-dist/tex/latex/playfair/

%files -n texlive-playfair-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/playfair/

%files -n texlive-poltawski
%license gfsl.txt
%{_datadir}/fonts/poltawski
%{_texdir}/texmf-dist/fonts/afm/gust/poltawski/
%{_texdir}/texmf-dist/fonts/enc/dvips/poltawski/
%{_texdir}/texmf-dist/fonts/map/dvips/poltawski/
%{_texdir}/texmf-dist/fonts/opentype/gust/poltawski/
%{_texdir}/texmf-dist/fonts/tfm/gust/poltawski/
%{_texdir}/texmf-dist/fonts/type1/gust/poltawski/
%{_texdir}/texmf-dist/tex/latex/poltawski/

%files -n texlive-poltawski-doc
%license gfsl.txt
%{_texdir}/texmf-dist/doc/fonts/poltawski/

%files -n texlive-palatino
%license gpl.txt
%{_texdir}/texmf-dist/dvips/palatino/
%{_texdir}/texmf-dist/fonts/afm/adobe/palatino/
%{_texdir}/texmf-dist/fonts/afm/urw/palatino/
%{_texdir}/texmf-dist/fonts/map/dvips/palatino/
%{_texdir}/texmf-dist/fonts/tfm/adobe/palatino/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/palatino/
%{_texdir}/texmf-dist/fonts/type1/urw/palatino/
%{_texdir}/texmf-dist/fonts/vf/adobe/palatino/
%{_texdir}/texmf-dist/fonts/vf/urw35vf/palatino/
%{_texdir}/texmf-dist/tex/latex/palatino/

%files -n texlive-pas-crosswords
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pas-crosswords/

%files -n texlive-pas-crosswords-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pas-crosswords/

%files -n texlive-pdf-trans
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/pdf-trans/

%files -n texlive-pdf-trans-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/pdf-trans/

%files -n texlive-plainpkg
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/plainpkg/

%files -n texlive-plainpkg-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/plainpkg/

%files -n texlive-path
%{_texdir}/texmf-dist/tex/generic/path/

%files -n texlive-path-doc
%{_texdir}/texmf-dist/doc/generic/path/

%files -n texlive-passivetex
%{_texdir}/texmf-dist/tex/xmltex/passivetex/

%files -n texlive-parallel
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/parallel/

%files -n texlive-parallel-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/parallel/

%files -n texlive-parrun
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/parrun/

%files -n texlive-parrun-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/parrun/

%files -n texlive-phonrule
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/phonrule/

%files -n texlive-phonrule-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/phonrule/

%files -n texlive-plari
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/plari/

%files -n texlive-plari-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/plari/

%files -n texlive-play
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/play/

%files -n texlive-play-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/play/

%files -n texlive-poemscol
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/poemscol/

%files -n texlive-poemscol-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/poemscol/

%files -n texlive-poetrytex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/poetrytex/

%files -n texlive-poetrytex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/poetrytex/

%files -n texlive-persian-bib
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/persian-bib/
%{_texdir}/texmf-dist/bibtex/csf/persian-bib/

%files -n texlive-persian-bib-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/persian-bib/

%files -n texlive-patgen2-tutorial-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/support/patgen2-tutorial/

%files -n texlive-pictexsum-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/pictexsum/

%files -n texlive-plain-doc-doc
%{_texdir}/texmf-dist/doc/plain/plain-doc/

%files -n texlive-pl
%license pd.txt
%{_texdir}/texmf-dist/dvips/pl/
%{_texdir}/texmf-dist/fonts/afm/public/pl/
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/
%{_texdir}/texmf-dist/fonts/map/dvips/pl/
%{_texdir}/texmf-dist/fonts/source/public/pl/
%{_texdir}/texmf-dist/fonts/tfm/public/pl/
%{_texdir}/texmf-dist/fonts/type1/public/pl/

%files -n texlive-pl-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/pl/

%files -n texlive-polski
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/polski/

%files -n texlive-polski-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/polski/

%files -n texlive-parskip
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/parskip/

%files -n texlive-parskip-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/parskip/

%files -n texlive-pdfpages
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pdfpages/

%files -n texlive-pdfpages-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pdfpages/

%files -n texlive-powerdot
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/powerdot/

%files -n texlive-powerdot-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/powerdot/

%files -n texlive-pb-diagram
%{_texdir}/texmf-dist/tex/latex/pb-diagram/

%files -n texlive-pb-diagram-doc
%{_texdir}/texmf-dist/doc/latex/pb-diagram/

%files -n texlive-pgf-blur
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pgf-blur/

%files -n texlive-pgf-blur-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pgf-blur/

%files -n texlive-pgf-soroban
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pgf-soroban/

%files -n texlive-pgf-soroban-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pgf-soroban/

%files -n texlive-pgf-umlcd
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/pgf-umlcd/

%files -n texlive-pgf-umlcd-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/pgf-umlcd/

%files -n texlive-pgf-umlsd
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/pgf-umlsd/

%files -n texlive-pgf-umlsd-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/pgf-umlsd/

%files -n texlive-pgfgantt
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pgfgantt/

%files -n texlive-pgfgantt-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pgfgantt/

%files -n texlive-pgfkeyx
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pgfkeyx/

%files -n texlive-pgfkeyx-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pgfkeyx/

%files -n texlive-pgfmolbio
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/pgfmolbio/
%{_texdir}/texmf-dist/tex/lualatex/pgfmolbio/

%files -n texlive-pgfmolbio-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/pgfmolbio/

%files -n texlive-pgfopts
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pgfopts/

%files -n texlive-pgfopts-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pgfopts/

%files -n texlive-pgfplots
%license gpl3.txt
%{_texdir}/texmf-dist/scripts/pgfplots/
%{_texdir}/texmf-dist/tex/context/third/pgfplots/
%{_texdir}/texmf-dist/tex/generic/pgfplots/
%{_texdir}/texmf-dist/tex/latex/pgfplots/
%{_texdir}/texmf-dist/tex/plain/pgfplots/

%files -n texlive-pgfplots-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/context/third/pgfplots/
%{_texdir}/texmf-dist/doc/generic/pgfplots/
%{_texdir}/texmf-dist/doc/latex/pgfplots/
%{_texdir}/texmf-dist/doc/plain/pgfplots/

%files -n texlive-picinpar
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/picinpar/

%files -n texlive-picinpar-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/picinpar/

%files -n texlive-pict2e
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pict2e/

%files -n texlive-pict2e-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pict2e/

%files -n texlive-pictex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pictex/

%files -n texlive-pictex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pictex/

%files -n texlive-pictex2
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pictex2/

%files -n texlive-pinlabel
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pinlabel/

%files -n texlive-pinlabel-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pinlabel/

%files -n texlive-pmgraph
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/pmgraph/

%files -n texlive-pmgraph-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/pmgraph/

%files -n texlive-paralist
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/paralist/

%files -n texlive-paralist-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/paralist/

%files -n texlive-placeins
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/placeins/

%files -n texlive-placeins-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/placeins/

%files -n texlive-pagecolor
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pagecolor/

%files -n texlive-pagecolor-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pagecolor/

%files -n texlive-pagecont
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pagecont/

%files -n texlive-pagecont-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pagecont/

%files -n texlive-pagenote
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pagenote/

%files -n texlive-pagenote-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pagenote/

%files -n texlive-pagerange
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pagerange/

%files -n texlive-pagerange-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pagerange/

%files -n texlive-pageslts
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pageslts/

%files -n texlive-pageslts-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pageslts/

%files -n texlive-paper
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/paper/

%files -n texlive-paper-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/paper/

%files -n texlive-papercdcase
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/papercdcase/

%files -n texlive-papercdcase-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/papercdcase/

%files -n texlive-papermas
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/papermas/

%files -n texlive-papermas-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/papermas/

%files -n texlive-papertex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/papertex/

%files -n texlive-papertex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/papertex/

%files -n texlive-paracol
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/paracol/

%files -n texlive-paracol-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/paracol/

%files -n texlive-paresse
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/paresse/

%files -n texlive-paresse-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/paresse/

%files -n texlive-parnotes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/parnotes/

%files -n texlive-parnotes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/parnotes/

%files -n texlive-parselines
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/parselines/

%files -n texlive-parselines-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/parselines/

%files -n texlive-pas-cours
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pas-cours/

%files -n texlive-pas-cours-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pas-cours/

%files -n texlive-pas-cv
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pas-cv/

%files -n texlive-pas-cv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pas-cv/

%files -n texlive-pas-tableur
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pas-tableur/

%files -n texlive-pas-tableur-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pas-tableur/

%files -n texlive-patchcmd
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/patchcmd/

%files -n texlive-patchcmd-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/patchcmd/

%files -n texlive-pauldoc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pauldoc/

%files -n texlive-pauldoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pauldoc/

%files -n texlive-pawpict
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/pawpict/

%files -n texlive-pawpict-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/pawpict/

%files -n texlive-pbox
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/pbox/

%files -n texlive-pbox-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/pbox/

%files -n texlive-pbsheet
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pbsheet/

%files -n texlive-pbsheet-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pbsheet/

%files -n texlive-pdf14
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pdf14/

%files -n texlive-pdf14-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pdf14/

%files -n texlive-pdfcomment
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pdfcomment/

%files -n texlive-pdfcomment-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pdfcomment/

%files -n texlive-pdfcprot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pdfcprot/

%files -n texlive-pdfcprot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pdfcprot/

%files -n texlive-pdfmarginpar
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/pdfmarginpar/

%files -n texlive-pdfmarginpar-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/pdfmarginpar/

%files -n texlive-pdfpagediff
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pdfpagediff/

%files -n texlive-pdfpagediff-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pdfpagediff/

%files -n texlive-pdfscreen
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pdfscreen/

%files -n texlive-pdfscreen-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pdfscreen/

%files -n texlive-pdfslide
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pdfslide/

%files -n texlive-pdfslide-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pdfslide/

%files -n texlive-pdfsync
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pdfsync/

%files -n texlive-pdfsync-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pdfsync/

%files -n texlive-pdfwin
%{_texdir}/texmf-dist/tex/latex/pdfwin/

%files -n texlive-pdfwin-doc
%{_texdir}/texmf-dist/doc/latex/pdfwin/

%files -n texlive-pdfx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pdfx/

%files -n texlive-pdfx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pdfx/

%files -n texlive-pecha
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/pecha/

%files -n texlive-pecha-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/pecha/

%files -n texlive-permute
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/permute/

%files -n texlive-permute-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/permute/

%files -n texlive-petiteannonce
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/petiteannonce/

%files -n texlive-petiteannonce-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/petiteannonce/

%files -n texlive-philex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/philex/

%files -n texlive-philex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/philex/

%files -n texlive-photo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/photo/

%files -n texlive-photo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/photo/

%files -n texlive-piff
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/piff/

%files -n texlive-piff-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/piff/

%files -n texlive-pkgloader
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pkgloader/

%files -n texlive-pkgloader-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pkgloader/

%files -n texlive-plantslabels
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/plantslabels/

%files -n texlive-plantslabels-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/plantslabels/

%files -n texlive-plates
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/plates/

%files -n texlive-plates-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/plates/

%files -n texlive-plweb
%{_texdir}/texmf-dist/tex/latex/plweb/

%files -n texlive-plweb-doc
%{_texdir}/texmf-dist/doc/latex/plweb/

%files -n texlive-polynom
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/polynom/

%files -n texlive-polynom-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/polynom/

%files -n texlive-polynomial
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/polynomial/

%files -n texlive-polynomial-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/polynomial/

%files -n texlive-polytable
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/polytable/

%files -n texlive-polytable-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/polytable/

%files -n texlive-postcards
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/postcards/

%files -n texlive-postcards-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/postcards/

%files -n texlive-poster-mac
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/poster-mac/

%files -n texlive-poster-mac-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/poster-mac/

%files -n texlive-ppr-prv
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ppr-prv/

%files -n texlive-ppr-prv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ppr-prv/

%files -n texlive-placeat
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/placeat/
%{_texdir}/texmf-dist/tex/lualatex/placeat/

%files -n texlive-placeat-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/placeat/

%files -n texlive-perfectcut
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/perfectcut/

%files -n texlive-perfectcut-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/perfectcut/

%files -n texlive-piechartmp
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/piechartmp/

%files -n texlive-piechartmp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/piechartmp/

%files -n texlive-piano
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/piano/

%files -n texlive-piano-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/piano/

%files -n texlive-pitex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/pitex/

%files -n texlive-pitex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/pitex/

%files -n texlive-placeins-plain
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/placeins-plain/

%files -n texlive-plipsum
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/plipsum/

%files -n texlive-plipsum-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/plipsum/

%files -n texlive-plnfss
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/plnfss/

%files -n texlive-plnfss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/plnfss/

%files -n texlive-plstmary
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/plstmary/

%files -n texlive-plstmary-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/plain/plstmary/

%files -n texlive-pdftricks
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/pdftricks/

%files -n texlive-pdftricks-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/pdftricks/

%files -n texlive-pdftricks2
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/pdftricks2/

%files -n texlive-pdftricks2-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/pdftricks2/

%files -n texlive-philosophersimprint
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/philosophersimprint/

%files -n texlive-philosophersimprint-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/philosophersimprint/

%files -n texlive-pittetd
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pittetd/

%files -n texlive-pittetd-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pittetd/

%files -n texlive-pkuthss
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/pkuthss/

%files -n texlive-pkuthss-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/pkuthss/

%files -n texlive-powerdot-FUBerlin
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/powerdot-FUBerlin/

%files -n texlive-powerdot-FUBerlin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/powerdot-FUBerlin/

%files -n texlive-physics
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/physics/

%files -n texlive-physics-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/physics/

%files -n texlive-philokalia
%{_datadir}/fonts/philokalia
%{_texdir}/texmf-dist/fonts/opentype/public/philokalia/
%{_texdir}/texmf-dist/tex/xelatex/philokalia/

%files -n texlive-philokalia-doc
%{_texdir}/texmf-dist/doc/xelatex/philokalia/

%files -n texlive-polyglossia
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/polyglossia/
%{_texdir}/texmf-dist/tex/latex/polyglossia/

%files -n texlive-polyglossia-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/polyglossia/

%files -n texlive-parades-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/parades/

%files -n texlive-parades
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/parades/

%files -n texlive-pbibtex-base-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/ptex/pbibtex/

%files -n texlive-pbibtex-base
%license bsd.txt
%{_texdir}/texmf-dist/pbibtex/

%files -n texlive-pgfornament-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pgfornament/

%files -n texlive-pgfornament
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/pgfornament/
%{_texdir}/texmf-dist/tex/latex/pgfornament/

%files -n texlive-pgf-spectra-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pgf-spectra/

%files -n texlive-pgf-spectra
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pgf-spectra/

%files -n texlive-platex-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/platex/

%files -n texlive-platex
%license bsd.txt
%{_texdir}/texmf-dist/tex/platex/
%{_mandir}/man1/platex.*
%exclude %{_mandir}/man1/*.pdf.gz

%files -n texlive-padauk
%license ofl.txt
%doc %{_texdir}/texmf-dist/doc/fonts/padauk/
%{_texdir}/texmf-dist/fonts/truetype/public/padauk/

%files -n texlive-pdfreview
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/latex/pdfreview/
%{_texdir}/texmf-dist/tex/latex/pdfreview/

%files -n texlive-phffullpagefigure
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/phffullpagefigure/
%{_texdir}/texmf-dist/tex/latex/phffullpagefigure/

%files -n texlive-phfnote
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/phfnote/
%{_texdir}/texmf-dist/bibtex/bst/phfnote/
%{_texdir}/texmf-dist/tex/latex/phfnote/

%files -n texlive-phfparen
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/phfparen/
%{_texdir}/texmf-dist/tex/latex/phfparen/

%files -n texlive-phfqit
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/phfqit/
%{_texdir}/texmf-dist/tex/latex/phfqit/

%files -n texlive-phfquotetext
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/phfquotetext/
%{_texdir}/texmf-dist/tex/latex/phfquotetext/

%files -n texlive-phfsvnwatermark
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/phfsvnwatermark/
%{_texdir}/texmf-dist/tex/latex/phfsvnwatermark/

%files -n texlive-phfthm
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/phfthm/
%{_texdir}/texmf-dist/tex/latex/phfthm/

%files -n texlive-phonenumbers
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/phonenumbers/
%{_texdir}/texmf-dist/tex/latex/phonenumbers/

%files -n texlive-platexcheat-doc
%doc %{_texdir}/texmf-dist/doc/latex/platexcheat/

%files -n texlive-platex-tools
%license bsd.txt
%doc %{_texdir}/texmf-dist/doc/latex/platex-tools/
%{_texdir}/texmf-dist/tex/latex/platex-tools/

%files -n texlive-poetry
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/poetry/
%{_texdir}/texmf-dist/tex/latex/poetry/

%files -n texlive-padcount
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/padcount/
%doc %{_texdir}/texmf-dist/doc/latex/padcount/

%files -n texlive-pdfoverlay
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/pdfoverlay/
%doc %{_texdir}/texmf-dist/doc/latex/pdfoverlay/

%files -n texlive-pdfpc-movie
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/pdfpc-movie/
%doc %{_texdir}/texmf-dist/doc/latex/pdfpc-movie/

%files -n texlive-pdfprivacy
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/pdfprivacy/
%doc %{_texdir}/texmf-dist/doc/latex/pdfprivacy/

%files -n texlive-penrose
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/penrose/
%doc %{_texdir}/texmf-dist/doc/latex/penrose/

%files -n texlive-pgfornament-han
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/pgfornament-han/
%doc %{_texdir}/texmf-dist/doc/latex/pgfornament-han/

%files -n texlive-pixelart
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/pixelart/
%doc %{_texdir}/texmf-dist/doc/latex/pixelart/

%files -n texlive-plantuml
%license lppl.txt
%{_texdir}/texmf-dist/tex/lualatex/plantuml/
%doc %{_texdir}/texmf-dist/doc/lualatex/plantuml/

%files -n texlive-plex
%license ofl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/plex/
%{_texdir}/texmf-dist/fonts/map/dvips/plex/
%{_texdir}/texmf-dist/fonts/opentype/ibm/plex/
%{_texdir}/texmf-dist/fonts/tfm/ibm/plex/
%{_texdir}/texmf-dist/fonts/type1/ibm/plex/
%{_texdir}/texmf-dist/fonts/vf/ibm/plex/
%{_texdir}/texmf-dist/tex/latex/plex/
%doc %{_texdir}/texmf-dist/doc/fonts/plex/

%files -n texlive-plex-otf
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/plex-otf/
%doc %{_texdir}/texmf-dist/doc/fonts/plex-otf/

%files -n texlive-pm-isomath
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/pm-isomath/
%doc %{_texdir}/texmf-dist/doc/latex/pm-isomath/

%files -n texlive-polexpr
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/polexpr/
%doc %{_texdir}/texmf-dist/doc/latex/polexpr/

%files -n texlive-postage
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/postage/
%doc %{_texdir}/texmf-dist/doc/latex/postage/

%files -n texlive-powerdot-tuliplab
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/powerdot-tuliplab/
%doc %{_texdir}/texmf-dist/doc/latex/powerdot-tuliplab/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
