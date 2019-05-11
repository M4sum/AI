clear;
no = round(rand()*50);  // Generation of the random number between 1 and 50
//no=23;
guessed = %f;           // Given a value false till the guess is correct
for i=1:10              // Loop to iterate through the no of guesses
    if(guessed == %f) then
        k=input("Enter your guess : ")  // taking guess
    end
    Ans(i)=k;                           // storing the input to for graph
    if guessed == %f then               // checking input in if elif ladder
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
k=1:10                  // for x-axis
disp("The Number Generated : ")
disp(no);           // Displaying the Randomly generated for self checking
disp("Your Guesses");
disp(Ans);          // Displaying guess
clf;
plot(k,Ans);        // plotting graph
xgrid();        // display grid
