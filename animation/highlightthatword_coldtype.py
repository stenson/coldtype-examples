from coldtype import *
from drafting.text.richtext import RichText

f1 = Font.Cacheable("~/Type/fonts/fonts/ObviouslyVariable.ttf")
tl = Timeline(30)

@animation((1000, 500), timeline=tl)
def highlight(f):
    e = f.a.progress(f.i, loops=1, easefn="eeio").e
    rt = (RichText(f.a.r,
        "HIGHLIGHT[h]\nTHAT WORD",
        {
            "default": Style(f1, 150,
                wght=0.25,
                wdth=0.15-e*0.15,
                fill=bw(0.2),
                slnt=e),
            "h": Style(f1, 150,
                ro=1,
                wdth=0.25,
                wght=e,
                slnt=1-e,
                fill=hsl(e, 0.8, 0.8),
                stroke=hsl(0.55, 0.7),
                strokeWidth=5)})
        .xa()
        .align(f.a.r))
    
    rt[-1].rotate(2)
    return rt