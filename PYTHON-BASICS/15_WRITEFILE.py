"""with open('RONALDO.txt','w') as f:
    f.write('ennavale adi ennavale')
    # THIS METHOD OVERWRITE THE FILE IF THE FILE ALREADY EXIST
    f.seek(0)
    f.write('my')
with open('AJUTXT.txt','r') as rf:
    with open('KRISHNA.txt','w') as wf: # IN WRITE MODE, IT WILL CREATE A FILE IF IT DOESN'T EXIST
        for i in rf: # TEXT COPY METHOD
            wf.write(i)

with open('123035.jpg','rb') as rf:
    with open('AJU_COPY.jpg','wb') as wf: # IN WRITE MODE, IT WILL CREATE A FILE IF IT DOESN'T EXIST
        for i in rf: # IMAGE COPY METHOD
            wf.write(i)"""
            
with open('123035.jpg','rb') as rf:
    with open('AJU_COPY2.jpg','wb') as wf: # IN WRITE MODE, IT WILL CREATE A FILE IF IT DOESN'T EXIST
        size = 3020
        g = rf.read(size)
        while len(g) > 0:
            wf.write(g)
            g = rf.read(3020)
