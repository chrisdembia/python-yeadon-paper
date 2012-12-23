pdf:
	latex humaninertia.tex
	bibtex humaninertia.aux
	latex humaninertia.tex
	latex humaninertia.tex
	dvipdf humaninertia.dvi
