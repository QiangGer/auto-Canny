%% ���Ǽ�������ͨ�ɷ����� 
% bwlabel��Ч���������ᵽ������㷨Ӧ����һ�µ�
% �ο���������https://blog.csdn.net/Dhane/article/details/81633723
function [ cnt ] = calcB( image )
temp = bwlabel(image,4);
cnt = 0;
for i=2:length(temp)-1
    for j=2:length(temp(1,:))-1
        if temp(i,j) ~= 0
            if temp(i,j) == temp(i-1,j) == temp(i+1,j) == temp(i,j-1) ==temp(i,j+1)
                cnt = cnt+1;
            end
        end
    end
end


end

