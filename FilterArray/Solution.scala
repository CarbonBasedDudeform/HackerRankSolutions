def f(delim:Int,arr:List[Int]):List[Int] = {
    var temp = List[Int]()
    arr.foreach(x => {
        if (x < delim) {
            temp = x :: temp
        }
    })
    return temp.reverse
}
