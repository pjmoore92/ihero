(TeX-add-style-hook "latex-template"
 (lambda ()
    (LaTeX-add-bibliographies
     "sig-proc")
    (TeX-add-symbols
     '("todo" 1)
     "newblock")
    (TeX-run-style-hooks
     "ifthen"
     "booktabs"
     "multirow"
     "colortbl"
     "epstopdf"
     "epsfig"
     "graphicx"
     "graphics"
     "color"
     "url"
     "latex2e"
     "sig-alt-release210"
     "sig-alt-release2")))

