i=0
variable=''
variablefinal=''
simbolo='+'
todas_lasx=['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12']
todas_lasy=['y1','y2','y3','y4','y5','y6','y7','y8','y9','y10','y11','y12']
while(i<len(todas_lasx)):
    variable+=(f"(|x-{todas_lasx[i]}|)+(|y-{todas_lasy[i]}|)+")   
    i+=1
variablefinal=variable[:-1]
print(f"f(x)={variablefinal}")