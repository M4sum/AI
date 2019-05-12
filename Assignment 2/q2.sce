function k=Map_Matrix(A)

k=zeros(A);
N=unique(A);
disp("The Total Unique are : ")
disp(length(N))
for i =1:1:length(N)
indexes = find(A==N(i));
for j = 1:1:length(indexes)
k(indexes(j))=i;
end
end
endfunction
A=imread('D:\example.png');
//disp("The image contents of the image are as follows : ")
disp(A)
Ans=Map_Matrix(A);
//disp("The Equivalent content of the image are as follows : ")
disp(Ans);
figure(1);
imshow(int8(Ans));
figure(2)
imshow(A)
