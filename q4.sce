clear; //clear all previous stored value
x=-20:20; // range of x
k=1./(1+exp(-x)); // computes the value of x for each element 

clf;
plot(x,k); // plot graph
xgrid(); // grid to check value
