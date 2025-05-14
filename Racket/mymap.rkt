#lang racket
(define (myMap op lst)
  (if (empty? lst)
      (list)
      (append (list (op (car lst))) (myMap op (cdr lst)))
  )
)
(myMap abs (list 1 -1 2 -2 3 -3))