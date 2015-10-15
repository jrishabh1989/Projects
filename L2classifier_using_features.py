# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:17:30 2015

@author: Rishabh
"""



import numpy as np
from PIL import Image

import os  
from sklearn import svm
from sklearn.externals import joblib



def main():
    count=0;
    testDir="mctestData"
    trainDir="mctrainData"
    extra_features=1
    trainSize= len([name for name in os.listdir(trainDir) if name.endswith(".JPEG")])
    testSize=len([name for name in os.listdir(testDir) if name.endswith(".JPEG")])    
    bigList=np.zeros((trainSize,3*300*300+extra_features))
    bigListTest=np.zeros((testSize,3*300*300+extra_features))  
    y_train=np.zeros(trainSize)
    y_test=np.zeros(testSize)
    #../downloads/sky/no_sky/
    print "going for second for"
    for fn in os.listdir(testDir):
        if os.path.isfile(testDir+"/"+fn):
            print (fn)
            if(fn.endswith(".JPEG")):
                im=Image.open(testDir+"/"+fn);

                pix=im.load();
                #print im.size

                k=0;
                for i in range(0,300):
                    for j in range(0,300):
                        col=3*k
                        #print (pix[i,j])
                        #print (pix[i,j][0])
                        #print i,j
                        #print count,col
                        bigListTest[count,col]=(pix[i,j][0])
                        bigListTest[count,col+1]=(pix[i,j][1])
                        bigListTest[count,col+2]=(pix[i,j][2])
                        k=k+1;
                add=4
                col=(3*k)-3    
                #bigListTest[count,col+3]=fn[add]
                """
                bigListTest[count,col+4]=fn[add+2]
                bigListTest[count,col+5]=fn[add+4]
                bigListTest[count,col+6]=fn[add+6]
                bigListTest[count,col+7]=fn[add+8]
                bigListTest[count,col+8]=fn[add+10]
                """                    
                y_test[count]=fn[4+2]
                #print y_test[count]
                count=count+1
    print "testList Size:",(bigListTest.shape)
    test_file=np.asarray(bigListTest);
    #np.savetxt("ShoreTest_File.txt",test_file,delimiter=",",fmt='%s'); 	

    count=0;
    print "going for for"    
    for fn in os.listdir(trainDir):
        #print "in for"
	if os.path.isfile(trainDir+"/"+fn):
            print (trainDir+"/"+fn)
            if(fn.endswith(".JPEG")):
                filename=trainDir+"/"+fn
                im=Image.open(filename);
                
                pix=im.load();
                #print im.size
                
                k=0;
                for i in range(0,300):
                    for j in range(0,300):
                        col=3*k
                        bigList[count,col]=(pix[i,j][0])
                        bigList[count,col+1]=(pix[i,j][1])
                        bigList[count,col+2]=(pix[i,j][2])
                        k=k+1;
                #print fn[4]
                add=4        
                col=(3*k)-3
                #print bigList[count,col+3]
                #print fn[add]
                #bigList[count,col+3]=fn[add]
                """                
                bigList[count,col+4]=fn[add+2]
                bigList[count,col+5]=fn[add+4]
                bigList[count,col+6]=fn[add+6]
                bigList[count,col+7]=fn[add+8]
                bigList[count,col+8]=fn[add+10]        
                """                
                #print fn[4]
                y_train[count]=fn[add+2]        
                #print y_train[count]                
                count=count+1
    
    print "saving"
    train_file=np.asarray(bigList);
    #np.savetxt("ShoreTrain_File.txt",train_file,delimiter=",",fmt='%s');

    """
    print "going for second for"
    count=0
    for fn in os.listdir(testDir):
        if os.path.isfile(testDir+"/"+fn):
            #print (fn)
            if(fn.endswith(".JPEG")):
                im=Image.open(testDir+"/"+fn);
                
                pix=im.load();
                #print im.size
                
                k=0;
                for i in range(0,300):
                    for j in range(0,300):
                        col=3*k
                        bigListTest[count,col]=(pix[i,j][0])
                        bigListTest[count,col+1]=(pix[i,j][1])
                        bigListTest[count,col+2]=(pix[i,j][2])
                        k=k+1;
                y_test[count]=fn[4]        
                #print y_test[count]
                count=count+1
    print "testList Size:",(bigListTest.shape)            
    """   
    ###################################
    """
    print "DIME REDN"
    #print lst
    #X = np.array(image_matrix)
    X=bigList
    print X
    pca = PCA(n_components=3)
    #print X
    #print(pca)
    pca.fit(X)
    PCA(copy=True, n_components=14, whiten=False)
    print(pca.explained_variance_ratio_) 
    print(pca.fit(X)) 
    print(pca.fit_transform(X))
    print 'x',X
    X_new=pca.fit_transform(X)
    #print 'inverse',pca.inverse_transform(X_new)
    """    
    ##############################
    print "SVM TRAIN"
    
    X_train=bigList
    X_test=bigListTest
    
    clf = svm.SVC()
    clf.fit(X_train, y_train) 
    joblib.dump(clf,'model_level2')

    dec = clf.predict(X_test)        
    print y_test
    print np.sign(dec)
    
 
	 
    y_out=np.zeros(len(dec))
    correct_count=0
    print len(dec),len(y_test)    
    for i in range(0,len(dec)):
        if(dec[i]>0):
            y_out[i]=1
        if(y_out[i]==y_test[i]):
            correct_count=correct_count+1
    
    print "accuracy:"
    print correct_count,len(dec),((correct_count*100)/len(dec))
    
    #print 'cluster';
    
    #print cluster;
    
    
    print "done";
if __name__=="__main__":
    main()
