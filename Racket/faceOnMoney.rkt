#lang racket
(define (faceOnMoney amt)
  (cond
    ((= amt 1) (display "George Washington"))
    ((= amt 2) (display "Thomas Jefferson"))
    ((= amt 5) (display "Abraham Lincoln"))
    ((= amt 10) (display "Alexander Hamilton"))
    ((= amt 20) (display "Andrew jackson"))
    ((= amt 50) (display "Ulysses S. Grant"))
    ((= amt 100) (display "Benjamin Franklin"))
    ((display "Not real bill"))
  )
)