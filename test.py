import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

raw_data = np.loadtxt('data.txt')
data = np.zeros((10,np.shape(raw_data)[0]))
data[0]=raw_data[:,0]#Gender
data[1]=raw_data[:,1]#Generation
data[2]=raw_data[:,2]#Race
data[3]=(raw_data[:,3]+raw_data[:,4]+raw_data[:,5]+raw_data[:,6])/4#Indiv Att
data[4]=(raw_data[:,7]+raw_data[:,8]+raw_data[:,9])/3#Subjec Norm
data[5]=(raw_data[:,10]+raw_data[:,11]+raw_data[:,12]+raw_data[:,13])/4#Perc Val
data[6]=(raw_data[:,14]+raw_data[:,15]+raw_data[:,16])/3#Perc Eff
data[7]=(raw_data[:,17]+raw_data[:,18]+raw_data[:,19])/3#Perc Behav
data[8]=(raw_data[:,20]+raw_data[:,21]+raw_data[:,22])/3#Behav Intent
data[9]=(raw_data[:,25]+raw_data[:,24]+raw_data[:,23])/3#Behav
data_labels=['Gender','Generation','Race','Individual Attitude','Subjective Norm','Percieved Value','Percieved Effectiveness','Percieved Behavioural Control','Behavioural Intention','Behaviour']
data_colours=['black','black','black','red','darkorange','deepskyblue','darkgreen','indigo','black','black']
data = np.transpose(data);N=len(data);N_column=np.shape(data)[1]
w_indx=[];nw_indx=[]
for i in range(N):
    if data[i][2]==1:
        w_indx.append(i)
    else:
        nw_indx.append(i)
N_w=len(w_indx);N_nw=len(nw_indx);white=np.zeros((N_w,N_column));not_white=np.zeros((N_nw,N_column))
for i in range(N_w):
    white[i]=data[w_indx[i]]
for i in range(N_nw):
    not_white[i]=data[nw_indx[i]]
##Behav intent (8) against Behav(9)
#White
result=stats.linregress(white[8,:],white[9,:])
print(result.intercept,result.intercept_stderr)
x=np.array([1,2,3,4,5])
y=result.slope*x+result.intercept
plt.plot(x,y,label='White')
#Not White
result=stats.linregress(not_white[8,:],not_white[9,:])
print(result.intercept,result.intercept_stderr)
x=np.array([1,2,3,4,5])
y=result.slope*x+result.intercept
plt.plot(x,y,label='Not White')
plt.title('White vs Not White')
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('BehavIntent');plt.ylabel('Behav');plt.legend();plt.show()

##Allvs Intent
#White
for i in range(3,8):
    slope,intercept,r_value,p_value,std_err=stats.linregress(white[i,:],white[8,:])
    x=np.array([1,2,3,4,5])
    y=slope*x+intercept
    plt.plot(x,y,label=data_labels[i],color=data_colours[i])
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Factors effecting BI');plt.ylabel('BI');plt.title('White');plt.legend();plt.show()
#Not White
for i in range(3,8):
    slope,intercept,r_value,p_value,std_err=stats.linregress(not_white[i,:],not_white[8,:])
    x=np.array([1,2,3,4,5])
    y=slope*x+intercept
    plt.plot(x,y,label=data_labels[i],color=data_colours[i])
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Factors effecting BI');plt.ylabel('BI');plt.title('Not White');plt.legend();plt.show()
#All
for i in range(3,9):
    slope,intercept,r_value,p_value,std_err=stats.linregress(data[i,:],data[0,:])
    x=np.array([1,2,3,4,5])
    y=slope*x+intercept
    plt.plot(x,y,label=data_labels[i],color=data_colours[i])

plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Factors effecting BI');plt.ylabel('BI');plt.title('All');plt.legend();plt.show()





