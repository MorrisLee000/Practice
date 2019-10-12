# Stack and Queue
## Stack
### stack 類似堆盤子的想法，盤子是由下面堆到上面，但是洗盤子時，是從上面先開始拿。
    - push(data):把資料放進最上面
    - pop:把最上面的資料移除
    - top:回傳最上面的資料
    - IsEmpty:確認stack是否有資料
    - getSize:回傳stack裡資料個數
## Queue
### queue 就類似我們排隊的樣子，先到的人先進去。
    - push(data):把資料從queue的後面放入queue，並更新成新的back
    - pop:把front所指向的資料從queue中移除，並更新front。此行為又稱為dequeue
    - getFront:回傳front的值
    - getBack:回傳back的值
    - IsEmpty:確認queue是否有資料
    - getSize:回傳queue裡資料個數
