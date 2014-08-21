pdf:
	pdflatex humaninertia.tex
	bibtex humaninertia.aux
	pdflatex humaninertia.tex
	pdflatex humaninertia.tex
clean:
	(rm -rf *.ps *.log *.dvi *.aux *.*% *.lof *.lop *.lot *.toc *.idx *.ilg *.ind *.bbl *blg)
