#lang racket
(define (mySum lst)
  (if (list? lst)
      (if (empty? lst)
          0
          (+ (first lst) (mySum (rest lst)))
      )
      (display "Sorry, that's not a list")
  )
)