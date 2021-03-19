import drafting.drawbot as dr
from drafting.text.richtext import RichText

f1 = dr.Font.Cacheable("~/Type/fonts/fonts/ObviouslyVariable.ttf")

r = dr.page_rect()

rt = (RichText(r,
        "HIGHLIGHT[high]\nTHAT WORD", {
        "default": dr.Style(f1, 200,
            wght=0.25,
            wdth=0.15,
            slnt=1,
            fill=dr.bw(0.2)),
        "high": dr.Style(f1, 250,
            ro=1,
            wdth=0.25,
            wght=1,
            tu=-50, # tracking-in-units
            fill=dr.hsl(0.9, 0.9, 0.8),
            stroke=dr.hsl(0.55, 0.9, 0.4),
            strokeWidth=5)})
    .xa() # center each line
    .align(r)
    .index(1, lambda p: p.rotate(2))
    .chain(dr.dbdraw))

#print(rt.tree()) # to see structure of RichText