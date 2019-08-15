function [ cnt ] = calcA( image )
cnt = 0;
for i=1:length(image)
    for j=1:length(image(1,:))
        if image(i,j) == 255
            cnt = cnt+1;
        end
    end
end
end


