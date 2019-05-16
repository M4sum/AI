x =[1 0 0
1 0 1
1 1 0
1 1 1];

yd=[0;0;0;1]; 
ya=[0 0 0 0];
w=rand(1,3);
w1=w
disp(w);
lr=0.2;
flag=0;
n=0;
err=0;
e=0;
t=0;
while flag==0 do
    for i=1:4
        for j=1:3
            n=n+w(1,j)*x(i,j);
        end;
        if n >= t then
            ya(i,1)=1;
        else
            ya(i,1)=0;
        end;
        err=yd(i,1)-ya(i,1);
        for j=1:3
            w(1,j)=w(1,j)+ (lr*x(i,j)*err);
        end;
        n=0.00;
    end
    e=e+1;
    disp(e);
    if e > 7 then
        disp("failed")
        break;
    end;
    if yd(1,1) == ya(1,1)& yd(2,1) == ya(2,1) & yd(3,1) == ya(3,1) & yd(4,1) == ya(4,1) then
        flag=1;
    else
        flag=0;
    end
    figure;
    plot(yd,ya);

end

disp("Initial Random Weights -");

disp(w1);

disp("Final Adjusted Weights -");

disp(w);

disp(lr,"Learning rate is – ")

figure;

plot(yd,ya);
