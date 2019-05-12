no = round(rand()*50);
guessed = %f;
for i=1:10
if(guessed == %f) then
k=input("Enter your guess : ")
end
Ans(i)=k;
if guessed == %f then
if k==no then
disp("correct Guess !!!");
guessed=%t;
elseif k-no<=-10 then

disp("Very low");
elseif k-no>10 then
disp("Very High");
elseif k-no<0 then
disp("Low");
else
disp("High");
end
end
end
k=1:10
disp("The Number Generated : ")
disp(no);
disp("Your Guesses");
disp(Ans);
clf;
plot(k,Ans);
xgrid();
