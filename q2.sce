function k=Map_Matrix(A)  // Map matrix function to generate mapping matrix
    k=zeros(A);     // create matrix of size A with zeros
    N=unique(A);  // finding Unique from A
    disp("The Total Unique are : ")  
    disp(length(N))  // display unique values
    for i =1:1:length(N)
        indexes = find(A==N(i));
        for j = 1:1:length(indexes)
            k(indexes(j))=i;    //  assign the value  to all the indices
        end    
    end
endfunction

A=imread('C:\Users\Kirtivadan\Desktop\sem 6 AI lab\Scilab assignment\lx.jpg'); // reading the image using absolute path to file
//disp("The image contents of the image are as follows : ")
//disp(A)
Ans=Map_Matrix(A); // calling Map Matrix function
//disp("The Equivalent content of the image are as follows : ")
//disp(Ans);
figure(1);
imshow(uint8(Ans)); // unsigned Int coversion of Mapping Matrix to display image
figure(2)
imshow(A); // Showing normal photo
