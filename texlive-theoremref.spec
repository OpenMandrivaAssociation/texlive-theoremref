Name:		texlive-theoremref
Version:	20180303
Release:	1
Summary:	References with automatic theorem names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/theoremref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theoremref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theoremref.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The theoremref package provides variants of the \label and \ref
commands for theorem-like environments, capable of
automatically typesetting references including the theorem name
(apart from the theorem number). The scheme is particularly
valuable if the author decides to change a lemma to a
proposition or a theorem (or whatever).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/theoremref
%doc %{_texmfdistdir}/doc/latex/theoremref

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
