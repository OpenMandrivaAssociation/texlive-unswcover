Name:		texlive-unswcover
Version:	66115
Release:	1
Summary:	Typeset a dissertation cover page following UNSW guidelines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unswcover
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unswcover.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unswcover.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package an UNSW cover sheet following the 2011 GRS
guidelines. It may also (optionally) provide other required
sheets such as Originality, Copyright and Authenticity
statements.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/unswcover/unswcover.sty
%doc %{_texmfdistdir}/doc/latex/unswcover/COPYING
%doc %{_texmfdistdir}/doc/latex/unswcover/Makefile
%doc %{_texmfdistdir}/doc/latex/unswcover/README
%doc %{_texmfdistdir}/doc/latex/unswcover/logo_unsw_short.pdf
%doc %{_texmfdistdir}/doc/latex/unswcover/thesis.bib
%doc %{_texmfdistdir}/doc/latex/unswcover/thesis.pdf
%doc %{_texmfdistdir}/doc/latex/unswcover/thesis.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
