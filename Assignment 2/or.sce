x=[1 0 0 ; 1 0 1 ; 1 1 0 ; 1 1 1];
disp("bias x1 x2");
disp(x);
yd=[0 ; 1 ; 1 ; 1];
disp("yd");
disp(yd);
w=rand(1,3);
w1=w;
disp("W1 W2 W3");
disp(w);
thresh=0;
ya=[0;0;0;0];
lr=0.1;
disp("LEARNING COEFFICIENT =");
disp(lr);
tries=0;
n=0;
net=0.0;
err=0;
while n==0
    for i=1:4
        for j=1:3
            net=net+(w(1,j)*x(i,j));
        end
        if net>=thresh then
            ya(1,j)=1;
        else 
            ya(1,j)=0;
        end
        err=yd(i,1)-ya(i,1);
            for j=1:3
                w(1,j)=w(1,j)+ (lr*x(i,j)*err);
            end
            net=0.00;
    end
    disp(ya,"Actual Output");
    disp(yd,"Desired Output");
    tries=tries+1;
    disp("End of epoch No:");
    disp(tries);
    disp("************************************************************ ");
    if tries > 20 then
        disp("LEARNING ATTEMPT FAILED")
        break;
    end;
    if yd(1,1) == ya(1,1)& yd(2,1) == ya(2,1) & yd(3,1) == ya(3,1) & yd(4,1) == ya(4,1) then
        n=1;
    else
        n=0;
    end
    figure;
    //plot(yd,ya);
end
disp("Initial Random Weights- ");
disp(w1);
disp("Funal Random Weights- ");
disp(w);
disp(lr,"Learning rate is - ");
figure;
plot(yd,ya);
