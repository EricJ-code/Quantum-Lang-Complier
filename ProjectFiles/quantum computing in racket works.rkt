#lang racket

;; Define types using structs in Racket
(struct numE (n) #:transparent)
(struct idE (s) #:transparent)
(struct qubitE (zero one) #:transparent)

(require racket/match)

;; Define the parse function
(define (parse s)
  (match s
    ["|0>" (qubitE 1 0)]
    ["|1>" (qubitE 0 1)]
    [(? number?) (numE s)]
    [(? symbol?) (idE s)]
    ;;[else (error 'parse "invalid input")]
    ))

;; Example uses of the parse function
(module+ test
  (require rackunit)

  (check-equal? (parse '2) (numE 2))
  (check-equal? (parse 'x) (idE 'x))
  (check-equal? (parse "|0>") (qubitE 1 0))
  (check-equal? (parse "|1>") (qubitE 0 1))
  ;;(check-exn "invalid input"
             ;;(lambda () (parse '(+ 1 2))))
  )
