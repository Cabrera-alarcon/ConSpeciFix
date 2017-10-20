from config import *
import os

species=getSelectedSpecies("geneSubsetHMVals.txt")

"""+PATH_TO_OUTPUT+sp+"""

for sp in species:
	print sp
	h=open('graphWithBox.R','w')
	h.write("""pdf('"""+PATH_TO_OUTPUT+sp+"""/gno2.pdf')
par(mfrow=c(1,1))
tab = read.table('"""+PATH_TO_OUTPUT+sp+"""/graph.txt',h=T)
secTab = read.table('"""+PATH_TO_OUTPUT+sp+"""/geneSubsetHMVals.txt',h=T)
w=c(tab$Nb,rev(tab$Nb))
v=c(tab$Median-tab$SD,rev(tab$Median + tab$SD))

overallMax <- max(v)
if(overallMax < max(secTab$hmRatio)){
	overallMax <- max(secTab$hmRatio)
}
overallMax + 0.1

par(fig=c(0,.85,0,1), new=TRUE)
plot(100,100,cex=0.5,cex.main=0.8,xlim=c(3,max(w)),ylim=c(0,overallMax),xlab=c("# Genomes"),ylab=c("h/m"),main='"""+sp+"""',plot=FALSE)
polygon(w,v,col="gray88",border=NA)
points(tab$Nb,tab$Median,pch=16,cex=0.3,t="b")
par(fig=c(0.65,1,0,1),new=TRUE)

boxplot(hmRatio~size, data=secTab,ylim=c(0,overallMax),axes=FALSE,xlab="end result with\nresampled core")

dev.off()""")
	h.truncate()
	h.close()
	os.system("Rscript graphWithBox.R  ")

#os.remove("kmean_graph.R")


