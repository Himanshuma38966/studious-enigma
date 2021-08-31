import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

Sp = ("Sp.csv")

mean = statistics.mean(Sp)
median = statistics.median(Sp)
mode = statistics.mode(Sp)
Sd =statistics.stdev(Sp) 
print("mean=",mean)
print("median=",median)
print("mode=",mode)
print("sd=",Sd)



sd1_start,sd1_end=mean-Sd,mean + Sd
sd2_start,sd2_end=mean-(2*Sd),mean + (2*Sd)
sd3_start,sd3_end=mean-(3*Sd),mean + (3*Sd)
sd1_ls=[result for result in Sp if result > sd1_start and result < sd1_end]
sd2_ls=[result for result in Sp if result > sd2_start and result < sd2_end]
sd3_ls=[result for result in Sp if result > sd3_start and result < sd3_end]

print((len(sd1_ls)*100)/len(Sp))
print((len(sd2_ls)*100)/len(Sp))
print((len(sd3_ls)*100)/len(Sp))

print("{}% of data lies within 1 standard deviation".format((len(sd1_ls)*100)/len(Sp)))

fig=ff.create_distplot([Sp],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1_start,sd1_start],y=[0,0.17],mode="lines",name=" standard deviation start 1"))
fig.add_trace(go.Scatter(x=[sd2_start,sd2_start],y=[0,0.17],mode="lines",name=" standard deviation start 2"))
fig.add_trace(go.Scatter(x=[sd1_end,sd1_end],y=[0,0.17],mode="lines",name=" standard deviation end 1"))
fig.add_trace(go.Scatter(x=[sd2_end,sd2_end],y=[0,0.17],mode="lines",name=" standard deviation end 2"))

fig.show()

