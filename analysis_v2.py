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
data[5]=(raw_data[:,17]+raw_data[:,18]+raw_data[:,19]+raw_data[:,14]+raw_data[:,15]+raw_data[:,16])/6#Perc Behav
data[6]=(raw_data[:,20]+raw_data[:, 21]+raw_data[:,22])/3#Behav Intent
data[7]=(raw_data[:,25]+raw_data[:,24]+raw_data[:,23])/3#Behav
data_labels=['Gender','Generation','Race','Individual Attitude','Subjective Norm','Percieved Behavioural Control','Behavioural Intention','Behaviour']
data_colours=['black','black','black','red','darkgreen','deepskyblue','black','black']
data_size = [10,10,10,20,45,30,10,10]
data_marker = ['o','o','o','o','+','x','o','o']
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


###All
#All Factors vs BI (raw)
for i in range(3,6):
    plt.scatter(data[:,i],data[:,6],label=data_labels[i],color=data_colours[i],s=data_size[i],marker=data_marker[i])
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Factors effecting BI');plt.ylabel('BI');plt.title('All (raw)');plt.legend();plt.show()

#ALL BI vs Behav (raw)
plt.scatter(data[:,6],data[:,7],marker='x')
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('BI');plt.ylabel('Behaviour');plt.title('All (raw)');plt.legend();plt.show()

#All FActors vs BI (trend)
for i in range(3,6):
    slope,intercept,r_value,p_value,std_err=stats.linregress(data[:,i],data[:,6])
    x=np.array([1,2,3,4,5])
    y=slope*x+intercept
    plt.plot(x,y,label=data_labels[i],color=data_colours[i])
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Factors effecting BI');plt.ylabel('BI');plt.title('All (trend line)');plt.legend();plt.show()

##Race

##Behav intent (6) against Behav(7)
#White
print(np.shape(white))
result=stats.linregress(white[:,6],white[:,7])
print(result.intercept,result.intercept_stderr)
x=np.array([1,2,3,4,5])
y=result.slope*x+result.intercept
plt.plot(x,y,label='White')
#Not White
result=stats.linregress(not_white[:,6],not_white[:,7])
print(result.intercept,result.intercept_stderr)
x=np.array([1,2,3,4,5])
y=result.slope*x+result.intercept
plt.plot(x,y,label='Not White')
plt.title('White vs Not White')
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Behavioural Intent');plt.ylabel('Behaviour');plt.legend();plt.show()

#White (Factors vs BI)
for i in range(3,6):
    slope,intercept,r_value,p_value,std_err=stats.linregress(white[:,i],white[:,6])
    x=np.array([1,2,3,4,5])
    y=slope*x+intercept
    plt.plot(x,y,label=data_labels[i],color=data_colours[i])
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Factors effecting BI');plt.ylabel('BI');plt.title('White');plt.legend();plt.show()
#Not White (Factors vs BI)
for i in range(3,6):
    slope,intercept,r_value,p_value,std_err=stats.linregress(not_white[:,i],not_white[:,6])
    x=np.array([1,2,3,4,5])
    y=slope*x+intercept
    plt.plot(x,y,label=data_labels[i],color=data_colours[i])
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Factors effecting BI');plt.ylabel('BI');plt.title('Not White');plt.legend();plt.show()
 
#Perc behav vs Behav
slope,intercept,r_value,p_value,std_err=stats.linregress(white[:,5],white[:,7])
x=np.array([1,2,3,4,5])
y=slope*x+intercept
plt.plot(x,y,label='White')
slope,intercept,r_value,p_value,std_err=stats.linregress(not_white[:,5],not_white[:,7])
x=np.array([1,2,3,4,5])
y=slope*x+intercept
plt.plot(x,y,label='Not White')
plt.xlim(1,5);plt.ylim(1,5);plt.xlabel('Percieved Behavioural Control');plt.ylabel('Behaviour');plt.legend();plt.show()
