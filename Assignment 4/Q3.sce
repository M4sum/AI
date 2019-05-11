clc;
clear;
//Setting neural NEtwork
rand('seed',0);
N=[4,16,3];
//reading CSV File
temp = csvRead("C:\Users\Kirtivadan\Desktop\sem 6 AI lab\Scilab assignment\Assignment 4\dataset.csv");
//Filtering the input
temp = temp(:,1:4);
//Filtering the Outputs
output = zeros(150,3);
output(1:50,1)=1;
output(51:100,2)=1;
output(101:150,3)=1;
output = output';
lp=[0.1,0]; // Seeting learning rate and Threshold
//Fixing input and output
x = [temp(1:35,:);temp(51:85,:);temp(101:135,:)]';
t = [output(:,1:35),output(:,51:85),output(:,101:135)];
test = [temp(36:50,:);temp(86:100,:);temp(136:150,:)]';
//Training Set of Weights
W=ann_FF_init(N);
T=400;
W=ann_FF_Std_online(x,t,N,W,lp,T);
a=ann_FF_run(test,N,W);
//Rounding to get the output in desired format
k = round(a);
desired = [output(:,36:50),output(:,86:100),output(:,136:150)]
//Error checking and determination of the Accuracy
Error = k - desired;
FOM = length(find(Error == -1));
disp('Accuracy : ');
disp(((45-FOM)/45)*100);
