import re
#import repeating-in-python
#mylist = [
#    '0045662100456621004566210045662100456621',
#    '0072992700729927007299270072992700729927',
#    '001443001443001443001443001443001443001443',
#    '037037037037037037037037037037037037037037037',
#    '047619047619047619047619047619047619047619',
#    '002457002457002457002457002457002457002457',
#    '001221001221001221001221001221001221001221',
#    '001230012300123001230012300123001230012300123',
#    '0013947001394700139470013947001394700139470013947',
#    '001001001001001001001001001001001001001001001001001',
#    '001406469760900140646976090014064697609',
#    '00469483568075117370892018779342723',
#    '001508295625942684766214177978883861236802413273',
#    '007518796992481203',
#    '0071942446043165467625899280575539568345323741',
#    '0434782608695652173913',
#    '0344827586206896551724137931',
#    '002481389578163771712158808933',
#    '002932551319648093841642228739',
#    '0035587188612099644128113879',
#    '003484320557491289198606271777',
#    '00115074798619102416570771',
#]

li = ["Ravin", "Devops", "Devops","Test","india"]
with open("data", 'w'): pass
for x in set(li):
    li.remove(x)
    out = list(set(li))
    print "Total count", out
    #if out:
    #    newf = open("data", "a+")
    #    newf.write("Repeasted\n")
    #    newf.close()

#count = len(open("data").readlines(  ))
#print "Total count", count
