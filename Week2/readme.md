Linked List
linked list 是由一連串的 node 所組成的，每一個 node 裡面包含了各自的 data , 儲存位置和 pointer ， pointer 的功能是用來串聯下一個 node ，因此這說明了只要我們想修改 linked list 我們只要從需要修改 node 以及和它有關的 node 下手，去修該它們的 pointer ，就可以對 linked list 進行調整
linked list 與 array 的差別
linked list 是由 node 所組成，每項 node 可以視為各自獨立的個體， array 則是許多的資料包覆成，因此 array 可以當作一個完整的個體，所以在修改 array 時，需要把修改的值以後的每項往前或往後推一個。因此如果是需要頻繁修改的資料可以使用 linked list 。 
linked list 可以不斷的增加 node 的數量，但是 array 則有數量的限制。
如果我們需要頻繁取得 list 裡面的內容的話，使用 array 會比較好，因為 array 可以透過 index 來索取目標，但是 linked list 則需要從第一個 node 開始來找直到找到目標 node 。
