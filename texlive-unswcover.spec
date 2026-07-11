%global tl_name unswcover
%global tl_revision 66115

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typeset a dissertation cover page following UNSW guidelines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unswcover
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unswcover.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unswcover.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package an UNSW cover sheet following the 2011 GRS guidelines. It
may also (optionally) provide other required sheets such as Originality,
Copyright and Authenticity statements.

