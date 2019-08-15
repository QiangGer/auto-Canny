clear;
clc;
%��ȡ��Ƭ
peppers = imread('peppers.png');

%% ��matlab��װ��������������Ե���
%תΪuint8��������Ϊ��װ�������ص��Ƕ�ֵͼ
%��Ҫ�Ѷ�ֵͼ��1תΪ255����Ϊ�˺�openCV�ı�Ե��⺯������ֵ��Ӧ
Mcanny = edge(peppers,'canny');
Mcanny = uint8(Mcanny);
Mcanny(Mcanny == 1) = 255;

sobel = edge(peppers,'sobel');
sobel = uint8(sobel);
sobel(sobel == 1) = 255;

prewitt = edge(peppers,'prewitt');
prewitt = uint8(prewitt);
prewitt(prewitt == 1) = 255;

log = edge(peppers,'log');
log = uint8(log);
log(log == 1) = 255;
%% ����������Ե�����������
% �ο��������ǡ�һ���µĻ�����ͨ�ɷֵı�Ե���۷��� �ֻܡ�
% �������µ��������ܴ��ڴ���(��ͨ�ɷ������󷨣��Ҿ�����������)���һ����Լ������ʵ���������ᵽ�����۷���
% A��ͼ�бߵ����ظ���
% B��ͼ�е�����ͨ�ɷ���
% C��ͼ�еİ���ͨ�ɷ���
% C/A��C/B����ֵԽС -> ��Ե����Ч��Խ��
aOfMcanny = calcA(Mcanny);
aOfsobel = calcA(sobel);
aOfprewitt = calcA(prewitt);
aOflog = calcA(log);


bOfMcanny = calcB(Mcanny);
bOfsobel = calcB(sobel);
bOfprewitt = calcB(prewitt);
bOflog = calcB(log);


cOfMcanny = calcC(Mcanny);
cOfsobel = calcC(sobel);
cOfprewitt = calcC(prewitt);
cOflog = calcC(log);

