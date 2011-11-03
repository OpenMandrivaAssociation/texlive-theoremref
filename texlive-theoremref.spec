# revision 20632
# category Package
# catalog-ctan /macros/latex/contrib/theoremref
# catalog-date 2010-12-01 16:02:54 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-theoremref
Version:	20101201
Release:	1
Summary:	References with automatic theorem names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/theoremref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theoremref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theoremref.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The theoremref package provides variants of the \label and \ref
commands for theorem-like environments, capable of
automatically typesetting references including the theorem name
(apart from the theorem number). The scheme is particularly
valuable if the author decides to change a lemma to a
proposition or a theorem (or whatever).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/theoremref/theoremref.sty
%doc %{_texmfdistdir}/doc/latex/theoremref/COPYING
%doc %{_texmfdistdir}/doc/latex/theoremref/README
%doc %{_texmfdistdir}/doc/latex/theoremref/theoremref-doc.pdf
%doc %{_texmfdistdir}/doc/latex/theoremref/theoremref-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
