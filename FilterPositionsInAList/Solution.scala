def f(arr:List[Int]):List[Int] = {
    var temp = List[Int]()
    for (i <- arr.indices) {
        if ((i+1)%2 == 0) {
            temp = arr(i) :: temp
        }
    }

    return temp.reverse
}
