def f(num:Int,arr:List[Int]):List[Int] = {
    var hd::tail = arr;
    for (i <- 1 to num) {
        print(hd+"\n");
    }

    return f(num, tail);
}
