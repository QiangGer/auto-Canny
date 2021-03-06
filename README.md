**前言**：本项目写于2019年hdu暑期数学建模集训期间。

## 边缘提取

Canny算子具有比较优越的边缘提取效果，在matlab中体现的尤为淋漓尽致。但是在openCV中，canny方法需要传入上下阈值作为边缘提取标准，人为确定的阈值（经验阈值[100,200]）往往不具备普遍性，也难以达到较好的效果，本项目设计了一种自适应获取阈值的方法，并给出了定量评价边缘提取质量的标准。

## 自适应阈值

考虑到边缘提取就是一个图像二值化的过程，而可以证明[^1]大津阈值（otsu算法）在图像二值化的过程中能起到最优的效果。由大津阈值得出的二值化图形，边缘其实已经被分割的非常好，事实上只要将边缘描出，不要把边缘内部也染上黑色，就可以得到一个由二值图转化来的边缘切割图，本项目的想法也是基于此。

Canny方法的最后一步就是双阈值确定边界，双阈值确定边界就可以将边缘细化，因此将大津阈值作为canny算法的阈值是一个很好的选择。

但考虑到大津阈值有一个缺陷，就是如果图像的直方图没有明显的双峰，效果可能不好。因此我们又引入了一个基于迭代的自适应阈值算法[^2]。（~~其实只是为了数模而这样做~~）

当然这样讲也没有说服力，因此我们还引入了一个评价标准[^3]来评价边缘切割的好坏。

评价函数那一块因为某些原因（在注释里已标明），需要使用matlab来完成。

## 后记

这个自适应的方法是没有经过严格的数学推倒的，完全形成于数模集训期间，但是实际使用起来，效果还是很不错的。

另外本项目基于openCV，关于openCV的环境搭建，会另开一文讲述。



[^1]: [Evaluation of binarization methods for document images](https://ieeexplore.ieee.org/author/37607744600)

[^2]: 《改进的Canny算子边缘检测算法研究》 段军 张博

[^3]: 《一种新的基于连通成分的边缘评价方法》林卉 原文在evaluate文件中
