package example.c.model

case class Box[A](value: A) {

  def map[B](f: A => B): Box[B] = Box(f(value))

  def show(fn: A => A): Box[A] = Box(fn(value))

  def flatMap[B](fn: A => Box[B]): Box[B] = fn(value)

}
