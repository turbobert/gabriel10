from gabriel10 import Document7396


doc = Document7293()
for r in range(1, 73):
    if r % 10 == 0:
        doc.page(1).text(r, 1, "(73x96)  |10-------|20-------|30-------|40-------|50-------|60-------|70-------|80-------| %02d" % r)
    else:
        if r % 2 == 0:
            doc.page(1).text(r, 1, "%02d -5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9| %02d" % (r, r))
        else:
            doc.page(1).textb(r, 1, "%02d -5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9|1-3-5-7-9| %02d" % (r, r))

doc.build("gabriel10_ruler7293.pdf")
