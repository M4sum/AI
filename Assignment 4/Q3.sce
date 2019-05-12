clc;
clear;
rand('seed',0);
f = csvRead('D:/Iris.csv');
model = [4,3,3];
training = [f(2:51,1:4);f(52:101,1:4);f(102:151,1:4)]';
testing = [f(37:51,1:4);f(87:101,1:4);f(137:151,1:4)]';
label = [
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1
0 0 1;
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0
0 1 0;
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0
1 0 0;
]';
lr = [0.1,0];
ws = ann_FF_init(model);
i = 200;
ws = ann_FF_Std_online(training,label,model,ws,lr,i);
result = ann_FF_run(testing,model,ws);
disp(result);
t=0;

f=0;
for i=1:1:15
m = max(result(1,i),result(2,i),result(3,i));
if(m>0.7 & result(3,i)>result(2,i) & result(1,i)<result(3,i))
t=t+1;
else
f=f+1;
end
end
for i=16:1:30
m = max(result(1,i),result(2,i),result(3,i));
disp(m);
if(m>0.7 & result(1,i)<result(2,i) & result(2,i)>result(3,i))
t=t+1;
else
f=f+1;
end
end
for i=31:1:45
m = max(result(1,i),result(2,i),result(3,i));
if(m<0.7 & result(1,i)>result(2,i) & result(1,i)>result(3,i))
t=t+1;
else
f=f+1;
end
end
disp('Total number of true classification are :');
disp(t);
disp(' out of 45');
disp('Accuracy of my model is: ' );
acc = t/45;
disp(acc*100);
