//function to find the function from derivative and initial condition
function yprim=f(t,y)
    yprim(1)=y(2);
    yprim(2)=-2*y(1);
endfunction

t0=0;
tmax=10;
t=t0:0.1:tmax; // time vector
y0=3;  // initial given condition
yprim0=0; //initial given condition
y=ode([y0;yprim0],t0,t,f); 
clf;
subplot(311);       // original plot
plot(t,y(1,:))  
y=ode([1;1],t0,t,f);    // sub question 1
subplot(312);
plot(t,y(1,:))
y=ode([4;1],t0,t,f)     // sub-question 2
subplot(313)
plot(t,y(1,:))


