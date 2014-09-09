pdf:
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex
	pdflatex main.tex
clean:
	(rm -rf *.ps *.log *.dvi *.aux *.*% *.lof *.lop *.lot *.toc *.idx *.ilg *.ind *.bbl *.blg *.cpt *.out)
