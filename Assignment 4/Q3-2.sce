clc;
clear;
rand('seed',0);
N=[4,4,3];
m=csvRead("1a.csv");
x=[m(1:35,1:4);m(51:85,1:4);m(101:135,1:4)]';
y=[m(36:50,1:4);m(86:100,1:4);m(136:150,1:4)]';
t=csvRead("2.csv");
s=[t(1:35,1:4);t(51:85,1:4);t(101:135,1:4)]
r=[t(36:50,1:4);t(86:100,1:4);t(136:150,1:4)]
lp=[0.25, 0];
W=ann_FF_init(N);
T=400;
train=ann_FF_Std_online(x,s,N,W,lp,T);
test=ann_FF_run(y,N,train)
//C:\Users\dishant.vict16\Desktop\1a.csv
//C:\Users\dishant.vict16\Desktop\2.csv
