package example.c

import example.c.model.Box

object Main {

  val numbers: List[Int] = List(1, 2, 3, 4, 5)

  //def procedure = numbers.foldRight(0){case (elm, acc) => acc + elm}
  def procedure: = numbers.map(num => Box(num)).foldRight(Box(0) {
    case (elm, cum) => cum.concat(elm).map(_.toInt)
  })
}
