clear;
clc;
// The Normal Function
function y=Rosenbrock(x)
    y=(100*(x(2)-x(1)^2)^2)+((1-x(1))^2);
//    g(1) = - 400*(x(2)-x(1)^2)*x(1) - 2*(1-x(1));
//    g(2) = 200*(x(2)-x(1)^2) ;
//    h(1,1) = 1200*x(1)^2 - 400*x(2) + 2;
//    h(1,2) = -400*x(1) ;
//    h(2,1) = -400*x(1);
//    h(2,2) = 200;   
endfunction
//Wrapper Function just to set as per normal function
function Ans=Rosplot(a,b)
    Ans=Rosenbrock([a b]);
endfunction

//Exercise 1 - Graph Plotting
a=-2:0.1:2;
b=-2:0.1:2;
k=feval(a,b,Rosplot);
surf(k');


//Exercise 2 - Value at [-1.2,1]
p=[-1.2,1];
Ans = Rosenbrock([-1.2,1]);
disp(Ans,"value of f,g,h at [-1.2,1] : ");
Ans = Rosenbrock([1,1]);
disp(Ans,"value of f,g,h at [1,1] : ");

//Exercise 3
[J, H]=numderivative(Rosenbrock,p);
disp(J,"Num-Derivative of G at [-1.2,1] :");
disp(H,"Num-Derivative of H at [-1.2,1] :");

