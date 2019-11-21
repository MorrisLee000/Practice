#1.新增
##binary search tree的新增和binary tree的不同在於，binary search tree是依照數值的大小來決定它所放的位置
##通常比節點小的放左邊，大的放右邊，這次作業有要求要把相同的也放在左邊。
#2.尋找
##binary search tree的尋找會比較快速一點，因為已經去比較過每個數值的大小了來決定放的位置，所以我們直接拿目標去和節點比較，
##然後順著方向來去尋找目標就可以了。
#3.刪除
##binary search tree的刪除需要先使用search來找到目標，然後對它進行刪除，但這邊又可以分成三種情況，
##1.沒有child 2.1個child 3.兩個child，child會影響到我們對樹進行調整，假如沒有child只要對目標進行刪除即可，
##如果有一個child，再刪除目標後，需要把後面的child給接上來，兩個child的情況比較複雜，因為binary search tree
##的規則是需要用大小來排位置，所以為了把影響降到最低，可以往目標的leftchild進行尋找，找到最小的數值，把它接再節點上，可以對整棵樹
##的高度影響降到最低
#4.修改
##修改就像是把前面三個function融合再一起，先進行search找目標，然後delete，最後在插入新的數值。


##參考網址1 https://www.youtube.com/watch?v=f5dU3xoE6ms
##參考網址2 https://www.youtube.com/watch?v=Zaf8EOVa72I
##參考網址3 https://github.com/bfaure/Python3_Data_Structures/blob/master/Binary_Search_Tree/main.py
