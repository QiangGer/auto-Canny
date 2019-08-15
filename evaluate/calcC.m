function [ cnt ] = calcC( image )
[temp,p] = bwlabel(image,8);
cnt = 0;
for i=2:length(temp)-1
    for j=2:length(temp(1,:))-1
        if temp(i,j) ~= 0
            if temp(i,j) == temp(i-1,j-1) == temp(i-1,j) == temp(i-1,j+1) ==temp(i,j-1)== temp(i,j+1) == temp(i+1,j-1) == temp(i+1,j) ==temp(i+1,j+1)
                cnt = cnt+1;
            end
        end
    end
end


end



