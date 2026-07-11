%global tl_name theoremref
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	References with automatic theorem names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/theoremref
License:	lppl1.3 gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/theoremref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/theoremref.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The theoremref package provides variants of the \label and \ref commands
for theorem-like environments, capable of automatically typesetting
references including the theorem name (apart from the theorem number).
The scheme is particularly valuable if the author decides to change a
lemma to a proposition or a theorem (or whatever).

